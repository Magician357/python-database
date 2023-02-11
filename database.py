from customfernet import Fernet
import string
chars=[*string.printable]
import os
base=os.getcwd() 

print(Fernet.generate_key())

key="iX6cFE1YAoZmlBMT0CmxAPShrfA7TxBzZGb4P4dacjc=" #Keep very safe or else

def encrypt_fer(message: str, tkey: bytes) -> bytes:
    return Fernet(tkey).encrypt(message.encode()).decode()

def decrypt_fer(token: str, tkey: bytes) -> str:
    return Fernet(tkey).decrypt(token.encode()).decode()

def encode(text: str):
    text=encrypt_fer(text,key)
    current=[chars.index(letter) for letter in text]
    return bytes(current)

def decode(text: bytes):
    text="".join(chars[i] for i in text)
    return decrypt_fer(text,key)

def compile_file(filenam: str):
    with open("python-database\\data\\"+filenam,"r") as f:
        full=f.read()
    list=full.split("||")
    return tuple(tuple(thing.split("::")) for thing in list)

def write_to_file(filenam:str,keyss:str,value:str):
    try:
        f=open("python-database\\data\\"+filenam,"ab")
        f.write(encode(keyss)+b"::"+encode(value)+b"||")
        f.close()
        return 1
    except:
        return 0

def get_from_file(filenam:str,keyss:str):
    for item in compile_file(filenam):
        print(decode(item[0].encode()),keyss)
        if item[0] == encode(keyss):
            return decode(item[1])

if __name__=="__main__":
    keys="hello"
    values="world"
    write_to_file("test",keys,values)
    print(get_from_file("test",keys))