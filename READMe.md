# Fract Test Suite

This repository contains a Selenium pytest test suite for automated testing of the Fract web application (`https://app.fract.com`). The suite validates critical functionalities, including login, UI interactions, map tools, list management, territory creation, and administrative features, ensuring robust performance across the application’s core components.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running Tests](#running-tests)
- [Test Suite Details](#test-suite-details)
- [Troubleshooting](#troubleshooting)
- [Contact](#contact)

## Overview
The Fract Test Suite automates end-to-end testing of the Fract application using Selenium WebDriver and pytest. It covers key functionalities such as:
- **Authentication**: Login and sign-out processes.
- **User Interface**: Navigation, panel expansion, and UI element interactions.
- **Map Features**: Map tools, list management, and location-based actions (e.g., Find Me).
- **Territory Management**: Creating, customizing, and reporting on territories and team lists.
- **Settings**: User profile, account, project, and notification configurations.
- **Communication**: In-app chat functionality.
- **Administration**: Admin dashboard and project management.

Tests generate HTML reports (`report.html`) for easy result analysis, use `webdriver-manager` for browser driver management, and secure credentials via `python-dotenv`.

## Prerequisites
- **Python**: 3.8 or higher (`python --version`).
- **Git**: For cloning the repository (`git --version`).
- **Google Chrome**: Latest version (`chrome://settings/help`).
- **ChromeDriver**: Auto-managed via `webdriver-manager`.
- **Operating System**: Windows.
- **Text Editor**: Optional (e.g., VS Code) for viewing/editing tests.

## Project Structure
```plaintext
fract-test-suite/
├── tests/
│   ├── test_login.py                     # Tests login functionality
│   ├── test_map_toolsp.py                # Tests map tools
│   ├── test_map_lists.py                 # Tests map list interactions
│   ├── test_findme.py                    # Tests "Find Me" feature
│   ├── test_user_profile.py              # Tests user profile settings
│   ├── test_project_settings.py          # Tests project settings
│   ├── test_notification.py              # Tests notification settings
│   ├── test_tutorials.py                 # Tests tutorial access
│   ├── test_new_territory.py             # Tests territory creation
│   ├── test_team_territory.py            # Tests team territory management
│   ├── test_new_list_creation.py         # Tests list creation and data upload
│   ├── test_team_list_mgt.py             # Tests team list management
│   ├── test_business_list.py             # Tests business list management
│   ├── test_business_Arts_Ents.py        # Tests arts & entertainment lists
│   ├── test_territory_color.py           # Tests map area customization
│   ├── test_signout.py                   # Tests sign-out
│   ├── test_expand.py                    # Tests panel expand/collapse
│   └── ...                              # Other tests (e.g., test_contact_us_form.py)
├── .gitignore                           # Ignores virtual env, reports, .env
├── requirements.txt                     # Python dependencies
├── pytest.ini                           # Pytest configuration
└── README.md                            # This documentation
```

**Note**: Do not commit `.env` files containing credentials.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/fract-test-suite.git
   cd fract-test-suite
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
   Activate:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Installs:
   - `pytest`: Test framework.
   - `selenium`: Web automation.
   - `pytest-html`: HTML reports.
   - `webdriver-manager`: ChromeDriver management.
   - `python-dotenv`: Environment variables.

4. **Verify Setup**:
   - Confirm Chrome version: `chrome://settings/help`.
   - Check Python: `python --version`.
   - List dependencies: `pip list`.

## Running Tests
Tests run in headless mode and generate an HTML report.

1. **Run All Tests**:
   ```bash
   pytest tests/ --html=report.html --self-contained-html
   ```
   - Outputs `report.html` with results.

2. **Run Specific Test**:
   Example:
   ```bash
   pytest tests/test_error_message_validation.py --html=report.html
   ```

3. **View Results**:
   - Open `report.html` in a browser to review pass/fail status and durations.
   - Example: "PASSED tests/test_error_message_validation.py::TestErrorMessageValidation::test_validate_error_message [20.000s]".

4. **Clean Up**:
   - Delete `report.html` if unneeded.
   - Deactivate virtual environment:
     ```bash
     deactivate
     ```

## Test Suite Details
The suite includes over 80 test cases, covering the following Fract application functionalities:

- **Login** (`test_login.py`):
  - Verifies successful login with valid credentials.
  - Duration: ~6 seconds.

- **UI** (`test_expand.py`, others):
  - Tests navigation, panel expand/collapse (e.g., left panel), and UI element visibility.
  - Duration: ~24 seconds (e.g., `test_expand.py`).

- **Map Tool** (`test_map_toolsp.py`, `test_map_tools.py`):
  - Validates map tool interactions (e.g., zoom, rulers).
  - Duration: ~29–63 seconds.

- **Map List** (`test_map_lists.py`, `test_map_list_search.py`):
  - Tests map list navigation and search (e.g., "24 Hour Fitness").
  - Duration: ~22–27 seconds.

- **Verify List Item Click** (`test_map_lists.py`):
  - Ensures clicking list items displays details.
  - Duration: ~27 seconds.

- **Verify Favorite Item Toggling** (`test_map_list_fav_vis.py`):
  - Tests toggling favorite status for list items.
  - Duration: ~28 seconds.

- **Find Me** (`test_findme.py`):
  - Verifies "Find Me" geolocation feature.
  - Duration: ~37 seconds.

- **User Profile** (`test_user_profile.py`):
  - Tests profile settings updates.
  - Duration: ~29 seconds.

- **Account Settings Panel** (`test_user_profile.py`):
  - Verifies account settings access.
  - Duration: ~29 seconds.

- **Profile Settings** (`test_insight.py`):
  - Tests profile configuration options.
  - Duration: ~37 seconds.

- **Project Settings** (`test_project_settings.py`):
  - Validates project configuration updates.
  - Duration: ~27 seconds.

- **Notification** (`test_notification.py`):
  - Tests notification settings and alerts.
  - Duration: ~25 seconds.

- **Tutorials** (`test_tutorials.py`):
  - Verifies tutorial access and navigation.
  - Duration: ~33 seconds.

- **Create New Territory** (`test_new_territory.py`):
  - Tests territory creation workflows.
  - Duration: ~22 seconds.

- **Team Territory Management** (`test_team_territory.py`):
  - Validates team territory assignments and settings.
  - Duration: ~26 seconds.

- **New List Creation & Data Upload** (`test_new_list_creation.py`):
  - Tests list creation and data import.
  - Duration: ~26 seconds.

- **Team Lists Management (Adding & Searching Lists by Project)** (`test_team_list_mgt.py`, `test_team_list_add.py`):
  - Verifies adding and searching team lists.
  - Duration: ~20–22 seconds.

- **Team Lists Management (Search & Navigation)** (`test_team_list_FNG.py`):
  - Tests team list search and navigation.
  - Duration: ~21 seconds.

- **Business Lists Management (Search & Category Filtering)** (`test_business_list.py`):
  - Validates business list search and filtering.
  - Duration: ~27 seconds.

- **Arts & Entertainment List Management (Search, Filtering, and Navigation)** (`test_business_Arts_Ents.py`):
  - Tests arts & entertainment list features.
  - Duration: ~32 seconds.

- **New Map Area Creation and Customization** (`test_territory_color.py`):
  - Verifies map area creation and styling.
  - Duration: ~41 seconds.

- **Territories Report Generation and Export** (assumed in `test_new_territory.py`):
  - Tests report generation and export.
  - Duration: ~22 seconds.

- **Pivot Table Data Visualization and File Upload** (assumed in `test_new_list_creation.py`):
  - Validates pivot table visualization and uploads.
  - Duration: ~26 seconds.

- **View Territory Details and Settings** (`test_team_territory.py`):
  - Tests territory details display.
  - Duration: ~26 seconds.

- **Sign Out** (`test_signout.py`):
  - Verifies logout functionality.
  - Duration: ~24 seconds.

- **In-App Chat** (`test_send_message_div.py`):
  - Tests initiating in-app chat (Intercom widget).
  - Duration: ~20 seconds.

- **Admin Dashboard** (assumed in `test_user_mgt.py`):
  - Validates admin dashboard access and functionality.
  - Duration: ~38 seconds.

- **Active Project** (assumed in `test_project_settings.py`):
  - Tests active project selection and management.
  - Duration: ~27 seconds.

- **Expand/Collapse Left Panel** (`test_expand.py`):
  - Verifies left panel toggle functionality.
  - Duration: ~24 seconds.

- **Form Validation** (`test_error_message_validation.py`):
  - Validates error messages (e.g., "Name is required") on forms.
  - Duration: ~20 seconds.

**Notes**:
- Durations are estimated from prior runs (see test results table).
- Some functionalities (e.g., Territories Report, Pivot Table) are assumed covered by related tests; confirm specific test files if needed.
- Tests use `https://app.fract.com`. Update URLs in `setup_method` if different (e.g., `/dashboard`, `/contact`).

## Troubleshooting
- **ChromeDriver Issues**:
  - `webdriver-manager` auto-installs ChromeDriver. If errors occur:
    ```bash
    pip install --upgrade webdriver-manager
    ```
    Or manually download from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) and place in PATH.

- **Element Not Found**:
  - UI changes may break selectors. Update tests (e.g., `span.error` to `span.error-message`).
  - Increase timeout:
    ```python
    WebDriverWait(self.driver, 15).until(...)
    ```
  - Debug:
    ```python
    print(self.driver.find_elements(By.CSS_SELECTOR, "span.error"))
    ```

- **Test Failures**:
  - Check `report.html` for details.
  - Run tests individually:
    ```bash
    pytest tests/test_login.py -v
    ```
  - Ensure stable internet.

- **Permission Errors**:
  - Use `sudo` (Linux/macOS) or Administrator mode (Windows) if needed.
  - Check directory write access.

- **Report Issues**:
  - Verify `pytest-html` (`pip show pytest-html`).
  - Ensure `--html=report.html` in command.

## Contact
- **GitHub Issues**: [https://github.com/your-username/fract-test-suite/issues](https://github.com/your-username/fract-test-suite/issues)

Provide `report.html` or error logs for support.
