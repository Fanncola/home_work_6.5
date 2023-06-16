import os

from selene import browser, have, command


def test_filling_form():
    # Открываем страницу формы
    browser.open('/automation-practice-form')

    # Проверяем title страницы
    browser.should(have.title('DEMOQA'))

    # Заполняем имя
    browser.element('#firstName').type('Demo')

    # Заполняем фамилию
    browser.element('#lastName').type('QA')

    # Заполняем почту
    browser.element('#userEmail').type('demoqa@demo.qa')

    # Выбираем пол
    browser.element('//label[contains(text(), "Male")]').click()

    # Заполняем номер телефона
    browser.element('#userNumber').type('1234567890')

    # Выбираем дату рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1988"]').click()
    browser.element('.react-datepicker__day--024').click()

    # Выбираем тематику
    browser.element('#subjectsInput').type('Co')
    browser.element('//*[.="Computer Science"]').click()

    # Выбираем хобби
    browser.element('//label[contains(text(), "Music")]').click()

    # Загружаем изображение
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/image.png'))

    # Заполняем адрес
    browser.element('#currentAddress').type('Asia/Kolkata')

    # Выбираем страну
    browser.element('#stateCity-wrapper') \
        .perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.element('//*[.="NCR"]').click()

    # Выбираем город
    browser.element('#city').click()
    browser.element('//*[.="Delhi"]').click()

    # Вытаскиваем сабмит формы
    browser.element('#state').click()
    browser.element('#submit').click().press_enter()

    # Проверяем наличие модального окна
    browser.element('#example-modal-sizes-title-lg') \
        .should(have.text('Thanks for submitting the form'))

    # Проверяем заполнение имени и фамилии
    browser.element('.table-responsive').should(have.text('Demo QA'))

    # Проверяем заполнение почты
    browser.element('.table-responsive').should(have.text('demoqa@demo.qa'))

    # Проверяем заполнение пола
    browser.element('.table-responsive').should(have.text('Male'))

    # Проверяем заполнение номера телефона
    browser.element('.table-responsive').should(have.text('1234567890'))

    # Проверяем заполнение даты рождения
    browser.element('.table-responsive').should(have.text('24 December,1988'))

    # Проверяем заполнение тематики
    browser.element('.table-responsive').should(have.text('Computer Science'))

    # Проверяем заполнение хобби
    browser.element('.table-responsive').should(have.text('Music'))

    # Проверяем название загруженного изображения
    browser.element('.table-responsive').should(have.text('image.png'))

    # Проверяем заполнение адреса
    browser.element('.table-responsive').should(have.text('Asia/Kolkata'))

    # Проверяем заполнение страны и города
    browser.element('.table-responsive').should(have.text('NCR Delhi'))

    # Закрыаем модальное окно
    browser.element('#closeLargeModal') \
        .perform(command.js.scroll_into_view).click()

    # Проверяем отсутствие модального окна
    browser.element('#example-modal-sizes-title-lg') \
        .should(have.no.text('Thanks for submitting the form'))
