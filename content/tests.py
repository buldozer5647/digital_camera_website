from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from django.urls import reverse, resolve

import os

from .models import DigitalImage
from .views import home_page

class DigitalImageModelTests(TestCase):
    def setUp(self):
        img_url = os.path.join(settings.BASE_DIR, "test_image.jpg")
        self.user = get_user_model().objects.create_user(username="test", email="test@gmail.com", password="123test123")
        
        self.dg_im = DigitalImage.objects.create(
            title="image title",
            description="image desc",
            alt_text="image alt text",
            user=self.user,
            image=SimpleUploadedFile(
                name="test_image.jpg",
                content=open(img_url, "rb").read(),
                content_type="image/png"
            )
        )

    def tearDown(self):
        self.dg_im.image.delete()
        return super().tearDown()
    
    def test_digital_image_creation(self):
        self.assertEqual(self.dg_im.title, "image title")
        self.assertEqual(self.dg_im.description, "image desc")
        self.assertEqual(self.dg_im.alt_text, "image alt text")

    def test_digital_image_image_upload(self):
        self.assertEqual(self.dg_im.image.name, "digital_images/test_image.jpg")
        self.assertTrue(self.dg_im.image.storage.exists(self.dg_im.image.name))

class DigitalImageUrlTests(TestCase):
    def setUp(self):
        self.url = reverse("homepage")
        self.response = self.client.get(self.url)

    def test_url_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "home.html")
    
    def test_template_contains(self):
        self.assertContains(self.response, "Hello")
        self.assertNotContains(self.response, "LALALAL")

    def test_used_view(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, home_page.__name__)
