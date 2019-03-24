from django import forms

class StartPage(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

class Authorization(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=(('1','Муж'),('2','Жен')))
