from itertools import cycle
import sys
import argparse
import hashlib
import codecs


def main():
    argParse = argparse.ArgumentParser(description='XOR an input with a given key')
    requiredArgs = argParse.add_argument_group('Required arguments')
    requiredArgs.add_argument('-if', dest="fileIn", help="Input File", required=True)
    requiredArgs.add_argument('-of', dest="fileOut", help="Output File", required=True)
    requiredArgs.add_argument('-k', dest="keyString", help="Key", required=True)
    argParse.add_argument('-v', dest="verbose", help="Verbose Mode")
    args = argParse.parse_args()

    fileIn = args.fileIn
    fileOut = args.fileOut
    key = args.keyString

    key = str.encode(key)
    keyhash = hashlib.sha3_256()
    keyhash.update(key)
    key = keyhash.digest()
    print(key, type(key))
    print(bin(int.from_bytes(key, 'little')))

    # key = map(bin, bytearray(key))

    # print(key.hexdigest)

    print(fileIn, fileOut, args.keyString)

    f = open(fileIn, 'rb')
    f.seek(0)
    out = open(fileOut, 'w+b')
    writting = True
    while writting:
        byte = f.read(32)
        if byte:
            bytelen = len(byte)
            print(bytelen, type(bytelen))
            byteXOR = ((int.from_bytes(byte, 'little')) ^ (int.from_bytes(key[0:bytelen], 'little')))
            bytewrite = byteXOR.to_bytes(bytelen, byteorder='little')
            out.write(bytewrite)
            print(bytewrite)
        else:
            writting = False
    f.close()
    out.close()

def getHash():
    fileHash = hashlib.md5(open(fileOut, 'rb').read()).hexdigest()
    print("Write Complete! with MD5 hash - {}".format(fileHash))

if __name__ == "__main__":
    main()
