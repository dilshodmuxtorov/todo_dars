from django.db import models
from django.core.exceptions import ValidationError



def password_validator(value):
    if len(value)<8:
        raise ValidationError("Password should be at least 8 character")
    elif value.isdigit():
        raise ValidationError("Password should contain a character as well")
    else:
        for i in value:
            if i.isdigit():
                return
        raise ValidationError("Password should contain number")

class UserModel(models.Model):
    name = models.CharField(default="", max_length=65)
    surname = models.CharField(default="",max_length=65)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    password = models.CharField(max_length=25,validators=[password_validator,])
    image = models.ImageField(upload_to='Users', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','password']

    class Meta:
        db_table = 'users'
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self) -> str:
        return self.name +" "+ self.surname
