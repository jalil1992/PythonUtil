import base64



    numeric = None
import base64
    type = "FunCaptchaTask"
    numeric = None
                'numeric': self.numeric,
                'websiteURL': self.websiteURL,

class CustomCaptchaTask(BaseTask):

                'case': self.case,

            forms = []
        data = {'type': self.type,
        return data

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
        super(FunCaptchaTask, self).__init__(*args, **kwargs)
                       'websiteURL': self.websiteURL,


        self.assignment = assignment
    type = 'CustomCaptchaTask'
            data['forms'] = forms
    type = "NoCaptchaTaskProxyless"

    websiteKey = None
    websiteSToken = None
class ImageToTextTask(object):

        super(FunCaptchaTask, self).__init__(*args, **kwargs)
    imageUrl = None
        self.websiteSToken = website_s_token
    assignment = None
    numeric = None
        self.websiteURL = website_url
        data = {'type': self.type,
    def __init__(self, website_url, website_key, min_score, page_action):
    numeric = None
    websiteKey = None
    type = "FunCaptchaTask"

    type = "FunCaptchaTask"
    type = 'CustomCaptchaTask'
    def serialize(self):

    numeric = None

        return data
                'numeric': self.numeric,

        self.assignment = assignment
        self.websiteURL = website_url
class ImageToTextTask(object):
    imageUrl = None

    def serialize(self, **result):
class ImageToTextTask(object):
        result.update({'type': self.type,
                       'websiteURL': self.websiteURL,
        self.assignment = assignment
    case = None
    type = "FunCaptchaTask"

            forms = []
                'websiteURL': self.websiteURL,
            data['assignment'] = self.assignment

                'websiteURL': self.websiteURL,
    type = "ImageToTextTask"
    imageUrl = None
        return data
            data['assignment'] = self.assignment
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
                'case': self.case,
        result['userAgent'] = self.userAgent
    type = "FunCaptchaTask"
    case = None
                'case': self.case,
                       'websitePublicKey': self.websiteKey})
    phrase = None

    def serialize(self):
        return data

                'numeric': self.numeric,
        if self.form:

    numeric = None
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
    phrase = None
                    field = field.copy()

    assignment = None
            data['forms'] = forms
    pageAction = None

    def __init__(self, website_url, website_key, min_score, page_action):

        result['proxyAddress'] = self.proxyAddress

    websiteKey = None
    minScore = None
                'websiteURL': self.websiteURL,
        self.websiteSToken = website_s_token
                'websiteURL': self.websiteURL,
        data = {'type': self.type,

        result['proxyPort'] = self.proxyPort
        data['pageAction'] = self.pageAction
    assignment = None