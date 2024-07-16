from django.contrib.auth.base_user import BaseUserManager


class CustomManager(BaseUserManager):
    def create_user(self,username,email, password, **extra_fields):
        if not username:
            raise ValueError('Username Must Be SET')
        if not email:
            raise ValueError('Email Must Be SET')
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,username,email, password, **extra_fields):
        user  = self.create_user(
            username= username,
            email= email,
            password= password,
            **extra_fields

        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user