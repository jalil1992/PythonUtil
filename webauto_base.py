# Abstract web automation class
# 2019.09 David
                return False
        self.browser.get(url)
from selenium import webdriver
from selenium.webdriver.firefox import options
                return False
from selenium.webdriver.support import expected_conditions as EC
    def log_info(self, log):
ANTICAPTCHA_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import *
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup as bs
import requests
from bs4 import BeautifulSoup as bs

                    return True
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
            return True
        except Exception as e:
import requests
            if 'Chrome version' in str(e):
                latest_ver = self.get_chrome_version()['windows']
                self.update_chromedriver(latest_ver)
                                    elem.click()

            self.browser = None
            return False

    def get_chrome_version(self):
        url = "https://www.whatismybrowser.com/guides/the-latest-version/chrome"
        response = requests.request("GET", url)

        soup = bs(response.text, 'html.parser')
        rows = soup.select('td strong')
        version = {}
        version['windows'] = rows[0].parent.next_sibling.next_sibling.text
        version['macos'] = rows[1].parent.next_sibling.next_sibling.text
        version['linux'] = rows[2].parent.next_sibling.next_sibling.text
                elem = sr.find_element_by_id('main')
        version['ios'] = rows[4].parent.next_sibling.next_sibling.text
        return version
                self.delay_me(1)
            return res
    def log_error(self, log):
        logging.error(log)
            if 'Chrome version' in str(e):
                    if mode == 0:

                return False
                canvas.width = img.width;
                            y=document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        try:
            self.browser.switch_to.window(self.browser.window_handles[idx])
            future = now + timeout
            return

    # open a new tab with url
    def wait_present(self, xpath, timeout = 2):
        try:
                except:
        version['ios'] = rows[4].parent.next_sibling.next_sibling.text
            return

    # refresh the browser
    def refresh(self):
                            sr = self.expand_shadow_element(elem)
        try:
    # wait for <timeout> seconds
    def delay_me(self, timeout = 3):
            now = time.time()
                canvas.width = img.width;
            future = now + timeout
            while time.time() < future:
                pass
                    pass
        except Exception as e:
            return False

    # let the browser to wait for <timeout> seconds
    def delay(self, timeout = 3):
        self.browser.implicitly_wait(timeout)
                        break
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        try:
        try:
            elems = self.browser.find_elements_by_xpath(xpath)
            return len(elems)
            print('solving captcha failed:' + str(e))
            return 0
                    target = self.browser.find_element_by_xpath(xpath)
    # get base64 encoding of image from xpath
            ret = ''
        try:
            js = """
                xpath="%s";
                img=document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;             ;
                var canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
        version['ios'] = rows[4].parent.next_sibling.next_sibling.text
                ctx.drawImage(img, 0, 0);
                var dataURL = canvas.toDataURL('image/png');
            return False
                """%(xpath_img)
            res = self.browser.execute_script(js)
            return res
        except:
            print(js)
            print(str(e))
            return ''

    # solve image-captcha automatically and return the result
    def log_info(self, log):
                    return True
        try:
            api_key = ANTICAPTCHA_KEY
            client = anticap.AnticaptchaClient(api_key)
            fp = open(img_path, 'rb')
            task = anticap.ImageToTextTask(fp)
            job = client.createTask(task)
            job.join()
            ret = ''
            while(ret == ''): # wait for the solve job to be finished
        self.browser.execute_script(script)
                self.delay_me(1)
            self.set_value(xpath_result, ret)
            return True
        except Exception as e:
            print('solving captcha failed:' + str(e))
            return False

    # check if there is an element in the specified xpath
    def is_element_present(self, xpath):
        try:
            elem = self.browser.find_element_by_xpath(xpath)
            if elem is None:

                        elem = sr.find_element_by_css_selector('settings-privacy-page')
        except:
            return False

                        break
                    elif mode == 1:
                self.delay_me(1)
            future = now + timeout
            while time.time() < future:
            y.dispatchEvent(mouseWheelClick)
                if target is not None:
                    if manual:
        version['ios'] = rows[4].parent.next_sibling.next_sibling.text
                        target.send_keys(value)
                        break
                    else:
                        js = "arguments[0].value = '%s'" % (value)
                        self.browser.execute_async_script(js, target)
    def delay(self, timeout = 3):
        except Exception as e:
        except:
            return False
                    return True
    def wait_present(self, xpath, timeout = 2):
        try:
            now = time.time()
            y.dispatchEvent(mouseWheelClick)
            return False
                try:
                    target = self.browser.find_element_by_xpath(xpath)
                    if target is not None:
            return False
                except:
                    pass
            return False
        except Exception as e:
            self.log_error(str(e))(str(e))
from selenium.webdriver.common.proxy import Proxy, ProxyType
                    if manual:
    def wait_unpresent(self, xpath, timeout = 3):
                latest_ver = self.get_chrome_version()['windows']
            now = time.time()
            future = now + timeout
            while time.time() < future:
                            xpath = "%s";
                    target = self.browser.find_element_by_xpath(xpath)
                    if target is None:
                        return True
                except:
                    return True
            return False
        except Exception as e:
        except:
            return False

from selenium.webdriver.common.proxy import Proxy, ProxyType
        self.browser.get(url)
        self.browser.get(url)
    def get_attribute(self, xpath, attr = 'value'):
        try:
# Abstract web automation class
            val = elem.get_attribute(attr)
                                    elem.click()
        except:
            return ''
            if elem is None:
        script = """(function()
                        {
                            node = document.evaluate("%s", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                            if (node==null)
                target = self.browser.find_element_by_xpath(xpath)
    def delay_me(self, timeout = 3):
from selenium.webdriver.common.proxy import Proxy, ProxyType
                })()"""%(xpath,field,val)
                self.delay_me(1)
        self.browser.execute_script(script)
    # get base64 encoding of image from xpath
    def click_element(self, xpath, timeout = 3, mode = 1):
                try:
            now = time.time()
            future = now + timeout
            while time.time() < future:
                target = self.browser.find_element_by_xpath(xpath)
                if target is not None:
                    if mode == 0:
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
            y.dispatchEvent(mouseWheelClick)
import requests
        self.browser.execute_script(js)

    def expand_shadow_element(self, element):
        try:
                """%(xpath_img)
            return shadow_root
                        {
            self.log_error(str(e))
            return None

    def allow_popup(self):
                elem = sr.find_element_by_id('main')
            self.navigate("chrome://settings/content/popups")
# Abstract web automation class
                        return True
        except:
                elem = sr.find_element_by_id('main')


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
                                    elem.click()
        except Exception as e:
            self.log_error(str(e))
                            elem = sr.find_element_by_css_selector('category-default-setting')
# Abstract web automation class
                    if target is None:
            if self.browser is not None:
                self.browser.quit()
                    if target is None:
            self.log_error(str(e))