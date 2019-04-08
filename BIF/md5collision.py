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

result = hashlib.md5(to_crash.encode())
result = hashlib.md5(result.digest())

print("Hash of input: ", end='')
print(result.hexdigest())


print("\n$$$$$$$$$$ FINISH $$$$$$$$$$$$$\n")
