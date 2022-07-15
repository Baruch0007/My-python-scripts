from time import sleep

text = 'attack at the dawn'
print(f'The Sentence we will encrypt:       {text}\n')
sleep(3)
Caesar_key=2

abc = 'abcdefghijklmnopqrstuvwxyz '
encoded_abc = abc[Caesar_key :-1]+abc[0: Caesar_key ]+ ' '

# יצירת מילון משני מערכים
caesar_cipher = dict()      
for i,j in zip(abc,encoded_abc):
    caesar_cipher[i]=j

#הצפנה
listed_encoded_text=[]
for letter in text:
    listed_encoded_text.append( caesar_cipher[letter] )
encoded_text=''.join(listed_encoded_text)
print(f'The encrypted sentence:     {encoded_text}\n')
sleep(3)

# יצירת מילון הפוך
caesar_cipher_reverse = dict()
for i,j in zip(abc,encoded_abc):
    caesar_cipher_reverse[j]=i

# פיענוח
listed_decoded_text=[]
for letter in encoded_text:
    listed_decoded_text.append( caesar_cipher_reverse[letter] )
decoded_text=''.join(listed_decoded_text)
print(f'The decrypted sentence:     {decoded_text}')


sleep(5)
