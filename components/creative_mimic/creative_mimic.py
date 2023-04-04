
import typing
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from core.workflows.abstract_workflow import AbstractWorkflow

# Input and Output Models
class CreativeMimicIn(BaseModel):
    WritingSamplesUpload: List[str]
    DesiredTopic: str
    style_features_extraction_method: Optional[str] = "default"
    content_generation_algorithm: Optional[str] = "transformers"


class CreativeMimicOut(BaseModel):
    GeneratedArticle: str


# Workflow class definition
class CreativeMimic(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: CreativeMimicIn, callbacks: typing.Any
    ) -> CreativeMimicOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        
        # Extract the generated article from the results_dict
        generated_article = results_dict["GeneratedArticle"].article
        
        out = CreativeMimicOut(GeneratedArticle=generated_article)
        return out

# FastAPI "/transform/" Endpoint
creative_mimic_app = FastAPI()

@creative_mimic_app.post("/transform/")
async def transform(args: CreativeMimicIn) -> CreativeMimicOut:
    creative_mimic = CreativeMimic()
    return await creative_mimic.transform(args, callbacks=None)
