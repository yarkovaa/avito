from playwright.sync_api import sync_playwright


def run_energy_test(playwright):
    firefox = playwright.firefox
    browser = firefox.launch()
    page = browser.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    # div:nth-child(-2n+6)
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(2)").screenshot(path='output/01.png')
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(4)").screenshot(path='output/02.png')
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(6)").screenshot(path='output/03.png')
    browser.close()

with sync_playwright() as playwright:
    run_energy_test(playwright)
