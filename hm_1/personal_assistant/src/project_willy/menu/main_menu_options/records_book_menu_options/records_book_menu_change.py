
from methods.imports import deepcopy
from methods import Record, MenuGeneral, autosave, error_handler, RECORDS_BOOK
from text_fields import GeneralText, ChangeRecordMenuText


class ChangeRecordMenu(MenuGeneral, GeneralText, ChangeRecordMenuText):
# OPTIONS
    def __init__(self, record: Record = None) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_change_name,
        '2': self.option_change_phone,
        '3': self.option_change_email,
        '4': self.option_change_birthday,
        '5': self.option_get_another_record,
        '6': self.option_delete_record,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.record = record
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        if not RECORDS_BOOK.data:
            print(self.empty_records_book_message)
            input(self.continue_input_message)
            return # to previous menu
        else:
            while True:
                if not self.record:
                    print(self.show_menu(self.premenu_title, self.premenu_options))
                    user_input = input(self.record_input_message)
                    self.options_handler(user_input, self.SUBMENU_OPTIONS)                    
                    self.get_record_to_change(user_input)
                else:
                    print(self.show_menu(self.menu_title, self.menu_options))
                    print(self.record.show_record())
                    user_input = input(self.input_message)
                    if not self.options_handler(user_input, self.MENU_OPTIONS):
                        print(self.wrong_input_message)

# GET RECORD TO CHANGE
    @error_handler
    def get_record_to_change(self, user_input) -> None:
        records_catalog = RECORDS_BOOK.find_records(user_input)
        if records_catalog:
            while True:
                print(self.show_menu(self.premenu_title, self.premenu_options))
                print(RECORDS_BOOK.show_records(records_catalog))
                user_input = input(self.record_indx_input_message)
                self.options_handler(user_input, self.SUBMENU_OPTIONS)
                if self.record_choosing(records_catalog, user_input):
                    return # to main call
        else:
            print(self.no_matches_message)
            input(self.continue_input_message)

    @error_handler
    def record_choosing(self, records_catalog: dict, user_input: str) -> bool:
        self.record = records_catalog[int(user_input.strip())]
        return True

#CHANGE NAME
    @error_handler
    def option_change_name(self) -> None:
        print(self.show_menu(self.submenu_title, self.submenu_options))
        while True:
            user_input = input(self.name_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_name_in_record(user_input):
                return # to main call

    @error_handler
    def change_name_in_record(self, user_input) -> None:
        old_record = deepcopy(self.record)
        self.record.add_name(user_input)
        if RECORDS_BOOK.check_record(self.record):
            print(self.record_exists_message)
            self.record = old_record
            return
        RECORDS_BOOK.add_record(self.record)
        RECORDS_BOOK.delete_record(old_record)
        autosave()
        print(self.change_successful_message)
        input(self.continue_input_message)
        return True

# CHANGE PHONE
    @error_handler
    def option_change_phone(self) -> None:
        print(self.show_menu(self.submenu_title, self.submenu_options))
        while True:
            user_input = input(self.phone_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_phone_in_record(user_input):
                return # to main call

    @error_handler
    def change_phone_in_record(self, user_input) -> None:    
        self.record.add_phone(user_input)
        RECORDS_BOOK.add_record(self.record)
        autosave()
        print(self.change_successful_message)
        input(self.continue_input_message)
        return True

# CHANGE EMAIL
    @error_handler
    def option_change_email(self) -> None:
        print(self.show_menu(self.submenu_title, self.submenu_options))
        while True:
            user_input = input(self.email_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_email_in_record(user_input):
                return # to main call

    @error_handler
    def change_email_in_record(self, user_input) -> None:
        self.record.add_email(user_input)
        RECORDS_BOOK.add_record(self.record)
        autosave()
        print(self.change_successful_message)
        input(self.continue_input_message)
        return True
    
# CHANGE BIRTHDAY
    @error_handler 
    def option_change_birthday(self) -> None:
        print(self.show_menu(self.submenu_title, self.submenu_options))
        while True:
            user_input = input(self.birthday_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_birthday_in_record(user_input):
                return # to main call
    
    @error_handler
    def change_birthday_in_record(self, user_input) -> None:
        self.record.add_birthday(user_input)
        RECORDS_BOOK.add_record(self.record)
        autosave()
        print(self.change_successful_message)
        input(self.continue_input_message)
        return True
    
# GET ANOTHER RECORD
    @error_handler
    def option_get_another_record(self) -> None:
        while True:
            user_input = input(self.record_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.get_record_to_change(user_input):
                return # to main call

# DELETE RECORD
    @error_handler
    def option_delete_record(self) -> None:
        user_input = input(self.delete_input)
        if user_input == 'y':
            RECORDS_BOOK.delete_record(self.record)
            self.record = None
            autosave()
            print(self.delete_successful_message)
            input(self.continue_input_message)
