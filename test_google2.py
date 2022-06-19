import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.mark.parametrize("text_search", [
    "cvcxbvxcbx 3 3 zzz",
    "ffwei 4hi5ty4w9tjw389u4t9w4j t"
])
def test_google2(text_search):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(text_search).press_enter()
    browser.element('//*[@role="heading"]/span/em').should(
        have.text(text_search))
    browser.element('[name="g tF2Cxc"]').should(be.not_.existing)
