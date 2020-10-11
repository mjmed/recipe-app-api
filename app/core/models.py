from django.db import models

# Importaciones necesarias para extender el modelo de usuario de Django
# y hacer uso de las características que vienen con modelo.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



# La clase UserManager provee las funciones necesarias para crear un usuario
# o un superusuario.
# Extendemos la clase de BaseUserManager, y la personalizamos a nuestras necesidades
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""

        if not email:
            raise ValueError('User must have an email adress')
        user = self.model(email=self.normalize_email(email), **extra_fields)      # normalize_email es una función auxiliar que viene con el administrador de usuarios base     
        user.set_password(password)     # set_password permite crear una contraseña encriptada
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Obtenemos las bases del modelo para luego personalizarlo a nuestras necesidades
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

