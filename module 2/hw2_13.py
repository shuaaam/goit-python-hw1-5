'''Довольно часто программисты сталкиваются с задачами кодирования информации. Закодировать сообщение в чате между двумя пользователями.
Зашифровать пароль и имя пользователя при аутентификации пользователя по сети и т.д.

Напишите программу, реализующую код Цезаря. Назван он в честь великого римского императора Юлия Цезаря.

Идея шифрования заключается в циклическом сдвиге букв на заданное количество. Например, если сдвиг на три позиции, то буква A становится буквой D, B – E, и т.д.
Последние три буквы алфавита зацикливаются и переносятся в начало. Буква X становится A, Y – B, а Z – C. Цифры, пробелы и другие символы не подвергаются шифрованию.

В программе пользователь вводит фразу и число для сдвига, после чего надо вычислить новое закодированное сообщение.
Программа будет шифровать как строчные (a-z), так и прописные буквы (A-Z).
Для решения этой задачи вам понадобится знание двух новых функций. Первая функция ord. Она преобразует символ в целочисленную позицию в таблице ASCII.

ord("a")  # 97
Можно считать, что полученный результат 97 — это числовое представление символа a для компьютера.

Обратная функция chr возвращает строковый символ в таблице ASCII по позиции, переданной в качестве аргумента.
chr(118)  # 'v'
Более подробный принцип шифрования.

Рассмотрим для примера, как зашифровать символ v. Чтобы получить позицию символа v относительно начального символа a, необходимо выполнить выражение
pos = ord('v') - ord('a')  # 21
Но, согласно алгоритму, нам необходимо учитывать смещение, которое может быть произвольным, например 33. И помнить, что алфавит английского языка основан на латинском алфавите и состоит из 26 букв. Поэтому конечная позиция символа v относительно символа a для шифровки с учетом этого — равна 2.

pos = ord('v') - ord('a')  # 21
pos = (pos + 33) % 26  # 2
Остался последний шаг, получить новый символ:

pos = ord('v') - ord('a')  # 21
pos = (pos + 33) % 26  # 2
new_char = chr(pos + ord("a"))  # 'c'
Символ v со смещением 33 шифруется символом c.

Тесты проверяют и кодируют следующие строки:

"Hello my little friends!", offset = 37,
"Hello world!", offset = 7'''

message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""

for ch in message:

    if 'a' <= ch <= 'z':
        encoded_message += chr((ord(ch) + offset - ord('a')) % 26 + ord('a'))

    elif 'A' <= ch <= 'Z':
        encoded_message += chr((ord(ch) + offset - ord('A')) % 26 + ord('A'))
    else:
        encoded_message += ch
