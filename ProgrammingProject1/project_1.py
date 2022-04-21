import hashlib
from typing import Counter

# create an array to hold results
bloom3 = [0] * 10
print(bloom3)

bloom5 = [0] * 10
print(bloom5)


def compute_sha256_hash(string):

    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (10 ** 1)
    print("sha256: ", sha256_hash)
    if bloom3[sha256_hash] == 0:
        bloom3[sha256_hash] = 1

    md5_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 1)
    print("md5: ", md5_hash)
    if bloom3[md5_hash] == 0:
        bloom3[md5_hash] = 1

    sha1_hash = int(hashlib.sha1(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 1)
    print("sha1: ", sha1_hash)
    if bloom3[sha1_hash] == 0:
        bloom3[sha1_hash] = 1


#file_name = input("file name: ")
# file_name
with open("sample_input.txt", 'r') as file:
    for file_contents in file:
        compute_sha256_hash(file_contents)

print(bloom3)

file.close()
