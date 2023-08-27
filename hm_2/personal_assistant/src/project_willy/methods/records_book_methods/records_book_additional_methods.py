
from methods.imports import datetime, timedelta


class RecordsBookExtended:

# ----------Birthdays checking----------
    CURRENT_DATE = datetime.now()

    def get_birthdays(self, days_from_user: str) -> dict:
        days = int(days_from_user)
        result = {}
        count = 0
        for record in self.data.values():
            if self.birthdays_check(days, record.birthday.value):
                count += 1
                result.update({count: record})
        return result

    def birthdays_check(self, days_from_user: int, record_birthday: datetime) -> None:
        if len(str(days_from_user)) > 3:
            raise ValueError
        if isinstance(record_birthday, datetime) and len(str(days_from_user)) <= 3:
            next_date = self.CURRENT_DATE + timedelta(days=days_from_user)
            try:
                record_birthday_date = datetime(year=datetime.now().year, month=record_birthday.month, day=record_birthday.day)
            except ValueError:
                record_birthday_date = datetime(year=datetime.now().year, month=3, day=1)
            if self.CURRENT_DATE <= record_birthday_date <= next_date:
                return True

    def records_book_for_csv(self) -> list:
        result = [['No', 'Name', 'Phones', 'Email', 'Birthday']]
        for indx, record in enumerate(self.data.values(), start=1):
            record_data = [indx, record.name.get_str(), record.get_phones_str(), record.email.get_str(), record.birthday.get_str()]
            result.append(record_data)
        return result

    def records_book_for_json(self) -> list:
        result = {}
        for indx, record in enumerate(self.data.values(), start=1):
            record_data = {indx: [record.name.get_str(), record.get_phones_str().strip().split('\n'), record.email.get_str(), record.birthday.get_str()]}
            result.update(record_data)
        return result