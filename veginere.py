from string import ascii_lowercase
alphabet = (list(ascii_lowercase))
def alphindex(letter):
    return (alphabet.index(letter)+1)
class veginere:
    def encrypt(plaintext, key):
        ciphertextlist = []
        plaintext = list(plaintext)
        key = list(key)
        i2 = 0 # used to iterate only letters and not spaces etc.
        for i in range(len(plaintext)):
            if plaintext[i].lower() in alphabet:
                plainletter = plaintext[i]
                keyletter = key[(i-i2)%len(key)] #Key letter 
                cipherlettern = (alphindex(keyletter)+alphindex(plainletter.lower())-2)%len(alphabet)#the alphabet index of key letter times alphindex of plainletter modulu(%) by 26
                cipherletter = alphabet[cipherlettern]
                if plainletter.islower():
                    ciphertextlist.append(cipherletter)
                else:
                    ciphertextlist.append(cipherletter.upper())
            else:
                i2 += 1 #Subtract from iteration of key
                ciphertextlist.append(plaintext[i])
        return ''.join(ciphertextlist)
    def decrypt(ciphertext, key):
        plaintextlist = []
        ciphertext = list(ciphertext)
        key = list(key)
        i2 = 0
        for i in range(len(ciphertext)):
            if ciphertext[i].lower() in alphabet:
                cipherletter = ciphertext[i]
                keyletter = key[(i-i2)%len(key)]
                plainlettern = (alphindex(cipherletter.lower())-alphindex(keyletter)+len(alphabet))%len(alphabet)
                if plainlettern < 0:
                    plainlettern *= -1
                plainletter = alphabet[plainlettern]
                if cipherletter.islower():
                    plaintextlist.append(plainletter.lower())
                else:
                    plaintextlist.append(plainletter.upper())
            else:
                i2 += 1
                plaintextlist.append(ciphertext[i])
        return "".join(plaintextlist)