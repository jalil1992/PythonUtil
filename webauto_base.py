            elem = self.browser.find_element_by_xpath(xpath)
# 2019.09 David
                return False
        self.browser.get(url)
            if elem is None:
            return False
                return False
        self.browser.execute_script(js)
    def log_info(self, log):
ANTICAPTCHA_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
            return False
from selenium.webdriver.chrome.options import Options
                latest_ver = self.get_chrome_version()['windows']
from selenium.common.exceptions import TimeoutException
            while time.time() < future:
from bs4 import BeautifulSoup as bs
ANTICAPTCHA_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
from bs4 import BeautifulSoup as bs

            return 0
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def __init__(self):
ANTICAPTCHA_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
            return False
                        break
    def __init__(self):
        pass

    # Start chrome browser for automation
    def wait_present(self, xpath, timeout = 2):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            self.browser = webdriver.Chrome(executable_path='chromedriver', chrome_options = chrome_options)
                        break
        except Exception as e:
import requests
            if 'Chrome version' in str(e):
                latest_ver = self.get_chrome_version()['windows']
                self.update_chromedriver(latest_ver)
                                    elem.click()

            self.browser = None
                try:

    def get_chrome_version(self):
    # get base64 encoding of image from xpath
                    if target is not None:
                    if target is None:
        soup = bs(response.text, 'html.parser')
        rows = soup.select('td strong')
        version = {}
        version['windows'] = rows[0].parent.next_sibling.next_sibling.text
        version['macos'] = rows[1].parent.next_sibling.next_sibling.text
        version['linux'] = rows[2].parent.next_sibling.next_sibling.text
                elem = sr.find_element_by_id('main')
                    pass
        return version
                self.delay_me(1)
            return res
    def log_error(self, log):
            while time.time() < future:
            if 'Chrome version' in str(e):
                    if mode == 0:

                return False
                canvas.width = img.width;
        self.browser.execute_script(js)
        try:
            self.browser.switch_to.window(self.browser.window_handles[idx])
            future = now + timeout
            return

                pass
    def wait_present(self, xpath, timeout = 2):
        try:
        try:
        version['ios'] = rows[4].parent.next_sibling.next_sibling.text
            return

                    sr = self.expand_shadow_element(elem)
    def refresh(self):
                            sr = self.expand_shadow_element(elem)
        try:
    # wait for <timeout> seconds
    def delay_me(self, timeout = 3):
            now = time.time()
                canvas.width = img.width;
            future = now + timeout
                    if mode == 0:
                pass
                    pass
        except Exception as e:
            return False
            if 'Chrome version' in str(e):
    # let the browser to wait for <timeout> seconds
    def delay(self, timeout = 3):
        self.browser.implicitly_wait(timeout)
                        break
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        try:
                    elem = sr.find_element_by_css_selector('settings-basic-page')
            elems = self.browser.find_elements_by_xpath(xpath)
            return len(elems)
            print('solving captcha failed:' + str(e))
            return 0
                            y=document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        pass
        try:
        try:
            js = """
                xpath="%s";
                img=document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;             ;
                var canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
            future = now + timeout
                ctx.drawImage(img, 0, 0);
                ctx.drawImage(img, 0, 0);
            return False
                """%(xpath_img)
            res = self.browser.execute_script(js)
                try:
        try:
            return
            print(str(e))
            return 0

    # solve image-captcha automatically and return the result
    def log_info(self, log):
from selenium.common.exceptions import TimeoutException
        try:
            api_key = ANTICAPTCHA_KEY
                return False
            fp = open(img_path, 'rb')
            task = anticap.ImageToTextTask(fp)
            job = client.createTask(task)
            job.join()
            ret = ''
                        target.send_keys(value)
        self.browser.execute_script(script)
from selenium.common.exceptions import TimeoutException
            self.log_error(str(e))
            return True
from selenium.webdriver.chrome.options import Options
            print('solving captcha failed:' + str(e))
            return False

