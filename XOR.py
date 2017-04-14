import sys
import os
import argparse
import hashlib
import base64

def main(args):
    try:
        logo = base64.b64decode(
            "Cl9fICBfX19fXyAgX19fXyAgClwgXC8gLyBfIFx8ICBfIFwgCiBcICAvIHwgfCB8IHxfKSB8CiAvICBcIHxffCB8ICBfIDwgCi9fL1xfXF9fXy98X3wgXF9cCiAgICAgICAgICAgICAgICAgCg==")
        print(logo.decode('ascii'))
    except:
        print("logo")
    fileIn = args.fileIn
    fileOut = args.fileOut
    key = hash_key(args.keyString)

    print("Input File: {}\n"
          "Output File: {}\n"
          "Key : {}".format(fileIn, fileOut, args.keyString))
    while True:
        confirm = input("Is this correct? (YES/NO):")
        if confirm.upper() == "NO":
            exit()
        elif confirm.upper() == "YES":
            break
        else:
            print("input must be \"YES\" or \"NO\"")
    try:
        f = open(fileIn, 'rb')
        try:
            out = open(fileOut, 'x')
        except IOError:
            overw = input("Overwrite file \"{}\"? (Y/N)".format(fileOut))
            if overw.upper() == 'Y':
                out = open(fileOut, 'w+b')
            else:
                exit()
    except IOError as error:
        print(error)
        exit()

    try:
        writting = True
        fileSize = len(f.read())
        f.seek(0)
        blockSize=32
        bytesRead = 0
        while writting:
            print("{comp}% complete".format(comp=("%0.2f" % (bytesRead / fileSize * 100))), end='\r')
            block = f.read(blockSize)
            if block:
                blockLen = len(block)
                byteXOR = ((int.from_bytes(block, 'little')) ^ (int.from_bytes(key[0:blockLen], 'little')))
                blockWrite = byteXOR.to_bytes(blockLen, byteorder='little')
                out.write(blockWrite)
                bytesRead += blockLen
            else:
                writting = False

    except KeyboardInterrupt:
        f.close()
        out.close()
        os.remove(fileOut)
        exit()

    print("\nXOR finished writing to file \"{}\"".format(fileOut))
    exit()


def parse_args():
    argParse = argparse.ArgumentParser(description='XOR an input with a given key')
    requiredArgs = argParse.add_argument_group('Required arguments')
    requiredArgs.add_argument('-i', dest="fileIn", help="Input File", required=True)
    requiredArgs.add_argument('-o', dest="fileOut", help="Output File", required=True)
    requiredArgs.add_argument('-k', dest="keyString", help="Key", required=True)
    return argParse.parse_args()

def hash_key(key):
    key = str.encode(key)
    keyhash = hashlib.sha3_256()
    keyhash.update(key)
    key = keyhash.digest()
    return key

if __name__ == "__main__":
    main(parse_args())
