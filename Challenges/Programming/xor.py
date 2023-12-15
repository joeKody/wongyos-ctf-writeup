import codecs

def xor(flag, key):
    flag = flag.encode()
    key = key.encode()
    msg = flag + b'&&' + key
    s = b''
    for i in range(len(msg)):
        s += bytes([msg[i] ^ key[i%len(key)]])
    return codecs.encode(s, "hex").decode()

# Flag format is flag{md5}
# 0b153e091a09536e0c4b6b4f09175b1f6c0a025b536d5f43681a5f10591d685c575a013e5b0e795e020b32173e0304320c2c360b300a



