from django.test import TestCase
from .models import Profile, Image

# Create your tests here.

# Profile Tests
class ProfileTest(TestCase):
    
    def setUp(self):
        self.new_user = Profile(id=1, name='Msee', profile_photo='image/yes.jpg', bio='Freelancer')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, Profile))

    def test_save_profile(self):
        self.new_user.save_profile()
        new_user = Profile.objects.all()
        self.assertTrue(len(new_user)>0)

# Image Tests
class ImageTest(TestCase):

    def setUp(self):
        self.profile = Profile(name='Msee')
        self.profile.save_profile()
        
        self.my_image = Image(id=1, image='image/photo.jpg', image_name='My Prof', image_caption='That is more like it', profile=self.profile, likes=True, comments='Kazi safi', date_created='2022-04-05')

    def test_instance(self):
        self.assertTrue(isinstance(self.my_image, Image))
    
    def test_image_save(self):
        self.my_image.save_image()
        my_image = Image.objects.all()
        self.assertTrue(len(my_image) > 0)