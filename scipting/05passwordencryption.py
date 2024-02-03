import base64

def enc(upass):
     encoded_bytes= base64.b64encode(upass.encode())
    #  print(upass.encode())
     return encoded_bytes

user_pass=  input ("enter your password : ")
encypted =enc(user_pass)
# print(encypted)
print(encypted.decode())
# rest pass -> cGFzcw==


def dec(encpass):
    decoded_bytes = base64.b64decode(encpass.encode())
    return decoded_bytes

user_enc_pass = input("enter the encrypted password : ")
decrpted = dec(user_enc_pass)
print(decrpted.decode())