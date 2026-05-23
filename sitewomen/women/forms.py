import string

from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible


from .models import Category, Husband, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARACTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя -0123456789'
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else 'Должны быть только русские буквы'

    def __call__(self, value, *args, **kwargs):
        if not(set(value) <= set(self.ALLOWED_CHARACTERS)):
            raise forms.ValidationError(self.message, code=self.code)


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, min_length=3, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}),
#                             validators=[RussianValidator(),])
#     slug = forms.SlugField(max_length=255, label='URL',
#                            validators=[
#                                MinLengthValidator(3, message='Минимум 3 символа'),
#                                MaxLengthValidator(100),
#                            ])
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5}), required=False, label='Контент')
#     is_published = forms.BooleanField(required=False, initial=True, label='Статус')
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='не выбрано', label='Категории')
#     husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label='не замужем', label='Муж')
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         ALLOWED_CHARACTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя -0123456789'
#         if not(set(title) <= set(ALLOWED_CHARACTERS)):
#             raise forms.ValidationError('Должны быть только русские буквы')
class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='не выбрано', label='Категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label='не замужем', label='Муж')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {
            'title': 'Заголовок',
            'slug': 'URL',
            'content': 'Контент',
            'is_published': 'Статус публикации',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise forms.ValidationError('Длина заголовка не должна превышать 50 символов')

        return title

class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')