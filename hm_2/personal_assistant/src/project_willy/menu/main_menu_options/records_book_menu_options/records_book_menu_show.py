
from methods import MenuGeneral, error_handler, RECORDS_BOOK
from text_fields import GeneralText, ShowRecordsMenuText


class ShowRecordsMenu(MenuGeneral, GeneralText, ShowRecordsMenuText):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_find_record,            
        '2': self.option_get_and_show_birthdays,
        '3': self.option_show_all,
        '4': self.option_debug,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.record = None
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        if not RECORDS_BOOK.data:
            print(self.empty_records_book_message)
            input(self.continue_input_message)
            return # to main call
        else:
            while True:
                print(self.show_menu(self.menu_title, self.menu_options))
                user_input = input(self.input_message)
                if not self.options_handler(user_input, self.MENU_OPTIONS):
                    print(self.wrong_input_message)

# FIND RECORD
    @error_handler
    def option_find_record(self) -> None:
        print(self.show_menu(self.submenu_title, self.submenu_options))
        while True:
            user_input = input(self.search_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.find_and_show_record(user_input):
                return # to main call

    @error_handler
    def find_and_show_record(self, user_input) -> None:
        records_catalog = RECORDS_BOOK.find_records(user_input)
        if records_catalog:
            print(RECORDS_BOOK.show_records(records_catalog))
            input(self.continue_input_message)
            return True
        print(self.no_matches_message)

# SHOW RECORD
    @error_handler
    def option_get_and_show_birthdays(self) -> None:
        while True:
            print(self.show_menu(self.submenu_title, self.submenu_options))
            user_input = input(self.days_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.get_birthdays(user_input):
                return # to main call

    @error_handler
    def get_birthdays(self, user_input: str) -> str:
        records_catalog = RECORDS_BOOK.get_birthdays(user_input)
        if records_catalog:
            print(RECORDS_BOOK.show_records(records_catalog))
            input(self.continue_input_message)
            return True
        print(self.no_matches_message)

# SHOW ALL
    @error_handler
    def option_show_all(self) -> None:
        print(RECORDS_BOOK.show_records(RECORDS_BOOK.get_records_catalog()))
        input(self.continue_input_message)

# DEBUG
    @error_handler
    def option_debug(self) -> None:
        print(RECORDS_BOOK.data)
        input(self.continue_input_message)
