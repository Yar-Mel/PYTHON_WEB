
from methods.imports import re, datetime
from methods.errors_methods import NameError, PhoneError, EmailError, BirthdayError
from text_fields import MethodsText

class Field:
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self) -> None:
        return self.__value

    @value.setter
    def value(self, new_value) -> None:
        self.__value = new_value


class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str) -> None:
        first_name, last_name = self.name_parser(value)
        if self.name_validate(first_name):
            if self.name_validate(last_name):
                Field.value.fset(self, (first_name, last_name))
            else:
                Field.value.fset(self, (first_name,))
        else:                                       
            raise NameError

    def name_parser(self, value: str) -> tuple:
        first_name = None
        last_name = None
        if value:
            name = value.strip().split()
            if len(name) == 1:
                first_name = name[0]
                last_name = None
            if len(name) == 2:
                first_name = name[0]
                last_name = name[1]
        return first_name, last_name

    def name_validate(self, value: str) -> bool:
        if value and 1 < len(value) <= 16:
            return True

    def get_str(self) -> str:
        if len(self.value) == 2:
            return f'{self.value[0]} {self.value[1]}'
        return f'{self.value[0]}'
    
    def __repr__(self) -> str:
        return f'Name(value={self.value} [{type(self.value)}])'


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    @Field.value.setter
    def value(self, value: str) -> None:
        phone_type, phone_number = self.phone_parser(value)
        if self.phone_number_validate(phone_number):
            if self.phone_type_validate(phone_type):
                Field.value.fset(self, ({phone_type: self.phone_number_normalize(phone_number)}))
            else:
                Field.value.fset(self, ({MethodsText.DEFAULT_PHONE_TYPE: self.phone_number_normalize(phone_number)}))
        else:
            raise PhoneError

    def phone_parser(self, value: str) -> tuple:
        phone_type = None
        phone_number = None
        for type in MethodsText.ALLOWED_PHONE_TYPES:
            if type in value:
                phone_type = type

        match = re.search(r'\d+', value)
        if match:
            phone_number = match[0]
        return phone_type, phone_number
    
    def phone_type_validate(self, phone_type: str) -> bool:
        if phone_type in MethodsText.ALLOWED_PHONE_TYPES:
             return True

    def phone_number_validate(self, phone_number: str) -> bool:
            if phone_number and len(phone_number) == 12 and phone_number.isnumeric():
                return True

    def phone_number_normalize(self, phone_number: str) -> str:
        return f'+{phone_number[0:2]} {phone_number[2:5]} {phone_number[5:8]} {phone_number[8:12]}'

    def get_str(self) -> str:
        for phone_type, phone_number in self.value.items():
            return f'{phone_type}: {phone_number}'
     
    def __repr__(self) -> str:
        return f'Phone(value={self.value} [{type(self.value)}])'


class Email(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
    
    @Field.value.setter
    def value(self, value: str) -> None:
        if value:
            email = self.email_parser(value)
            if self.email_length_validate(email):
                Field.value.fset(self, email)
            else:
                raise EmailError
        else:
            Field.value.fset(self, MethodsText.DEFAULT_EMPTY_FIELD)

    def email_parser(self, value: str) -> str:
        email = None
        match = re.search(r"[a-zA-Z]{1}[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", value)
        if match:
            email = match[0]
        return email
    
    def email_length_validate(self, value: str) -> bool:
        if value and len(value) <= 32:
            return True        

    def get_str(self) -> str:
        return f'{self.value}'

    def __repr__(self) -> str:
        return f'Email(value={self.value} [{type(self.value)}])'


class Birthday(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
    
    @Field.value.setter
    def value(self, value: str) -> None:
        if value:
            birthday_date = self.birthday_normalize(value)
            if birthday_date:
                Field.value.fset(self, birthday_date)
            else:
                raise BirthdayError
        else:
            Field.value.fset(self, MethodsText.DEFAULT_EMPTY_FIELD)

    def birthday_normalize(self, value: str) -> datetime:
        result = None
        birthday_match = re.search(fr'^\d\d-\d\d-\d\d\d\d$', value)
        if birthday_match:
            birthday_date = (datetime.strptime(birthday_match[0], '%d-%m-%Y'))
            if birthday_date < datetime.now():
                result = birthday_date
        return result

    def get_str(self) -> str:
        if isinstance(self.value, datetime):
            return f'{self.value.date()}'
        return f'{self.value}'

    def __repr__(self) -> str:
        return f'Birthday(value={self.value} [{type(self.value)}])'
