
class ShowRecordsMenuText:

    menu_title = '---SHOW RECORDS MENU---'
    menu_options = [
        '1. FIND RECORD',
        '2. SHOW BIRTHDAYS',
        '3. SHOW ALL RECORDS',
        '4. DEBUG INFO',
        '0. RETURN TO RECORDS BOOK MENU',
        'EXIT'
    ]

    submenu_title = '---SHOW RECORDS SUBMENU---'
    submenu_options = [
        '0. RETURN TO SHOW RECORDS MENU',
        'EXIT'
    ]

    input_message = 'You are in "SHOW RECORDS MENU". Choose one of the options.\n>>> '
    days_input_message = 'Enter number of days to search. [Only digits!]\n>>> '
    search_input_message = 'Enter name, phone or email to find record.\n>>> '
    no_matches_message = "\nNo matches. Try again\n"
    record_not_exists_message = "\nRecord do not exists. Nothing to show\n"
    record_input_message = 'You want to see some record? But who will it be?\n>>> '
    empty_records_book_message = '\nRecord book is empty. Nothing to look at.\n'
    birthday_info = '\nCurrent year info.\n'
