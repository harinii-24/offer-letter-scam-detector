def login(username, password):
    if username.strip() != "" and password.strip() != "":
        return True
    return False