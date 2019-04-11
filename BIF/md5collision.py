import sys
import hashlib
import binascii

print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("md5collision ver 0.1c")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print("****************** START ******************\n")

if len(sys.argv) < 2:
    print("Not enough args!")
    print("python3 md5collision.py string_to_find_collision")
    exit()

prefix = sys.argv[1]
prefix_unhex = str(binascii.unhexlify(prefix.encode()), "ascii")

def hashGen(text):
    return  hashlib.md5(hashlib.md5((prefix_unhex + text).encode()).digest()).hexdigest()

def hashGenHare(text):
    partial = hashGen(text)
    return hashGen(partial)

def floydSolver():
    text =  prefix #str(binascii.hexlify(prefix.encode()), "ascii")
    print("Input: ", prefix, "\n")
    #print("Input <hex>: ", text)
    print("<<<<<<<<< STAGE 0 >>>>>>>>>")
    tortoise = hashGen(text)
    hare = hashGenHare(text)
    print(" 0000000", "\t", "tortoise: ", tortoise[0:14], " hare: ", hare[0:14])
    
    counter = 0
    final = ""
    print("<<<<<<<<< STAGE 1 >>>>>>>>>")
    while(tortoise[0:14] != hare[0:14]):
        tortoise = hashGen(tortoise)
        hare = hashGenHare(hare)
        counter += 1
        if(counter % 10000000) == 0:
            print("", counter, "\t", tortoise[0:14], " ",hare[0:14])
    
    print("<<<<<<<<< STAGE 2 >>>>>>>>>")
    tortoise = text
    counter = 0
    temp_tortoise = 0
    temp_hare = 0
    while(tortoise[0:14] != hare[0:14]):
        tortoise = hashGen(tortoise)
        hare = hashGen(hare)
        counter += 1
        if(counter % 10000000) == 0:
            print("", counter, "\t", tortoise[0:14], " ",hare[0:14])
        
        if(tortoise[0:14] != hare[0:14]):
            temp_tortoise = tortoise
            temp_hare = hare
            continue
        
        if( hashGen(tortoise)[0:14] ==  hashGen(hare)[0:14]):
            print("FOUND HASHES")
            print("tortoise: ", temp_tortoise)
            print("hare: ", temp_hare)
  
    print("CHECKING CALCULATIONS ...")
    print("COLLISION:")
    print("", prefix, " tortoise ", temp_tortoise, " > ",  hashlib.md5(hashlib.md5((prefix + temp_tortoise).encode()).digest()).hexdigest())
    print("", prefix, " hare ", temp_hare, " > ", hashlib.md5(hashlib.md5((prefix + temp_hare).encode()).digest()).hexdigest())


floydSolver()

print("\n****************** FINISH ******************\n")
