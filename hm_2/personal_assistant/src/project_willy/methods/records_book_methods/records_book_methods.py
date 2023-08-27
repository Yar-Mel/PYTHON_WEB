
from methods.imports import re, UserDict
from methods.records_book_methods.record_methods import Record
from methods.records_book_methods.records_representation_methods import RecordsBookRepr
from methods.records_book_methods.records_book_additional_methods import RecordsBookExtended


class RecordsBook(UserDict, RecordsBookRepr, RecordsBookExtended):

    def __init__(self) -> None:
        UserDict.__init__(self)
        RecordsBookRepr.show_records
        RecordsBookExtended.get_birthdays
        RecordsBookExtended.records_book_for_json
        RecordsBookExtended.records_book_for_csv

# UPDATE BOOK
    def update(self, another_records_book: dict) -> None:
        self.data.update(another_records_book)

    def clear(self) -> None:
        self.data.clear()

# RECORDS PROCESSING
    def check_record(self, record: Record) -> None:
        if record.name.value in self.data.keys():
            return True

    def add_record(self, record: Record) -> None:
            self.data[record.name.value] = record

    def delete_record(self, record: Record) -> None:
        del self.data[record.name.value]
        
    def get_records_catalog(self) -> dict:
        return {indx: record for indx, record in enumerate(self.data.values(), start=1)}
        
# FIND RECORD
    def find_records(self, user_input: str) -> dict:
        result = {}
        count = 0
        search_string = user_input.strip().lower()
        clean_search_string = re.sub(r'[+ ]', '', search_string)
        if clean_search_string:
            for record in self.data.values():
                if self.search_in_names(clean_search_string, record):
                    count += 1
                    result.update({count: record})
                elif self.search_in_phones(clean_search_string, record):
                    count += 1
                    result.update({count: record})
                elif self.search_in_email(clean_search_string, record):
                    count += 1
                    result.update({count: record})
        return result

    def search_in_names(self, search_string: str, record: Record) -> bool:
        for name in record.name.value:
            if search_string in name.lower():
                return True
            
    def search_in_phones(self, search_string: str, record: Record) -> bool:
        for phone in record.phones:
            for phone_number in phone.value.values():
                clean_phone_number = re.sub(r'[+ ]', '', phone_number)
                if search_string in clean_phone_number:
                    return True
            
    def search_in_email(self, search_string: str, record: Record) -> bool:
        if search_string in record.email.value:
            return True

# RECORDS ITERATION
    # def iterator(self, N: int = 1, flag: bool = False) -> Record:
    #     result = None
    #     if flag:
    #         N = len(self.data.keys())
    #     count = 0
    #     for key in self.data.keys():
    #         result = self.data[key]
    #         count += 1
    #         if count == N:
    #             yield result
    #             result = ''
    #             count = 0

# RECORDS CALCULATING
    def records_calculatig(self) -> str:
        return f'Number of records in the book: {len(self.data)}\n'
