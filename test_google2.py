import hashlib
import time
from selene import be
from selene.support.jquery_style_selectors import s
from selene.support.shared import browser




def test_case1():

    # Заполняем форму
    s('//*[@id="firstName"]').type('Jack')
    s('//*[@id="lastName"]').type('Shepard')
    s('//*[@id="userEmail"]').type('Jack@mail.ru')
    s('//*[@id="userNumber"]').type('4815162342')
    s('//*[@id="currentAddress"]').type('Oceanic')
    s('//*[@id="subjectsInput"]').type('H')


    element_click = ('//*[@id="react-select-2-option-0"]',
                     '//*[@id="dateOfBirthInput"]', '//*[@id="dateOfBirthInput"]',
                     '//*[contains(@aria-label,"20th")]',
                     '//*[@class="custom-control custom-radio custom-control-inline"]',
                     '//*[@class="custom-control custom-checkbox custom-control-inline"]/*[@value="1"]/..',
                     '//*[contains(text(),"Select State")]/..',
                     '//*[contains(text(),"NCR")]',
                     '//*[contains(text(),"Select City")]/..',
                     '//*[contains(text(),"Delhi")]')
    s('//*[@id="react-select-2-option-0"]').click()
    # Отправка картинки
    browser.element('//*[@id="uploadPicture"]').type('C:\\123.png')
    browser.element('//*[@id="submit"]').click()
    # Пришлось поставить Слип, не успевали подгружаться данные в таблицу, даже через JS waitPageLoad не помог
    time.sleep(1)
    el = browser.elements('td')
    elements_text = ''
    # Ожидаемый результат в md5
    elements_expected = '1a78428ae3be6b6389555ef11407145e'
    for el1 in el:
        elements_text += el1.text
    # Конверт полученных данных с таблицы в md5
    hash_expected = hashlib.md5(elements_text.encode())
    browser.element('//*[@id="closeLargeModal"]').click()
    empty_field = browser.element('//*[@id="firstName"]').text
    # Ассерт на чистку полей после закрытия таблицы
    assert empty_field == ''
    # Ассерт на верное отображение данных в таблице, после заполнения формы
    assert elements_expected == hash_expected.hexdigest()
