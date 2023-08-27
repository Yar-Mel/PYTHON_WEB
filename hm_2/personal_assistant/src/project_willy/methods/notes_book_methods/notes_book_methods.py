
from methods.imports import UserList, UserDict, datetime
from methods.errors_methods import NotesError
from methods.notes_book_methods.notes_book_representation_methods import NotesBookRepr, NotesRepr

class Notes(UserDict, NotesRepr):
    def __init__(self) -> None:
        UserDict.__init__(self)
        self.data = {
            'tags': None,
            'text': None,
            'date_of_change': None
        }
    
# ADD TAGS TO NOTES
    def add_tags(self, user_input: str) -> None:
        if user_input.strip():
            new_tags = user_input.strip().split()
            if len(new_tags) == 1:
                tags = new_tags
            if len(new_tags) >= 2:
                _set = set(new_tags)
                tags = [i for i in _set]
            self.data['tags'] = tags  
        else:
            raise NotesError

# ADD TEXT TO NOTES
    def add_text(self, user_input: str) -> None:
        text = user_input.strip()
        if len(text) > 300:
            raise NotesError
        self.data['text'] = text

# CREATE OR CHANGING NOTES
    def create_notes(self) -> None:
        if self.data['tags'] != None and self.data['text'] != None:
            self.data['date_of_change'] = datetime.now()
            
# GET STR            
    def get_tags(self) -> str:
        return ', '.join(self.data['tags'])

    def get_text(self) -> str:
        return self.data['text']

    def get_date(self) -> str:
        return f"{self.data['date_of_change'].date()}"

class NotesBook(UserList, NotesBookRepr):
    def __init__(self) -> None:
        UserList.__init__(self)

# ADD NOTES
    def add_notes(self, notes: Notes) -> None:
        self.data.append(notes)

# DELETE NOTES
    def delete_notes(self, notes: Notes)-> None:
        self.data.remove(notes)

# CLEAR NOTES BOOK
    def clear(self) -> None:
        self.data.clear()

# FIND NOTES
    def find_notes(self, user_input: str) -> dict:
        result = {}
        count = 0
        search_tags = user_input.strip().split()
        for notes in self.data:
            for tag in search_tags:
                if tag.lower() in ''.join(notes['tags']).lower():
                    count += 1
                    result.update({count: notes})
        if result.values():
            return result 
     

# SORT NOTES BY DATE
    def sort_by_date(self) -> dict:
        result = {}
        index = 1

        # Збираємо та сортуємо всі наявні дати
        sorted_dates = sorted([note['date_of_change'] for note in self.data])

        # Ітеруємось по списку та повертаємо словник із нотатками, відсортованих по даті
        for note_date in sorted_dates:
            for note in self.data:
                if note_date == note['date_of_change']:
                    result.update({index: note})
                    index += 1
        return result

# SORT NOTES BY TAGS
    def sort_a_z(self) -> dict:
        list_of_tags = []
        result = {}
        index = 1

        # Збираємо та відсортовуємо всі наявні теги
        for note in self.data:
            temp_result = ''
            temp_list = sorted([tag for tag in note['tags']])
            for elem in temp_list:
                temp_result += elem + ' '
            temp_list.clear()

            list_of_tags.append(temp_result.removesuffix(' '))
            list_of_tags.sort()

        # Ітеруємось по списку та повертаємо словник із нотатками, відсортованих по тегах
        for sorted_tags in list_of_tags:
            temp_tags = set(sorted_tags.split(' '))
            for note in self.data:
                check_set = temp_tags & set(note['tags'])
                if len(check_set) == len(temp_tags):
                    result.update({index: note})
                    index += 1
        return result

# NOTES CALCULATING
    def notes_calculatig(self) -> str:
        return f'Number of notes in the book: {len(self.data)}\n'
    