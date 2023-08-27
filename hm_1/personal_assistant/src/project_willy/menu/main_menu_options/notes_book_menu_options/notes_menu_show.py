
from methods import MenuGeneral, error_handler, NOTES_BOOK
from text_fields import GeneralText, ShowNotesMenuText


class ShowNotesMenu(MenuGeneral, GeneralText, ShowNotesMenuText):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_find_notes,
        '2': self.option_sort_a_z,
        '3': self.option_sort_date,
        '4': self.option_debug,
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
        if not NOTES_BOOK.data:
            print(self.empty_notes_book_message)
            input(self.continue_input_message)
        else:
            while True:
                print(self.show_menu(self.menu_title, self.menu_options))
                user_input = input(self.input_message)
                if not self.options_handler(user_input, self.MENU_OPTIONS):
                    print(self.wrong_input_message)

# FIND RECORD
    @error_handler
    def option_find_notes(self) -> None:
        while True:
            print(self.show_menu(self.submenu_title, self.submenu_options))
            user_input = input(self.search_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.find_and_show_notes(user_input):
                return # to main call

    @error_handler
    def find_and_show_notes(self, user_input) -> None:
        notes_catalog = NOTES_BOOK.find_notes(user_input)
        if notes_catalog:
            print(NOTES_BOOK.show_notes_book(notes_catalog))
            input(self.continue_input_message)
            return True
        print(self.no_matches_message)

# SHOW SORTED ALL BY A-Z
    @error_handler
    def option_sort_a_z(self) -> None:
        print(NOTES_BOOK.show_notes_book(NOTES_BOOK.sort_a_z()))
        input(self.continue_input_message)   

# SHOW SORTED ALL BY DATE
    @error_handler
    def option_sort_date(self) -> None:
        print(NOTES_BOOK.show_notes_book(NOTES_BOOK.sort_by_date()))
        input(self.continue_input_message)

# DEBUG
    @error_handler
    def option_debug(self) -> None:
        print(NOTES_BOOK)
        input(self.continue_input_message)
