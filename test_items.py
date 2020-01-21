import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket_button_is_present_on_the_page(browser):
    browser.get(link)
    time.sleep(30)
    basket_buttons = browser.find_elements_by_css_selector('button.btn-add-to-basket')
    assert len(basket_buttons) > 0, 'Basket button does not present on the page'