from selenium.webdriver.common.proxy import *
    def is_element_present(self, xpath):
        try:
            elem = self.browser.find_element_by_xpath(xpath)
            if elem is None:

                        elem = sr.find_element_by_css_selector('settings-privacy-page')
# Abstract web automation class
            return False

                        break
                    elif mode == 1:
                self.delay_me(1)
            future = now + timeout
            while time.time() < future:
            y.dispatchEvent(mouseWheelClick)
        except Exception as e:
    def __init__(self):
        version['ios'] = rows[4].parent.next_sibling.next_sibling.text
                        target.send_keys(value)
    def wait_present(self, xpath, timeout = 2):
                        break
                    else:
                        self.browser.execute_async_script(js, target)
    def delay(self, timeout = 3):
        except Exception as e:
        except:
            return False
                    return True
            return False
        try:
            now = time.time()
            y.dispatchEvent(mouseWheelClick)
            return False
    def wait_unpresent(self, xpath, timeout = 3):
                    target = self.browser.find_element_by_xpath(xpath)
                    if target is not None:
            return False
                except:
                    pass
            return False

                    pass
from selenium.webdriver.common.proxy import Proxy, ProxyType
                    if manual:
    def wait_unpresent(self, xpath, timeout = 3):
                latest_ver = self.get_chrome_version()['windows']
            now = time.time()
            future = now + timeout
# Abstract web automation class
                            xpath = "%s";
                        target.send_keys(value)
                    if target is None:
                        return True
                except:
                    return True
            return False
        except Exception as e:
        except:
        self.browser.get(url)

from selenium.webdriver.common.proxy import Proxy, ProxyType
                    if mode == 0:
        self.browser.get(url)
    def get_attribute(self, xpath, attr = 'value'):
        try:
            future = now + timeout
            val = elem.get_attribute(attr)
        return version
        except:
                    if target is None:
            if elem is None:
        script = """(function()
        except Exception as e:
                            node = document.evaluate("%s", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                            if (node==null)
                target = self.browser.find_element_by_xpath(xpath)
    def delay_me(self, timeout = 3):
from selenium.webdriver.common.proxy import Proxy, ProxyType
                })()"""%(xpath,field,val)
                self.delay_me(1)
        self.browser.execute_script(script)
    # get base64 encoding of image from xpath
# Abstract web automation class
                try:
            now = time.time()
            future = now + timeout
            while time.time() < future:
                            elem = sr.find_element_by_css_selector('category-default-setting')
                if target is not None:
            return
                        target.click()
                    elif mode == 1:
                        js = """
                    sr = self.expand_shadow_element(elem)
                            y=document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        try:
                            """%(xpath)
                        self.browser.execute_script(js)
                    return True
            return False

            self.log_error(str(e))

    def middle_click(self, xpath, timeout = 3):
                self.delay_me(1)
                    pass
            var mouseWheelClick = new MouseEvent('click', {'button': 1, 'which': 1 });
    def is_element_present(self, xpath):
                    return True
import requests
        self.browser.execute_script(js)

    def expand_shadow_element(self, element):
        try:
                """%(xpath_img)
            return shadow_root
                        {
                try:
            return None

    def allow_popup(self):
                elem = sr.find_element_by_id('main')
            self.navigate("chrome://settings/content/popups")
# Abstract web automation class
                        return True
        except:
                elem = sr.find_element_by_id('main')
            return False

                    elem = sr.find_element_by_css_selector('settings-basic-page')
                    sr = self.expand_shadow_element(elem)
                    if sr is not None:
                        elem = sr.find_element_by_css_selector('settings-privacy-page')
    def middle_click(self, xpath, timeout = 3):
    def wait_present(self, xpath, timeout = 2):
                            elem = sr.find_element_by_css_selector('category-default-setting')
                try:
                            if sr is not None:
            while time.time() < future:
                                if elem is not None:
            chrome_options.add_argument("--no-sandbox")
        except Exception as e:
                    return True
                            elem = sr.find_element_by_css_selector('category-default-setting')
# Abstract web automation class
                    if target is None:
            if self.browser is not None:
                self.browser.quit()
                    if target is None:
            self.log_error(str(e))