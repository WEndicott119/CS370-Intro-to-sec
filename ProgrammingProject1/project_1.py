#########################################
# Resources:
# https://stackoverflow.com/questions/16008670/how-to-hash-a-string-into-8-digits/16008760#16008760
# https://llimllib.github.io/bloomfilter-tutorial/
##########################################

import hashlib
import sys

# create an array to hold results
bloom3 = [0] * 9388608
bloom5 = [0] * 9388608

# converts each line into hash and then inputs them into the bloom filter

# hash functions populating the bloom filters.


def pop_bloom(string):

    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (9388608)
    bloom3[sha256_hash] = 1
    bloom5[sha256_hash] = 1

    md5_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)
    bloom3[md5_hash] = 1
    bloom5[md5_hash] = 1

    sha512_hash = int(hashlib.sha512(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)
    bloom3[sha512_hash] = 1
    bloom5[sha512_hash] = 1

    sha224_hash = int(hashlib.sha224(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)
    bloom5[sha224_hash] = 1

    sha384_hash = int(hashlib.sha384(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)
    bloom5[sha384_hash] = 1

# 3 hashing function bloom filter.


def check_user_3(string):
    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (9388608)

    md5_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)

    sha512_hash = int(hashlib.sha512(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)

    if bloom3[sha256_hash] == 1 and bloom3[md5_hash] == 1 and bloom3[sha512_hash] == 1:
        result = "Maybe     "
    else:
        result = "No    "

    # checking each hash against what has been seen before
    if bloom3[sha256_hash] == 0:
        bloom3[sha256_hash] = 1

    if bloom3[md5_hash] == 0:
        bloom3[md5_hash] = 1

    if bloom3[sha512_hash] == 0:
        bloom3[sha512_hash] = 1

    file = open('output3.txt', 'a')

    file.write(result)
    file.write(string)
    file.close()

# this is the 5 hashing function bloom filter


def check_user_5(string):
    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (9388608)

    md5_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)

    sha512_hash = int(hashlib.sha512(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)

    sha224_hash = int(hashlib.sha224(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)

    sha384_hash = int(hashlib.sha384(string.encode(
        "utf-8")).hexdigest(), 16) % (9388608)

    if bloom5[sha256_hash] == 1 and bloom5[md5_hash] == 1 and bloom5[sha512_hash] == 1 and bloom5[sha224_hash] == 1 and bloom5[sha384_hash] == 1:
        result = "Maybe     "
    else:
        result = "No    "

    # checking each hash against what has been seen before
    if bloom5[sha256_hash] == 0:
        bloom5[sha256_hash] = 1

    if bloom5[md5_hash] == 0:
        bloom5[md5_hash] = 1

    if bloom5[sha512_hash] == 0:
        bloom5[sha512_hash] = 1

    if bloom5[sha224_hash] == 0:
        bloom5[sha224_hash] = 1

    if bloom5[sha384_hash] == 0:
        bloom5[sha384_hash] = 1

    file = open('output5.txt', 'a')

    file.write(result)
    file.write(string)
    file.close()

# function to populate the bloom filters from a file with X amount of words


def read_file_contents(string):

    with open(string, 'r') as file:
        next(file)
        for file_contents in file:
            file_contents.strip()
            pop_bloom(file_contents)

    file.close()

# function to read the input from a file given by the user.


def read_user_input(string):

    with open(string, 'r') as file:
        next(file)
        for file_contents in file:
            file_contents.replace("\n", "")
            check_user_5(file_contents)
            check_user_3(file_contents)

    file.close()


# takes the arguments at run time and for the file.
read_file_contents(sys.argv[1])
read_user_input(sys.argv[2])
