import sys
import os

#Дщобавляем src в путь, чтобы Python видел модули
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.password_generator import generate_password
from src.notes_manager import add_note, search_notes, load_notes, delete_note, reindex_notes

def print_notes(notes):
    """Выводит список заметок"""
    if not notes:
        return print("Not have notes!")
    
    for note in notes:
        if isinstance(note, dict):
            print(f"[{note.get('id', '?')}] {note.get('title', 'Без заголовка')} - {note.get('text', '')[:30]}... ({note.get('create_at', '')})")
        else:
            print(f"[{note.id}] {note.title} - {note.text[:30]}... ({note.create_at})")

def main():
    while True:
        print("\n" + "="*40)
        print("🐱‍🏍Менеджер паролей и заметок")
        print("1 Сгенерировать пароль")
        print("2 Добавить заметку")
        print("3 Найти")
        print("4 Показать все")
        print("5 Удалить")
        print("6 Сортировка ID")
        print("7 Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("password_name: ")
            length_input = int(input("Длина (по умолч. 12): ")) or "12"
            pas = generate_password(length_input)
            add_note(f"Password: {name}", f"Password:{pas}\nCreated: {__import__('datetime').datetime.now()}")
            print(f"Password is from: {name} saved.\nPassword: {pas}")

        elif choice == "2":
            try:
                title = input("Заголовок: ")
                text = input("Текст: ")
                add_note(title, text)
            except KeyboardInterrupt:
                print("\n Ок, отмена")
            except Exception as e:
                print(f"Ошибка: {e}")
                
        elif choice == "3":
            keyword = input("Ключевое слово: ")
            results = search_notes(keyword)
            print_notes(results)

        elif choice == "4":
            notes = load_notes()
            print_notes(notes)

        elif choice == "5":
            note_id = int(input("ID заметки для удаления: "))
            if delete_note(note_id):
                print("Note deleted")
            else:
                print("Note don't delet")

        elif choice == "6":
            reindex_notes()
        
        elif choice == "7":
            print("See you!")
            break
        else:
            print('Wrong input, try again')

if __name__ == "__main__":
    main()