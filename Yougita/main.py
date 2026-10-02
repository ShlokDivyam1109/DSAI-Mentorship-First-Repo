def check(password):
    pass

def read_secret():
    f = open("password.txt", "r")  
    password = f.read().strip()  
    f.close()                    
    check(password)

def main():
    read_secret()

if __name__ == '__main__':
    main()