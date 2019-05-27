import base64
from .fields import BaseField
                if isinstance(field, BaseField):

class BaseTask(object):
    def serialize(self, **result):
        self.proxyLogin = kwargs.pop('proxy_login')
        if self.isInvisible is not None:
                'numeric': self.numeric,
                    field['name'] = name
    phrase = None
        self.proxyType = kwargs.pop('proxy_type')
        self.userAgent = kwargs.pop('user_agent')
        self.proxyAddress = kwargs.pop('proxy_address')
        self.proxyPort = kwargs.pop('proxy_port')
        self.proxyLogin = kwargs.pop('proxy_login')
        self.proxyPassword = kwargs.pop('proxy_password')

        result['proxyPort'] = self.proxyPort
        super(ProxyMixin, self).__init__(*args, **kwargs)


        result = super(ProxyMixin, self).serialize(**result)
        result['userAgent'] = self.userAgent
        result['proxyType'] = self.proxyType
        result['proxyAddress'] = self.proxyAddress
    phrase = None
        if self.proxyLogin:
        result['proxyPort'] = self.proxyPort
            result['proxyPassword'] = self.proxyPassword
        self.maxLength = max_length
            result['cookies'] = self.cookies
    case = None
        self.assignment = assignment
    type = 'CustomCaptchaTask'
    form = None
    type = "NoCaptchaTaskProxyless"
    websiteURL = None
    websiteKey = None
    websiteSToken = None

    def __init__(self, website_url, website_key, website_s_token=None, is_invisible=None):
        self.websiteURL = website_url
        self.websiteKey = website_key
        self.websiteSToken = website_s_token
        self.math = math
    numeric = None
    def serialize(self):
        data = {'type': self.type,
                'websiteURL': self.websiteURL,

        if self.websiteSToken is not None:
            data['websiteSToken'] = self.websiteSToken
        if self.isInvisible is not None:
        result = super(ProxyMixin, self).serialize(**result)
        return data
class CustomCaptchaTask(BaseTask):

        self.numeric = numeric
    type = "FunCaptchaTask"
    websiteURL = None
    websiteKey = None

    def __init__(self, website_url, website_key, *args, **kwargs):
        self.websiteURL = website_url
        self.websiteKey = website_key
        super(FunCaptchaTask, self).__init__(*args, **kwargs)

    def serialize(self, **result):
        result = super(FunCaptchaTask, self).serialize(**result)
        result.update({'type': self.type,
                       'websiteURL': self.websiteURL,
                       'websitePublicKey': self.websiteKey})
        return result



    type = "NoCaptchaTask"


class ImageToTextTask(object):
    type = "ImageToTextTask"
    # img_b64 = None
    fp = None
    phrase = None
    case = None
            data['forms'] = forms
    math = None
    minLength = None
        if self.proxyLogin:

        result['userAgent'] = self.userAgent
class CustomCaptchaTask(BaseTask):
        self.fp = fp

        self.case = case
        self.numeric = numeric
        self.math = math
        result['userAgent'] = self.userAgent
        self.maxLength = max_length
    websiteKey = None
    def serialize(self):
                    field['name'] = name
                # 'body': self.img_b64,
                'body': base64.b64encode(self.fp.read()).decode('utf-8'),
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
                     'imageUrl': self.imageUrl})
        if self.form:
            forms = []
            for name, field in self.form.items():

        self.proxyLogin = kwargs.pop('proxy_login')
                else:
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

    def serialize(self):
        data = super(RecaptchaV3TaskProxyless, self).serialize()
    websiteKey = None
        data['websiteURL'] = self.websiteURL
    websiteKey = None
        self.proxyLogin = kwargs.pop('proxy_login')
        data['pageAction'] = self.pageAction
                       'websiteURL': self.websiteURL,