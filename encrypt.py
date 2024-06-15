# data_file_path: location of file need to be encrypted
# public_key: {"n": number, "e": number}
# encrypted_file_path: location where we write encrypted data
def encrypt(data_file_path, public_key, encrypted_file_path):
    data_file = open(data_file_path, 'rb')
    encrypted_file = open(encrypted_file_path, 'w')

    from os import stat
    encrypted_file.write(str(stat(data_file_path).st_size) + '\n')
    
    from custom_library import get_segment_size
    segment_size = get_segment_size(public_key['n'])

    from custom_library import modular_exponentiation
    while segment := data_file.read(segment_size):
        segment = int.from_bytes(segment)
        encrypted_segment = modular_exponentiation(segment, public_key['e'], public_key['n'])
        encrypted_file.write(str(encrypted_segment) + '\n')

    data_file.close()
    encrypted_file.close()


# demo
data_file_path = 'data.txt'
public_key_path = 'result/public_key.json'
encrypted_file_path = 'result/encrypted_data.txt'

import json
with open(public_key_path, 'r') as f:
    public_key = json.loads(f.read())


encrypt(data_file_path, public_key, encrypted_file_path)
print('done.')
