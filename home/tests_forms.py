from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        comment_form = ContactForm({ "name": '',
            "email": 'test@test.com',
            "message": 'Hello!'})
        self.assertTrue(form.is_valid(), msg="Form is not valid")