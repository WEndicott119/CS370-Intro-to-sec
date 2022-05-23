import pyqrcode
import hmac
import base64
import struct
import hashlib
import time
import string
import random
import sys
from datetime import datetime


##############################################
# This recevies the secret key and interval  #
# which is used to replace the counter for   #
# hotp.                                      #
##############################################

def hotp(secret, interval):
    # The base64.b32decode() method decodes a bytes-like object using Base32 alphabets into a plain byte-string.
    key = base64.b32decode(secret, True)
    # Return a string containing the values v1, v2, … , that are packed according to the given format
    msg = struct.pack(">Q", interval)
    # generating a new hash
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000

    return h


##############################################
# This recevies the secret key and sends it  #
# to the hotp function where the counter for #
# hotp is replaced with the time interval in #
# our case we are using 30 second intervals. #
##############################################

def totp(secret):
    # setting the otp for 30 seconds intervals
    otp = str(hotp(secret, interval=int(time.time())//30))
    # this makes sure our otp has 6 digits
    while len(otp) != 6:
        otp += '0'
    return otp

##############################################
# The first part creates the key that will be#
# used for the otp and then writes it to .txt#
##############################################


def create_qr():
    # used to generate a random key
    letter = string.ascii_letters
    secret = ''.join(random.choice(letter) for i in range(16))
    qrpath = "otpauth://totp/Example:endicott@google.com?secret=" + \
        secret + "&issuer=Example"

    # This creates a QR code and saves it to QR.svg
    url = pyqrcode.create(qrpath)
    url.svg('QR.svg', scale=8)
    print(url.terminal(quiet_zone=1))

    file = open('secret.txt', 'a')
    file.write(secret)
    file.close()


##############################################
# The first part creates the key that will be#
# used for the otp.                          #
# this takes the first argument and creates a#
# secret file.                               #
##############################################


if(sys.argv[1] == "--generate-qr"):
    now = datetime.now()
    if(int(now.second) <= 30):
        wait_time = abs(30 - int(now.second))
        print("syncing please wait")
    else:
        wait_time = abs(60 - int(now.second))
        print("syncing please wait")
    time.sleep(wait_time)
    create_qr()


##############################################
# this takes the first argument and opens the#
# avalible secret file and runs it in a loop #
# until the user kills it. Printing each otp #
##############################################
if(sys.argv[1] == "--get-otp"):

    now = datetime.now()
    if(int(now.second) <= 30):
        wait_time = abs(30 - int(now.second))
        print("syncing please wait")
    else:
        wait_time = abs(60 - int(now.second))
        print("syncing please wait")
    time.sleep(wait_time)

    with open("secret.txt") as f:
        secret = next(f)

    while(True):
        print("This OTP is valid for the next 30 seconds")
        print(totp(secret))
        time.sleep(30)
