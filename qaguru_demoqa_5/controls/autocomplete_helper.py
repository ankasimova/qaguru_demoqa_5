from selene import have

class AutocompleteHelper:
    def __init__(self, browser):
        self.browser = browser

    def by_tab_button(self, input_locator, first_letters):
        """
        :param input_locator: Input field locator
        :param first_letters: First letter(s) of target word
        Autocomplete subject by pressing the TAB button
        """

        self.browser.element(input_locator).type(first_letters).press_tab()

    def by_full_name(self, input_locator, list_locator, first_letters, target_full_name):
        """
        :param input_locator: Input field locator
        :param list_locator: Suggestion list locator
        :param first_letters: First letter(s) of target word
        :param target_full_name: Full target word
        Autocomplete subject by suggestion list
        """

        self.browser.element(input_locator). \
            type(first_letters)
        self.browser.all(list_locator). \
            element_by(have.text(target_full_name)).click()
