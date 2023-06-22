import os

from selene import browser, have, command


def test_filling_form():
    browser.open('/automation-practice-form')

    browser.should(have.title('DEMOQA'))
    browser.element('#firstName').type('Demo')
    browser.element('#lastName').type('QA')
    browser.element('#userEmail').type('demoqa@demo.qa')
    browser.element('[name=gender][value=Male]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1988"]').click()
    browser.element('.react-datepicker__day--024').click()
    browser.element('#subjectsInput').type('Co')
    browser.element('//*[.="Computer Science"]').click()
    browser.element('//label[contains(text(), "Music")]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/image.png'))
    browser.element('#currentAddress').type('Asia/Kolkata')
    browser.element('#stateCity-wrapper') \
        .perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.element('//*[.="NCR"]').click()
    browser.element('#city').click()
    browser.element('//*[.="Delhi"]').click()
    browser.element('#state').click()
    browser.element('#submit').click().press_enter()

    browser.element('#example-modal-sizes-title-lg') \
        .should(have.text('Thanks for submitting the form'))

    browser.element('.table-responsive').should(have.text('Demo QA'))
    browser.element('.table-responsive').should(have.text('demoqa@demo.qa'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('1234567890'))
    browser.element('.table-responsive').should(have.text('24 December,1988'))
    browser.element('.table-responsive').should(have.text('Computer Science'))
    browser.element('.table-responsive').should(have.text('Music'))
    browser.element('.table-responsive').should(have.text('image.png'))
    browser.element('.table-responsive').should(have.text('Asia/Kolkata'))
    browser.element('.table-responsive').should(have.text('NCR Delhi'))
    browser.element('#closeLargeModal') \
        .perform(command.js.scroll_into_view).click()
    browser.element('#example-modal-sizes-title-lg') \
        .should(have.no.text('Thanks for submitting the form'))
