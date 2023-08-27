
from methods import MenuGeneral, error_handler, autosave, RECORDS_BOOK
from text_fields import GeneralText, RecordsBookMenuText
from menu.main_menu_options.records_book_menu_options import AddRecordMenu, ChangeRecordMenu, ShowRecordsMenu, ImportMenu, ExportMenu


class RecordsBookMenu(MenuGeneral, GeneralText, RecordsBookMenuText):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_add_record,
        '2': self.option_change_record,
        '3': self.option_show_records,
        '4': self.option_import,
        '5': self.option_export,
        '6': self.option_clear_records_book,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        while True:
            print(self.show_menu(self.menu_title, self.menu_options))
            print(RECORDS_BOOK.records_calculatig())
            user_input = input(self.input_message)
            if not self.options_handler(user_input, self.MENU_OPTIONS):
                print(self.wrong_input_message)

# ADD RECORD
    def option_add_record(self) -> None:
        AddRecordMenu()

# CHANGE RECORD
    def option_change_record(self) -> None:
        ChangeRecordMenu()

# SHOW RECORDS
    def option_show_records(self) -> None:
        ShowRecordsMenu()

# IMPORT
    def option_import(self) -> None:
        ImportMenu()

# EXPORT
    def option_export(self) -> None:
        ExportMenu()

# CLEAR RECORDS BOOK
    @error_handler
    def option_clear_records_book(self) -> None:
        if RECORDS_BOOK.data:
            user_input = input(self.clear_input)
            if user_input == 'y':
                RECORDS_BOOK.clear()
                autosave()
                print(self.clear_successful_message)
                input(self.continue_input_message)
        else:
            print(self.empty_notes_book_message)
            input(self.continue_input_message)
