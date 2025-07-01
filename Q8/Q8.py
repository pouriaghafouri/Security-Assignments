from Crypto.Cipher import AES
from functools import reduce
from operator import xor

BLOCK_SIZE = 128 // 8
def enc_mac(k, m):
    # PKCS pad
    r = BLOCK_SIZE - len(m) % BLOCK_SIZE
    pad_size = r if r != 0 else BLOCK_SIZE
    m += pad_size.to_bytes(1, 'big') * pad_size
    # encrypt
    c = AES.new(mode=AES.MODE_OFB, key=k, iv=k).encrypt(m)
    # MAC
    t = AES.new(mode=AES.MODE_CBC, key=k, iv=c[:BLOCK_SIZE]).encrypt(m)[-BLOCK_SIZE:]
    return (c, t)

def dec_mac(k, c, t):
    # decrypt
    m = AES.new(mode=AES.MODE_OFB, key=k, iv=k).decrypt(c)
    # MAC
    t_dec = AES.new(mode=AES.MODE_CBC, key=k, iv=c[:BLOCK_SIZE]).encrypt(m)[-BLOCK_SIZE:]
    
    pad_size = m[-1]
    pad_size = int(pad_size) if int(pad_size) != 0 else BLOCK_SIZE
    m = m[0:len(m) - pad_size]
    return m.decode('utf-8`'), t == t_dec

def exploit(c, t):
    valid_data = "delete all keys".encode('utf-8')
    

    invalid_data = "everything is o".encode('utf-8')
    r = BLOCK_SIZE - len(invalid_data) % BLOCK_SIZE
    pad_size = r if r != 0 else BLOCK_SIZE
    invalid_data += pad_size.to_bytes(1, 'big') * pad_size

    one = 1
    tmp = bytes(a ^ b for a, b in zip(valid_data + one.to_bytes(1, 'big'), c))
    new_cipher = bytes(a ^ b for a, b in zip(tmp, invalid_data))

    return new_cipher.hex()

def verification(k):
    valid_data = "delete all keys".encode('utf-8')

    invalid_data = "everything is o".encode('utf-8')
    r = BLOCK_SIZE - len(invalid_data) % BLOCK_SIZE
    pad_size = r if r != 0 else BLOCK_SIZE
    invalid_data += pad_size.to_bytes(1, 'big') * pad_size

    c_valid, t_valid = enc_mac(k, valid_data)
    one = 1
    tmp = bytes(a ^ b for a, b in zip(valid_data + one.to_bytes(1, 'big'), c_valid))
    new_cipher = bytes(a ^ b for a, b in zip(tmp, invalid_data))
    
    return dec_mac(k, new_cipher, t_valid)

k = '875faffbaeea63eb878613b98460f4d2'
while True:
    print()
    print()
    user_in = int(input("Choose part: "))
    if user_in == 1:
        for c, t in (['d8b8239628a3f44c81e50cbd57aaac62586cdf1376c25fa8c23e8becf6be4688', 'abb859c60dd1450bd789a40bc3638f4e'], ['f8a0238928a3fc4b9efa1aef03aaa62e4f668c0633dc21cdba4dafe3f9b14987', 'b893a8d5032f5c004f11543626fc942e']):
            print(f'For (c, t) = {c, t}')
            print('result:')
            print(dec_mac(bytes.fromhex(k), bytes.fromhex(c), bytes.fromhex(t)))
            print()
    elif user_in == 2:
        print(f"New exploited cipher text = {exploit(bytes.fromhex('fb7c5373f3713de7f41cee2ee49e09ef'), bytes.fromhex('33228cc0d41f4c94bfb7b2c47b5f69cd'))}")
        print(f"Verification = {verification(bytes.fromhex(k))}")
    else:
        exit()