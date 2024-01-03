from django import forms 
from . models import Order, Package, Profile, CleanerProfile, Proposal, Review
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating', 'communication_rating']

    text = forms.CharField(
        label='Leave your comment',
        widget=forms.Textarea(attrs={
        'placeholder': 'Enter your review',
        'class': 'w-full py-3 px-4 rounded-xl border',
        'rows': 4,
    }))

    rating = forms.IntegerField(
        label='Rate a client',
        widget=forms.NumberInput(attrs={
        'placeholder': 'Enter your rating (1-5)',
        'class': 'w-full py-3 px-4 rounded-xl border',
        'min': 1,
        'max': 5,
    }))

    communication_rating = forms.IntegerField(
        label='Rate a communication with client',
        widget=forms.NumberInput(attrs={
        'placeholder': 'Enter your rating (1-5)',
        'class': 'w-full py-3 px-4 rounded-xl border',
        'min': 1,
        'max': 5,
    }))


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['price', 'comment']

    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter your price',
        'class': ' py-3 px-4 rounded-xl border'
    }))

    comment = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter comment',
        'class': 'mt-3 w-full py-3 px-4 rounded-xl border mr-10'
    }))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'street',
            'city',
            'building_number',
            'apartment_number',
            'metres',
            'client_price',
            'date',
            'time',
            'enter',
            'package',
        ]

    street = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter street',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))
    
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter city',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    building_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter building number',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    apartment_number = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter apartment number',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    metres = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter metres',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    client_price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter your price',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    date = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'Enter date',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'placeholder': 'Enter time',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    enter = forms.ChoiceField(
        choices=Order.WAYS_TO_ENTER,
        initial='H',
        widget=forms.Select(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
    )

    package = forms.ModelChoiceField(
        queryset=Package.objects.all(),
        empty_label="Select a package",
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
    )

class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'street',
            'city',
            'building_number',
            'apartment_number',
            'metres',
            'client_price',
            'date',
            'time',
            'enter',
            'package',
        ]

    street = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter street',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))
    
    city = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter city',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    building_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter building number',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    apartment_number = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter apartment number',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    metres = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter metres',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    client_price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter your price',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    date = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'Enter date',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'placeholder': 'Enter time',
        'class': 'w-full py-3 px-4 rounded-xl border'
    }))

    enter = forms.ChoiceField(
        choices=Order.WAYS_TO_ENTER,
        initial='H',
        widget=forms.Select(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
    )

    package = forms.ModelChoiceField(
        queryset=Package.objects.all(),
        empty_label="Select a package",
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
    )


class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(
        label=('Password'),
        widget=forms.HiddenInput,
        required=False,
        help_text=('Raw passwords are not stored, so there is no way to see this user’s password, '
                    'but you can change the password using this form.'),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

    username = forms.CharField(
        label=('Email'),
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
        required=False,
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter first name',
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
        required=False,
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter last name',
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
        required=False,
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'building_number', 'apartment_number']

    address = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter address',
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
        required=False,
    )

    building_number = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter building number',
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
        required=False,
    )

    apartment_number = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter apartment number',
            'class': 'w-full py-3 px-4 rounded-xl border'
        }),
        required=False,
    )

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border',
            'placeholder': 'Enter old password',
        }),
    )

    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border',
            'placeholder': 'Enter new password',
        }),
    )

    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full py-3 px-4 rounded-xl border',
            'placeholder': 'Confirm new password',
        }),
    )

