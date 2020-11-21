import unittest # Importing the unittest module
from user import User # Importing the User class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("BenardBett","34512177b") # create user object
        
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"BenardBett")
        self.assertEqual(self.new_user.password,"34512177b")
       


if __name__ == '__main__':
    unittest.main()
