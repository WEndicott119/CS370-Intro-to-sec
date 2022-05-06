from cryptography.hazmat.primitives import hashes
import string
import random


weak_trials = 0

while(1):

    digest_1 = hashes.Hash(hashes.SHA256())
    digest_2 = hashes.Hash(hashes.SHA256())

    string_1 = "Thisisatest"
    take_string = string_1[0:3]

    digest_1.update(bytes(take_string, 'utf-8'))

    check_1 = digest_1.finalize()
    finish_1 = check_1.hex()

    # will be a random set of bits
    data2_list = random.choices(string.ascii_letters, k=6)
    data2 = ''.join(data2_list)
    digest_2.update(bytes(data2, 'utf-8'))

    check_2 = digest_2.finalize()
    finish_2 = check_2.hex()

    weak_trials += 1

    if(finish_1[0:3] == finish_2[0:3]):
        print("weak: ", weak_trials)
        break


strong_trials = -1
flag = 0
birthdays = []
digest_4 = hashes.Hash(hashes.SHA256())
# will be a random set of bits
data4_list = random.choices(string.ascii_letters, k=6)
data4 = ''.join(data4_list)
digest_4.update(bytes(data4, 'utf-8'))
check_4 = digest_4.finalize()
finish_4 = check_4.hex()

birthdays.append(finish_4[0:3])

while(1):

    digest_3 = hashes.Hash(hashes.SHA256())

    # will be a random set of bits
    data3_list = random.choices(string.ascii_letters, k=6)
    data3 = ''.join(data3_list)
    digest_3.update(bytes(data3, 'utf-8'))

    check_3 = digest_3.finalize()
    finish_3 = check_3.hex()

    for x in range(0, len(birthdays)-1):
        if birthdays[x] == finish_3[0:3]:
            flag = 1
            break
        else:
            break

    birthdays.append(finish_3[0:3])

    strong_trials += 1

    if(flag == 1):
        print("strong: ", strong_trials)
        break
