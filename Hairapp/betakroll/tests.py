# Author Kjærsti L. Bergli, email: klb022@uit.no 

from django.test import TestCase
from users.models import User 


class UserTest (TestCase):
    def setUp(self):
        # Test user object that has admin rights
        User.objects.create(email = "testadmin@test.no", username="Admintester", role=3, phone="12345678")
        # Test user object that has customer rights
        User.objects.create(email = "testuser@test.no", username="Usertester", role=1, phone="12345679")
        # Test user object with too long phonenumber
        User.objects.create(email = "testphonelong@test.no", username="Longnumber", role=1, phone="12345678901234")
        # Test user object with too short phone number
        User.objects.create(email = "testphoneshort@test.no", username="Shortnumber", role=1, phone="123456")
    
    def tearDown(self):
        return super().tearDown()

    # Test that an admin user and a customer user is created correctly and stored in the database
    def test_create_user_success(self):
        adminUser = User.objects.get(email="testadmin@test.no")
        customerUser = User.objects.get(email="testuser@test.no")
        self.assertIsNotNone(adminUser)
        self.assertIsNotNone(customerUser)
        # check that the username is correct
        self.assertEqual(adminUser.username, "Admintester")
        self.assertEqual(customerUser.username, "Usertester")
        # Print the content of the new object
        print("OBJECT INFO:")
        print(adminUser.__dict__)

    # Testing the length of a phonenumber. 
    # It is supposed to not be shorter than 9 digits or longer than 12 to make sense in Norway. 
    def test_phone_to_long (self):
        longPhoneUser = User.objects.get(email="testphonelong@test.no")
        shortPhoneUser = User.objects.get(email="testphoneshort@test.no")
        self.assertGreater(len(longPhoneUser.phone), 13)
        # A phone number longer than 9 digits is not implemented in the database (yet). 
        # This could be an example of TDD, as one could implement a way to throw an exception if the phonenumber is to short.
        self.assertLess(len(shortPhoneUser.phone), 9)