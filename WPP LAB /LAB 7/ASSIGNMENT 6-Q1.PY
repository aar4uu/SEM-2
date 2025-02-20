class Password_manager:
    def __init__(self):  # Changed _init_ to __init__
        self.password_list = []
    
    def get_password(self):
        if self.password_list:
            return self.password_list[-1]
        return None

    def set_password(self, new_password):
        if new_password not in self.password_list:
            self.password_list.append(new_password)
            return True
        return False

    def is_correct(self, password):
        if password == self.password_list[-1]:
            return 1
        return 0

# Test the class
pm1 = Password_manager()
print(pm1.set_password("xyz"))  # Should print True (password added)
print(pm1.set_password("mysecondpassword"))  # Should print True (password added)
print(pm1.set_password("abc123"))  # Should print True (password added)
print(pm1.set_password("xyz"))  # Should print False (password already exists)

