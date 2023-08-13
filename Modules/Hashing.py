import hashlib
import random
from random_word import RandomWords

class Hashing:

    # * Function to create Hash
    # * Parameters: Password
    # * Return Value: Hashed Password
    @classmethod
    def creatingHash(cls, password: str) -> str:
        password_hash = hashlib.sha512(password.encode()).hexdigest()
        return password_hash

    # * Function to verify Hash
    # * Parameters: Password, Stored Passowrd Hash
    # * Return Value: True or False
    @classmethod
    def verifyingHash(cls, password: str, stored_password_hash: str) -> bool:
        password_hash = hashlib.sha512(password.encode()).hexdigest()
        if (password_hash == stored_password_hash):
            return True
        return False

    # * Function to generate Random Password
    # * No Parameters
    # * Return Value: Password -> String
    @classmethod
    def generatePassword(cls) -> str:
        spec_char = r'''!@$%^&*()_+-={}[]|\:;"'?/><,.~`#'''
        spec_char_len = len(spec_char)
        rw = RandomWords()
        hash = hashlib.sha512(rw.get_random_word().encode()).hexdigest()
        rInt = random.randint(0, 92)
        l = list(hash[rInt:rInt+35])
        for i in range(18):
            rIndex = random.randint(0,len(l)-1)
            if l[rIndex].isdigit():
                l[rIndex] = spec_char[random.randint(0,spec_char_len-1)]
            elif l[rIndex].islower():
                l[rIndex] = l[rIndex].upper()
        
        generated_password = "".join(l)
        return generated_password
