import string

def vigenere_crypter(message, key):
    """
    Cette fonction prend un message et une clé et renvoie le message crypté par le chiffrement de Vigenère.
    Les espaces sont conservés dans le message crypté.
    """
    message = message.upper()
    key = key.upper()
    encrypted_message = ""
    key_index = 0

    for i in range(len(message)):
        if message[i] == " ":
            encrypted_message += " "
        else:
            key_letter = key[key_index % len(key)]
            encrypted_letter = chr(((ord(message[i]) + ord(key_letter) - 2 * ord('A')) % 26) + ord('A'))
            encrypted_message += encrypted_letter
            key_index += 1

    return encrypted_message     # Renvoi du message crypté

