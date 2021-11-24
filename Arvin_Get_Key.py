import os
import rsa
from cryptography.fernet import Fernet





def Get_Keys():
    
    # create the symmetric key
    
    key = Fernet.generate_key()

    # write the symmetric key to a file
    
    k = open('symmetric.key', 'wb')
    
    k.write(key)
    
    k.close()

    # create the pub & private keys
    
    (pubkey, privkey) = rsa.newkeys(2048)

    # write the public key to a file
    
    pukey = open('publickey.key', 'wb')
    
    pukey.write(pubkey.save_pkcs1('PEM'))
    
    pukey.close()

    # write the private key to a file
    
    prkey = open('privkey.key', 'wb')
    
    prkey.write(privkey.save_pkcs1('PEM'))
    
    prkey.close()


def Encrypt(nn):
    
    # open the symmetric key file
    
    skey = open('symmetric.key', 'rb')
    
    key = skey.read()

    # create the cipher
    
    cipher = Fernet(key)

    # open file for encrypting

    myfile = open(nn, 'rb')
    
    myfiledata = myfile.read()

    # encrypt the data
    
    encrypted_data = cipher.encrypt(myfiledata)
    
    edata = open('encrypted_file', 'wb')
    
    edata.write(encrypted_data)

 

    # open the public key file
    
    pkey = open('publickey.key', 'rb')
    
    pkdata = pkey.read()

    # load the file
    
    pubkey = rsa.PublicKey.load_pkcs1(pkdata)

    # encrypt the symmetric key file with the public key
    
    encrypted_key = rsa.encrypt(key, pubkey)

    ekey = open('encrypted_key', 'wb')
    
    ekey.write(encrypted_key)

  

def Decrypt(nn):
    
    # load the private key to decrypt the public key
    
    prkey = open('privkey.key', 'rb')
    
    pkey = prkey.read()
    
    private_key = rsa.PrivateKey.load_pkcs1(pkey)

    e = open('encrypted_key', 'rb')
    
    ekey = e.read()

    dpubkey = rsa.decrypt(ekey, private_key)

    cipher = Fernet(dpubkey)

    with open(nn, 'rb') as encrypted_data:
        
        edata = encrypted_data.read()

    decrypted_data = cipher.decrypt(edata)

    with open('decrypted_file', 'wb') as ee:
        
        ee.write(decrypted_data)


def main():
    
    Get_Keys()
    
    print('by right click on the desired file and then copy path you can access to file path')
    
    print('example D:\\download\pp.png')
    
    u = input('please enter path of the file: ')
    
    Encrypt(u)
  
    print('File Encrypted Successfully')
    
    b= input('please enter path of the encrypted file: ')
    
    Decrypt(b)
  
    print('File Decrypted Successfully')


if __name__ == "__main__":
    
    main()
