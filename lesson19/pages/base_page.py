import allure
# from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    TIMEOUT = 10

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open a browser')
    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        return self._wait().until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self._wait().until(EC.presence_of_all_elements_located(locator))

    def find_and_scroll(self, locator):
        element = self._wait().until(EC.presence_of_element_located(locator))
        self._scroll_to_element(element)
        return element


    def _scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _wait(self, timeout=TIMEOUT):
        return Wait(self.driver, timeout)

    # def element_is_visible(self, locator):
    #     self.scroll_to_element(self.element_is_present(locator))
    #     return self.wait().until(EC.visibility_of_element_located(locator))

    # @allure.step('Find visible elements')
    # def elements_are_visible(self, locator, timeout=TIMEOUT):
    #     return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # @allure.step('Find present elements')
    # def elements_are_present(self, locator, timeout=TIMEOUT):
    #     return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    # @allure.step('Find a not visible element')
    # def element_is_not_visible(self, locator, timeout=TIMEOUT):
    #     return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    #
    # @allure.step('Find clickable elements')
    # def element_is_clickable(self, locator, timeout=TIMEOUT):
    #     return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    # @allure.step('Go to specified element')
    # def go_to_element(self, element):
    #     self.driver.execute_script("arguments[0].scrollIntoView();", element)
    #
    # @allure.step('Double click')
    # def action_double_click(self, element):
    #     action = ActionChains(self.driver)
    #     action.double_click(element)
    #     action.perform()
    #
    # @allure.step('Right click')
    # def action_right_click(self, element):
    #     action = ActionChains(self.driver)
    #     action.context_click(element)
    #     action.perform()
    #
    # @allure.step('Drag and drop by offset')
    # def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
    #     action = ActionChains(self.driver)
    #     action.drag_and_drop_by_offset(element, x_coords, y_coords)
    #     action.perform()
    #
    # @allure.step('Drag and drop element to element')
    # def action_drag_and_drop_to_element(self, what, where):
    #     action = ActionChains(self.driver)
    #     action.drag_and_drop(what, where)
    #     action.perform()
    #
    # @allure.step('Move cursor to element')
    # def action_move_to_element(self, element):
    #     action = ActionChains(self.driver)
    #     action.move_to_element(element)
    #     action.perform()
    #
    # @allure.step('Remove footer')
    # def remove_footer(self):
    #     self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
    #     self.driver.execute_script("document.getElementsById('close-fixedban').remove();")
