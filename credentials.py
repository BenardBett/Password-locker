class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = [] # Empty credential list

    def __init__(self,username,password,account):
        self.username = username
        self.password= password
        self.account= account