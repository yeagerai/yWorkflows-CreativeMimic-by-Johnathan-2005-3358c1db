
import pytest
from fastapi import UploadFile
from fastapi.testclient import TestClient
from io import BytesIO
from pydantic import ValidationError
from app import text_extractor_app, TextExtractor, TextExtractorInputDict, TextExtractorOutputDict

client = TestClient(text_extractor_app)

# Define test cases with mocked input and expected output data
test_data = [
    (
        "sample1.pdf", 
        1024, 
        200, 
        "Sample 1 text content."
    ),
    (
        "sample2.pdf", 
        2048, 
        200, 
        "Sample 2 text content."
    ),
    (
        "oversized_sample.pdf", 
        2049, 
        400, 
        ""
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("file_name, file_size, expected_status, expected_text", test_data)
def test_text_extractor(file_name, file_size, expected_status, expected_text):
    # Mock an UploadFile instance
    def _gen_mock_file(file_name: str, file_size: int) -> UploadFile:
        file = BytesIO(b"\x00" * file_size)
        return UploadFile(
            filename=file_name,
            content_type="application/pdf",
            file=file
        )

    # Create test input data
    input_data = TextExtractorInputDict(WritingSamplesUpload=_gen_mock_file(file_name, file_size))

    # Run the transform() method with the input data
    text_extractor_output = TextExtractor().transform(input_data)

    # Assert the output matches the expected result
    assert text_extractor_output.component_internal_status == expected_status
    assert text_extractor_output.ExtractedText == expected_text

def test_text_extractor_input_dict():
    # Test with valid input
    valid_request = {
        "WritingSamplesUpload": {
            "filename": "sample1.pdf",
            "content_type": "application/pdf",
            "file": BytesIO(b"Sample 1 text content.")
        }
    }
    try:
        input_data = TextExtractorInputDict(**valid_request)
        assert isinstance(input_data, TextExtractorInputDict)
        assert input_data.WritingSamplesUpload.filename == "sample1.pdf"
    except ValidationError as e:
        assert False, f"TextExtractorInputDict raised an unexpected ValidationError: {e}"
    
    # Test with invalid input (missing filename)
    invalid_request = {
        "WritingSamplesUpload": {
            "filename": "",
            "content_type": "application/pdf",
            "file": BytesIO(b"Sample 1 text content.")
        }
    }
    try:
        input_data = TextExtractorInputDict(**invalid_request)
        assert False, "TextExtractorInputDict should have thrown a ValidationError for missing filename"
    except ValidationError as e:
        assert "filename" in str(e)

