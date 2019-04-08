import sys
import hashlib

print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("md5collision ver 0.1a")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
print("$$$$$$$$$$$$ START $$$$$$$$$$$$$$\n")

if len(sys.argv) < 2:
    print("Not enough args!")
    print("python2 md5collision.py string_to_find_collision")
    exit()

def hashGen(text):
    temp = hashlib.md5(text).hexdigest()
    bytes = []
    temp = ''.join(temp.split(" "))
    for i in range(0, len(temp), 2):
        bytes.append(chr(int(temp[i:i+2], 16)))
    first_hash = ''.join(bytes)
    return hashlib.md5(first_hash).hexdigest()[0:14]

def floydSolver(text):
    tortoise = hashGen(text)
    hare = hashGen(hashGen(text))
    counter = 0
    final = ""
    print("<STAGE 1>")
    while(tortoise != hare):
        tortoise = hashGen(tortoise)
        hare = hashGen(hashGen(hare))
        counter += 1
        if(counter % 10000000) == 0:
            print(counter)
    tortoise = text
    print("<STAGE 2>")
    counter = 0
    temp_tortoise = 0
    temp_hare = 0
    while(tortoise != hare):
        tortoise = hashGen(tortoise)
        here = hashGen(hare)
        counter += 1
        if(counter % 10000000) == 0:
            print(counter)
        if(tortoise != hare):
            temp_tortoise = tortoise
            temp_hare = hare
        if(hashGen(tortoise) == hashGen(hare)):
            print("FOUND HASHES")
            print("tortoise: ", temp_tortoise)
            print("hare: ", temp_hare)
            final = 'tortoise: ' + temp_tortoise + '\n' + 'hare: ' + temp_hare
            with open('hashes.log', 'w') as f:
                f.write(final)
            break
    print("CHECKING CALCULATIONS ...")
    print("tortoise ", temp_tortoise, " > ", hashGen(temp_tortoise))
    print("hare ", temp_hare, " > ", hashGen(temp_hare))

to_crash = sys.argv[1]
in_text_hash = hashlib.md5(to_crash.encode())
in_text_hash = hashlib.md5(in_text_hash.digest())

print("Full hash of input: ")
print(in_text_hash.hexdigest())
print("First 56 bytes of hash of input: ")
print(in_text_hash.hexdigest()[:7])

floydSolver(to_crash)
print("\n$$$$$$$$$$ FINISH $$$$$$$$$$$$$\n")
