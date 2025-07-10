import pytest

from playwright.sync_api import sync_playwright

def test_orangehrm_login():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.fill("input[name='username']", "Admin")
        page.fill("input[name='password']", "admin123")
        page.click("button[type='submit']")

        page.wait_for_selector("h6:has-text('Dashboard')")

        print("✅ OrangeHRM login test passed.")
        context.close()
        browser.close()

