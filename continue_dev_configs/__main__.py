from continue_dev_configs.StringMaker import StringMaker

def main():
    while True:
        nextResponse = input("Give the next response: ")
        stringMaker = StringMaker()
        stringMaker.execute()
        break

if __name__ == '__main__':
    main()
