#########################################
# Resources:
# https://stackoverflow.com/questions/16008670/how-to-hash-a-string-into-8-digits/16008760#16008760
# https://llimllib.github.io/bloomfilter-tutorial/
##########################################

import hashlib
import sys

# create an array to hold results
bloom3 = [0] * 1000000
bloom5 = [0] * 1000000

# converts each line into hash and then inputs them into the bloom filter


def pop_bloom(string):

    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (10 ** 6)
    print("sha256: ", sha256_hash)

    md5_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 6)
    print("md5: ", md5_hash)

    sha1_hash = int(hashlib.sha1(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 6)
    print("sha1: ", sha1_hash)

    sha224_hash = int(hashlib.sha224(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 6)
    print("sha224: ", sha224_hash)

    sha384_hash = int(hashlib.sha384(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 6)
    print("sha384: ", sha384_hash)

    if bloom3[sha256_hash] == 1 & bloom3[md5_hash] == 1 & bloom3[sha1_hash] == 1:
        print("That password maybe no good.")

    # checking each hash against what has been seen before
    if bloom3[sha256_hash] == 0:
        bloom3[sha256_hash] = 1

    if bloom3[md5_hash] == 0:
        bloom3[md5_hash] = 1

    if bloom3[sha1_hash] == 0:
        bloom3[sha1_hash] = 1


def read_file_contents(string):

    with open(string, 'r') as file:
        for file_contents in file:
            pop_bloom(file_contents)

    file.close()


print(bloom3)

# takes the arguments at run time and for the file.
string_one = read_file_contents(sys.argv[1])
print("break")
string_two = read_file_contents(sys.argv[2])


# way to calculate how big each bloom filter should be.
# way to tell the user if the password passes the bloom filter or has been seen maybe
# wrtie to a file the output of the users file input
# Need to add two more hash functions and a way to input data into both bloom filters
