class RSA_Key_Generator:
    import math
    import sympy
    import custom_library
    
    def __init__(self, key_size = 1024):
        # lower and upper limit should be a varaible
        self.p = self.sympy.randprime(2**int((key_size/2 - 1)), 2**int((key_size/2)))
        self.q = self.sympy.randprime(2**int((key_size/2 - 1)), 2**int((key_size/2)))
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)
        
        self.e = 65537
        while self.math.gcd(self.e, self.phi_n) != 1:
            self.e += 2

        self.d = self.custom_library.extended_euclidean(self.e, self.phi_n)[0]
        if self.d < 0:
            self.d += self.phi_n

        self.public_key = {
            "n": self.n,
            "e": self.e
        }

        self.private_key = {
            "n": self.n,
            "d": self.d
        }

# demo

key_size = input("key_size [1024, 2048, 4096] (default: 1024): ")
while key_size not in ['1024', '2048', '4096', '']:
    key_size = input("key_size [1024, 2048, 4096] (default: 1024): ")
key_size = int(key_size) if key_size != '' else 1024


key_instance = RSA_Key_Generator(key_size)
print('generated.')

public_key_path = 'result/public_key.json'
private_key_path = 'result/public_key.json'

import json
with open(public_key_path, 'w') as f:
    f.write(json.dumps(key_instance.public_key))
    print('wrote public key in: ' + public_key_path)

with open(private_key_path, 'w') as f:
    f.write(json.dumps(key_instance.private_key))
    print('wrote private key in: ' + private_key_path)

input('done. you can now close this window.')


# print('p = ', asdf.p)
# print('q = ', asdf.q)
# print('n = ', asdf.n)
# print('e = ', asdf.e)
# print('d = ', asdf.d)
# print('public.n = ', asdf.public_key['n'])
# print('public.e = ', asdf.public_key['e'])
# print('private.n = ', asdf.private_key['n'])
# print('private.d = ', asdf.private_key['d'])
