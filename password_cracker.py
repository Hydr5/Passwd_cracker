import hashlib

def load_passwords(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def load_salts(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()

def crack_sha1_hash(hash, use_salts=False):
    passwords = load_passwords('top-10000-passwords.txt')
    if use_salts:
        salts = load_salts('known-salts.txt')
        for salt in salts:
            for password in passwords:
            
                salted_password1 = salt + password
                salted_password2 = password + salt
            
                if hash_password(salted_password1) == hash or hash_password(salted_password2) == hash:
                    return password
    else:
        for password in passwords:
       
            if hash_password(password) == hash:
                return password
    return "PASSWORD NOT IN DATABASE"
