from django.db import models


class registers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    Password = models.CharField(max_length=20)
    confirm_Password = models.CharField(max_length=20)
    phone = models.IntegerField()


class signin(models.Model):
    email = models.EmailField(primary_key=True, max_length=20)
    Password = models.CharField(max_length=20)

    def get_user(self):
        return self.email

    def get_pswd(self):
        return self.Password
