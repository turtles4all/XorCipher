import binascii


def str2bin(message):
    binary = bin(int(binascii.hexlify(message), 16))
    return binary[2:]


def bin2str(binary):
    message = binascii.unhexlify('%x' % (int('0b' + binary, 2)))
    return message

message = 'hello'
binary = str2bin(message)
print binary
gggg = bin2str(binary)
print gggg