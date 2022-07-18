import os.path
import time
from selene import have, command
from selene.support.shared import browser
from qaguru_demoqa_5.controls.autocomplete_helper import AutocompleteHelper

# User data dict
user_data = {
    'first_name': 'Lika',
    'last_name': 'Kasimova',
    'gender': 'Female',
    'email': 'test@gmail.com',
    'phone_number': '9101111111',
    'date_of_birth': {'day': '20', 'month': 'May', 'year': '1990'},
    'picture': {'path': '../picture/dog.png', 'file_name': 'dog.png'},
    'subjects': ['Computer Science', 'Maths'],
    'hobbies': ['Reading', 'Music', 'Sports'],
    'address': {'state': 'Haryana', 'city': 'Karnal', 'current': 'World city'}
}

# Connected strings of user full name, subjects, date of birth, hobbies and address
user_full_name = ' '.join([user_data['first_name'], user_data['last_name']])  # -> Lika Kasimova
user_subjects_string = ', '.join(user_data['subjects'])  # -> Computer Science, Maths
user_hobbies = ', '.join(user_data['hobbies'])
user_full_date_of_birth = f'{user_data["date_of_birth"]["day"]} {user_data["date_of_birth"]["month"]},' \
                          f'{user_data["date_of_birth"]["year"]}'  # -> 20 May,1990
user_full_address = ' '.join([user_data['address']['state'], user_data['address']['city']])  # -> Haryana Karnal


def test_fill_in_form():
    browser.open('/automation-practice-form')
    browser.all('[id*="Advertisement"]').perform(command.js.remove)
    browser.all('[id*="google_ads"]').perform(command.js.remove)
    browser.all('#fixedban').perform(command.js.remove)

    # Input user full name
    browser.element('#firstName').type(user_data['first_name'])
    browser.element('#lastName').type(user_data['last_name'])
    browser.element('#userEmail').type(user_data['email'])

    # Set gender
    if user_data['gender'] == 'Female':
        browser.element('[for="gender-radio-2"]').click()
    elif user_data['gender'] == 'Male':
        browser.element('[for="gender-radio-1"]').click()
    else:
        browser.element('[for="gender-radio-3"]').click()

    # Set user number
    browser.element('#userNumber').type(user_data['phone_number'])

    # Set date of birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(
        user_data['date_of_birth']['year'])).click()

    browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(
        user_data['date_of_birth']['month'])).click()

    browser.element(f'.react-datepicker__day--0{user_data["date_of_birth"]["day"]}').click()

    # Set subjects
    autocomplete_helper = AutocompleteHelper(browser)
    autocomplete_helper.by_tab_button('#subjectsInput', user_data['subjects'][0][0:4])  # -> Computer Science
    autocomplete_helper.by_full_name('#subjectsInput', '.subjects-auto-complete__option',
                                     user_data['subjects'][1][0: 3], user_data['subjects'][1])  # -> Maths

    # Toggle hobbies checkboxes
    for hobby in user_data['hobbies']:
        browser.element(f'//label[text()="{hobby}"]').click()

    # Upload Picture if exists
    browser.element('#uploadPicture').send_keys(os.path.abspath(user_data['picture']['path']))

    # Input Current Address
    browser.element('#currentAddress').type(user_data['address']['current'])

    # Choose State and City
    autocomplete_helper.by_tab_button('#react-select-3-input', user_data['address']['state'])
    autocomplete_helper.by_tab_button('#react-select-4-input', user_data['address']['city'])

    # Submit Form
    browser.element('#submit').perform(command.js.click)

    # ASSERTIONS
    browser.all('table tr').element(1).should(have.text(user_full_name))
    browser.all('table tr').element(2).should(have.text(user_data['email']))
    browser.all('table tr').element(3).should(have.text(user_data['gender']))
    browser.all('table tr').element(4).should(have.text(user_data['phone_number']))
    browser.all('table tr').element(5).should(have.text(user_full_date_of_birth))
    browser.all('table tr').element(6).should(have.text(user_subjects_string))
    browser.all('table tr').element(7).should(have.text(user_hobbies))
    browser.all('table tr').element(8).should(have.text(user_data['picture']['file_name']))
    browser.all('table tr').element(9).should(have.text(user_data['address']['current']))
    browser.all('table tr').element(10).should(have.text(user_full_address))

    time.sleep(5)
