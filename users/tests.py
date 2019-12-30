from django.contrib.auth import get_user_model

from django.test import TestCase



class CustomUserModel(TestCase):

	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(
			username='alex',
			email='praise1234@mail.ru',
			password='2470730praise'
			)
		self.assertEqual(user.username, 'alex')
		self.assertEqual(user.email, 'praise1234@mail.ru')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)

	def test_create_superuser(self):
		User = get_user_model()
		admin_user = User.objects.create_superuser(
			username='superadmin',
			email='superadmin@email.com',
			password='testpass123'
			)

		self.assertEqual(admin_user.username, 'superadmin')
		self.assertEqual(admin_user.email, 'superadmin@email.com')
		self.assertTrue(admin_user.is_active)
		self.assertTrue(admin_user.is_staff)
		self.assertTrue(admin_user.is_superuser)












