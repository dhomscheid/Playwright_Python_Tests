https://playwright.dev/python/docs/intro
pip install pytest-playwright
playwright install

https://playwright.dev/python/docs/running-tests

Running tests
Command Line

To run your tests, use the pytest command. This will run your tests on the Chromium browser by default. Tests run in headless mode by default meaning no browser window will be opened while running the tests and results will be seen in the terminal.

pytest

Run tests in headed mode

To run your tests in headed mode, use the --headed flag. This will open up a browser window while running your tests and once finished the browser window will close.

pytest --headed

Run tests on different browsers

To specify which browser you would like to run your tests on, use the --browser flag followed by the name of the browser.

pytest --browser webkit

To specify multiple browsers to run your tests on, use the --browser flag multiple times followed by the name of each browser.

pytest --browser webkit --browser firefox

Run specific tests

To run a single test file, pass in the name of the test file that you want to run.

pytest test_login.py

To run a set of test files, pass in the names of the test files that you want to run.

pytest tests/test_todo_page.py tests/test_landing_page.py

To run a specific test, pass in the function name of the test you want to run.

pytest -k test_add_a_todo_item


#MyTests######
pytest test_example.py --headed --browser firefox

pytest test_refresh.py --headed