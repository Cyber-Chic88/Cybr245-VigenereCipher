import os
#allow secret transit
os.system(vault secrets enable transit)

#Create key
os.system(vault write transit/keys/mytestkey type=aes256-gcm96)

#Encrypt data
os.system(vault write transit/encrypt/k1 plaintext=$(base64 <<< "my very secret data"))

#Decrypt data
os.system(vault write transit/decrypt/k1 ciphertext=$(base24 <<< vault:v1:4bTFZAk3yi5U3hdaoTgDBPslIfWFZDO86a56NjbNLUrS4KTfdhE7nyqvSJL3DRiw) #Paige make sure this is the right ciphertext from the lab

