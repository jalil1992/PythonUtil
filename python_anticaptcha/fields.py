        for choice in self.choices:
from .exceptions import InvalidWidthException, MissingNameException

        self.labelHint = labelHint
        for value, caption in self.get_choices():
    label = None
        self.width = width

        if self.labelHint:
        self.width = width
        self.labelHint = labelHint
        else:
        if self.labelHint:
        self.label = label



        self.labelHint = labelHint
    name = None

        data = super(Image, self).serialize(name)
            data['inputOptions']['rows'] = str(self.rows)
    def serialize(self, name=None):
            data['name'] = name
        data['inputType'] = self.type
            data['name'] = self.name
        else:
        data = super(Image, self).serialize(name)
        if self.labelHint:



        self.labelHint = labelHint
        self.labelHint = labelHint
    def __init__(self, content, label=None, labelHint=None, width=None):
        self.label = label
            if isinstance(choice, six.text_type):


        self.width = width

    def serialize(self, name=None):
        data = super(SimpleText, self).serialize(name)
        if self.labelHint:


        if self.width:
        data['contentType'] = self.contentType
            data['inputOptions'].append({"value": value,
        self.imageUrl = imageUrl
            data['width'] = self.width
        return data
        data = {}
    def serialize(self, name=None):

    contentType = 'image'
        self.width = width

        self.label = label
    def serialize(self, name=None):
        self.imageUrl = imageUrl


        data = super(Image, self).serialize(name)
        data['contentType'] = self.contentType
    type = 'select'
        self.text = text
        data = super(SimpleText, self).serialize(name)

        self.labelHint = labelHint
        return data
        self.choices = choices or ()

        self.labelHint = labelHint
    def serialize(self, name=None):

        data = super(TextInput, self).serialize(name)


            if isinstance(choice, six.text_type):

                                 'text': self.linkText}})
        data = super(WebLink, self).serialize(name)
        data['contentType'] = self.contentType

    contentType = 'image'


            data['inputOptions'] = {}

        if self.labelHint:
        data['contentType'] = self.contentType
                                 'text': self.linkText}})





        self.labelHint = labelHint
    def __init__(self, text, label=None, labelHint=None):
        self.labelHint = labelHint

        self.placeHolder = placeHolder
        self.linkUrl = linkUrl
        self.width = width

        self.imageUrl = imageUrl

        data['inputType'] = 'text'



        self.width = width
        return data
    def __init__(self, label=None, labelHint=None):




            data['inputOptions']['placeHolder'] = self.placeHolder
        return data


    def serialize(self, name=None):
                yield choice, choice
        self.label = label
        for choice in self.choices:
        data = super(TextInput, self).serialize(name)
        self.placeHolder = placeHolder

        self.width = width
class SimpleText(BaseField):
            data['inputOptions'].append({"value": value,
        data = super(Textarea, self).serialize(name)
        self.labelHint = labelHint


    def __init__(self, text, label=None, labelHint=None):
        return data

        if self.width:
        self.imageUrl = imageUrl
        return data
class BaseField(object):

    contentType = 'image'
    def __init__(self, text, label=None, labelHint=None):
        self.label = label
        self.labelHint = labelHint
        self.labelHint = labelHint
        self.text = text

    def serialize(self, name=None):

        data['inputType'] = 'checkbox'
        data = super(SimpleText, self).serialize(name)
        return data
    def serialize(self, name=None):
    def __init__(self, content, label=None, labelHint=None, width=None):
        if self.labelHint:
        data['inputType'] = 'text'
    def get_choices(self):
                                 'text': self.linkText}})

        if self.width:
        self.choices = choices or ()

    def get_choices(self):
        for choice in self.choices:
            if isinstance(choice, six.text_type):
                yield choice, choice
        data['inputType'] = self.type
    def __init__(self, content, label=None, labelHint=None, width=None):
        return data
    def serialize(self, name=None):
        self.placeHolder = placeHolder
        data['inputType'] = self.type
    def __init__(self, content, label=None, labelHint=None, width=None):

        for value, caption in self.get_choices():
            data['inputOptions'].append({"value": value,
                                         "caption": caption})




class Radio(Select):
    def __init__(self, content, label=None, labelHint=None, width=None):



    def __init__(self, label=None, labelHint=None):
        self.imageUrl = imageUrl
        if self.labelHint:


    def serialize(self, name=None):
        data['inputType'] = 'imageUpload'
        return data