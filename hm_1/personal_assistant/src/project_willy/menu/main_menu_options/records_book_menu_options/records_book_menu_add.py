
from methods import Record, MenuGeneral, autosave, error_handler, RECORDS_BOOK
from text_fields import GeneralText, AddRecordMenuText


class AddRecordMenu(MenuGeneral, GeneralText, AddRecordMenuText):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.record = Record()
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        while True:
            print(self.show_menu(self.menu_title, self.menu_options))
            print(self.record.show_record())
            if not self.record.name:
                user_input = input(self.name_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_name_to_record(user_input)
            elif not self.record.phones:
                user_input = input(self.phone_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_phone_to_record(user_input)
            elif not self.record.email:
                user_input = input(self.email_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_email_to_record(user_input)
            elif not self.record.birthday:
                user_input = input(self.birthday_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_birthday_to_record(user_input)
            else:
                RECORDS_BOOK.add_record(self.record)
                autosave()
                print(self.add_successful_message)
                input(self.continue_input_message)
                return # to previous menu

# ADD FIELDS TO NEW RECORD
    @error_handler
    def add_name_to_record(self, user_input) -> None:
        self.record.add_name(user_input)
        if RECORDS_BOOK.check_record(self.record):
            print(self.record_exists_message)
            self.record.name = None

    @error_handler
    def add_phone_to_record(self, user_input) -> None:
        self.record.add_phone(user_input)

    @error_handler
    def add_email_to_record(self, user_input) -> None:
        self.record.add_email(user_input)

    @error_handler
    def add_birthday_to_record(self, user_input) -> None:
        self.record.add_birthday(user_input)
