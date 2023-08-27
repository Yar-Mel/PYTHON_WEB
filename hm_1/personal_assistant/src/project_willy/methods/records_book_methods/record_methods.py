
from methods.records_book_methods.record_fields_methods import Name, Phone, Email, Birthday
from methods.records_book_methods.records_representation_methods import RecordRepr


class Record(RecordRepr):

    def __init__(
        self,
        name: Name | None = None,
        phone: Phone | None = None,
        email: Email | None = None,
        birthday: Birthday | None = None
        ) -> None:
        
        RecordRepr.show_record
        self.name = name
        self.email = email
        self.birthday = birthday
        self.phones = []
        if phone:
            self.add_phone(phone)

# ADD FIELDS
    def add_name(self, input_value: str) -> None:
        self.name = Name(input_value)

    def add_phone(self, input_value: str) -> None:
        new_phone = Phone(input_value)
        for phone in self.phones:
            for phone_type, new_phone_type in zip(phone.value, new_phone.value):
                if phone_type == new_phone_type:
                    phone.value.update(new_phone.value)
                    return
        self.phones.append(new_phone)

    def add_email(self, input_value: str) -> None:
        self.email = Email(input_value)

    def add_birthday(self, input_value: str) -> None:
        self.birthday = Birthday(input_value)

    def get_phones_str(self) -> str:
        result = ''
        for phone in self.phones:
            result += f'{phone.get_str()}\n'
        return result

    def __repr__(self) -> str:
        return f"Record: {self.name}, phones: {self.phones}, email: {self.email}, birthday: {self.birthday}"

# DAYS TO BIRTHDAY CALCULATE
    # def days_to_birthday(self, birthday: Birthday | datetime) -> int:
    #     result = None
    #     current_date = datetime.now()
    #     if isinstance(birthday, datetime):
    #         try:
    #             current_year_birthday = datetime(year=current_date.year, month=birthday.month, day=birthday.day+1)
    #         except ValueError:
    #             current_year_birthday = datetime(year=current_date.year, month=3, day=1)
    #         if current_year_birthday < current_date:
    #             next_year_birthday = datetime(year=current_date.year+1, month=birthday.month, day=birthday.day)
    #             result = next_year_birthday - current_date
    #         else:
    #             result = current_year_birthday - current_date
    #         return result.days
