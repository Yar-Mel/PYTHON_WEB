from mongoengine import Document, StringField, ReferenceField, ListField


class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(required=True)
    author = ReferenceField(Authors)
    quote = StringField()
