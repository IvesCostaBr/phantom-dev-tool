from fastapi.routing import APIRouter
from src.api.models import respository
from src.driver.runner import pipeline_runner

router = APIRouter(tags=["Repository"])


@router.post("", response_model=dict)
async def create_repo(data: respository.InRepository):
    return pipeline_runner("create_repo", data.model_dump())


@router.get("/{repo_name}")
async def get_repo_tree(repo_name: str):
    return pipeline_runner("list_tree_repo", {"repo_name": repo_name})


@router.get("/file/detail", response_model=respository.ResponseDetailFile)
async def detail_file(file_dir: str):
    return pipeline_runner("detail_file", {"file_dir": file_dir})


@router.get("")
async def list_repo():
    return pipeline_runner("list_repo")


@router.put("/{repo_name}")
async def update_file(repo_name: str, payload: respository.UpdateFile):
    payload = payload.model_dump()
    payload["repo_name"] = repo_name
    return pipeline_runner("update_file", payload)


@router.post("/{repo_name}/push")
async def commit_repo(repo_name: str):
    return pipeline_runner("upload_repo", {"repo_name": repo_name})


@router.post("/auto-change")
async def auto_change(data: respository.AutoReplace):
    return pipeline_runner("auto_update", data.model_dump())
