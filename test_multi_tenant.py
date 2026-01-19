from playwright.sync_api import expect

def test_multi_tenant_access(page):
    page.goto("https://app.workflowpro.com/login", wait_until="networkidle")

    page.fill("#email", "user@company2.com")
    page.fill("#password", "password123")

    with page.expect_navigation(wait_until="networkidle"):
        page.click("#login-btn")

    projects = page.locator(".project-card")
    expect(projects.first).to_be_visible()

    for i in range(projects.count()):
        assert "Company2" in projects.nth(i).text_content()

