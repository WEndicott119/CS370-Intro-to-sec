import hashlib

# create an array to hold results
bloom3 = [0] * 1000000
# print(bloom3)

bloom5 = [0] * 1000000
# print(bloom5)


def check_hash(string):

    sha256_hash = int(hashlib.sha256(
        string.encode("utf-8")).hexdigest(), 16) % (10 ** 6)
    print("sha256: ", sha256_hash)

    md5_hash = int(hashlib.md5(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 6)
    print("md5: ", md5_hash)

    sha1_hash = int(hashlib.sha1(string.encode(
        "utf-8")).hexdigest(), 16) % (10 ** 6)
    print("sha1: ", sha1_hash)

    if bloom3[sha256_hash] == 1 & bloom3[md5_hash] == 1 & bloom3[sha1_hash] == 1:
        print("That password maybe no good.")

    if bloom3[sha256_hash] == 0:
        bloom3[sha256_hash] = 1

    if bloom3[md5_hash] == 0:
        bloom3[md5_hash] = 1

    if bloom3[sha1_hash] == 0:
        bloom3[sha1_hash] = 1


with open("dictionary2.txt", 'r') as file:
    for file_contents in file:
        check_hash(file_contents)


print(bloom3)

file.close()
