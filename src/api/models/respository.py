from pydantic import BaseModel, root_validator, Field


class InRepository(BaseModel):

    repo_url: str
    repo_name: str
    branch: str
    key: list[str] = None


class UpdateFile(BaseModel):

    file_dir: str
    start: int
    end: int
    code: list[str] = Field([], examples=[
        [
            "print('teste here')",
            "print('...')"
        ]
    ])

    @root_validator(pre=True)
    def validate(cls, fields):
        if fields.get("end") < fields.get("start"):
            raise ValueError(
                "a linha final não pode ser menor ou igual a inicial")

        return fields


class AutoReplace(BaseModel):
    """
    Caso você queira sommente o rafactor basta não preencher o campo 'problem'.
    No caso de correção informe o problema a qual queira corrigir dentro do arquivo.
    """
    repo_name: str
    type: str = Field("fix", examples=["fix", "refact"])
    problem: str = None
    file_dir: str


class ResponseDetailFile(BaseModel):
    data: list[str] = Field(..., examples=[
        [
            "0: from fastapi import FastAPI",
            "1: ",
            "2: ",
            "3: app = FastAPI(title=\"Example Service\")",
        ]
    ]
    )
