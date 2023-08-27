
from settings import NotesReprSettings, NotesBookReprSettings
from text_fields import MethodsText


class NotesRepr(NotesReprSettings):

    def table_title(self) -> str:
        result = self.notes_title_pattern.format('---NOTES---')
        result += self.notes_end_of_row_pattern.format(self.notes_end_of_row)
        return result

    def show_notes(self) -> str:
        result = self.table_title()
        if self.data['tags']:
            result += self.notes_head_row_pattern.format(self.get_tags())
        else: 
            result += self.notes_head_row_pattern.format(f'Tags: {MethodsText.DEFAULT_EMPTY_FIELD}')
        result += self.notes_end_of_row_pattern.format(self.notes_end_of_row)

        if self.data['text']:
            result += self.notes_head_row_pattern.format(self.get_text())
        else:
            result += self.notes_head_row_pattern.format(f'Text: {MethodsText.DEFAULT_EMPTY_FIELD}')            
        result += self.notes_end_of_row_pattern.format(self.notes_end_of_row)

        return result

class NotesBookRepr(NotesBookReprSettings):

    def table_title(self) -> str:
        result = self.notes_book_title_pattern.format('---NOTES BOOK---')
        return result

    def show_notes_book(self, notes_catalog: dict) -> str:
        result = self.table_title()
        for indx, notes in notes_catalog.items():
            result += self.notes_book_end_of_row_pattern.format(self.notes_book_end_of_row)
            result += self.notes_book_head_pattern.format(indx, notes.get_tags(), notes.get_date())
            result += self.notes_book_end_of_row_pattern.format(self.notes_book_end_of_row)
            result += self.notes_book_row_pattern.format(notes.get_text())
            result += self.notes_book_end_of_row_pattern.format(self.notes_book_end_of_row)
            result += '\n'
        return result
