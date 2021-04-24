from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import settings
import time
import tools


class YahooPage():

    options = Options()
    # Through screenshots I know that when in headless mode the yahoo anti-bot
    # detection stops naviagtion. Though the repo run's often, error free in
    # headless mode, to run completely error free you must disable headless mode
    #options.add_argument('--headless')
    # adblocker extension is needed to hide ads that obscured elements
    options.add_argument('load-extension=' + settings.path_to_adBlock)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # the remaining options below help when running in headless mode
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--proxy-bypass-list=*')
    options.add_argument('--disable-web-security')

    def __init__(self, driver):
        self.driver = driver
        driver.get("https://www.yahoo.com")

        # after loading adBlock extension it opens in a new window's tab,
        # this tabs to the yahoo window
        self.switch_to_yahoo_window_tab()

    # Class Variable:
    random_option_title = ""

    # Error Messages

    def short_password_error_message(self):
        password_status_loc = (
            By.XPATH, '//span[contains(@id,"error-password-msg")]')
        password_status_element = wait(self.driver, 15).until(
            EC.presence_of_element_located(password_status_loc))
        return password_status_element

    def moderate_password_error_message(self):
        weak_password_status_loc = (By.XPATH,
                                    '//span[@data-error="WEAK_PASSWORD"]')
        # the wait below is necessary since yahoo always shows the weak
        # passord text before the moderate password text. I Made My Own
        # explicit wait, for this problem, that can be seen in the
        # diff_explicit_wait_ErrorMessagePassword branch. In README.txt
        # there are more notes on the pros and cons of these two solutions
        wait(self.driver, 15).until(EC.invisibility_of_element_located(
                                                     weak_password_status_loc))
        password_status_loc = (
            By.XPATH, '//span[contains(@id,"error-password-msg")]')
        return self.driver.find_element(*password_status_loc)

    def long_password_error_message(self):
        weak_password_status_loc = (By.XPATH,
                                    '//span[@data-error="WEAK_PASSWORD"]')
        moderate_password_status_loc = (By.XPATH,
                                        '//span[@data-error="ALMOST_THERE"]')
        # Both waits are needed since yahoo always shows weak password
        # then moderate password texts before, hopefully, showing the
        # strong password text.
        wait(self.driver, 15).until(EC.invisibility_of_element_located(
                                                     weak_password_status_loc))
        wait(self.driver, 15).until(EC.invisibility_of_element_located(
                                                 moderate_password_status_loc))
        password_status_loc = (
            By.XPATH, '//span[contains(@id,"error-password-msg")]')
        return self.driver.find_element(*password_status_loc)

    # Buttons

    def click_sign_in_button(self):
        sign_in_button_loc = (By.LINK_TEXT, 'Sign in')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(sign_in_button_loc))
        url_before_click = self.driver.current_url
        self.driver.find_element(*sign_in_button_loc).click()
        wait(self.driver, 15).until(EC.url_changes(url_before_click))

    def click_username_next_button(self):
        username_next_button_loc = (By.ID, "login-signin")
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(username_next_button_loc))
        self.driver.find_element(*username_next_button_loc).click()

    def click_password_next_button(self):
        self.driver.find_element(
            By.CLASS_NAME, "button-container").find_element(
                                          By.ID, 'login-signin').click()

    def click_search_button(self):
        search_button_loc = (By.XPATH, '//input[@type="submit"]')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(search_button_loc))
        url_before_click = self.driver.current_url
        self.driver.find_element(*search_button_loc).click()
        wait(self.driver, 15).until(EC.url_changes(url_before_click))

    # Fields

    def username_field(self):
        username_field_loc = (By.ID, 'login-username')
        wait(self.driver, 15).until(
            EC.presence_of_element_located(username_field_loc))
        return self.driver.find_element(*username_field_loc)

    def input_username_field(self, userName):
        self.username_field().send_keys(userName)

    def password_field(self):
        # Below is a locator for a dynaminc element that changes when the
        # cursor appears on the password field. This required its own waits
        password_field_loc = (
            By.XPATH, "//div[@class='input-group password-container focussed']")
        wait(self.driver, 10).until(
                            EC.presence_of_element_located(password_field_loc))
        input_password_field_loc = (By.XPATH, "//input[@id='login-passwd']")
        return self.driver.find_element(*input_password_field_loc)

    def input_password_field(self, passWord):
        self.password_field().send_keys(passWord)

    def new_password_field(self):
        new_password_field_loc = (By.XPATH, "//input[@name='password']")
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(new_password_field_loc))
        return self.driver.find_element(*new_password_field_loc)

    def input_new_password_field(self, newPassWord):
        self.new_password_field().send_keys(newPassWord)

    def search_field(self):
        search_field_loc = (By.ID, 'ybar-sbq')
        wait(self.driver, 15).until(
            EC.presence_of_element_located(search_field_loc))
        return self.driver.find_element(*search_field_loc)

    def search_field_id(self):
        return self.search_field().get_attribute('id')

    def input_search_field(self, search):
        self.search_field().send_keys(search)

    # Field Attributes

    def current_cursor_id(self):
        return self.driver.switch_to.active_element.get_attribute('id')

    def search_field_contents(self):
        return self.driver.find_element(
            By.XPATH, '//input[@type="text"]').get_attribute('value')

    # Popup

    def pop_up_apperears_tab_off_it(self):
        wait(self.driver, 10).until(EC.url_changes('yahoo.com'))
        current_tab = self.driver.current_window_handle
        # time.sleep(2) is needed to give the pop up time to appear. Outside of
        # using a pop up selenium tool this is the only way to handle this.
        time.sleep(2)
        self.driver.switch_to.window(current_tab)

    # Drop Downs

    def hover_over_profile_menu(self):
        profile_menu_loc = (By.XPATH, '//label[@id="ybarAccountMenuOpener"]')
        wait(self.driver, 15).until(
                            EC.visibility_of_element_located(profile_menu_loc))
        profile_menu_element = self.driver.find_element(*profile_menu_loc)
        ActionChains(self.driver).move_to_element(profile_menu_element).perform()

    def click_profile_menu_settings(self):
        setting_link_loc = (By.LINK_TEXT, 'Settings')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(setting_link_loc))
        self.driver.find_element(*setting_link_loc).click()

    def hover_over_originals_drop_down(self):
        originals_drop_down_loc = (By.XPATH, '//a[@title="Originals"]')
        wait(self.driver, 15).until(
            EC.visibility_of_element_located(originals_drop_down_loc))
        drop_down_element = self.driver.find_element(*originals_drop_down_loc)
        ActionChains(self.driver).move_to_element(drop_down_element).perform()

    # Tabs and Options

    def click_account_security_tab(self):
        account_security_loc = (By.PARTIAL_LINK_TEXT, 'Account Security')
        wait(self.driver, 15).until(
            EC.presence_of_element_located(account_security_loc))
        self.driver.find_element(*account_security_loc).click()

    def click_random_option_from_originals_drop_down(self):
        all_options_loc = (
            By.XPATH, '//a[@title="Originals"]/following-sibling::div//a')
        wait(self.driver, 15).until(
            EC.visibility_of_all_elements_located(all_options_loc))

        all_options = self.driver.find_elements(*all_options_loc)
        random_option = all_options[tools.generate_random_num(1, 3)]
        self.random_option_title = random_option.get_attribute('title')

        url_before_click = self.driver.current_url
        random_option.click()
        wait(self.driver, 15).until(EC.url_changes(url_before_click))

    # Links

    def click_change_password_link(self):
        change_password_loc = (By.PARTIAL_LINK_TEXT, 'Change password')
        wait(self.driver, 15).until(
            EC.element_to_be_clickable(change_password_loc))
        self.driver.find_element(*change_password_loc).click()

    def click_news_link(self):
        self.driver.find_element(By.LINK_TEXT, 'News').click()

    # Action Keys

    def tab_to_next_field(self):
        ActionChains(self.driver).send_keys(Keys.TAB).perform()

    # User Flow

    def login(self):
        self.click_sign_in_button()
        self.input_username_field(settings.yahoo_username)
        self.click_username_next_button()
        self.input_password_field(settings.yahoo_password)
        self.click_password_next_button()
        self.pop_up_apperears_tab_off_it()

    def navigate_to_security_tab(self):
        self.hover_over_profile_menu()
        self.click_profile_menu_settings()
        self.click_account_security_tab()

    # Special Functions

    def switch_to_yahoo_window_tab(self):
        yahoo_window = self.driver.current_window_handle
        self.driver.switch_to.window(yahoo_window)
