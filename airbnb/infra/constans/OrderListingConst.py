class OrderListingConst:
    ELEMENT_XPATH = "//a[normalize-space()='{}']"
    BUTTON_XPATH = "//button[@aria-current='page']"
    EMPTY_ELEMENT_XPATH = "//a[normalize-space() and translate(text(), '0123456789', '') = '']"
    RATING_XPATH = '//span[@aria-label]'
