
import os
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from core.abstract_component import AbstractComponent
from typing import Union
from io import BytesIO
import textract

class TextExtractorInputDict(BaseModel):
    WritingSamplesUpload: UploadFile

class TextExtractorOutputDict(BaseModel):
    component_name: str
    ExtractedText: str
    component_internal_status: int

class TextExtractor(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.max_file_size: str = yaml_data["parameters"]["max_file_size"]

    def _get_max_file_size_bytes(self) -> int:
        size = int(self.max_file_size[:-2])
        if self.max_file_size[-2:] == "MB":
            return size * 1024 * 1024
        elif self.max_file_size[-2:] == "KB":
            return size * 1024

    def _is_valid_file_size(self, file_size: int) -> bool:
        return file_size <= self._get_max_file_size_bytes()

    def transform(
        self, args: TextExtractorInputDict
    ) -> TextExtractorOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        if not self._is_valid_file_size(args.WritingSamplesUpload.file.size_in_bytes):
            return TextExtractorOutputDict(
                component_name=type(self).__name__,
                ExtractedText="",
                component_internal_status=400
            )

        content = args.WritingSamplesUpload.file.read()
        mem_file = BytesIO(content)

        try:
            extracted_text = textract.process(mem_file, method="pdftotext", encoding="utf-8").decode("utf-8")
        except Exception as e:
            return TextExtractorOutputDict(
                component_name=type(self).__name__,
                ExtractedText=str(e),
                component_internal_status=500
            )

        return TextExtractorOutputDict(
            component_name=type(self).__name__,
            ExtractedText=extracted_text,
            component_internal_status=200
        )

load_dotenv()
text_extractor_app = FastAPI()

@text_extractor_app.post("/transform/")
async def transform(
    args: TextExtractorInputDict,
) -> TextExtractorOutputDict:
    text_extractor = TextExtractor()
    return text_extractor.transform(args)
