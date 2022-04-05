from django.test import TestCase
from .models import Profile, Image

# Create your tests here.

# Profile Tests
class ProfileTest(TestCase):
    
    def setUp(self):
        self.new_user = Profile(2,'Msee','Null','Freelancer')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, Profile))

# Image Tests
class ImageTest(TestCase):

    def setUp(self):
        self.my_image = Image(9,'Not Found', 'My Prof','That is more like it', 'Yea', 20, 'So nice')

    def test_instance(self):
        self.assertTrue(isinstance(self.my_image, Image))