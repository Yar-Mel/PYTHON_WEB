
from menu import MainMenu
from text_fields import GeneralText, StartText


# ----------ENTER TO MAIN MENU----------
def main() -> None:
    print(StartText.start_message)
    input(GeneralText.continue_input_message)
    MainMenu()


# ----------ENTRY POINT----------
if __name__ == '__main__':
    main()
