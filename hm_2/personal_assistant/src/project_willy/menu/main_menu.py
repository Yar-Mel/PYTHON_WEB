
from methods.imports import traceback
from methods import MenuGeneral, error_handler, clean_folder
from text_fields import GeneralText, MainMenuText
from menu.main_menu_options import RecordsBookMenu, NotesBookMenu


class MainMenu(MenuGeneral, GeneralText, MainMenuText):
# OPTIONS
    def __init__(self) -> None:
        self.MENU_OPTIONS = {
        '1': self.option_records_book_menu,
        '2': self.option_notes_menu,
        '3': self.option_clean_folder_tool,
        'call_stack': self.option_show_current_call_stack,
        'exit': self.option_exit_from_cli,
        }
        self.__call__()

# MAIN CALL
    @error_handler
    def __call__(self) -> None:
        while True:
            print(self.show_menu(self.menu_title, self.menu_options))
            user_input = input(self.input_message)
            if not self.options_handler(user_input, self.MENU_OPTIONS):
                print(self.wrong_input_message)

# RECORDS BOOK
    def option_records_book_menu(self) -> None:
        RecordsBookMenu()
        
# NOTES MENU
    def option_notes_menu(self) -> None:
        NotesBookMenu()

# CLEAN FOLDER TOOL
    def option_clean_folder_tool(self) -> None:
        clean_folder()
        input(self.continue_input_message)

# SHOW CURRENT CALL STACK
    def option_show_current_call_stack(self) -> None:
        for line in traceback.format_stack():
            print(f'{line.strip()}\n')
        print(f'Number of calls: {len(traceback.format_stack())}\n')
        input(self.continue_input_message)
