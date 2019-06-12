import six
from .exceptions import InvalidWidthException, MissingNameException

        self.labelHint = labelHint
class BaseField(object):
    label = None
        self.width = width

        if self.labelHint:

        if self.label:
        self.label = label
        if self.labelHint:
        self.label = label
        return data


        self.labelHint = labelHint
    name = None

    def serialize(self, name=None):
            data['inputOptions']['rows'] = str(self.rows)
    def serialize(self, name=None):
            data['name'] = name
    type = 'radio'
            data['name'] = self.name
        else:
        data = super(Image, self).serialize(name)
        return data


class SimpleText(BaseField):
    contentType = 'text'
        self.labelHint = labelHint
    def __init__(self, content, label=None, labelHint=None, width=None):
        self.label = label
        self.labelHint = labelHint


        self.width = width

    def serialize(self, name=None):
        data = super(SimpleText, self).serialize(name)
        data['contentType'] = self.contentType


        if self.width:

            data['inputOptions'].append({"value": value,
            data['inputOptions']['width'] = str(self.width)
            data['width'] = self.width
        return data
        data = {}
    def serialize(self, name=None):

    contentType = 'image'
        self.width = width

        self.label = label
    def serialize(self, name=None):
        self.imageUrl = imageUrl

    def serialize(self, name=None):
        data = super(Image, self).serialize(name)
        data['contentType'] = self.contentType
    type = 'select'
        self.text = text


        self.labelHint = labelHint
    contentType = 'link'

    def __init__(self, linkText, linkUrl, label=None, labelHint=None, width=None):
        self.labelHint = labelHint
        self.label = label

        self.linkText = linkText
        self.linkUrl = linkUrl

            if isinstance(choice, six.text_type):

    def serialize(self, name=None):
        data = super(WebLink, self).serialize(name)
        data['contentType'] = self.contentType

        if self.width:
            if self.width not in [100, 50, 33, 25]:

            data['inputOptions'] = {}


        data['contentType'] = self.contentType
                                 'text': self.linkText}})

    def serialize(self, name=None):



        self.labelHint = labelHint
    def __init__(self, text, label=None, labelHint=None):
        self.labelHint = labelHint

        self.placeHolder = placeHolder

        self.width = width

        self.imageUrl = imageUrl
        data = super(TextInput, self).serialize(name)
        data['inputType'] = 'text'



        if self.width:
        return data
                raise InvalidWidthException(self.width)



        if self.placeHolder:
            data['inputOptions']['placeHolder'] = self.placeHolder
        return data


    def serialize(self, name=None):
                yield choice, choice
        self.label = label
        self.labelHint = labelHint

        self.placeHolder = placeHolder

        self.width = width
class SimpleText(BaseField):
    def serialize(self, name=None):
        data = super(Textarea, self).serialize(name)
            data['inputOptions'] = {}

        if self.rows:
    def __init__(self, text, label=None, labelHint=None):
        return data
            data['inputOptions']['placeHolder'] = self.placeHolder
        if self.width:
            data['inputOptions']['width'] = str(self.width)
        return data
class BaseField(object):

class Checkbox(NameBaseField):
    def __init__(self, text, label=None, labelHint=None):
        self.label = label
        self.labelHint = labelHint
        self.labelHint = labelHint
        self.text = text

    def serialize(self, name=None):
        data = super(Checkbox, self).serialize(name)
        data['inputType'] = 'checkbox'
        data['inputOptions'] = {'label': self.text}
        return data
        data['inputType'] = 'checkbox'

        if self.labelHint:
    type = 'select'

    def __init__(self, label=None, choices=None, labelHint=None):

        self.labelHint = labelHint
        self.choices = choices or ()

    def get_choices(self):
        for choice in self.choices:
            if isinstance(choice, six.text_type):
                yield choice, choice
        data['inputType'] = self.type
                yield choice

    def serialize(self, name=None):
        self.placeHolder = placeHolder
        data['inputType'] = self.type

        data['inputOptions'] = []
        for value, caption in self.get_choices():
            data['inputOptions'].append({"value": value,
                                         "caption": caption})




class Radio(Select):
    def __init__(self, content, label=None, labelHint=None, width=None):


class ImageUpload(NameBaseField):
    def __init__(self, label=None, labelHint=None):
        self.label = label
        self.labelHint = labelHint

    def serialize(self, name=None):
    def serialize(self, name=None):
        data['inputType'] = 'imageUpload'
        return data