import sys
import hashlib

print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("md5collision ver 0.1a")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
print("$$$$$$$$$$$$ START $$$$$$$$$$$$$$\n")

if len(sys.argv) < 2:
    print("Not enough args!")
    print("python3 md5collision.py string_to_find_collision")
    exit()

to_crash = sys.argv[1]

in_text_hash = hashlib.md5(to_crash.encode())
in_text_hash = hashlib.md5(in_text_hash.digest())

print("Full hash of input: ", end='')
print(in_text_hash.hexdigest())
print("First 56 bytes of hash of input: ", end='')
print(in_text_hash.hexdigest()[:7])


print("\n$$$$$$$$$$ FINISH $$$$$$$$$$$$$\n")
