
class ChangeNotesMenuText:

    menu_title = '---CHANGE NOTES MENU---'
    menu_options = [
        '1. CHANGE TAGS',
        '2. CHANGE NOTES TEXT',
        '3. DELETE NOTES',
        '4. CHOOSE ANOTHER NOTES',
        '0. RETURN TO NOTES MENU',
        'EXIT'
    ]
    
    premenu_title = '---CHANGE NOTES PREMENU---'
    premenu_options = [
        '0. RETURN TO NOTES MENU',
        'EXIT'
    ]
    
    submenu_title = '---CHANGE NOTES SUBMENU---'
    submenu_options = [
        '0. RETURN TO CHANGE NOTES MENU',
        'EXIT'
    ]

    tags_input_message = 'Input some tags to begin.\n>>> '
    input_message = 'You are in "CHANGE NOTES MENU". Choose one of the options.\n>>> '
    tags_input_message = 'Input tags for notes, please.\n>>> '
    text_input_message = 'Input text of notes, please.\n>>> '
    empty_notes_book_message = '\nNotes book is empty. Nothing to look at.\n'
    notes_indx_input_message = 'Input number of one of notes to change.\n>>> '
    delete_input = 'Are you sure? Enter "y" to continue.\n>>> '
    change_successful_message = '\nThe notes has been changed successfully!\n'
    delete_successful_message = '\nThe notes has been deleted successfully!\n'
    no_matches_message = '\nNo matches. Try again\n'
