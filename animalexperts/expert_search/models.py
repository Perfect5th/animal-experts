from django.db import models

# Create your models here.
class FieldCategory(models.Model):
    # Browseable field of expertise categories
    name = models.CharField(max_length=200)
    code = models.SlugField()
    
    class Meta:
        verbose_name = "Field of Expertise"
        verbose_name_plural = "Fields of Expertise"


class Expert(models.Model):
    # Representation of an individal Animal Expert
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    affiliation = models.CharField(max_length=200, 
        help_text='University/Institution/Business')
    subjects = models.TextField()
    fields = models.ManyToManyField(FieldCategory)
    email = models.EmailField()
    website = models.URLField()
    description = models.TextField()
