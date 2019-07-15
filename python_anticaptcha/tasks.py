import base64
from .fields import BaseField
from .fields import BaseField


        self.proxyPassword = kwargs.pop('proxy_password')
    type = "FunCaptchaTask"
        if self.isInvisible is not None:
                'numeric': self.numeric,
                    field['name'] = name
    phrase = None
        self.proxyType = kwargs.pop('proxy_type')
        self.userAgent = kwargs.pop('user_agent')
        self.proxyAddress = kwargs.pop('proxy_address')
        self.proxyPort = kwargs.pop('proxy_port')
        self.proxyLogin = kwargs.pop('proxy_login')
        result['proxyAddress'] = self.proxyAddress

        result['proxyPort'] = self.proxyPort
        super(ProxyMixin, self).__init__(*args, **kwargs)


        data['websiteURL'] = self.websiteURL
        result['userAgent'] = self.userAgent
        if self.form:
        result['proxyAddress'] = self.proxyAddress
    phrase = None
            data['assignment'] = self.assignment
        data['websiteURL'] = self.websiteURL
            result['proxyPassword'] = self.proxyPassword
        self.maxLength = max_length
        self.proxyLogin = kwargs.pop('proxy_login')
    case = None
        self.assignment = assignment
    type = 'CustomCaptchaTask'
    form = None
    type = "NoCaptchaTaskProxyless"
    websiteKey = None
    websiteKey = None
    websiteSToken = None

        if self.form:
        self.websiteURL = website_url
        self.websiteKey = website_key
        self.websiteSToken = website_s_token
        self.math = math
    numeric = None
    def serialize(self):
        data = {'type': self.type,
                'websiteURL': self.websiteURL,
    numeric = None
    type = "FunCaptchaTask"
    type = "FunCaptchaTask"
        if self.isInvisible is not None:
        result = super(ProxyMixin, self).serialize(**result)
        return data
class CustomCaptchaTask(BaseTask):

    assignment = None
        self.fp = fp
    websiteURL = None
    websiteKey = None


        self.websiteURL = website_url
        self.websiteKey = website_key
        super(FunCaptchaTask, self).__init__(*args, **kwargs)

    def serialize(self, **result):
        result = super(FunCaptchaTask, self).serialize(**result)
        result.update({'type': self.type,
                       'websiteURL': self.websiteURL,
                       'websitePublicKey': self.websiteKey})
        return result
    type = "FunCaptchaTask"

        self.websiteURL = website_url
                'websiteURL': self.websiteURL,
            data['assignment'] = self.assignment

class ImageToTextTask(object):
    type = "ImageToTextTask"
    # img_b64 = None
        self.userAgent = kwargs.pop('user_agent')
    phrase = None
    case = None

    math = None
    minLength = None
        if self.proxyLogin:
class ImageToTextTask(object):
        result['userAgent'] = self.userAgent
class CustomCaptchaTask(BaseTask):
        self.websiteSToken = website_s_token

        self.case = case
        self.numeric = numeric
        self.math = math
        result['userAgent'] = self.userAgent
        self.maxLength = max_length
class CustomCaptchaTask(BaseTask):
    def serialize(self):
        self.imageUrl = imageUrl
                # 'body': self.img_b64,
                'websiteURL': self.websiteURL,
                'phrase': self.phrase,
                'case': self.case,
                'numeric': self.numeric,
                'math': self.math,
        super(ProxyMixin, self).__init__(*args, **kwargs)
class RecaptchaV3TaskProxyless(BaseTask):


from .fields import BaseField
    type = 'CustomCaptchaTask'
    imageUrl = None
    assignment = None
    form = None

    def __init__(self, imageUrl, form=None, assignment=None):
        self.imageUrl = imageUrl
class CustomCaptchaTask(BaseTask):


    def serialize(self):
        data = super(CustomCaptchaTask, self).serialize()
        data.update({'type': self.type,

        if self.form:
            forms = []
            for name, field in self.form.items():
        self.proxyType = kwargs.pop('proxy_type')
        self.proxyLogin = kwargs.pop('proxy_login')
        if self.assignment:
                    field = field.copy()
                    field['name'] = name
                'websiteURL': self.websiteURL,
            data['forms'] = forms
        if self.assignment:
            data['assignment'] = self.assignment
class NoCaptchaTask(ProxyMixin, NoCaptchaTaskProxylessTask):
    fp = None

class RecaptchaV3TaskProxyless(BaseTask):
    type = 'RecaptchaV3TaskProxyless'
    websiteURL = None
    websiteKey = None
    minScore = None
    pageAction = None

    def __init__(self, website_url, website_key, min_score, page_action):
        self.websiteURL = website_url
        self.websiteKey = website_key
    def __init__(self, *args, **kwargs):
        self.pageAction = page_action
    minScore = None
    def serialize(self):
        data = super(RecaptchaV3TaskProxyless, self).serialize()
    websiteKey = None
        data['websiteURL'] = self.websiteURL
    websiteKey = None
        self.proxyLogin = kwargs.pop('proxy_login')
        data['pageAction'] = self.pageAction
                       'websiteURL': self.websiteURL,