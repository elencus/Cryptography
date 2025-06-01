from hashlib import md5
import json
import os


USER_DB = 'users.txt'

def load_users():
    users = {}
    if os.path.exists(USER_DB):
        with open(USER_DB, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    username, usr_hash, password = line.split(',')
                    users[username] = [usr_hash, password]
    return users


def save_user(username, usr_hash, password):
    with open(USER_DB, 'a') as f:
        f.write(f"{username},{usr_hash},{password}\n")


def get_option():
    return input('''
    Welcome to my login application scaredy cat ! I am using MD5 to save the passwords in the database.
                          I am more than certain that this is secure.                       
                                   You can't prove me wrong!          

    [1] Login
    [2] Register
    [3] Exit

    Option (json format) :: ''')


def main():
    while True:
        try:
            option = json.loads(get_option())

            if 'option' not in option:
                print('[-] please, enter a valid option!')
                continue

            users = load_users()
            option = option['option']

            if option == 'login':
                creds = json.loads(input('enter credentials (json format) :: '))
                usr, pwd = creds['username'], creds['password']
                usr_hash = md5(usr.encode()).hexdigest()

                for db_user, v in users.items():
                    if [usr_hash, pwd] == v:
                        if usr == db_user:
                            print(f'[+] welcome, {usr} 🤖!')
                        else:
                            print(f"[+] what?! this was unexpected. shutting down the system :: {open('flag.txt').read()} 👽")
                            exit()
                        break
                else:
                    print('[-] invalid username and/or password!')

            elif option == 'register':
                creds = json.loads(input('enter credentials (json format) :: '))
                usr, pwd = creds['username'], creds['password']
                if usr.isalnum() and pwd.isalnum():
                    if usr in users:
                        print('[-] this user already exists!')
                        continue
                    usr_hash = md5(usr.encode()).hexdigest()
                    save_user(usr, usr_hash, pwd)
                    print('[+] registered successfully!')
                else:
                    print('[-] your credentials must contain only ascii letters and digits.')

            elif option == 'exit':
                print('byeee.')
                break
        except Exception as e:
            print(f'[-] error: {str(e)}')


if __name__ == '__main__':
    main()
