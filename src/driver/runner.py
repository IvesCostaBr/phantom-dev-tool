from src.driver.executor import executor
from src.repository import log_repo
import time
from copy import deepcopy
from src.utils import show_log


def validate_step_valid(step: dict):
    """validate Required keys."""
    required_keys = ["name", "provider"]
    for each in required_keys:
        if not each in step.keys():
            raise Exception("step invalid")


def pipeline_runner(pipeline: str, data=None):
    """Runner."""

    module_path = f"src.pipelines.{pipeline}"
    try:
        function = getattr(__import__(
            module_path, fromlist=["return_pipe"]), "return_pipe")

    except Exception as ex:
        raise Exception(
            "error execute pipeline -> {} | {}".format(pipeline, str(ex)))

    pipeline_steps = function(data)

    show_log("Executing Pipeline -> {}".format(pipeline))
    pipeline_time = time.time()
    pipeline_data = {"payload": deepcopy(data), "errors": []}
    errors = []
    counter = 0
    for each in pipeline_steps:
        try:
            counter += 1
            start_time = time.time()
            validate_step_valid(each)
            if each.get("condition"):
                if not pipeline_data.get(each.get("condition").get("step")).get("status") == each.get("condition").get("value"):
                    show_log(
                        "Ignoring Step {} -> {}".format(counter, each.get("name")))
                    continue
            show_log("Executing Step {} -> {}".format(counter, each.get("name")))
            result = executor(pipeline_data, each.get("provider"), each.get(
                "module") if each.get("module") else None, each.get("async"))
            end_time = time.time()
            pipeline_data[each.get("name")] = result
            if not result.get("status"):
                pipeline_data["errors"].append(
                    {each.get("name"): result.get("data")})
            elapsed_time = round(end_time - start_time, 5)
            show_log(
                "Step Finished {} -> {} - time exec -> {} sec.".format(counter, each.get("name"), elapsed_time))
        except Exception as ex:
            print(ex)

            raise Exception(
                "error execute pipeline -> {} | {}".format(pipeline, str(ex)))
    end_time = time.time()
    elapsed_time = round(end_time - pipeline_time, 5)
    show_log(
        "Pipeline Finished -> {} - time exec -> {} sec. ".format(pipeline, elapsed_time))

    log_repo.create(data=pipeline_data)
    return pipeline_data["response"].get("data")
