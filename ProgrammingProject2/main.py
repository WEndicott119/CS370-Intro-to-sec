from cryptography.hazmat.primitives import hashes

data = b'This is going to be hashed'
digest = hashes.Hash(hashes.SHA256())
digest.update(data)
print(digest.finalize())
# print(data)
