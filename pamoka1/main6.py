class MyClass:
    def __init__(self):
        self.my_var = 42
        self._password = None
        self._bank_account_number = None

    def _generate_password(self):
        self._password = "password"

    def log_password(self) -> str:
        self._generate_password()
        return self._password


my_class = MyClass()
my_class.log_password()


class MyAnotherClass:
    def __init__(self):
        self.my_var = 42
        self.__password = None

    def __generate_password(self):
        self.__password = "password"

    def _set_password(self):
        self.__generate_password()
        return self.__password

    def send_data_to_database(self, data: str):
        password = self._set_password()
        print(f"Data: {data} Password: {password}")


# module database.py
# import MyClass from main

my_class = MyAnotherClass()

data = "data"
my_class.send_data_to_database("data")