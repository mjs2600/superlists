from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Firefox()  # type: ignore
    yield browser
    browser.quit()


def test_can_start_a_list_and_retrieve_it_later(browser):
    browser.get("http://localhost:8000")

    assert "To-Do" in browser.title

    header_text = browser.find_element_by_tag_name("h1").text
    assert "To-Do" in header_text
