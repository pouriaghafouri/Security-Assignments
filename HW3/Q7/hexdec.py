hex_str = (
    "00:c2:bc:d1:a9:fb:bf:60:3f:c5:f7:3c:ec:12:87:"
    "17:80:9f:49:04:2e:00:c9:75:21:f1:5f:26:a7:d2:"
    "d8:a3:1b:b4:b5:ab:64:2e:25:09:e5:5f:d1:d2:93:"
    "a9:df:39:6b:9d:3c:d2:9a:81:34:1b:f2:96:f3:e3:"
    "4e:b9:84:c0:8b:e3:0b:a9:cb:b1:40:14:38:74:c0:"
    "dd:94:bd:c2:f0:22:c4:74:75:86:07:0a:dd:ec:9f:"
    "18:be:58:07:b5:93:39:07:26:80:f4:26:48:f7:9e:"
    "d7:b8:fe:f8:77:25:13:d8:10:d7:10:7e:a3:c0:37:"
    "70:95:61:d5:4f:82:4f:a5:f3:0a:eb:b5:50:2a:a9:"
    "1e:d2:93:af:49:16:d2:f6:6d:de:7e:7d:5a:d6:50:"
    "ea:b8:f6:86:27:d4:bc:1f:de:87:9d:d7:3c:f2:e9:"
    "a5:ca:9f:4c:a0:b2:33:1d:3b:86:8f:91:26:dd:67:"
    "a9:c0:80:03:ac:52:da:7e:23:68:2f:e0:26:89:07:"
    "02:08:ce:0e:fb:82:09:db:5a:04:22:56:73:7b:b2:"
    "8d:c4:1c:af:5d:e1:8c:16:fb:67:39:b5:9d:b0:eb:"
    "47:3d:4c:e9:34:79:9d:1c:1d:04:f2:85:e0:ce:9e:"
    "b3:4d:8e:c8:c1:9b:e5:1d:2a:8f:e4:b6:86:d6:f2:"
    "62:0f"
)

clean_hex = hex_str.replace(":", "").replace("\n", "")

decimal_number = int(clean_hex, 16)

print(decimal_number)

