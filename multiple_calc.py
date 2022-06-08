#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 2 2022
# display 5 ints in a line

def pig_latin_convert(u_sentence):
    words = u_sentence.split()

    for i, word in enumerate(words):

        '''
        if first letter is a vowel
        '''
        if word[0] in 'aeiou':
            words[i] = words[i]+ "ay"
        else:
            '''
            else get vowel position and postfix all the consonants
            present before that vowel to the end of the word along with "ay"
            '''
            has_vowel = False

            for j, letter in enumerate(word):
                if letter in 'aeiou':
                    words[i] = word[j:] + word[:j] + "ay"
                    has_vowel = True
                    break

            #if the word doesn't have any vowel then simply postfix "ay"
            if(has_vowel == False):
                words[i] = words[i]+ "ay"

    pig_latin = ' '.join(words)
    return pig_latin


def common_elements(list_1, list_2):
    common_str = ""
    for temp_str1 in list_1:
        for temp_str2 in list_2:
            if temp_str1 == temp_str2:
                common_str += temp_str1
    return common_str


def palindrome_check(string):
    reversed_word = ""
    for i in string:
        reversed_word = i + reversed_word
    return reversed_word


def main():
    while True:
        calc = input(
            "What would you like to calculate(P = checking if a string is a Palindrome/PL = converts your string into pig latin/CE = Checks for the common elements in two lists): "
        ).upper()
        try:
            if calc == "PL" or calc == "PIG LATIN":
                u_sentence = input("What is the string you want to convert: \n")
                answer = pig_latin_convert(u_sentence)
                print("The string converted to pig latin is:\n{}".format(answer))
            elif calc == "CE" or calc == "COMMON ELEMENTS":
                u_list_1 = list(
                        input("Enter in your first array of characters(seperated by a comma): \n").strip().split())
                u_list_2 = list(
                        input("Enter in your second array of characters(seperated by a comma): \n").strip().split())
                answer = common_elements(u_list_1, u_list_2)
                print("The common elements in the array are: {}".format(answer))
            elif calc == "P" or calc == "PALINDROME":
                u_string = input("Enter in a string of characters:\n")
                answer = palindrome_check(u_string)
            else:
                print("You have to enter a valid calculator")
        except:
            print("You have to input a valid number")
        input("Press <enter> to restart: ")


if __name__ == "__main__":
    main()
