
from methods.imports import Path, os
from methods import MenuGeneral, FileOperations, error_handler, RECORDS_BOOK
from text_fields import GeneralText, ExportMenuText


class ExportMenu(MenuGeneral, GeneralText, ExportMenuText, FileOperations):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_export_txt,
        '2': self.option_export_pickle,
        '3': self.option_export_json,
        '4': self.option_export_csv,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
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
                print(self.show_menu(self.menu_title, self.menu_options))
                user_input = input(self.input_message)
                if not self.options_handler(user_input, self.MENU_OPTIONS):
                    print(self.wrong_input_message)

# EXPORT TO TXT
    @error_handler
    def option_export_txt(self) -> None:
        while True:
            print(self.show_menu(self.submenu_title, self.submenu_options))
            user_input = input(self.txt_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.records_book_to_txt(user_input):
                return # to main call

    @error_handler
    def records_book_to_txt(self, path_from_user: str) -> None:
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.txt'
        else:
            path_for_export = Path(path_from_user+'.txt')
        FileOperations.export_to_txt(path_for_export, RECORDS_BOOK.show_records(RECORDS_BOOK.get_records_catalog()))
        print(self.records_book_successful_message)
        input(self.continue_input_message)
        return True

# EXPORT TO PICKLE
    @error_handler
    def option_export_pickle(self) -> None:
        print(self.show_menu(self.submenu_title, self.submenu_options))
        while True:
            user_input = input(self.pickle_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.records_book_to_pickle(user_input):
                return # to main call

    @error_handler
    def records_book_to_pickle(self, path_from_user: str) -> None:
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.bin'
        else:
            path_for_export = Path(path_from_user+'.bin')
        FileOperations.export_to_pickle(path_for_export, RECORDS_BOOK)
        print(self.records_book_successful_message)
        input(self.continue_input_message)
        return True

# EXPORT TO JSON
    @error_handler
    def option_export_json(self) -> None:
        print(self.show_menu(self.submenu_title, self.submenu_options))
        while True:
            user_input = input(self.json_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.records_book_to_json(user_input):
                return # to main call

    @error_handler   
    def records_book_to_json(self, path_from_user: str) -> None: #TODO
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.json'
        else:
            path_for_export = Path(path_from_user+'.json')
        FileOperations.export_to_json(path_for_export, RECORDS_BOOK.records_book_for_json())
        print(self.records_book_successful_message)
        input(self.continue_input_message)
        return True

# EXPORT TO CSV
    @error_handler
    def option_export_csv(self) -> None:
        print(self.show_menu(self.submenu_title, self.submenu_options))
        while True:
            user_input = input(self.csv_path_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.records_book_to_csv(user_input):
                return # to main call

    @error_handler
    def records_book_to_csv(self, path_from_user: str) -> None: #TODO
        if path_from_user == '':
            path_for_export = Path(os.getcwd()) / 'records_book.csv'
        else:
            path_for_export = Path(path_from_user+'.csv')
        FileOperations.export_to_csv(path_for_export, RECORDS_BOOK.records_book_for_csv())
        print(self.records_book_successful_message)
        input(self.continue_input_message)
        return True
