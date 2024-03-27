import os
from selene import browser, have

def test_demoqa_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('test@mail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('9989000000')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').send_keys('1999')
    browser.element('.react-datepicker__day--024').click()
    browser.element('#subjectsInput').type('test')
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys((os.path.abspath('image_test.jpg')))
    browser.element('#currentAddress').type('test_adress')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('delhi').press_enter()
    browser.element('#submit').click()


    #Проверка модального окна

    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('John Doe'))
    browser.element('.modal-body').should(have.text('test@mail.com'))
    browser.element('.modal-body').should(have.text('Female'))
    browser.element('.modal-body').should(have.text('9989000000'))
    browser.element('.modal-body').should(have.text('24 March,1999'))
    browser.element('.modal-body').should(have.text('Reading'))
    browser.element('.modal-body').should(have.text('image_test.jpg'))
    browser.element('.modal-body').should(have.text('test_adress'))
    browser.element('.modal-body').should(have.text('NCR Delhi'))
