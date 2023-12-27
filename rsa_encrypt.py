from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import json

begin = "-----BEGIN PUBLIC KEY-----\n"
end = "\n-----END PUBLIC KEY-----"

public_key_str = """
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA1qZUNIqZieNc6NYJ00r5
LWeXXx+HagdIuzVihRskjI6BjVCAwOjwphDlg9VSYH98Df2gQc5rbXSe4c64mB6U
Qjvtsf44a9/ySBEpRcCBNT/TSZoBkzznB130YhgwUE6TSVkXFY3Jk6uSxyQufuai
LE0//ij90CTajNWcGjIQyOTbZEWNEMejcebAfEzfqClQfJ04ycvD+RW0cxA5y7FF
Nbhk16Vh7DZ8hp/BXlDK0quotUz0qIfesquoE55dmwue43opfBb50RYEgisHnBiy
mzdWM0cNTD/Mm1R4LA1QO+mzzpgUGT9GEhLtHrJVEx3IaGzFeuVnEjh64vZgZ1NT
eilwQCSSRduiGvhA01ly3WEiLWkHUfSNOIqQR+OY1qtGUWy/CQa/WWrfroIVZKI2
5ge5tvSlcVrcNVS8a2VmPT9bhQNG9xTpcB+/TvWJzCPSsnF9dKY/QyVuwO9waIce
iEFmRvksll3vr0a70nubbxHrJIsHBENWFeRPEOzFIVxCQLbhKw18TkJ3G9brC8mu
2VB01iLmtrDmHVQnVo1DjP9mfCdY5wakLqf6iHnundNMLREAijiBDxK+3Ttkl8/D
bJyeuowxUyOpsgzamkfbd4ZlU49OJRvgFRERtez29cr3jd+zGKcEwIDXj+s5Rm2w
J6C6Iepju5NBDGYxcnSLK9UCAwEAAQ=="""


json_test = {
    "public_key" : public_key_str
}

json_str = json.dumps(json_test)
print(json_str)

json_data = json.loads(json_str)

public_key_str = json_data['public_key']

public_key_str = public_key_str.strip()

public_key_str = begin + public_key_str + end
# print(public_key_str)

public_key = RSA.importKey(public_key_str)

message = "이 글자가 보인다면 당신은 복호화에 성공한것"

cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message.encode())


encoded_encrypted_message = base64.b64encode(encrypted_message)

encoded_encrypted_message.decode()

print(encoded_encrypted_message.decode())

print(({"public_key": public_key_str}))