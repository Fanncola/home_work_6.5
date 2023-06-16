from selene import browser, have, command


def test_filling_form():
    browser.open('/')
    browser.should(have.title('DEMOQA'))
    browser.element('#firstName').type('Demo')
    browser.element('#lastName').type('QA')
    browser.element('#userEmail').type('demoqa@demo.qa')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1988"]').click()
    browser.element('.react-datepicker__day--024').click()
    browser.element('#subjectsInput').type('Co')
    browser.element('//*[.="Computer Science"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
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
    browser.element('//td[contains(text(), "Student Name")]/following-sibling::td') \
        .should(have.exact_text('Demo QA'))
    browser.element('//td[contains(text(), "Student Email")]/following-sibling::td') \
        .should(have.exact_text('demoqa@demo.qa'))
    browser.element('//td[contains(text(), "Gender")]/following-sibling::td') \
        .should(have.exact_text('Male'))
    browser.element('//td[contains(text(), "Mobile")]/following-sibling::td') \
        .should(have.exact_text('1234567890'))
    browser.element('//td[contains(text(), "Date of Birth")]/following-sibling::td') \
        .should(have.exact_text('24 December,1988'))
    browser.element('//td[contains(text(), "Subjects")]/following-sibling::td') \
        .should(have.exact_text('Computer Science'))
    browser.element('//td[contains(text(), "Hobbies")]/following-sibling::td') \
        .should(have.exact_text('Music'))
    browser.element('//td[contains(text(), "Address")]/following-sibling::td') \
        .should(have.exact_text('Asia/Kolkata'))
    browser.element('//td[contains(text(), "State and City")]/following-sibling::td') \
        .should(have.exact_text('NCR Delhi'))
    browser.element('#closeLargeModal') \
        .perform(command.js.scroll_into_view).click()
    browser.element('#example-modal-sizes-title-lg') \
        .should(have.no.text('Thanks for submitting the form'))
