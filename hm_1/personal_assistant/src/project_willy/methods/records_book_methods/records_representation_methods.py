
from settings import RecordReprSettings, RecordsBookReprSettings
from text_fields import MethodsText

class RecordRepr(RecordReprSettings):

    def show_record(self) -> str:
        result = ''

        # name as title
        if self.name:
            result += self.record_title_pattern.format(self.name.get_str(), self.record_line_of_row)
        else:
            result += self.record_title_pattern.format(f'Name: {MethodsText.DEFAULT_EMPTY_FIELD}', self.record_line_of_row)

        # phones
        if self.phones:
            result += self.record_row_pattern.format(self.phones[0].get_str(), self.record_line_of_row)
            if len(self.phones) > 1:
                for phone in self.phones[1:]:
                    result += self.record_row_pattern.format(phone.get_str(), self.record_line_of_row)            
        else:
            result += self.record_row_pattern.format(f'Phone: {MethodsText.DEFAULT_EMPTY_FIELD}', self.record_line_of_row)        

        # email
        if self.email:
            result += self.record_row_pattern.format(f'Email: {self.email.get_str()}', self.record_line_of_row)
        else:
            result += self.record_row_pattern.format(f'Email: {MethodsText.DEFAULT_EMPTY_FIELD}', self.record_line_of_row)

        # birthday
        if self.birthday:
            result += self.record_row_pattern.format(f'Birthday: {self.birthday.get_str()}', self.record_line_of_row)
        else:
            result += self.record_row_pattern.format(f'Birthday: {MethodsText.DEFAULT_EMPTY_FIELD}', self.record_line_of_row)       

        return result  


class RecordsBookRepr(RecordsBookReprSettings):

    def get_records_book_head(self) -> str:
        result = self.records_book_title_pattern.format('---RECORDS BOOK---', self.records_book_line_of_row)
        result += self.records_book_row_pattern.format('No', 'Name', 'Phone', 'Email', 'Birthday')
        result += self.records_book_line_of_row_pattern.format(self.records_book_line_of_row)
        return result

    def show_records(self, dict_of_records: dict) -> str:
        result = self.get_records_book_head()
        for indx, record in dict_of_records.items():
            result += self.records_book_row_pattern.format(indx, record.name.get_str(), record.phones[0].get_str(), record.email.get_str(), record.birthday.get_str())
            if len(record.phones) > 1:
                for phone in record.phones[1:]:
                    result += self.records_book_row_pattern.format('','', phone.get_str(), '', '',)
            result += self.records_book_line_of_row_pattern.format(self.records_book_line_of_row)
        return result
