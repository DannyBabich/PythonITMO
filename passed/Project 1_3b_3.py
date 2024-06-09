word = input('Введите слово ')
new_word = []
while True:
    new_word.append(word[0])
    word = input('Введите слово ')
    if word =='':
        break

print(''.join(new_word))






