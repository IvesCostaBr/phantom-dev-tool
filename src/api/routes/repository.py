from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from src.api.models import respository
from src.driver.runner import pipeline_runner
from starlette import status

router = APIRouter(tags=["Repository"])


@router.post("", response_model=dict)
async def create_repo(data: respository.InRepository):
    response = pipeline_runner("create_repo", data.model_dump())
    if response.get("errors"):
        return JSONResponse(response, status_code=status.HTTP_400_BAD_REQUEST)
    return response


@router.get("/{repo_name}")
async def get_repo_tree(repo_name: str):
    return pipeline_runner("list_tree_repo", {"repo_name": repo_name})


@router.get("/file/detail", response_model=list)
async def detail_file(file_dir: str):
    return pipeline_runner("detail_file", {"file_dir": file_dir})


@router.get("")
async def list_repo():
    return pipeline_runner("list_repo")


@router.put("/{repo_name}")
async def update_file(repo_name: str, payload: respository.UpdateFile):
    payload = payload.model_dump()
    payload["repo_name"] = repo_name
    response = pipeline_runner("update_file", payload)
    if response.get("errors"):
        return JSONResponse(response, status_code=status.HTTP_400_BAD_REQUEST)
    return response


@router.post("/{repo_name}/push")
async def commit_repo(repo_name: str):
    response = pipeline_runner("upload_repo", {"repo_name": repo_name})
    if response.get("errors"):
        return JSONResponse(response, status_code=status.HTTP_400_BAD_REQUEST)
    return response


@router.post("/auto-change")
async def auto_change(data: respository.AutoReplace):
    response = pipeline_runner("auto_update", data.model_dump())
    if response.get("errors"):
        return JSONResponse(response, status_code=status.HTTP_400_BAD_REQUEST)
    return response


@router.post("/revert-changes")
async def revert_changes(repo_name: str):
    response = pipeline_runner("revert_changes", {"repo_name": repo_name})
    if response.get("errors"):
        return JSONResponse(response, status_code=status.HTTP_400_BAD_REQUEST)
    return response
