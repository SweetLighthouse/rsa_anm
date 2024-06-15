# encrypted_file_path: location where we wrote encrypted data
# private_key: {"n": number, "d": number}
# decrypted_file_path: location where we write decrypted data
def decrypt(encrypted_file_path, private_key, decrypted_file_path):
    encrypted_file = open(encrypted_file_path, 'r')
    decrypted_file = open(decrypted_file_path, 'wb')
    
    original_data_file_size = int(encrypted_file.readline())
    remain_data_to_read = original_data_file_size

    from custom_library import get_segment_size
    segment_size = get_segment_size(private_key['n'])

    from custom_library import modular_exponentiation
    while segment := encrypted_file.readline():
        # percent = (original_data_file_size - remain_data_to_read) / original_data_file_size * 100
        # print(f'{percent:.2f}')
        segment = int(segment)
        segment = modular_exponentiation(segment, private_key['d'], private_key['n'])
        remain_data_to_read -= segment_size
        if remain_data_to_read <= 0: # last segment
            remain_data_to_read += segment_size
            segment = segment.to_bytes(remain_data_to_read)
            decrypted_file.write(segment)
            break # out of while loop
        else:
            segment = segment.to_bytes(segment_size)
            decrypted_file.write(segment)

    encrypted_file.close()
    decrypted_file.close()

    
# demo
encrypted_file_path = 'result/encrypted_data.txt'
private_key_path = 'result/private_key.json'
decrypted_file_path = 'result/decrypted_data.txt'

import json
with open(private_key_path, 'r') as f:
    private_key = json.loads(f.read())

decrypt(encrypted_file_path, private_key, decrypted_file_path)
print('done.')
