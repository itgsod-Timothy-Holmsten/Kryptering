

def encrypt(cleartext, offset):
    """This function encrypts a string by using an offset and the alphabet.

    :args:
        cleartext (str): The string the function will try to encrypt.

        offset (int): Offset is the amount the index should added upon.

    :returns:
        Returns an encrypted version of cleartext.

    :raises:
        :ValueError: If the string is empty.
        :ValueError: If the offset is zero.


    *Example:*
        Use:
            encrypt("grillkorv", 4)

        Returns:
            string: *"KVMPPOSVZ"*
    """

    if len(cleartext) == 0:
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    encrypted_str = ""

    for char in cleartext:
        if char.upper() in alphabet:
            ## Takes the index of the letter from the list called alphabet
            ## and adds the offset to that index and compares that with the
            ## modulo of list's length.
            index = (alphabet.index(char.upper()) + offset) % len(alphabet)
            ## This is the encrypted character it will add to the encrypted_str.
            new_char = alphabet[index]
            ## This is the encrypted string it will later return, here it adds
            ## the encrypted character to the string.
            encrypted_str += new_char
        else:
            encrypted_str += char
    return encrypted_str

def decrypt(cleartext, offset):
    return encrypt(cleartext, -offset).lower()

print(encrypt("grillkorv", 4))