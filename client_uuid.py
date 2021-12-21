from random import random
from datetime import datetime
from struct import pack
from base64 import b64encode
from time import mktime

user_id = int("YOUR D1SC0RD ID")
number = int(4294967296 * random())
creation_time = int(mktime(datetime.now().timetuple()) * 1000)

bytes1 = bytes(pack("<i", user_id % 4294967296 if user_id % 4294967296 <= 2147483647 else user_id % 4294967296 - 2147483647))
bytes2 = bytes(pack("<i", user_id >> 32))
bytes3 = bytes(pack("<i", number if number <= 2147483647 else number - 4294967296))
bytes4 = bytes(pack("<i", creation_time % 4294967296 if creation_time % 4294967296 <= 2147483647 else creation_time % 4294967296 - 2147483647))
bytes5 = bytes(pack("<i", creation_time >> 32))
bytes6 = bytes(pack("<i", 0))

bytearray = bytearray(pack('24x'))
bytearray[0: len(bytes1)] = bytes1
bytearray[4:4 + len(bytes2)] = bytes2
bytearray[8:8 + len(bytes3)] = bytes3
bytearray[12:12 + len(bytes4)] = bytes4
bytearray[16:16 + len(bytes5)] = bytes5
bytearray[20:20 + len(bytes6)] = bytes6

print(b64encode(bytearray).decode('ascii'))
