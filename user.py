class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty user list

    def __init__(self,username,password):
        self.username = username
        self.password= password

    def save_user(self):
        '''
        save new user to the application
        '''
        User.user_list.append(self)
              
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
        
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username: user to search for
        Returns :
            user  that matches the username.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user