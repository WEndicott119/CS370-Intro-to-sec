#########################################
# Resources:
# https://stackoverflow.com/questions/16008670/how-to-hash-a-string-into-8-digits/16008760#16008760
# https://llimllib.github.io/bloomfilter-tutorial/
##########################################

import hashlib
import sys

# create an array to hold results
bloom3 = [0] * 1000000000
bloom5 = [0] * 1000000000

# converts each line into hash and then inputs them into the bloom filter


def pop_bloom(string):

    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha256: ", sha256_hash)
    bloom3[sha256_hash] = 1
    bloom5[sha256_hash] = 1

    md5_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("md5: ", md5_hash)
    bloom3[md5_hash] = 1
    bloom5[md5_hash] = 1

    sha1_hash = int(hashlib.sha1(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha1: ", sha1_hash)
    bloom3[sha1_hash] = 1
    bloom5[sha1_hash] = 1

    sha224_hash = int(hashlib.sha224(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha224: ", sha224_hash)
    bloom5[sha224_hash] = 1

    sha384_hash = int(hashlib.sha384(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha384: ", sha384_hash)
    bloom5[sha384_hash] = 1


def check_user_3(string):
    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha256: ", sha256_hash)

    md5_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("md5: ", md5_hash)

    sha1_hash = int(hashlib.sha1(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha1: ", sha1_hash)

    if bloom3[sha256_hash] == 1 & bloom3[md5_hash] == 1 & bloom3[sha1_hash] == 1:
        result = "Maybe     "
    else:
        result = "No    "

    # checking each hash against what has been seen before
    if bloom3[sha256_hash] == 0:
        bloom3[sha256_hash] = 1

    if bloom3[md5_hash] == 0:
        bloom3[md5_hash] = 1

    if bloom3[sha1_hash] == 0:
        bloom3[sha1_hash] = 1

    file = open('output3.txt', 'a')

    file.write(result)
    file.write(string)


def check_user_5(string):
    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha256: ", sha256_hash)

    md5_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("md5: ", md5_hash)

    sha1_hash = int(hashlib.sha1(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha1: ", sha1_hash)

    sha224_hash = int(hashlib.sha224(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha224: ", sha224_hash)

    sha384_hash = int(hashlib.sha384(string.encode(
        "utf-8")).hexdigest(), 16) % (1000000000)
    # print("sha384: ", sha384_hash)

    if bloom5[sha256_hash] == 1 & bloom5[md5_hash] == 1 & bloom5[sha1_hash] == 1 & bloom5[sha224_hash] == 1 & bloom5[sha384_hash] == 1:
        result = "Maybe     "
    else:
        result = "No    "

    # checking each hash against what has been seen before
    if bloom5[sha256_hash] == 0:
        bloom5[sha256_hash] = 1

    if bloom5[md5_hash] == 0:
        bloom5[md5_hash] = 1

    if bloom5[sha1_hash] == 0:
        bloom5[sha1_hash] = 1

    if bloom5[sha224_hash] == 0:
        bloom5[sha224_hash] = 1

    if bloom5[sha384_hash] == 0:
        bloom5[sha384_hash] = 1

    file = open('output5.txt', 'a')

    file.write(result)
    file.write(string)


def read_file_contents(string):

    with open(string, 'r') as file:
        for file_contents in file:
            pop_bloom(file_contents)

    file.close()


def read_user_input(string):

    with open(string, 'r') as file:
        next(file)
        for file_contents in file:
            file_contents.strip()
            check_user_5(file_contents)
            check_user_3(file_contents)

    file.close()


# takes the arguments at run time and for the file.
read_file_contents(sys.argv[1])
read_user_input(sys.argv[2])
