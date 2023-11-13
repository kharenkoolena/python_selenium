# Automated testing in Python


## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)    


## Description

This project contains automated tests for testing a "https:/leetcode.com/" website. There are login, logout and user progress tests in the project.

This project is built using Python, a high-level programming language known for its simplicity and readability. Python offers a robust and extensive standard library and has a thriving community that contributes to its development and support. For more information on Python, visit the official Python website: [Python Official Website](https://www.python.org/)

This project uses the Selenium WebDriver, a popular tool for automating web applications for testing purposes. Selenium provides a user-friendly API that enables the interaction with various web elements, making it an ideal choice for web testing and automation tasks. To learn more about Selenium WebDriver, refer to the Selenium documentation: [Selenium Documentation](https://www.selenium.dev/documentation/en/)

This project is designed to be compatible with both Windows and Ubuntu operating systems. Whether you're using a Windows machine or running Ubuntu, you can easily set up and utilize the functionalities of this project.


## Installation

To use this project, follow these steps:

1. Clone the repository to your local machine using the following command:

    ```bash
    https://github.com/kharenkoolena/python_selenium.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-project
    ```

3. Install the required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

Make sure you have Python and pip installed on your machine before running the project. You can integrate this project into your to automate the testing process. Please share details and commands related to your usage.


## Usage

To utilize the automated tests in this project, follow these steps:

1. Run the specific test files to execute the tests. Project runs in Chrome by default. For example, you can use the following commands to run the tests:

	- run all tests from the tests folder:

    ```bash
	pytest tests
    ```
	
	- run all tests from test_login.py:

    ```bash
	pytest tests/test_login.py
    ```
	
	- run the specific test from test_login.py:
	
    ```bash
	pytest tests/test_login.py -k test_login_invalid_password
    ```
	
	If you need Firefox or Chrome-headless, you can use the following command to run the tests:
	
	Firefox:
	```bash
	pytest tests/test_login.py --browser=firefox
    ```
	
	Chrome-headless:
	```bash
	pytest tests/test_login.py --browser=chrome --headless
    ```
	
2. Check the test results to verify whether the expected outcomes match the actual results.

You can explore and modify the tests based on your requirements.
