import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Firefox()  # type: ignore
    yield browser
    browser.quit()


def test_can_start_a_list_and_retrieve_it_later(browser):
    # Edith heard about a cool new online to-do app. She goes
    # to check out its home page.
    browser.get("http://localhost:8000")

    # She notices the page title and header mention to-do lists.
    assert "To-Do" in browser.title

    header_text = browser.find_element(by=By.TAG_NAME, value="h1").text
    assert "To-Do" in header_text

    # She is invited to enter a to-do list item straight away.
    inputbox = browser.find_element(by=By.ID, value="id_new_item")
    assert inputbox.get_attribute("placeholder") == "Enter a to-do list item"

    # She types "Buy peacock feathers" into a text box (Edith's hobby
    # is tying fly-fishing lures.
    inputbox.send_keys("Buy peacock feathers")

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table.
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    table = browser.find_element(by=By.ID, value="id_list_table")
    rows = table.find_elements(by=By.TAG_NAME, value="tr")
    assert any(
        row.text == "1: Buy peacock feathers" for row in rows
    ), "New to-do item does not appear in table"

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock features to make a fly" (Edith is very
    # methodical)
    assert False, "Finish the test!"

    # The page updates again, and now shows both items on her list.
