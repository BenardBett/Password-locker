class User:
    """
    Class that generates new instances of users.
    """

    contact_list = [] # Empty user list

    def __init__(self,username,password):
        self.username = username
        self.password= password

    