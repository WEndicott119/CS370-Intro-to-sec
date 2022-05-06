import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

plain_text = b'This is a top secret.\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'
cipher_check = bytes.fromhex(
    "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9")


def read_file_contents(name):

    with open(name, 'r') as file:
        for file_contents in file:
            word = file_contents.strip()
            if len(word) > 16:
                continue
            iv = "0000000000000000"
            iv = iv.encode('utf-8')
            key = word.ljust(16)
            key_b = key.encode('utf-8')

            algo = algorithms.AES(bytes(key, 'ascii'))
            mode = modes.CBC(bytes.fromhex('00000000000000000000000000000000'))
            cipher = Cipher(algo, mode).encryptor()
            encryped_text = cipher.update(plain_text) + cipher.finalize()

            if(encryped_text == cipher_check):
                print("found it")
                print(word)

    file.close()


read_file_contents(sys.argv[1])
