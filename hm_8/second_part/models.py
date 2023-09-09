from mongoengine import Document, StringField, DateField, BooleanField


class Contact(Document):
    fullname = StringField(required=True)
    born_date = DateField(required=True)
    email = StringField(required=True)
    phone_number = StringField(required=True)
    prefer_sms = BooleanField(default=False)

    meta = {
        'collection': 'contacts'
    }
