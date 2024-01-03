from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from client.models import Profile, CleanerProfile


class LogInFormClient(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

class SignUpFormClient(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    username = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype your password',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))


class SignUpFormCleaner(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
    
    card_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter building number',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    INN = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter building number',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    username = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype your password',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['username']
        user.save()

        profile, created = Profile.objects.get_or_create(user=user)
        profile.card_number = self.cleaned_data['card_number']
        profile.INN = self.cleaned_data['INN']

        if commit:
            profile.save()

        return user
    
class CleanerProfileForm(forms.ModelForm):
    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]

    class Meta:
        model = CleanerProfile
        fields = ['age', 'reason_for_leaving', 'previous_work_experience',
                  'punctuality', 'stress_resilience', 'cleaning_speed', 'cleaning_quality',
                  'willing_to_work_in_team', 'own_cleaning_equipment', 'city']

    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter your age',
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
        required=False,
    )

    reason_for_leaving = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter reason for leaving',
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
        required=False,
    )

    previous_work_experience = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border',  
        }),
        required=False,
    )

    punctuality = forms.IntegerField(
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 6)],
            attrs={
                'class': 'w-full py-3 px-4 rounded-xl border'
            }),
        required=False,
    )

    stress_resilience = forms.IntegerField(
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 6)],
            attrs={
                'class': 'w-full py-3 px-4 rounded-xl border'
            }),
        required=False,
    )

    cleaning_speed = forms.IntegerField(
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 6)],
            attrs={
                'class': 'w-full py-3 px-4 rounded-xl border'
            }),
        required=False,
    )

    cleaning_quality = forms.IntegerField(
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 6)],
            attrs={
                'class': 'w-full py-3 px-4 rounded-xl border'
            }),
        required=False,
    )

    willing_to_work_in_team = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border',  
        }),
        required=False,
    )

    own_cleaning_equipment = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border',  
        }),
        required=False,
    )

    city = forms.ChoiceField(
        choices=CleanerProfile.CITY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
        required=False,
    )