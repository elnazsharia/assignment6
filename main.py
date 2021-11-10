from os import read


words_bank = []


def dict_data():
    with open('wordsBank.txt', 'r') as f:
        text = f.read()
        words = text.split('\n')
        for i in range(0, len(words), 2):
            words_bank.append({'english': words[i], 'persian': words[i+1]})


def translate_en_to_per():
    user_input_text = input("please enter your text:  ")
    user_words = user_input_text.split(" ")

    output = ""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word['english']:
                output += word['persian'] + ' '
                break
        else:
            output += user_word + ' '
    print(output)


dict_data()


def translate_per_to_en():
    user_input_text = input("please enter your text:  ")

    user_words = user_input_text.split(" ")

    output = ""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word['persian']:
                output += word['english'] + ' '
                break
        else:
            output += user_word + ' '
    print(output)


def add_new_word():

    with open('wordsBank.txt', 'r') as f:
        text = f.read()
        en_word = f.write(input("enter a word!  "))
        """ fa_word = f.write(
            input("please translate in to farsi to add it to your database!:  ")) """
        for word in words_bank:
            if en_word != word:
                flag = 1
            else:
                flag = 0

            if(flag == 1):
                text.append(en_word)
    print(words_bank)


def menu():
    user_choice = int(input(
        "please enter a number:\n1-dd new word\n2-english 2 persian\n3-persian 2 english\n4-exit"))
    if user_choice == 1:
        add_new_word()
    elif user_choice == 2:
        translate_en_to_per()
    elif user_choice == 3:
        translate_per_to_en()
    else:
        exit


menu()
