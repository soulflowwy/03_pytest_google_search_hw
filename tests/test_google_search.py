from selene import browser, be, have

def test_google_search(browser_set_up):
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('html').should(have.text('About this page'))

def test_google_search_negative(browser_set_up):
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type(';;;;;;sadjdsakdk asdjkas kds kjasd sadldjkl jasd ------------').press_enter()
    browser.element('body').should(have.text('Your search - ;;;;;;sadjdsakdk asdjkas kds kjasd sadldjkl jasd ------------ - did not match any documents.'))