from time import sleep

text = 'attack at the dawn'
print(f'The Sentence we will encrypt:       {text}\n')
sleep(3)
Caesar_key=2

abc = 'abcdefghijklmnopqrstuvwxyz '
encoded_abc = abc[Caesar_key :-1]+abc[0: Caesar_key ]+ ' '

# יצירת מילון משני מערכים
caesar_cipher = dict(zip(abc,encoded_abc))

# הצפנה
encoded_text=''.join([caesar_cipher[letter]
                      if letter in caesar_cipher
                      else letter
                      for letter in text])
print(f'The encrypted sentence:     {encoded_text}\n')
sleep(3)


# יצירת מילון הפוך
caesar_cipher = dict(zip(encoded_abc,abc))

# פיענוח
decoded_text=''.join([caesar_cipher[letter]
                      if letter in caesar_cipher
                      else letter
                      for letter in encoded_text])
print(f'The decrypted sentence:     {decoded_text}')


sleep(5)
