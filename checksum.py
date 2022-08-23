import sys
import hashlib

def checksum(file1, file2):
    file_1_hash = hashfile(file1)
    file_2_hash = hashfile(file2)

    return hash_check(file_1_hash, file_2_hash)


def hashfile(file):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break

            sha256.update(data)
        return sha256.hexdigest()


def hash_check(hash_1, hash_2):
    if hash_1 == hash_2:
        return True
    else:
        return False
