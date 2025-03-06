

def remove_vowels(string: str) -> str:
    # Определяем латинские и кириллические гласные
    vowels = "aeiouyYAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    # Удаляем гласные из строки
    return ''.join(char for char in string if char not in vowels)

# Запрашиваем строку у пользователя
input_string = input("Input any word: ")

# Выводим строку без гласных
output_string = remove_vowels(input_string)
print("Removed vowels:", output_string)
