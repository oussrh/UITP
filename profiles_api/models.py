from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):
    """Class required by Django for managing our users from the management
    command.
    """

    def create_user(self, email, name, password=None):
        """Creates a new user with the given detials."""

        # Check that the user provided an email.
        if not email:
            raise ValueError('Users must have an email address.')

        # Create a new user object.
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        # Set the users password. We use this to create a password
        # hash instead of storing it in clear text.
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given detials."""

        # Create a new user with the function we created above.
        user = self.create_user(
            email,
            name,
            password
        )

        # Make this user an admin.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """A user profile in our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Required function so Django knows what to use as the users full name.
        """

        self.name

    def get_short_name(self):
        """
        Required function so Django knows what to use as the users short name.
        """

        self.name

    def __str__(self):
        """What to show when we output an object as a string."""

        return self.email


class StatusUpdate(models.Model):
    """A users status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """A users message from one user to another."""

    sender = models.ForeignKey('UserProfile', related_name='fk_message_sender',on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        'UserProfile', related_name='fk_message_recipient',on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date_sent = models.DateTimeField(auto_now_add=True)
    
class Rapports(models.Model):
    userId = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    annee = models.IntegerField()
    is_Done = models.BooleanField(default=False)
    def __str__(self):
        return 'User: {}'.format(self.userId)


class Transports(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return 'Transports: {}'.format(self.nom)
    
class TypeIncidents(models.Model):
    nomType = models.CharField(max_length=50)
    def __str__(self):
        return 'Type Incidents: {}'.format(self.nomType)
    
class Incidents(models.Model):
    nomIncident = models.CharField(max_length=50)
    idTypeIncidents = models.ForeignKey(TypeIncidents, on_delete=models.CASCADE)
    def __str__(self):
        return 'Incidents: {}'.format(self.nomIncident)


class Detail(models.Model):
    idRapport = models.ForeignKey(Rapports, on_delete=models.CASCADE)
    idTransport = models.ForeignKey(Transports, on_delete=models.CASCADE)
    idIncidents = models.ForeignKey(Incidents, on_delete=models.CASCADE)
    frequence = models.IntegerField()
    commentaire = models.TextField()
    motivation = models.TextField()
    def __str__(self):
        return 'Incidents: {}'.format(self.idRapport)
