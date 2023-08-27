
from methods.errors_methods import Return, ExitFromCLI
from settings import MenuReprSettings


class MenuGeneral(MenuReprSettings):
    
# MENU REPRESENTATION
    def show_menu(self, menu_title: str, options: list) -> str:
        result = self.menu_title_pattern.format(menu_title, self.menu_end_of_line)
        for option in options:
            result += self.menu_row_pattern.format(option, self.menu_end_of_line)
        return result
    
    
# OPTIONS HANDLER FOR MENU
    def options_handler(self, user_command: str, options: dict) -> bool:
        command = user_command.strip().lower()
        if command in options:
            options[command]()
            return True

# RETURN TO PREVIOUS OPTION
    def option_return_to_previous(self) -> None:
        raise Return

# EXIT FROM PROGRAM OPTION
    def option_exit_from_cli(self) -> None:
        raise ExitFromCLI
