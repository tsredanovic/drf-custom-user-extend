from allauth.account.models import EmailAddress
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=commit)

        EmailAddress.objects.create(user=user, email=user.email, primary=True, verified=True)

        return user

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    def save(self, commit=True):
        user = super().save(commit=commit)

        email_address = EmailAddress.objects.filter(user=user).first()
        email_address.email = user.email
        email_address.save()

        return user

    class Meta:
        model = CustomUser
        fields = ('email',)
