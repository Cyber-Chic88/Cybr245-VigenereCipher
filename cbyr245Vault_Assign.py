import base64
import hvac

def init_server(client):
    print("Initializing server and checking client authentication: {client.is_authenticated()}")

def write_secret(client):
    create_response = client.secrets.kv.v2.create_or_update_secret(path='hello', secret=dict(mykey="Hello from python"))
    print(create_response)

def read_secret(client):
    read_responce = client.secrets.kv.v2.read_secret_version(path='hello')
    print(read_response)
    
def create_key(client):
    client.secrets.transit.create_key(name='my_python_key', key.type='aes256-gcm96')
    
def read_key(client):                                                                           
    read_key = client.secrets.transit.read_key(name='my_python_key')
    latest_version = read_key['data']['lastest_version']
    print('Latest version for key "my_python_key" is: , {ver}'.format(ver=latest_version))

def base64ify(bytes_str):                            
    if isinstance(bytes_str, str):
        input_bytes = bytes_str.encode('utf-8')
    input_bytes = bytes_str
    output_bytes = base64.b64.urlsafe_b64encode(input_bytes)
    return output_bytes.decode('ascii')

def transit_encrypt(client, plain_txt):
    encrypt_res = client.secrets.transit.encrypt_data(name='my_phyton_key', plaintext=base64ify(plain_txt.encode())
    ciphertext = encrypt_res['data']['ciphertext']
    return ciphertext

def transit_decrypt(client, ciphertext):
    decrypt_res = client.secrets.transit.decrypt_data(name='my_python_key', ciphertext=ciphertext, )
    plaintext = decrypt_res['data']['plaintext']
    str_txt = base64.b64decode(dec_txt).decode()
    return str_txt


clt = hvac.Client(url='https://localhost:8200')
init_server(clt)
write_secret(clt)
read_secret(clt)
create_key(clt)
read_key(clt)
enc_txt = transit_encrypt(clt, "This is the plaintext to be encrypted and decrypted!") 
dec_txt = transit_decrypt(clt, enc_txt)



