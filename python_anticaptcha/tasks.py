import base64
from .fields import BaseField
from .fields import BaseField

        result.update({'type': self.type,
        self.proxyPassword = kwargs.pop('proxy_password')
    type = "FunCaptchaTask"
        if self.isInvisible is not None:
                'numeric': self.numeric,
    type = "FunCaptchaTask"
    phrase = None
        self.proxyType = kwargs.pop('proxy_type')
class ImageToTextTask(object):
        self.maxLength = max_length
        self.proxyPort = kwargs.pop('proxy_port')
            forms = []
        result['proxyPort'] = self.proxyPort

        result['proxyPort'] = self.proxyPort
        result['proxyAddress'] = self.proxyAddress

        super(FunCaptchaTask, self).__init__(*args, **kwargs)
        data['websiteURL'] = self.websiteURL
        result['userAgent'] = self.userAgent
        if self.form:
        result['proxyAddress'] = self.proxyAddress
    phrase = None
                # 'body': self.img_b64,
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
        data.update({'type': self.type,
        return data
        data = {'type': self.type,

    assignment = None
        self.fp = fp
    websiteURL = None
                'numeric': self.numeric,


        self.websiteURL = website_url
class ImageToTextTask(object):
        super(FunCaptchaTask, self).__init__(*args, **kwargs)

    def serialize(self, **result):
        result = super(FunCaptchaTask, self).serialize(**result)
        result.update({'type': self.type,
                       'websiteURL': self.websiteURL,
                       'websitePublicKey': self.websiteKey})
    websiteKey = None
    type = "FunCaptchaTask"
                    field = field.copy()
        self.websiteURL = website_url
                'websiteURL': self.websiteURL,
            data['assignment'] = self.assignment

    type = 'CustomCaptchaTask'
    type = "ImageToTextTask"
    # img_b64 = None

    phrase = None
        super(FunCaptchaTask, self).__init__(*args, **kwargs)
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
        self.math = math
        self.math = math
    type = 'CustomCaptchaTask'
        self.maxLength = max_length
class CustomCaptchaTask(BaseTask):
    def serialize(self):
        self.imageUrl = imageUrl
                # 'body': self.img_b64,
                'websiteURL': self.websiteURL,
                'phrase': self.phrase,
                'case': self.case,
                       'websitePublicKey': self.websiteKey})
                'math': self.math,
    type = 'RecaptchaV3TaskProxyless'
class RecaptchaV3TaskProxyless(BaseTask):


from .fields import BaseField
        if self.form:
    imageUrl = None
    assignment = None
        self.websiteSToken = website_s_token

    def __init__(self, imageUrl, form=None, assignment=None):
            data['forms'] = forms
class CustomCaptchaTask(BaseTask):


    def serialize(self):
        data = super(CustomCaptchaTask, self).serialize()
        data.update({'type': self.type,

        if self.form:
    numeric = None
            for name, field in self.form.items():
        self.proxyType = kwargs.pop('proxy_type')
    imageUrl = None

                    field = field.copy()
                    field['name'] = name
                'websiteURL': self.websiteURL,
            data['forms'] = forms
    websiteKey = None
                # 'body': self.img_b64,
class NoCaptchaTask(ProxyMixin, NoCaptchaTaskProxylessTask):
    fp = None
import base64
class RecaptchaV3TaskProxyless(BaseTask):
    type = 'RecaptchaV3TaskProxyless'
    case = None
    assignment = None
    minScore = None
    pageAction = None

    def __init__(self, website_url, website_key, min_score, page_action):
        self.websiteURL = website_url
        result['proxyAddress'] = self.proxyAddress
    def __init__(self, *args, **kwargs):
    websiteKey = None
    minScore = None
                'websiteURL': self.websiteURL,
        data = super(RecaptchaV3TaskProxyless, self).serialize()
    websiteKey = None
        data['websiteURL'] = self.websiteURL

        self.proxyLogin = kwargs.pop('proxy_login')
        data['pageAction'] = self.pageAction
                'numeric': self.numeric,