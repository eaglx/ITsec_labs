import sys
import hashlib
import binascii

print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("\tmd5collision ver 0.1e")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
print("****************** START ******************\n")

if len(sys.argv) < 2:
    print("Not enough args!")
    print("python3 md5collision.py string_to_find_collision")
    exit()

prefix = sys.argv[1]
prefix_unhex = str(binascii.unhexlify(prefix.encode()), "cp1252") # replace "utf-8", issue with 0x93
length_to_analysis = 14

def hashGen(text):
    return  hashlib.md5(hashlib.md5((prefix_unhex + text).encode()).digest()).hexdigest()

def hashGenHare(text):
    partial = hashGen(text)[0:length_to_analysis]
    return hashGen(partial)

def floydSolver():
    text =  prefix #str(binascii.hexlify(prefix.encode()), "ascii")
    print("Input hex: ", prefix, "\n")#"Input: ", prefix_unhex, " Input bin", prefix_unhex.encode(), "\n")
    print("<<<<<<<<< STAGE 0 >>>>>>>>>")
    tortoise = hashGen(text)[0:length_to_analysis]
    hare = hashGenHare(text)[0:length_to_analysis]
    print(" 00000000", "\t", "tortoise: ", tortoise[0:length_to_analysis], " hare: ", hare[0:length_to_analysis])
    
    counter = 0
    print("<<<<<<<<< STAGE 1 >>>>>>>>>")
    while(tortoise[0:length_to_analysis] != hare[0:length_to_analysis]):
        tortoise = hashGen(tortoise)[0:length_to_analysis]
        hare = hashGenHare(hare)[0:length_to_analysis]
        counter += 1
        if(counter % 1000000) == 0:
            print("", counter, "\t", tortoise[0:length_to_analysis], " ",hare[0:length_to_analysis])
    
    print("<<<<<<<<< STAGE 2 >>>>>>>>>")
    tortoise = text
    counter = 0
    temp_tortoise = 0
    temp_hare = 0
    while(tortoise[0:length_to_analysis] != hare[0:length_to_analysis]):
        tortoise = hashGen(tortoise)[0:length_to_analysis]
        hare = hashGen(hare)[0:length_to_analysis]
        counter += 1
        if(counter % 1000000) == 0:
            print("", counter, "\t", tortoise[0:length_to_analysis], " ",hare[0:length_to_analysis])
        
        if(tortoise[0:length_to_analysis] != hare[0:length_to_analysis]):
            temp_tortoise = tortoise
            temp_hare = hare
            continue
        
        if( hashGen(tortoise)[0:length_to_analysis] ==  hashGen(hare)[0:length_to_analysis]):
            print("FOUND HASHES")
            print("tortoise:\t", temp_tortoise)
            print("hare:\t\t", temp_hare)
            break
  
    print("COLLISION:")
    print("1: prefix<hex>: ", prefix, " tort: ", temp_tortoise, " > ",  hashlib.md5(hashlib.md5((prefix_unhex + temp_tortoise).encode()).digest()).hexdigest())
    print("2: prefix<hex>: ", prefix, " hare: ", temp_hare, " > ", hashlib.md5(hashlib.md5((prefix_unhex + temp_hare).encode()).digest()).hexdigest())


floydSolver()

print("\n****************** FINISH ******************\n")
