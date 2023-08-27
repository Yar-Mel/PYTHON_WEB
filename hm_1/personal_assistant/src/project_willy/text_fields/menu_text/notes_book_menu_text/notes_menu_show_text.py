
class ShowNotesMenuText:

    menu_title = '---SHOW NOTES MENU---'
    menu_options = [
        '1. FIND NOTES',
        '2. SORT ALL BY A-Z',
        '3. SORT ALL BY DATE',
        '4. DEBUG INFO',
        '0. RETURN TO NOTES MENU',
        'EXIT'
    ]

    submenu_title = '---SHOW NOTES SUBMENU---'
    submenu_options = [
        '0. RETURN TO SHOW NOTES MENU',
        'EXIT'
    ]

    empty_notes_book_message = '\nNotes book is empty. Nothing to look at.\n'
    input_message = 'You are in "SHOW NOTES MENU". Choose one of the options.\n>>> '
    search_input_message = 'Enter tags to find notes.\n>>> '
    no_matches_message = '\nNo matches. Try again\n'
