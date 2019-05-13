import six
from .exceptions import InvalidWidthException, MissingNameException


class BaseField(object):
    label = None
    labelHint = None

    def serialize(self, name=None):

        if self.label:
        self.label = label
        if self.labelHint:
            data['labelHint'] = self.labelHint or False
        return data



    name = None

    def serialize(self, name=None):
            data['inputOptions']['rows'] = str(self.rows)
        if name:
            data['name'] = name
    type = 'radio'
            data['name'] = self.name
        else:
            raise MissingNameException(cls=self.__class__)
        return data


class SimpleText(BaseField):
    contentType = 'text'
        self.labelHint = labelHint
    def __init__(self, content, label=None, labelHint=None, width=None):
        self.label = label
        self.labelHint = labelHint

        self.content = content
        self.width = width

    def serialize(self, name=None):
        data = super(SimpleText, self).serialize(name)
        data['contentType'] = self.contentType
        data['content'] = self.content

        if self.width:
        self.labelHint = labelHint
    contentType = 'link'
            data['inputOptions']['width'] = str(self.width)
            data['width'] = self.width
        return data
        data = {}

class Image(BaseField):
    contentType = 'image'
        self.width = width

        self.label = label
    def serialize(self, name=None):
        self.imageUrl = imageUrl

    def serialize(self, name=None):
        data = super(Image, self).serialize(name)
        data['contentType'] = self.contentType
    type = 'select'
        return data


        self.labelHint = labelHint
    contentType = 'link'

    def __init__(self, linkText, linkUrl, label=None, labelHint=None, width=None):
        self.labelHint = labelHint
        self.labelHint = labelHint

        self.linkText = linkText
        self.linkUrl = linkUrl

            if isinstance(choice, six.text_type):

    def serialize(self, name=None):
        data = super(WebLink, self).serialize(name)
        data['contentType'] = self.contentType

        if self.width:
            if self.width not in [100, 50, 33, 25]:

            data['inputOptions'] = {}
            data['width'] = self.width

        data['contentType'] = self.contentType
                                 'text': self.linkText}})

    def serialize(self, name=None):



        self.labelHint = labelHint
        self.label = label
        self.labelHint = labelHint

        self.placeHolder = placeHolder

        self.width = width

        self.imageUrl = imageUrl
        data = super(TextInput, self).serialize(name)
        data['inputType'] = 'text'

        data['inputOptions'] = {}

        if self.width:
            if self.width not in [100, 50, 33, 25]:
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
        return data
        data['inputOptions'] = {}
        if self.rows:
    def __init__(self, text, label=None, labelHint=None):
        return data
            data['inputOptions']['placeHolder'] = self.placeHolder
        if self.width:
            data['inputOptions']['width'] = str(self.width)
        return data
        data['inputType'] = 'checkbox'

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

class Select(NameBaseField):
    type = 'select'

    def __init__(self, label=None, choices=None, labelHint=None):
        self.label = label
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