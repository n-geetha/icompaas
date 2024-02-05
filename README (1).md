# Flask Application with Sanitization Tests

This is a Flask application with a sanitization function to check for special characters. The application includes a set of tests to ensure the correct functionality of the sanitization function.

## Flask Application

The main application is in the `app.py` file. It includes a Flask web server with a simple "Hello, World!" endpoint and a sanitization function.

## Sanitization Function

The sanitization function (`sanitize_input`) checks for Special characters in the input string. It uses regular expressions to identify potential security risks. However, it is recommended to use parameterized queries for database interactions for a more secure approach.

## Running the Application

To run the Flask application, execute the following command:

```bash
python app.py
```
The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Running Tests

Tests for the sanitization function are included in the tests.py file. To run the tests, use the following command:

```bash
pytest tests.py
```

Make sure to install the necessary dependencies by running:
```bash
pip install -r requirements.txt
```

## Testing with Postman
You can use Postman to test the API with custom inputs. Follow the steps below:

1. Open Postman.

2. Set the request type to POST.

3. Enter the URL `http://127.0.0.1:5000/v1/sanitized/input/`

4. In the request body, choose raw and set the content type to `JSON` `(application/json)`.

5. Provide custom input in the following format:
```bash
{
    "input": "your_custom_input_here"
}

```
6. Replace "your_custom_input_here" with the input you want to test.

7. Click the "Send" button to make the request.

8. The response will indicate whether the input is sanitized or unsanitized.