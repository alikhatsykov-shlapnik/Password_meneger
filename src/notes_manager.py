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

def save_notes(notes: list[Note]) -> None:
    """Сохраняет объекты Note в JSON"""
    with open(NOTES_FILE, "w", encoding = "utf-8") as f:
        #Превращаем объекты в словари ждя JSON
        json.dump([note.__dict__ for note in notes], f, ensure_ascii = False, indent = 2)

def add_note(title: str, text: str) -> None:
    notes = load_notes()
    new_note = Note.create(title, text)
    new_note.id =len(notes) + 1
    notes.append(new_note)
    save_notes(notes)
    print(f"✔ Заметка '{title}' сохранена!")

def search_notes(keyword: str) ->list[Note]:
    notes = load_notes()
    results = [
        note for note in notes
        if keyword.lower() in note.title.lower() or keyword.lower() in note.text.lower()
    ]
    return results

def delete_note(note_id: int) -> bool:
    notes = load_notes()
    initial_len = len(notes)
    notes = [note for note in notes if note.id != note_id]
    save_notes(notes)
    return len(notes) <initial_len