from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core import validators
from theoffice.ValidateModelMixin import ValidateModelMixin
from django.db.models.loading import get_model


class KeydistUserManager(BaseUserManager):
    def create_user(self, curtin_id, first_name, last_name, password = None):
        user = self.model(
            curtin_id = curtin_id,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, curtin_id, first_name, last_name, password):
        user = self.model(
            curtin_id = curtin_id,
            first_name = first_name,
            last_name = last_name,
            password = password
        )

        user.is_superuser = True
        user.is_staff = True

        user.set_password(password)
        user.save(using = self._db)
        return user


class KeydistUser(ValidateModelMixin, AbstractBaseUser, PermissionsMixin):
    STAFFASSOC = 1
    STUDENT = 2

    curtin_id = models.CharField(
        max_length = 20,
        blank = False,
        unique = True,
        validators = [validators.RegexValidator(
            regex = r'^[0-9]+[A-Z]?$',
            message = "Must be a valid curtin ID",
        )]
    )

    first_name = models.CharField(
        max_length = 30,
        blank = False,
    )

    last_name = models.CharField(
        max_length = 30,
        blank = False,
    )

    tidyclub_api_token = models.CharField(
        max_length = 256,
        blank = True,
        editable = False
    )

    is_active = models.BooleanField(
        default = True
    )

    is_staff = models.BooleanField(
        default = False
    )

    objects = KeydistUserManager()

    USERNAME_FIELD = 'curtin_id'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def curtin_status(self):
        if self.curtin_id[-1].isdigit():
            return self.STUDENT
        else:
            return self.STAFFASSOC

    @property
    def email(self):
        if self.curtin_status == self.STUDENT:
            return "%s@student.curtin.edu.au" % self.curtin_id
        else:
            return "%s@curtin.edu.au" % self.curtin_id
    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def short_name(self):
        return "%s %s" % (self.first_name, self.last_name[0])

    # Compatibility with Django admin
    def get_short_name(self):
        return self.short_name

    @property
    def keys_allocated_by(self):
        return get_model('keys', 'Key').objects.filter(allocated_by = self)

    @property
    def keys_allocated_to(self):
        return get_model('keys', 'Key').objects.filter(allocated_to = self)

    class Meta():
        permissions = {
            ('see_admin', "User can see the admin page"),
            ('change_user_passowrd', "Can change any user's password"),
            ('sync_permissions', "Can sync permissions"),
        }

        ordering = ['first_name']


    def __unicode__(self):
        return self.full_name
