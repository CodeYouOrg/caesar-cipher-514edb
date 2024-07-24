# add your code here
from itertools import cycle
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def matchingLetter(letter):
    if letter in alphabet :
        longitud = alphabet.index(letter)+5
        if longitud > 25:
            letter = alphabet[longitud - 26]
        else:
            letter = alphabet[alphabet.index(letter)+5]
    return letter    


user_text = input('Please enter a senctence: ')
user_text = user_text.lower()

resp = ""
for let in user_text:
    resp = resp + matchingLetter(let)
print('The encrypted sentence is:', resp)
