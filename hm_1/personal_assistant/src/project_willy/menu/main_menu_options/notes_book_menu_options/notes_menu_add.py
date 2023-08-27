
from methods import Notes, MenuGeneral, autosave, error_handler, NOTES_BOOK
from text_fields import GeneralText, AddNotesMenuText


class AddNotesMenu(MenuGeneral, GeneralText, AddNotesMenuText):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.notes = Notes()
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        print(self.show_menu(self.menu_title, self.menu_options))
        while True:
            print(self.notes.show_notes())
            if not self.notes['tags']:
                user_input = input(self.tags_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_tags_to_notes(user_input)
            elif not self.notes['text']:
                user_input = input(self.tags_input_message)
                self.options_handler(user_input, self.MENU_OPTIONS)
                self.add_text_to_notes(user_input)
            else:
                self.notes.create_notes()
                NOTES_BOOK.add_notes(self.notes)
                autosave()
                print(self.add_successful_message)
                input(self.continue_input_message)
                return # to previous menu

# ADD FILEDS TO NOTES    
    @error_handler
    def add_tags_to_notes(self, user_input) -> None:
        self.notes.add_tags(user_input)
    
    @error_handler
    def add_text_to_notes(self, user_input) -> None:
        self.notes.add_text(user_input)
