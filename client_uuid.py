from datetime import datetime
from struct import pack
from base64 import b64encode
from random import randint


def _get_creation_time():
    return int(datetime.now().timestamp() * 1000)

def _find_client_uuid(user_id: int):
    global bytearray
    
    creation_time = _get_creation_time()
    bytearray = bytearray(pack("<6i", *[
        user_id % 2**31, 
        user_id >> 32, 
        randint(0, 4294967295) % 2**31, 
        creation_time % 2**31, 
        creation_time >> 32, 0
    ]))

    return b64encode(bytearray).decode("ascii")


if (__name__ == '__main__'):
    user_id = 803241947954151459
    client_uuid = _find_client_uuid(
        user_id=user_id
    )
    
    print(client_uuid)
