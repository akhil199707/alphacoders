from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
class UserAccountTest(TestCase):
    def test_new_superuser(self):
        db = get_user_model()
        Super_user = db.objects.create_superuser('test@test.com','username','alpha','beta','Password@1')
        self.assertEqual(Super_user.email,'test@test.com')
        self.assertEqual(Super_user.user_name,'username')
        self.assertEqual(Super_user.first_name,'alpha')
        self.assertEqual(Super_user.last_name,'beta')
        self.assertTrue(Super_user.is_superuser)
        self.assertTrue(Super_user.is_staff)
        self.assertTrue(Super_user.is_active)
        self.assertEqual(str(Super_user), "username")
