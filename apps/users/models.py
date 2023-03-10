from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
from simple_history.models import HistoricalRecords


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name,  password, True, True, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, verbose_name="Nombre de Usuario")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Correo Electronico")
    name = models.CharField(max_length=255, blank=True, null=True,  verbose_name="Nombre")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Apellido")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def natural_key(self):
        return (self.username)

    def __str__(self):
        return f'{self.name} {self.last_name}'