
from methods import Notes, MenuGeneral, autosave, error_handler, NOTES_BOOK
from text_fields import GeneralText, ChangeNotesMenuText


class ChangeNotesMenu(MenuGeneral, GeneralText, ChangeNotesMenuText):
# OPTIONS
    def __init__(self, notes: Notes = None) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_change_tags,
        '2': self.option_change_notes_text,
        '3': self.option_delete_notes,
        '4': self.option_get_another_notes,
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.SUBMENU_OPTIONS = {
        '0': self.option_return_to_previous,
        'exit': self.option_exit_from_cli,
        }
        self.notes = notes
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        if not NOTES_BOOK.data:
            print(self.empty_notes_book_message)
            input(self.continue_input_message)
            return # to previous menu
        else:
            while True:
                if not self.notes:
                    print(self.show_menu(self.premenu_title, self.premenu_options))
                    user_input = input(self.tags_input_message)
                    self.options_handler(user_input, self.SUBMENU_OPTIONS)
                    self.get_notes_to_change(user_input)
                else:
                    print(self.show_menu(self.menu_title, self.menu_options))
                    print(self.notes.show_notes())
                    user_input = input(self.input_message)
                    if not self.options_handler(user_input, self.MENU_OPTIONS):
                        print(self.wrong_input_message)

# GET NOTES TO CHANGE
    @error_handler
    def get_notes_to_change(self, user_input) -> None:
        notes_catalog = NOTES_BOOK.find_notes(user_input)
        if notes_catalog:
            while True:
                print(self.show_menu(self.premenu_title, self.premenu_options))
                print(NOTES_BOOK.show_notes_book(notes_catalog))
                user_input = input(self.notes_indx_input_message)
                self.options_handler(user_input, self.SUBMENU_OPTIONS)
                if self.notes_choosing(notes_catalog, user_input):
                    return # to main call
        else:
            print(self.no_matches_message)
            input(self.continue_input_message)

    @error_handler
    def notes_choosing(self, notes_catalog: dict, user_input: str) -> bool:
        self.notes = notes_catalog[int(user_input.strip())]
        return True

#CHANGE TAGS
    @error_handler
    def option_change_tags(self) -> None:
        while True:
            print(self.show_menu(self.submenu_title, self.submenu_options))
            user_input = input(self.tags_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_tags_in_notes(user_input):
                return #to main call

    @error_handler
    def change_tags_in_notes(self, user_input) -> None:
        self.notes.add_tags(user_input)
        self.notes.create_notes()
        autosave()
        print(self.change_successful_message)
        input(self.continue_input_message)
        return True

# CHANGE TEXT
    @error_handler
    def option_change_notes_text(self) -> None:
        while True:
            print(self.show_menu(self.submenu_title, self.submenu_options))
            user_input = input(self.text_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.change_text_in_notes(user_input):
                return #to main call

    @error_handler
    def change_text_in_notes(self, user_input) -> None:
        self.notes.add_text(user_input)
        self.notes.create_notes()
        autosave()
        print(self.delete_successful_message)
        input(self.continue_input_message)
        return True

# GET ANOTHER NOTES
    @error_handler
    def option_get_another_notes(self) -> None:
        while True:
            print(self.show_menu(self.submenu_title, self.submenu_options))
            user_input = input(self.tags_input_message)
            self.options_handler(user_input, self.SUBMENU_OPTIONS)
            if self.get_notes_to_change(user_input):
                return # to main call

# DELETE NOTES
    @error_handler
    def option_delete_notes(self) -> None:
        user_input = input(self.delete_input)
        if user_input == 'y':
            NOTES_BOOK.delete_notes(self.notes)
            self.notes = None
            autosave()
            print(self.delete_successful_message)
            input(self.continue_input_message)
