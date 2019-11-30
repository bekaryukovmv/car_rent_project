from django.test import SimpleTestCase, TestCase
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
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'Email')
        self.assertTrue(self.form.fields['username'].label == None or self.form.fields['username'].label == 'Имя пользователя')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Язык')

    def test_user_change_eng_form_fields_label(self):
        activate('en')
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'Email')
        self.assertTrue(self.form.fields['username'].label == None or self.form.fields['username'].label == 'Username')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Language')


class MyCustomSignupFormTest(TestCase):

    def setUp(self):
        self.form = MyCustomSignupForm()

    def test_user_change_rus_form_fields_label(self):
        activate('ru')
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'E-mail')
        self.assertTrue(self.form.fields['password1'].label == None or self.form.fields['password1'].label == 'Пароль')
        self.assertTrue(self.form.fields['password2'].label == None or self.form.fields['password2'].label == 'Пароль (еще раз)')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Язык')

    def test_user_change_eng_form_fields_label(self):
        activate('en')
        # print(self.form.fields['password2'].label)
        self.assertTrue(self.form.fields['email'].label == None or self.form.fields['email'].label == 'E-mail')
        self.assertTrue(self.form.fields['password1'].label == None or self.form.fields['password1'].label == 'Password')
        self.assertTrue(self.form.fields['password2'].label == None or self.form.fields['password2'].label == 'Password (again)')
        self.assertTrue(self.form.fields['user_lang'].label == None or self.form.fields['user_lang'].label == 'Language')

    def test_valid_sign_up_user_eng(self):
        form_data = {'email': 'a@a.com', 'password1': 'testpass123', 'password2': 'testpass123', 'user_lang': 'en'}
        form = MyCustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['user_lang'], 'en')

    def test_valid_sign_up_user_rus(self):
        form_data = {'email': 'a@a.com', 'password1': 'testpass123', 'password2': 'testpass123', 'user_lang': 'ru'}
        form = MyCustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['user_lang'], 'ru')

    def test_invalid_password_sign_up_user(self):
        form_data = {'email': 'a@a.com', 'password1': 'testpass123', 'password2': 'poptpass1234', 'user_lang': 'ru'}
        form = MyCustomSignupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_language_sign_up_user(self):
        form_data = {'email': 'a@a.com', 'password1': 'testpass123', 'password2': 'testpass123', 'user_lang': 'br'}
        form = MyCustomSignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertWarnsMessage(form.errors, f'Выберите корректный вариант. br нет среди допустимых значений.')
