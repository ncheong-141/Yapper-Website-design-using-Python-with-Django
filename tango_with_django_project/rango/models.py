from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False)
    follows = models.ManyToManyField('self', symmetrical=False, blank=True)
    bio = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=128, blank=True) 
    picture = models.ImageField(upload_to='profile_images', blank=True)
    user_slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.user_slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def set_Follows(self, field):
        self.follows = field

    def __str__(self):
        return self.user.username





class Dog(models.Model):
    pass



class Sport(models.Model):
    
    # Enforce consistent name length accross all instances
    NAME_MAX_LENGTH = 128

    # Model attributes 
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    description = models.TextField()
    breed_restricitons = models.TextField()
    follows = models.IntegerField(default=0)

    # Slug attributes
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sport, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Competition(models.Model):
    
    # Enforce consistent name length accross all instance
    NAME_MAX_LENGTH = 128
    ADDRESS_MAX_LENGTH = 200
    URL_MAX_LENGTH = 200

    # Model attributes 
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH)   # Address of compititon
    location = models.CharField(max_length=100)                 # Google API information in String form
    date = models.DateField(null = True)                        # Date object
    eventpage = models.URLField()                               # Url of event page if avaialble
    isCompleted = models.BooleanField(default=False)            # Boolean field for is completed or not 
    description = models.TextField()                            # Description about competition

    # Relationship attribute 
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    # Slug attributes
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Competition, self).save(*args, **kwargs)

    # Verbose print
    def __str__(self):
        return self.name



class Breed(models.Model):
    pass

class Participation(models.Model):
    pass

class Award(models.Model):
    pass




