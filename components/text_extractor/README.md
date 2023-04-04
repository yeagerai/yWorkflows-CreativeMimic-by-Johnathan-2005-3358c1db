markdown
# Component Name

TextExtractor

# Description

TextExtractor is a Yeager component designed to extract text from a provided PDF file. The component validates the file size against a pre-defined maximum file size before extracting the text. The text extraction process is performed using the `textract` library.

# Input and Output Models

Inputs:
- `TextExtractorInputDict`: A Pydantic BaseModel class containing the following field:
    - `WritingSamplesUpload: UploadFile`: The input PDF file to be processed.

Outputs:
- `TextExtractorOutputDict`: A Pydantic BaseModel class containing the following fields:
    - `component_name: str`: The name of the component.
    - `ExtractedText: str`: The extracted text from the PDF file.
    - `component_internal_status: int`: The internal status of the component execution (200, 400, or 500).

# Parameters

- `max_file_size`: A string representing the maximum allowed file size for the text extraction (e.g., "10MB"). It is read from the component configuration file and stored as a class variable.

# Transform Function

The `transform()` method performs the following steps:

1. Check if the input PDF file size is lower than or equal to the `_get_max_file_size_bytes()` calculated value using the `_is_valid_file_size()` method.
2. If the file size is not valid, return a `TextExtractorOutputDict` with an empty `ExtractedText` field and `component_internal_status` set to 400.
3. Read the PDF file content and store the bytes in a `BytesIO` object.
4. Use the `textract.process()` method to extract the text from the PDF file with the "pdftotext" method and "utf-8" encoding.
5. If an exception is encountered during the text extraction, return a `TextExtractorOutputDict` with the `ExtractedText` field set to the exception message and `component_internal_status` set to 500.
6. If the text extraction succeeds, return a `TextExtractorOutputDict` containing the extracted text and `component_internal_status` set to 200.

# External Dependencies

- `os`: Standard Python library for OS-related tasks (used to access environment variables).
- `yaml`: A Python library used to read the configuration file containing the `max_file_size` parameter.
- `dotenv`: A Python library used to load environment variables from a .env file.
- `FastAPI`: A Python web framework, used to create the TextExtractor API.
- `UploadFile`: A FastAPI class used to handle file uploads.
- `Pydantic`: A Python library for data validation and serialization, used to define input and output models.
- `textract`: A Python library used to extract text from the input PDF file.

# API Calls

The TextExtractor component does not make any external API calls.

# Error Handling

The component handles errors during text extraction by catching any raised exceptions and returning a `TextExtractorOutputDict` with the `ExtractedText` field containing the error message and `component_internal_status` set to 500. If the file size is not within the allowed limit, the component returns a `TextExtractorOutputDict` with an empty `ExtractedText` field and `component_internal_status` set to 400.

# Examples

To use the TextExtractor component in a Yeager Workflow, follow these steps:

1. Initialize a `TextExtractorInputDict` with a valid `UploadFile` containing the PDF file to be processed.
2. Create an instance of the `TextExtractor` component.
3. Call the `transform()` method of the component, passing the `TextExtractorInputDict` as an argument.
4. The returned `TextExtractorOutputDict` will contain the extracted text and the component's internal status.

Example:

