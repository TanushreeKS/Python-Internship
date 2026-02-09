# Decorator Function
def admin_only(func):
    def wrapper(username):
        if username == "admin":
            func(username)
        else:
            print("Access Denied")
    return wrapper
def dashboard(username):
    print("Welcome to Admin Dashboard")
dashboard("admin")      # Allowed
dashboard("rahul")      # Blocked
