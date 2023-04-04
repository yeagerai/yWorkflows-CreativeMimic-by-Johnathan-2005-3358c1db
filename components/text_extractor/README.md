
# TextExtractor

A Yeager Component that processes the uploaded documents from WritingSamplesUpload and extracts the text content from them. The TextExtractor is designed to handle a variety of document formats, such as PDF, DOCX, and TXT files, and to convert the extracted text into a plain text format for further processing in the workflow.

## Initial generation prompt
description: 'A Yeager Component that processes the uploaded documents from WritingSamplesUpload
  and extracts the text content from them. Inputs: WritingSamplesUpload, Outputs:
  ExtractedText.'
name: TextExtractor


## Transformer breakdown
- 1. Verify WritingSamplesUpload is within the max_file_size parameter.
- 2. Identify the file format of WritingSamplesUpload.
- 3. Extract the text content from WritingSamplesUpload based on its file format.
- 4. Convert the extracted text into plain text format.
- 5. Return the plain text as ExtractedText output.

## Parameters
[{'name': 'max_file_size', 'default_value': '10MB', 'description': 'The maximum file size allowed for uploaded documents.', 'type': 'string'}]

        