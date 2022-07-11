import os.path
import time

from selene import have, be, command
from selene.support.shared import browser
import pytest
from qaguru_demoqa_5.controls.upload_picture import resource

first_name = 'Lika'
last_name = 'Kasimova'
email = 'test@gmail.com'
telephone_number = '9101111111'

def test_fill_in_form():
    browser.open('/automation-practice-form')
    browser.all('[id*="Advertisement"]').perform(command.js.remove)
    browser.all('[id*="google_ads"]').perform(command.js.remove)
    browser.all('#fixedban').perform(command.js.remove)

    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)

    browser.element('[for="gender-radio-2"]').click()

    browser.element('#userNumber').type(telephone_number)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text('1990')).click()
    browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text('May')).click()
    browser.element('.react-datepicker__day--020').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter().type('Math').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../picture/dog.png'))

    browser.element('#currentAddress').type('World city')

    browser.element('#state').element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').perform(command.js.click)
    

    # ASSERT
    browser.all('table tr').element(1).should(have.text('Lika Kasimova'))
    browser.all('table tr').element(2).should(have.text('test@gmail.com'))
    browser.all('table tr').element(3).should(have.text('Female'))
    browser.all('table tr').element(4).should(have.text('9101111111'))
    browser.all('table tr').element(5).should(have.text('20 May,1990'))
    browser.all('table tr').element(6).should(have.text('Computer Science, Maths'))
    browser.all('table tr').element(7).should(have.text('Sports, Reading, Music'))
    browser.all('table tr').element(8).should(have.text('dog.png'))
    browser.all('table tr').element(9).should(have.text('World city'))
    browser.all('table tr').element(10).should(have.text('NCR Delhi'))

    time.sleep(5)


