import json
import os
from src.models import Note

NOTES_FILE = "data/notes.json"

def load_notes() -> list[Note]:
    """Загружает заметки из JSON и превращает их в обьекты Note"""
    if not os.path.exists(NOTES_FILE):
        return[]
    with open(NOTES_FILE, "r", encoding = "utf-8") as f:
        data = json.load(f)
        return[Note(**item) for item in data]

def save_notes(notes):
    try:
        """Сохраняет объекты Note в JSON"""
        with open(NOTES_FILE, "w", encoding = "utf-8") as f:
            #Превращаем объекты в словари ждя JSON
            json.dump([note.__dict__ for note in notes], f, ensure_ascii = False, indent = 2)
    except Exception as e:
        print(f"💣 ошибка при сохранении: {e}")

def add_note(title: str, text: str) -> None:
    try:
        notes = load_notes()
        existing_ids = {note.id for note in notes} #получение всех ID
        new_id = 1
        while new_id in existing_ids:
            new_id += 1

        new_note = Note.create(title, text)
        new_note.id = new_id #заметка с найденным свободным ID

        notes.append(new_note)
        save_notes(notes)
        print(f"✔ Заметка '{title}' сохранена! (ID: {new_id})")
    except Exception as e:
        print(f"💣 ошибка при сохранении заметки: {e}")
        
def search_notes(keyword: str) ->list[Note]:
    try:
        notes = load_notes()
        results = [
            note for note in notes
            if keyword.lower() in note.title.lower() or keyword.lower() in note.text.lower()
        ]
        return results
    except Exception as e:
        print(f"💣 ошибка при поиске: {e}")


def get_note_by_id(note_id):
    """Получает заметку по ID"""
    notes = load_notes()
    for note in notes:
        if note.id == note.id:
            return note
    return None

def delete_note(note_id: int) -> bool:
    try:
        note = get_note_by_id(note_id) #получаем заметку
        if note is None:
            print(f"Заметка с ID {note_id} не найдена") 
            return False
        
        notes = load_notes() #Загружает все заметки
        notes = [n for n in notes if n.id != note_id]#Сохраняет

        save_notes(notes)
        print(f"Заметка '{note.title}' удалена.")
        return True
    except Exception as e:
        print(f"💣 ошибка при удалении: {e}")
        return False

def reindex_notes():
    """Перенумеровывает все заметки по порядку"""
    notes = load_notes()
    if not notes:
        print("Заметок нет, переиндексация не ыозможна.")
        return
    for index, note  in enumerate(notes, start = 1):
        note.id = index

    save_notes(notes)
    print(f"ID перенумерованы по порядку (1..{len(notes)})")
