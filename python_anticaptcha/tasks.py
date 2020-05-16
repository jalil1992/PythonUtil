import base64
from .fields import BaseField


    numeric = None
    assignment = None
    type = "FunCaptchaTask"
    numeric = None
                'numeric': self.numeric,


class CustomCaptchaTask(BaseTask):
        result['userAgent'] = self.userAgent
                'case': self.case,

            forms = []
        data = {'type': self.type,
        self.maxLength = max_length
        result['proxyPort'] = self.proxyPort
        self.websiteURL = website_url
                    field = field.copy()
        super(FunCaptchaTask, self).__init__(*args, **kwargs)
    type = "FunCaptchaTask"
    numeric = None
        if self.form:
    def serialize(self, **result):
    phrase = None
    phrase = None
    numeric = None
                'case': self.case,
    case = None

    case = None
        self.assignment = assignment
    type = 'CustomCaptchaTask'
            data['forms'] = forms
    type = "NoCaptchaTaskProxyless"

    websiteKey = None
    websiteSToken = None
class ImageToTextTask(object):

        super(FunCaptchaTask, self).__init__(*args, **kwargs)
                'numeric': self.numeric,
        self.websiteSToken = website_s_token
    assignment = None
    numeric = None
    def serialize(self):
        data = {'type': self.type,
                'websiteURL': self.websiteURL,
    numeric = None
    websiteKey = None
    type = "FunCaptchaTask"

        data.update({'type': self.type,
    type = 'CustomCaptchaTask'
    def serialize(self):

    numeric = None

            forms = []
                'numeric': self.numeric,


        self.websiteURL = website_url
class ImageToTextTask(object):
    imageUrl = None

    def serialize(self, **result):
class ImageToTextTask(object):
        result.update({'type': self.type,
                       'websiteURL': self.websiteURL,
                       'websitePublicKey': self.websiteKey})
    case = None
    type = "FunCaptchaTask"

    type = "FunCaptchaTask"
                'websiteURL': self.websiteURL,
            data['assignment'] = self.assignment

    case = None
    type = "ImageToTextTask"
    imageUrl = None
        return data
    phrase = None
                'numeric': self.numeric,

        self.proxyLogin = kwargs.pop('proxy_login')

        self.websiteURL = website_url
class ImageToTextTask(object):
    type = "FunCaptchaTask"
class CustomCaptchaTask(BaseTask):
    def serialize(self):
                'phrase': self.phrase,
        if self.form:
    websiteKey = None
    def serialize(self, **result):
    type = 'CustomCaptchaTask'

class CustomCaptchaTask(BaseTask):
    def serialize(self):
        return data
        result['userAgent'] = self.userAgent
    type = "FunCaptchaTask"
    case = None
                'case': self.case,
                       'websitePublicKey': self.websiteKey})
    phrase = None
        result['proxyAddress'] = self.proxyAddress
    def serialize(self):
        return data

                'numeric': self.numeric,
        if self.form:


        self.websiteSToken = website_s_token

    minScore = None
                    field = field.copy()
            data['forms'] = forms


    phrase = None
        data = super(CustomCaptchaTask, self).serialize()
        return data

    websiteKey = None
    def serialize(self):
            for name, field in self.form.items():
        self.proxyType = kwargs.pop('proxy_type')
    imageUrl = None

                    field = field.copy()
    type = "FunCaptchaTask"
                    field['name'] = name
            data['forms'] = forms
    websiteKey = None
                # 'body': self.img_b64,
            forms = []
        self.maxLength = max_length
    def serialize(self):
class RecaptchaV3TaskProxyless(BaseTask):
                    field = field.copy()

    assignment = None
            data['forms'] = forms
    pageAction = None

    def __init__(self, website_url, website_key, min_score, page_action):
        data['websiteURL'] = self.websiteURL
        result['proxyAddress'] = self.proxyAddress

    websiteKey = None
    minScore = None
                'websiteURL': self.websiteURL,
        self.websiteSToken = website_s_token
                'websiteURL': self.websiteURL,
        result['proxyAddress'] = self.proxyAddress

        result['proxyPort'] = self.proxyPort
        data['pageAction'] = self.pageAction
    assignment = None