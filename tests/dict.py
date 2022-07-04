from selene import have, be, command
from selene.support.shared import browser
import pytest

def test_open_form():
    browser.open('/text-box')
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.exact_text('Text Box'))

    browser.element('#userName').type('Lika')
    browser.element('#userEmail').type('test@qmail.com')
    browser.element('#currentAddress').type('Universe')
    browser.element('#permanentAddress').type('Earth')

    # browser.element("[id^=google_ads]")._execute_script('element.remove()')
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    # удаление всех элементов
    # browser.all("[id^=google_ads]").perform(command.js.remove)

    # click через JS
    # browser.element('#submit').perform(command.js.click)

    browser.element('#output')
