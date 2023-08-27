
class RecordsBookMenuText:

    menu_title = '---RECORDS BOOK MENU---'
    menu_options = [
        '1. ADD NEW RECORD',
        '2. CHANGE EXISTS RECORD',
        '3. SHOW RECORDS',
        '4. IMPORT RECORDS BOOK',
        '5. EXPORT RECORDS BOOK',
        '6. CLEAR RECORDS BOOK',
        '0. RETURN TO MAIN MENU',
        'EXIT'
    ]

    input_message = 'You are in "RECORDS BOOK MENU". Choose one of the options.\n>>> '
    empty_notes_book_message = '\nRecords book is empty. Nothing to clear.\n'
    clear_input = 'Are you sure? Enter "y" to continue.\n>>> '
    clear_successful_message = '\nThe record book has been cleared successfully!\n'
