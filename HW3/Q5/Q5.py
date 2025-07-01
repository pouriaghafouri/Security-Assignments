import owiener
from Crypto.Util.number import long_to_bytes

e = 0
n = 0
cipher_text = 0
with open("Q5.txt", "r") as file:
    for line in file:
        if "=" in line:
            name, value = line.strip().split(" = ")
            if name == "e":
                e = int(value.strip(), 16)
            elif name == "n":
                n = int(value.strip(), 16)
            elif name == "cipher_text":
                cipher_text = int(value.strip(), 16)

d = owiener.attack(e, n)

print(f"d = {d}")
print(f"flag = {long_to_bytes(pow(cipher_text, d, n)).decode('utf-8')}")
