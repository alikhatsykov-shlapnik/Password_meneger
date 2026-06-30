import keyword
import sys
import os


#Дщобавляем src в путь, чтобы Python видел модули
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.password_generator import generate_password
from src.notes_manager import add_note, search_notes, load_notes, delete_note

def print_notes(notes):
    """Выводит список заметок красиво"""
    if not notes:
        return print("Not have notes!")
    for note in notes:
        return print(f"[{note.id}] {note.title} - {note.text[:30]}... ({note.created_at})")

def main():
    while True:
        print("\n" + "="*40)
        print("🐱‍🏍Менеджер паролей и заметок")
        print("1 Сгенерировать пароль")
        print("2 Добавить заметку")
        print("3 Найти заметку")
        print("4 Показать все заметки")
        print("5 Удалить заметку")
        print("6 Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            length_input = input("Длина (по умолч. 12): ") or "12"
            length = int(length_input)
            print("Password:", generate_password(length))

        elif choice == "2":
            title = input("Заголовок: ")
            text = input("Текст: ")
            add_note(title, text)

        elif choice == "3":
            keyword = input("Ключевое слово: ")
            results = search_notes(keyword)
            print_notes(results)

        elif choice == "4":
            notes = load_notes()
            print_notes(notes)

        elif choice == "5":
            note_id = int(input("ID замутки для удаления: "))
            if delete_note(note_id):
                print("Note deleted")
            else:
                print("Note don't delet")

        elif choice == "6":
            print("See you!")
            break

if __name__ == "__main__":
    main()