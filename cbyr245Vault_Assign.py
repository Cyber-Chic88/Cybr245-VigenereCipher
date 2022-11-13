import os
import base64

def env_var():
    os.environ["VAULT_ADDR"] = "https://127.0.0.1:8200"
    os.environ["VAULT_TOKEN"] = ##"PASTE YOUR TOKEN HERE"

def intit_trans():
    os.system("vault secrets enable transit")

def key():
    k = "set_key"
    os.system("vault write transit/keys/{} type=aes256-gcm96".format(k))

def enc_msg(plain_txt, key):
    vault_dec = base64.b64encode(bytes(plain_txt, 'utf-8'))
    os.system('vault write transit/encrypt/{} plaintext={}'.format(key, vault_dec.decode('utf-8')))
    return

def dec_msg(cipher, key):
    os.system('vault write transit/decrypt/{} ciphertext={}'.format(key, cipher))
    return



env_var()
intit_trans()
key()
enc_msg("This is the plaintext being encrypted and decrypted!", "set_key")
dec_msg(##'PASTE YOUR ENC TXT HERE' , "set_key")
vault_plain = base64.b64decode(##'PASTE YOUR VAULT DEC TXT HERE')
print(vault_plain.decode())
