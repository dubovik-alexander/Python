# Начнем с импорта библиотеки:
import tkinter as tk

# Затем создадим основное окно:
root = tk.Tk()
root.title("Слова из букв")
root.geometry("500x500")

# Создадим текстовое поле для ввода текста:
input_text = tk.Text(root, height=2, width=50)
input_text.pack()

# создаем текстовое поле для вывода результата
output_text = tk.Text(root, height=20, width=50)
output_text.pack()

# Загружаем библиотеку для генерации перестановок
from itertools import permutations


# Функция, которая проверяет, существует ли слово в словаре
def is_word(word, dictionary):
    return word in dictionary

# Считываем словарь из файла
with open('russian_nouns.txt', 'r', encoding='utf-8') as f:
    dictionary = set(line.strip() for line in f)

# Затем создадим кнопку, которая будет запускать обработку текста и выводить результат в окне ниже:
def process_text():
    text = input_text.get("1.0", "end-1c")
    output_text.delete("1.0", "end") # удаляем предыдущий результат перед выводом нового
    # здесь ваш код обработки текста
    # Получаем буквы от пользователя
    letters = text.lower()

    # Генерируем всевозможные перестановки букв
    perms = {"".join(perm) for length in range(3, len(letters)+1) for perm in permutations(letters, length)}

    # Фильтруем перестановки, оставляя только те, из которых можно составить слово из словаря
    words = sorted(filter(lambda x: is_word(x, dictionary), perms))

    words.sort(key=len)

    lines = sorted((sorted(word.rstrip().split(), key=len) for word in words), key=len)
    for word in words:
        output_text.insert("end", f"Кол-во букв: {len(word)}, слово: {' '.join(word)}\n")
    
process_button = tk.Button(root, text="Ввод", command=process_text)
process_button.pack()

# И наконец, запустим основной цикл приложения:
root.mainloop()