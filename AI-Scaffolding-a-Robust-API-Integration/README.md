# AI: Scaffolding a Robust API Integration

## Task Overview

This task demonstrates the use of AI-assisted software development and Contextual Prompting to improve a Python sentiment analysis tool. The original program connects to the Text Processing API and converts the API response into positive, negative, or neutral sentiment labels.

The goal was to use an AI tool to refactor the `analyze_sentiment` function so that it securely reads an API key from an environment variable, includes the key in an Authorization header, and provides more comprehensive error handling for timeout and connection failures.

## AI Tool Used

Google Gemini was used to formulate and generate the refactored Python code. A Contextual Prompting technique was used by providing the complete original Python code as context and explicitly describing the required security and error-handling improvements.

## Files

### `sentiment_analyzer_initial.py`

This file contains the original sentiment analysis implementation provided as the starting point for the task. It sends the input sentence to the Text Processing API and handles general HTTP, request, and response-format errors.

### `sentiment_analyzer.py`

This file contains the AI-refined implementation. The improvements include:

- Securely reading `TEXT_PROCESSING_API_KEY` from an environment variable.
- Adding the API key to the request using the `Authorization: Bearer <key>` header format.
- Adding a 10-second request timeout.
- Explicitly handling `requests.exceptions.Timeout`.
- Explicitly handling `requests.exceptions.ConnectionError`.
- Retaining HTTP, general request, and invalid response handling.
- Mapping the API response labels `pos` and `neg` to `positive` and `negative`.

The API key is not hard-coded into the source code.

## Testing and Verification

The refactored program was checked using `pycodestyle` and `python3 -m py_compile` with no errors.

The required environment variable was configured using a dummy value:

`export TEXT_PROCESSING_API_KEY="DUMMY_KEY"`

The program was then tested with the sentence:

`I love this amazing product`

The program successfully returned:

`positive`

The API endpoint used in the final implementation was changed from the original `api.text-processing.com` endpoint to the working `text-processing.com` endpoint because the original endpoint produced a TLS certificate hostname error during testing.

## Robustness Improvements

The final implementation improves security by keeping the API key outside the source code and retrieving it from an environment variable. It also improves reliability by distinguishing timeout and connection failures from other HTTP and request errors, allowing users to receive more informative error messages when communication with the API fails.

## AI-Assisted Development

The task demonstrates how Contextual Prompting can provide an AI coding tool with the existing implementation, technical requirements and specific non-functional requirements. Providing the complete source code and explicitly defining the authentication and error-handling requirements allowed Gemini to produce a focused refinement rather than an unrelated replacement implementation.