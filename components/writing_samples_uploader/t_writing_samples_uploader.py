
import pytest
from typing import List
from fastapi import UploadFile
from pydantic import BaseModel
from your_module.path import WritingSamplesInputDict, WritingSamplesOutputDict, WritingSamplesUploader

# Mocked input data for testing
test_input_data = [
    {
        "args": WritingSamplesInputDict(),
        "files": [
            UploadFile("sample1.txt", content_type="text/plain"),
            UploadFile("sample2.txt", content_type="text/plain"),
            UploadFile("sample3.txt", content_type="text/plain"),
            UploadFile("sample4.txt", content_type="text/plain"),
            UploadFile("sample5.txt", content_type="text/plain"),
        ],
    },
    {
        "args": WritingSamplesInputDict(),
        "files": [
            UploadFile("sample1.txt", content_type="text/plain"),
            UploadFile("sample2.txt", content_type="text/plain"),
            UploadFile("sample3.txt", content_type="text/plain"),
        ],
    },
]

# Expected output data for testing
test_output_data = [
    WritingSamplesOutputDict(
        writing_samples=[
            UploadFile("sample1.txt", content_type="text/plain"),
            UploadFile("sample2.txt", content_type="text/plain"),
            UploadFile("sample3.txt", content_type="text/plain"),
            UploadFile("sample4.txt", content_type="text/plain"),
            UploadFile("sample5.txt", content_type="text/plain"),
        ]
    ),
    ValueError("At least 5 writing samples must be uploaded."),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("test_input,expected_output", zip(test_input_data, test_output_data))
def test_writing_samples_uploader_transform(test_input, expected_output):
    writing_samples_uploader = WritingSamplesUploader()
    
    # If the expected output is a ValueError, test for raising the error
    if isinstance(expected_output, ValueError):
        with pytest.raises(ValueError) as e_info:
            result = writing_samples_uploader.transform(test_input["args"], test_input["files"])
        assert str(e_info.value) == str(expected_output)
    else:
        # Call the component's transform() method and check if the output matches the expected output
        result = writing_samples_uploader.transform(test_input["args"], test_input["files"])
        assert result == expected_output
