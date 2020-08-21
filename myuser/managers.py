from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Manager


class UserManager(BaseUserManager):

    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        

        groups = extra_fields.pop('groups', None)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
       
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(email, password, **extra_fields)



