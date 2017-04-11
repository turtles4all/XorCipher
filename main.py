import hashlib

block_sz = 64  # in bytes
blocks = []
pt = ''
ct = []
key = '1e2r3t4y5u6i7o8p' * 2 # 256 bit key
print "Key ;", key
key = int(key.encode("hex"), 16) # convet ascii key to int
print "Key in hex"
print key
# print binascii.hexlify(key)
# hashed_key = hashlib.sha256(key)
print "bin of key in sha256"
# print bin(int(hashed_key.hexdigest(), 16))
pt = 'this is some test data ' * 2
pt = pt.encode("hex")
print "Hex of PT :", pt
sb = 0
bs = 0
full_blocks = len(pt) / block_sz
leftover_bytes = len(pt) % block_sz
print full_blocks, " Blocks, ", leftover_bytes, " Leftover Bytes"

for block in range(0, full_blocks):
    sb = block * block_sz
    bs = sb + block_sz
    blocks.append(int(pt[sb:bs], 16))
if leftover_bytes != 0:
    padding = 'f' * (block_sz - leftover_bytes)
    blocks.append(int(pt[bs + 1:] + padding, 16))
# dump the pt data
pt = ''
print "PT - ", blocks

# XOR the blocks
for block in range(0, len(blocks)):
    ct.append(blocks[block] ^ key)


print "CT - ", ct
blocks = []

for block in range(0, len(ct)):
    blocks.append(ct[block] ^ key)
print "PT - ", blocks
block = bin(blocks[0])
print block
block = block[1:]
print len(block) % 8
print type(block)
print binascii.hexlify(block)