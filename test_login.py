from playwright.sync_api import expect

def test_user_login(page):
    page.goto("https://app.workflowpro.com/login", wait_until="networkidle")

    page.fill("#email", "admin@company1.com")
    page.fill("#password", "password123")

    with page.expect_navigation(wait_until="networkidle"):
        page.click("#login-btn")

    expect(page).to_have_url(lambda url: "dashboard" in url)
    expect(page.locator(".welcome-message")).to_be_visible()

