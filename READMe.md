Fract Test Suite
This repository contains a Selenium pytest test suite for automated testing of the Fract web application (https://app.fract.com). The suite validates critical UI interactions, form submissions, error messages, and navigation flows, ensuring the application's functionality for features like messaging, team list management, and form validation.
Table of Contents

Overview
Prerequisites
Project Structure
Setup Instructions
Running Tests
Test Suite Details
Troubleshooting
Contributing
Contact

Overview
The Fract Test Suite automates end-to-end testing of the Fract application using Selenium WebDriver and pytest. Tests cover:

UI Interactions: Clicking buttons (e.g., "Messages", "Send us a message") and verifying panel visibility.
Form Validation: Checking error messages (e.g., "Name is required") on form submissions.
Navigation: Accessing dashboards, team lists, and contact forms.
Error Handling: Ensuring no unexpected errors appear during interactions.

The suite is designed for reliability, using webdriver-manager to handle browser drivers and python-dotenv for secure credential management. Tests generate HTML reports for easy result analysis.
Prerequisites
Before running the tests, ensure the following are installed:

Python: Version 3.8 or higher (python --version).
Git: For cloning the repository (git --version).
Google Chrome: Latest version (chrome://settings/help to check).
ChromeDriver: Automatically managed via webdriver-manager (included in dependencies).
Operating System: Windows, macOS, or Linux.
Text Editor: Optional, for viewing or editing tests (e.g., VS Code).

Project Structure
fract-test-suite/
├── tests/
│   ├── test_error_message_validation.py  # Validates "Name is required" error
│   ├── test_send_message_div.py          # Tests "Send us a message" div
│   ├── test_team_list_add.py             # Tests adding "Campground List"
│   └── ...                              # Other tests (e.g., test_contact_us_form.py)
├── .gitignore                           # Ignores virtual env, reports, etc.
├── requirements.txt                     # Python dependencies
├── pytest.ini                           # Pytest configuration
└── README.md                            # This documentation

Note: Do not commit .env files containing credentials.
Setup Instructions
Follow these steps to set up the test suite on your machine.

Clone the Repository:
git clone https://github.com/your-username/fract-test-suite.git
cd fract-test-suite


Create a Virtual Environment (recommended):
python -m venv venv

Activate the virtual environment:

Linux/macOS:source venv/bin/activate


Windows:venv\Scripts\activate




Install Dependencies:
pip install -r requirements.txt

This installs:

pytest: Test framework.
selenium: Web automation.
pytest-html: HTML report generation.
webdriver-manager: Auto-manages ChromeDriver.
python-dotenv: Handles environment variables.


Configure Login Credentials:

Create a .env file in the project root:FRACT_USERNAME=your-username
FRACT_PASSWORD=your-password


Contact [your-email@example.com] for valid credentials.
Security Note: Do not share .env publicly or commit it to Git.


Verify Setup:

Ensure Chrome is installed.
Check Python version:python --version


Confirm dependencies:pip list





Running Tests
Tests are executed using pytest, with results saved as an HTML report.

Run All Tests:
pytest tests/ --html=report.html --self-contained-html


Generates report.html with test results.
Tests run in headless mode (no browser UI visible).


Run a Specific Test:Example:
pytest tests/test_error_message_validation.py --html=report.html


View Results:

Open report.html in a web browser to review pass/fail status, durations, and errors.
Example output: "PASSED tests/test_error_message_validation.py::TestErrorMessageValidation::test_validate_error_message [20.000s]".


Clean Up:

Delete report.html if no longer needed.
Deactivate virtual environment:deactivate





Test Suite Details
The test suite includes over 80 test cases, covering various Fract application features. Key tests include:

test_error_message_validation.py:

Validates the "Name is required" error on a contact form when submitted without a name.
Verifies error visibility and style.
Duration: ~20 seconds.


test_send_message_div.py:

Clicks the "Send us a message" div (Intercom widget).
Verifies chat panel visibility.
Duration: ~20 seconds.


test_team_list_add.py:

Clicks the "Add" button to include "Campground List" in Team Lists.
Verifies list addition.
Duration: ~20 seconds.


Other Tests:

test_contact_us_form.py: Tests form submission and redirects (~24 seconds).
test_map_toolsp.py: Validates map tools UI (~63 seconds, longest test).
test_login.py: Verifies login functionality (~6 seconds).
See tests/ for full list, covering UI, forms, navigation, and map features.



Notes:

Tests assume access to https://app.fract.com. Update URLs in test files if the application changes.
Some tests require navigation (e.g., to /contact or /dashboard). Ensure correct URLs in setup_method.
Tests use WebDriverWait for robustness, with 10-15 second timeouts.

Troubleshooting
Common issues and solutions:

ChromeDriver Version Mismatch:

webdriver-manager should auto-install the correct ChromeDriver.
If errors occur, verify Chrome version (chrome://settings/help) and update:pip install --upgrade webdriver-manager


Manual install (if needed):
Download from chromedriver.chromium.org.
Place in PATH (e.g., /usr/local/bin or C:\bin).




Login Failures:

Verify .env contains correct FRACT_USERNAME and FRACT_PASSWORD.
Check login selectors in tests (e.g., input[name='username']).
Contact [your-email@example.com] for updated credentials.


Element Not Found Errors:

Application UI may have changed. Update selectors in test files (e.g., span.error to span.error-message).
Increase timeout:WebDriverWait(self.driver, 15).until(...)


Debug:print(self.driver.find_elements(By.CSS_SELECTOR, "span.error"))




Tests Timeout or Fail:

Ensure stable internet connection.
Check report.html for failure details.
Run tests individually to isolate issues:pytest tests/test_error_message_validation.py -v




Permission Issues:

Ensure you have write access to the project directory.
Run commands with sudo (Linux/macOS) or as Administrator (Windows) if needed.


Report Not Generated:

Verify pytest-html is installed (pip show pytest-html).
Check command includes --html=report.html.



Contributing
To contribute to the test suite:

Fork the repository.
Create a feature branch:git checkout -b feature/new-test


Add tests in tests/, following existing structure.
Update requirements.txt if new dependencies are added:pip freeze > requirements.txt


Commit and push:git add .
git commit -m "Add new test for feature X"
git push origin feature/new-test


Open a pull request on GitHub.

Guidelines:

Use descriptive test names (e.g., test_validate_error_message).
Include assertions for visibility and state.
Avoid hardcoding credentials; use .env.
Test locally before pushing:pytest tests/



Contact
For support, contact:

Email: [your-email@example.com]
Issues: Open a GitHub issue at https://github.com/your-username/fract-test-suite/issues
Credentials: Request updated FRACT_USERNAME and FRACT_PASSWORD securely.

Please provide report.html or error logs when reporting issues for faster resolution.
