import random as rd
# This is a Data Class, the attributes are the most important things, as data retainer,
# User Class (and other data classes, if added), represent the data "Model" of the system.

class User:    
    def __init__(self, full_name, age, role):
        self.full_name, self.age, self.role = full_name, age, role
        # This put everything in lowercase, then substitute the spaces with _ 
        # and add age and random number
        # Beware: It doesn't do anything for any other special characters like ' or , or .!
        self.user_id = f"{full_name.lower().replace(' ', '_')}_{age}_{rd.randint(0000,9999)}"
        self.password_hash = None
    def set_hash_password(self, password):
        self.password_hash = hash(password)
    def __str__(self):
        return (f"ID: {self.user_id}, full name: {self.full_name} - age: {self.age}")


# In this class we don't need a state, it is only a "Controller"
class UserManager:
    def create_user(self):
        # This function lacks checks of the input, beware
        name = input("Full name: ")
        age = input("Age: ")
        role = input("Role (admin/editor/user): ")
        return User(name, age, role)
    def handle_password(self, user):
        # also this function
        pwd = input(f"Enter password for {user.user_id}: ")
        user.set_hash_password(pwd)
        print("Password set")

# I added this class for 2 purposes, first, encapsulation, second, to divide the "View" of the system.
# It was not specifically required (but it is a good practice)
class MainView:
        user_list = []
        def __call__(self):
            input_str = input("[Enter] for the list, new to create a new user: ")
            if  input_str == 'new':
                manager = UserManager()
                user = manager.create_user()
                print(f"User created -> ID: {user.user_id}, Role: {user.role}")
                manager.handle_password(user)
                # __str__ in action
                print(user)
                self.user_list.append(user)
            elif(input_str=='Q'):
                return False
            else:
                for user in self.user_list:
                # __str__ in action
                    print(user)
            return True

# Encapsulating the main function!
def main():
    mainView = MainView()
    while True:
        # when the function return False, exit
        if not mainView(): # __call__ in action
            raise ValueError

# This is a really useful way to avoid module interaction while we operate outside functions or classes
if __name__ == "__main__":
    main()