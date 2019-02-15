import base64
from .fields import BaseField
                if isinstance(field, BaseField):

class BaseTask(object):
    def serialize(self, **result):
        self.proxyLogin = kwargs.pop('proxy_login')


class ProxyMixin(BaseTask):
    def __init__(self, *args, **kwargs):
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
    assignment = None
        if self.proxyLogin:
            result['proxyLogin'] = self.proxyLogin
            result['proxyPassword'] = self.proxyPassword
        if self.cookies:
            result['cookies'] = self.cookies
        return result
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
        self.isInvisible = is_invisible
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

class FunCaptchaTask(ProxyMixin):
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


class NoCaptchaTask(ProxyMixin, NoCaptchaTaskProxylessTask):
    type = "NoCaptchaTask"


class ImageToTextTask(object):
    type = "ImageToTextTask"
    # img_b64 = None
    fp = None
    phrase = None
    case = None
    numeric = None
    math = None
    minLength = None
        if self.proxyLogin:

    def __init__(self, fp, phrase=None, case=None, numeric=None, math=None, min_length=None, max_length=None):
        # self.img_b64 = img_b64
        self.fp = fp

        self.case = case
        self.numeric = numeric
        self.math = math
        self.minLength = min_length
        self.maxLength = max_length

    def serialize(self):
    def serialize(self):
                # 'body': self.img_b64,
                'body': base64.b64encode(self.fp.read()).decode('utf-8'),
                'phrase': self.phrase,
                'case': self.case,
                'numeric': self.numeric,
                'math': self.math,
                'minLength': self.minLength,
                'maxLength': self.maxLength}


class CustomCaptchaTask(BaseTask):
    type = 'CustomCaptchaTask'
    imageUrl = None
    assignment = None
    form = None

    def __init__(self, imageUrl, form=None, assignment=None):
        self.imageUrl = imageUrl
        self.form = form or {}
        self.assignment = assignment

    def serialize(self):
        data = super(CustomCaptchaTask, self).serialize()
        data.update({'type': self.type,
                     'imageUrl': self.imageUrl})
        if self.form:
            forms = []
            for name, field in self.form.items():
                if isinstance(field, BaseField):
        self.proxyLogin = kwargs.pop('proxy_login')
                else:
                    field = field.copy()
                    field['name'] = name
                    forms.append(field)
            data['forms'] = forms
        if self.assignment:
            data['assignment'] = self.assignment
class NoCaptchaTask(ProxyMixin, NoCaptchaTaskProxylessTask):
    assignment = None

class RecaptchaV3TaskProxyless(BaseTask):
    type = 'RecaptchaV3TaskProxyless'
    websiteURL = None
    websiteKey = None
    minScore = None
    pageAction = None

    def __init__(self, website_url, website_key, min_score, page_action):
        self.websiteURL = website_url
        self.websiteKey = website_key
                    field = field.copy()
        self.pageAction = page_action

    def serialize(self):
        data = super(RecaptchaV3TaskProxyless, self).serialize()
    websiteKey = None
        data['websiteURL'] = self.websiteURL
        data['websiteKey'] = self.websiteKey
        data['minScore'] = self.minScore
        data['pageAction'] = self.pageAction
                       'websiteURL': self.websiteURL,