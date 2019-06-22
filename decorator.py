import time
user="bruce"
pwd="1234"
def auth(auth_type):
    def outter_wraper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and pwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    func(*args, **kwargs)
                else:
                    exit("\033[32;1mUser has not passed authentication\033[0m")
            elif auth_type == "ldap":
                print("good")
        return wrapper
    return outter_wraper

# @auth(auth_type="local")
# def test1():
#     print('wecome to test1')

@auth(auth_type="ldap")
def test2():
    print('wecome to test1')
test2()