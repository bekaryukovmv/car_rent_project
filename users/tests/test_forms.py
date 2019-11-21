from django.test import SimpleTestCase
from django.utils.translation import activate

from users.forms import UserFormForEdit, CustomUserCreationForm, MyCustomSignupForm, CustomUserChangeForm


# Create your tests here.
class UserFormForEditTest(SimpleTestCase):

    def setUp(self):
        self.form = UserFormForEdit()
    
    def test_user_edit_rus_form_fields_label(self):
        activate('ru')
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'Email')
        self.assertTrue(self.form.fields['first_name'].label == None or self.form.fields['first_name'].label == 'Имя')
        self.assertTrue(self.form.fields['last_name'].label == None or self.form.fields['last_name'].label == 'Фамилия')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Язык')

    def test_user_edit_eng_form_fields_label(self):
        activate('en')
        form = UserFormForEdit()
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'Email')
        self.assertTrue(self.form.fields['first_name'].label == None or self.form.fields['first_name'].label == 'First name')
        self.assertTrue(self.form.fields['last_name'].label == None or self.form.fields['last_name'].label == 'Last name')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Language')


class CustomUserCreationFormTest(SimpleTestCase):

    def setUp(self):
        self.form = CustomUserCreationForm()

    def test_create_user_rus_form_fields_label(self):
        activate('ru')
        # print(self.form.fields['username'].label)
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'Email')
        self.assertTrue(self.form.fields['username'].label == None or self.form.fields['username'].label == 'Имя пользователя')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Язык')

    def test_create_user_eng_form_fields_label(self):
        activate('en')
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'Email')
        self.assertTrue(self.form.fields['username'].label == None or self.form.fields['username'].label == 'Username')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Language')


class CustomUserChangeFormTest(SimpleTestCase):
    def setUp(self):
        self.form = CustomUserChangeForm()
    
    def test_user_change_rus_form_fields_label(self):
        activate('ru')
        # print(self.form.fields['username'].label)
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'Email')
        self.assertTrue(self.form.fields['username'].label == None or self.form.fields['username'].label == 'Имя пользователя')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Язык')

    def test_user_change_eng_form_fields_label(self):
        activate('en')
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'Email')
        self.assertTrue(self.form.fields['username'].label == None or self.form.fields['username'].label == 'Username')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Language')


class MyCustomSignupFormTest(SimpleTestCase):

    def setUp(self):
        self.form = MyCustomSignupForm()
    
    