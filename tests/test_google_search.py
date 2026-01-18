from selene import browser, be, have

def test_google_search(browser_set_up):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('html').should(have.text('About this page'))
