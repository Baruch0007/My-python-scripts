code_morse = {
              '.-' : 'a',
              '-...' : 'b',
              '-.-.' : 'c',
              '-..' : 'd',
              '.' : 'e',
              '..-.' : 'f',
              '--.' : 'g',
              '....' : 'h',
              '..' : 'i',
              '.---' : 'j',
              '-.-' : 'k',
              '.-..' : 'l',
              '--' : 'm',
              '-.' : 'n',
              '---' : 'o',
              '.--.' : 'p',
              '--.-' : 'q',
              '.-.' : 'r',
              '...' : 's',
              '-' : 't',
              '..-' : 'u',
              '...-' : 'v',
              '.--' : 'w',
              '-..-' : 'x',
              '-.--' : 'y',
              '--..' : 'z',
              '/' : ' '
            }

sentence_in_morse = '.. ..-. / -.-- --- ..- / -.-. .- -. / .-. . .- -.. / - .... .. ... / -.-- --- ..- / .- .-. . / .- / --. . -. .. ..- ...'
 
listed_morse = sentence_in_morse.split(' ')
listed_english = []
for  letter in listed_morse:
    listed_english.append(code_morse[letter])
sentence_in_english = ''.join(listed_english)

print('\n',sentence_in_morse,'\n')
print(sentence_in_english)
import time
time.sleep(3)
