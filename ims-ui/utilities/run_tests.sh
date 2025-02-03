#!/bin/bash

# Navigate to the project directory
cd /Users/Deepak/Desktop/Python_Pytest_UI_Automation/ims-ui/reports/

# Generate a filename based on the current date and time
REPORT_FILENAME="./apollo_$(date +'%Y-%m-%d_%H-%M-%S').html"

# Run pytest with the dynamically generated filename
pytest -sv /Users/Deepak/Desktop/Python_Pytest_UI_Automation/ims-ui/tests/test_login_page/test_login_page_qa.py --html="$REPORT_FILENAME"
