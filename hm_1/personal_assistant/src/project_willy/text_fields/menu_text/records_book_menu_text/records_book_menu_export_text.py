
class ExportMenuText:

    menu_title = '---EXPORT MENU---'
    menu_options = [
        '1. TXT',
        '2. PICKLE (RECOMENDED FOR BACKUP)',
        '3. JSON',
        '4. CSV (TABLE WIEV)',
        '0. RETURN TO RECORDS BOOK MENU',
        'EXIT'
    ]

    submenu_title = '---EXPORT SUBMENU---'
    submenu_options = [
        '0. RETURN TO EXPORT MENU',
        'EXIT'
    ]

    empty_records_book_message = '\nRecord book is empty. Nothing to export.\n'
    input_message = 'Choose file format to export.\n>>> '
    txt_path_input_message = 'TXT. Specify the path for export.\n>>> '
    pickle_path_input_message = 'PICKLE. Specify the path for export.\n>>> '
    json_path_input_message = 'JSON. Specify the path for export.\n>>> '
    csv_path_input_message = 'CSV. Specify the path for export.\n>>> '
    records_book_successful_message = '\nRecords book has been successfully exported!\n'
