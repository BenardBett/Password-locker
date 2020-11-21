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
        
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)
        
        
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a credential that matches that username.
        Args:
            username:  username to search for
        Returns :
            Credential that matches the username.
        '''

        for credential in cls.credential_list:
            if credential.username == username:
                return credential 
            
    @classmethod
    def credential_exist(cls,name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            name: name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.name == name:
                    return True

        return False       
 