class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list

    def __init__(self,account,username,password):
        self.account= account   
        self.username = username
        self.password= password
       
    def save_credential(self):
        '''
        method that saves credential objects into application
        '''
        Credential.credential_list.append(self)