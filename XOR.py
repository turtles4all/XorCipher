import argparse


def main():
    argList = argparse.ArgumentParser(description='XOR a file.')
    argList.add_argument('--input', dest='inFile', action='store_const', help='Input file to XOR')
    arguments = argList.parse_args()
    print(arguments.inFile)

'''
    key = 170
    f = open(fileIn, 'rb')
    f.seek(0)
    out = open(fileout, 'w+b')
    byte = f.read(1)

    while byte:
        # out.write(byte)
        print(byte)
        byteXOR = (int.from_bytes(byte, 'little') ^ key)
        bytewrite = byteXOR.to_bytes(1, byteorder='little')
        out.write(bytewrite)
        byte = f.read(1)


    f.close()
    out.close()
'''
if __name__ == "__main__":
    main()
