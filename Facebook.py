class Facebook:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email

    def printAll(self):
        print('first_name: ' + self.first_name)
        print('last_name: ' + self.last_name)
        print('mobile: ' + self.mobile)
        print('email: ' +  self.email)
        print('\n')

'''데이터가 잘 입력되는지 확인
def test():
    lee = Facebook('Yuna', 'Lee', '010-1234-5678', 'abc@gmail.com')
    lee.printAll()

if __name__ == "__main__":
    test() '''

#사용자로부터 입력받기
def create_facebook():
    first_name = input("What's your first name? ")
    last_name = input("What's your last name? ")
    mobile = input("What's your mobile phone number? ")
    email = input("What's your email address? ")
    facebook = Facebook(first_name, last_name, mobile, email)
    return facebook

def read_facebook(facebook_list):
    for facebook in facebook_list:
        facebook.printAll()

#def search_facebook(facebook_list):
#    for facebook in facebook_list:


def main_menu():
    print('Choose the menu you want below: ')
    print('1: create')
    print('2: read all')
    print('3: read by condition')
    print('4: exit')
    menu = input('prompt> ')
    return int(menu)

def run():
    facebook_list = []
    while 1:
        menu = main_menu()
        if menu == 1:
            facebook = create_facebook()
            facebook_list.append(facebook)
        if menu == 2:
            read_facebook(facebook_list)
        if menu == 4:
            break
        if menu not in [1, 2, 3, 4]:
            return main_menu()



if __name__ == "__main__":
    run()
