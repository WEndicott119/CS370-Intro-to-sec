import hashlib
from typing import Counter

# create an array to hold results
bloom3 = [0] * 20
print(bloom3)

bloom5 = [0] * 10
print(bloom5)


def compute_sha256_hash(string):

    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (10 ** 4)
    print("sha256: ", sha256_hash)

    mds_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 4)
    print("md5: ", mds_hash)

    sha1_hash = int(hashlib.sha1(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 4)
    print("sha1: ", sha1_hash)


#file_name = input("file name: ")
# file_name
with open("sample_input.txt", 'r') as file:
    for file_contents in file:
        compute_sha256_hash(file_contents)

file.close()
