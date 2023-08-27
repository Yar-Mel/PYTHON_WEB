
from methods.imports import Path
from methods import RecordsBook, MenuGeneral, FileOperations, error_handler, autosave, RECORDS_BOOK
from text_fields import GeneralText, ImportMenuText


class ImportMenu(MenuGeneral, GeneralText, ImportMenuText):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(self.show_menu(self.menu_title, self.menu_options))
        while True:
            user_input = input(self.input_message)
            self.options_handler(user_input, self.MENU_OPTIONS)
            if self.import_records_book_from_pickle(user_input):
                return # to previous menu

    @error_handler
    def import_records_book_from_pickle(self, path_from_user: str) -> None:
        path_for_import = Path(path_from_user)
        if path_for_import.is_file():
            imported_records_book = FileOperations.import_from_pickle(path_for_import)
            if isinstance(imported_records_book, RecordsBook):
                RECORDS_BOOK.update(imported_records_book)
                autosave()
                print(self.import_records_book_successful_message)
                input(self.continue_input_message)
                return True
            else:
                print(self.invalid_file_message)
        else:
            print(self.file_not_exists_message)
