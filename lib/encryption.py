def encrypt(cleartext, offset):
    if len(cleartext) == 0:
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    encrypted_str = ""

    for char in cleartext:
        if char.upper() in alphabet:
            index = (alphabet.index(char.upper()) + offset) % len(alphabet)
            new_char = alphabet[index]
            encrypted_str += new_char
        else:
            encrypted_str += char
    return encrypted_str

def decrypt(cleartext, offset):
    return encrypt(cleartext, -offset).lower()