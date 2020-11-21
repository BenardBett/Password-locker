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
        
    def find_user(username):
        '''
        function that finds a user
        '''
        return User.find_by_username( username)
    
    def check_existing_users(username):
        '''
        function that checks if a user exist
        '''
        return User.user_exist(username)
    
    def display_all_users()
        '''
        function that returns all the saved users in the application
        '''
        return user.display= all_user()
    def main():
        print("Hi! welcome to an application that help you manage your credentials")
        print("\n")
        print("please use the following short codes to perform any task you want")
        print("\n")
        while True:
            print("Use the short codes: cu- create a new user,du-display user, fu-find a user, ex-exist in the user list")
            
            short_code= input(), lower()
            if short_code==cu:
                print("New User")
                print("_"*10)
                print("username......")
                username= input()
                print("password......")
                password=input
                save_user(create_user(username,password))
                print("\n")
                print("New User{username}created")
                print("\n")
            else short_code=="du":
                if display_all_users:
                    print("This a list of all saved users")
                    print("\n")
                    
                    for user in display_all_users():
                        print(fu*{user.username})
                        print("\n")