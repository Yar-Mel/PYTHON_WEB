
from methods import MenuGeneral, autosave, error_handler, NOTES_BOOK
from text_fields import GeneralText, NotesMenuText
from menu.main_menu_options.notes_book_menu_options import AddNotesMenu, ChangeNotesMenu, ShowNotesMenu


class NotesBookMenu(MenuGeneral, GeneralText, NotesMenuText):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_add_new_notes,
        '2': self.option_change_notes,
        '3': self.option_show_notes,
        '4': self.option_clear_notes_book,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        while True:
            print(self.show_menu(self.menu_title, self.menu_options))
            print(NOTES_BOOK.notes_calculatig())
            user_input = input(self.input_message)
            if not self.options_handler(user_input, self.MENU_OPTIONS):
                print(self.wrong_input_message)

    def option_add_new_notes(self) -> None:
        AddNotesMenu()
    
    def option_change_notes(self) -> None:
        ChangeNotesMenu()
        
    def option_show_notes(self) -> None:
        ShowNotesMenu()

# CLEAR NOTES BOOK
    @error_handler
    def option_clear_notes_book(self) -> None:
        if NOTES_BOOK.data:
            user_input = input(self.clear_input)
            if user_input == 'y':
                NOTES_BOOK.clear()
                autosave()
                print(self.clear_successful_message)
                input(self.continue_input_message)
        else:
            print(self.empty_notes_book_message)
            input(self.continue_input_message)
