import netrc

def oqish():
    try:
        netrc_file = netrc.netrc()
        login, parol, host = netrc_file.authenticators('example.com')
        return login, parol
    except netrc.NetrcParseError:
        return None, None

def yozish(login, parol):
    netrc_file = netrc.netrc()
    netrc_file.authenticators('example.com', login, parol)
    netrc_file.write()

def main():
    login, parol = oqish()
    if login and parol:
        print(f"Login: {login}, Parol: {parol}")
    else:
        login = input("Istalgan login kiriting: ")
        parol = input("Istalgan parol kiriting: ")
        yozish(login, parol)
        print("Parol saqlandi")

if __name__ == "__main__":
    main()
