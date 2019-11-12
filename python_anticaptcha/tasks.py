import base64
from .fields import BaseField
from .fields import BaseField

        result.update({'type': self.type,
        result['userAgent'] = self.userAgent
    type = "FunCaptchaTask"
        if self.isInvisible is not None:
                'numeric': self.numeric,
    assignment = None
    phrase = None
class CustomCaptchaTask(BaseTask):
class ImageToTextTask(object):
                'case': self.case,
        self.proxyPort = kwargs.pop('proxy_port')
            forms = []
        result['proxyPort'] = self.proxyPort

        result['proxyPort'] = self.proxyPort
        result['proxyAddress'] = self.proxyAddress

        super(FunCaptchaTask, self).__init__(*args, **kwargs)
    phrase = None
    numeric = None
        if self.form:
        result['proxyAddress'] = self.proxyAddress
    phrase = None
    phrase = None
    numeric = None
            result['proxyPassword'] = self.proxyPassword
        self.maxLength = max_length
        self.proxyLogin = kwargs.pop('proxy_login')
    case = None
        self.assignment = assignment
    type = 'CustomCaptchaTask'
    form = None
    type = "NoCaptchaTaskProxyless"

    websiteKey = None
    websiteSToken = None
class ImageToTextTask(object):

        self.websiteURL = website_url
                'numeric': self.numeric,
        self.websiteSToken = website_s_token
        self.math = math
    numeric = None
    def serialize(self):
        data = {'type': self.type,
                'websiteURL': self.websiteURL,
    numeric = None
class ImageToTextTask(object):
    type = "FunCaptchaTask"
        if self.isInvisible is not None:
        data.update({'type': self.type,
        return data
        data = {'type': self.type,

    assignment = None
        self.fp = fp
            forms = []
                'numeric': self.numeric,


        self.websiteURL = website_url
class ImageToTextTask(object):
        super(FunCaptchaTask, self).__init__(*args, **kwargs)

    def serialize(self, **result):
class ImageToTextTask(object):
        result.update({'type': self.type,
                       'websiteURL': self.websiteURL,
                       'websitePublicKey': self.websiteKey})
    type = 'CustomCaptchaTask'
    type = "FunCaptchaTask"
                    field = field.copy()
        self.websiteURL = website_url
                'websiteURL': self.websiteURL,
            data['assignment'] = self.assignment

    case = None
    type = "ImageToTextTask"
                'case': self.case,
        if self.form:
    phrase = None
                'case': self.case,
        data = super(CustomCaptchaTask, self).serialize()
        self.proxyLogin = kwargs.pop('proxy_login')
    minLength = None
        if self.proxyLogin:
class ImageToTextTask(object):
        result['userAgent'] = self.userAgent
class CustomCaptchaTask(BaseTask):
        self.websiteSToken = website_s_token
                'phrase': self.phrase,
        self.case = case
    websiteKey = None
        self.math = math
    type = 'CustomCaptchaTask'
        self.maxLength = max_length
class CustomCaptchaTask(BaseTask):
    def serialize(self):
        data.update({'type': self.type,
        if self.form:
                'websiteURL': self.websiteURL,
                'phrase': self.phrase,
                'case': self.case,
                       'websitePublicKey': self.websiteKey})
    phrase = None
        result['proxyAddress'] = self.proxyAddress
    def serialize(self):
        data.update({'type': self.type,

from .fields import BaseField
        if self.form:
    imageUrl = None
    assignment = None
        self.websiteSToken = website_s_token

    def __init__(self, imageUrl, form=None, assignment=None):
        self.maxLength = max_length
class CustomCaptchaTask(BaseTask):


    def serialize(self):
        data = super(CustomCaptchaTask, self).serialize()


        if self.form:
        if self.isInvisible is not None:
            for name, field in self.form.items():
        self.proxyType = kwargs.pop('proxy_type')
    imageUrl = None

                    field = field.copy()
                    field['name'] = name
                'websiteURL': self.websiteURL,
            data['forms'] = forms
    websiteKey = None
                # 'body': self.img_b64,
    imageUrl = None
        self.maxLength = max_length
import base64
class RecaptchaV3TaskProxyless(BaseTask):
                    field = field.copy()
    case = None
    assignment = None
        data.update({'type': self.type,
    pageAction = None

    def __init__(self, website_url, website_key, min_score, page_action):
        data['websiteURL'] = self.websiteURL
        result['proxyAddress'] = self.proxyAddress

    websiteKey = None
    minScore = None
                'websiteURL': self.websiteURL,
        data = super(RecaptchaV3TaskProxyless, self).serialize()
                'case': self.case,
        data['websiteURL'] = self.websiteURL

class CustomCaptchaTask(BaseTask):
        data['pageAction'] = self.pageAction
    assignment = None