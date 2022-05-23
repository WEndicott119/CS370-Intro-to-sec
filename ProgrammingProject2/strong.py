from cryptography.hazmat.primitives import hashes
import random
import string

# length of strings
n = 6

flag = False
# used to proceed in hash comparison and counting
d1 = False
d2 = False
count = 0

# pick random string and add to list.
# if not in list, append
hash_list1 = []
hash_list2 = []

while flag == False:
    digest1 = hashes.Hash(hashes.SHA256())
    a1 = random.choices(string.ascii_letters, k=n)
    a = ''.join([str(elem) for elem in a1]).strip()

    digest2 = hashes.Hash(hashes.SHA256())
    b1 = random.choices(string.ascii_letters, k=n)
    b = ''.join([str(elem) for elem in b1]).strip()

    # check if a and b are already in the hash_list
    for item in hash_list1:
        if a == item:
            # generate a new string
            a1 = random.choices(string.ascii_letters, k=n)
            a = ''.join([str(elem) for elem in a1]).strip()

    for item in hash_list2:
        if b == item:
            # generate a new string
            b1 = random.choices(string.ascii_letters, k=n)
            b = ''.join([str(elem) for elem in b1]).strip()

    if d1 == False:
        hash_list1.append(a)
        digest1.update(bytes(a, 'utf-8'))
        d1 = True

    if d2 == False:
        hash_list2.append(b)
        digest2.update(bytes(b, 'utf-8'))
        d2 = True

    if d1 == True and d2 == True:
        fin1 = digest1.finalize()
        fin2 = digest2.finalize()

        defend = fin1.hex()
        attack = fin2.hex()

        if defend[0:n] == attack[0:n]:
            flag = True
        else:
            d1 = False
            d2 = False

        count += 1

print(a, defend[0:n])
print(b, attack[0:n])
print(count)
file = open("strong-results.txt", "a")
file.write(str(count))
file.write("\n")
file.close()
