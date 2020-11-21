from user import user
    def create_user(username,password);
        '''
        function to create  new user
        '''
        new_user= User(username,password)
        return new_user
    
   def save_user(user):
        '''
        function to save new user
        '''
        User.save_user()
       
    def delete_user(user):
        '''
        function that deletes a user
        '''
        User.delete_user() 
        