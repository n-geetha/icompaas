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


