from playwright.sync_api import Playwright
import os

# Playwright Configuration for QA Automation
class PlaywrightConfig:
    # Directory where test files are located
    test_dir = "automation/tests"

    # Global timeout for each test (in milliseconds)
    timeout = 30000

    # Expect assertion timeout
    expect_timeout = 10000

    # Run tests sequentially (recommended for UI tests)
    workers = 1

    # Browser settings
    browser_name = "chromium"
    headless = True

    # Capture artifacts for debugging
    screenshot = "only-on-failure"
    video = "retain-on-failure"
    trace = "retain-on-failure"

    # Base URL (can be changed per environment)
    base_url = "https://app.workflowpro.com"

    # Reporter configuration
    reporter = [
        ["html", {"outputFolder": "reports", "open": "never"}]
    ]

    # Retry failed tests in CI
    retries = 2 if os.getenv("CI") else 0

