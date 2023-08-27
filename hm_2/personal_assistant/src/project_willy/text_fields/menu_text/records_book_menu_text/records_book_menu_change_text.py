
class ChangeRecordMenuText:
    
    menu_title = '---CHANGE RECORD MENU---'
    menu_options = [
        '1. CHANGE RECORD NAME',
        '2. CHANGE RECORD PHONE',
        '3. CHANGE RECORD EMAIL',
        '4. CHANGE RECORD BIRTHDAY',
        '5. CHOOSE ANOTHER RECORD',
        '6. DELETE RECORD',
        '0. RETURN TO RECORDS BOOK MENU',
        'EXIT'
    ]
    
    premenu_title = '---CHANGE RECORD PREMENU---'
    premenu_options = [
        '0. RETURN TO RECORDS BOOK MENU',
        'EXIT'
    ]
    
    submenu_title = '---CHANGE RECORD SUBMENU---'
    submenu_options = [
        '0. RETURN TO CHANGE RECORD MENU',
        'EXIT'
    ]
    
    empty_records_book_message = '\nRecord book is empty. Nothing to change.\n'
    
    record_not_exists_message = "\nRecord do not exists. First create record\n"
    input_message = 'You are in "CHANGE RECORD MENU". What do you want to change?\n>>> '
    record_input_message = 'Input something to find record.\n>>> '
    name_input_message = 'Input new name for user.\n>>> '
    phone_input_message = 'Input new or additional phone for user.\n>>> '
    email_input_message = 'Input new email for user.\n>>> '
    birthday_input_message = 'Input new birthday date for user.\n>>> '
    change_successful_message = '\nRecord has been successfully changed.\n'
    delete_input = 'Are you sure? Enter "y" to continue.\n>>> '
    delete_successful_message = '\nRecord has been successfully deleted.\n'
    record_indx_input_message = 'Input number of one of records to change.\n>>> '
    no_matches_message = '\nNo matches. Try again\n'
    record_exists_message =  '\nRecord wiht this name alredy exists!\n'