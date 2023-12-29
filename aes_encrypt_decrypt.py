from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


# key = get_random_bytes(32) 
# iv = get_random_bytes(16)

def aes_encrypt(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plaintext.encode(), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    print()
    return base64.b64encode(encrypted_text).decode()

def aes_decrypt(key, iv, encrypted_text):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(base64.b64decode(encrypted_text))
    return unpad(decrypted_padded_text, AES.block_size).decode()

f = open('aes.key', 'r')
key = f.readlines()
print(key)

aes_key = base64.b64decode(key[0])
iv_key = base64.b64decode(key[1])

plaintext = """안녕!"""

encrypted_text = aes_encrypt(aes_key, iv_key, plaintext)
decrypted_text = aes_decrypt(aes_key, iv_key, encrypted_text)

print(encrypted_text)
print(decrypted_text)


# aes_key = base64.b64encode(key).decode()
# iv_encoded = base64.b64encode(iv).decode()


# print(key == base64.b64decode(aes_key))
# print(iv == base64.b64decode(iv_encoded))

# f = open('aes.key', 'w')
# f.writelines('\n'.join([aes_key, iv_encoded]))
# f.close()

# f = open('aes.key', 'r')
# key = f.readlines()
# print(key)

# aes_key = base64.b64decode(key[0])
# iv_key = base64.b64decode(key[1])

# decrypted_text = aes_decrypt(aes_key, iv_key, encrypted_text)

# print(decrypted_text.strip())