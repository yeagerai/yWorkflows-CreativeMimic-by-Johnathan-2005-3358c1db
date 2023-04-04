
from typing import List
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from core.abstract_component import AbstractComponent

class WritingSamplesInputDict(BaseModel):
    pass

class WritingSamplesOutputDict(BaseModel):
    writing_samples: List[UploadFile]

class WritingSamplesUploader(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: WritingSamplesInputDict, files: List[UploadFile]
    ) -> WritingSamplesOutputDict:
        if len(files) < 5:
            raise ValueError("At least 5 writing samples must be uploaded.")
        
        return WritingSamplesOutputDict(writing_samples=files)

writing_samples_uploader_app = FastAPI()

@writing_samples_uploader_app.post("/transform/")
async def transform(
    args: WritingSamplesInputDict, files: List[UploadFile] = File(...)
) -> WritingSamplesOutputDict:
    writing_samples_uploader = WritingSamplesUploader()
    return writing_samples_uploader.transform(args, files)
