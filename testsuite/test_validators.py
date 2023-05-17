import unittest
from validators import UserAuthorizationValidator
from validators import UserInputValidator, NewReminderFields

class TestUserAuthorizationValidator(unittest.TestCase):

    def test_is_user_authorized(self):
        mock_authorized_user_list = ['lebronjames','stephcurry']
        test_user_authorization_obj = UserAuthorizationValidator(mock_authorized_user_list)
        self.assertTrue(test_user_authorization_obj.is_user_authorized('lebronjames'))
        self.assertFalse(test_user_authorization_obj.is_user_authorized('stephhhhhh'))

