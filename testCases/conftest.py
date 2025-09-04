from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching the Chromer Browser.....")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching the Firefox Browser.....")

    else:
        driver = webdriver.Chrome()
        print("Launching the Chrome Browser.....")
        return driver

    driver.maximize_window()



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

############ Pytest HTML Reports ##########

# Set HTML Reports Title
def pytest_html_report_title(report):
    report.title = 'OrangeHRM Test Report'


#Add Customer Environment Info
def pytes_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project Name : OrangeHRM",
        "Tester : Pratik"
    ])


# Remove unwanted environment info
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("plugins", None)