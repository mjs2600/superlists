from selenium import webdriver


def test_getting_the_page_title():
    browser = webdriver.Firefox()
    browser.get("http://localhost:8000")

    assert "To-Do" in browser.title

    browser.quit()
