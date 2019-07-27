from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, product_link)
    page.open()
    page.can_add_product_to_cart()
