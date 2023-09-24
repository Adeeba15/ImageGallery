from django.db import models

class Upload(models.Model):
    """Model definition for Upload."""

    caption = models.CharField(max_length=100)   
    image = models.ImageField(upload_to="images/")

    # class Meta:
    #     """Meta definition for Upload."""

    #     verbose_name = 'Upload'
    #     verbose_name_plural = 'Uploads'

    def __str__(self):
        """Unicode representation of Upload."""
        return self.caption

class DemoTable(models.Model):
    #models is a file and Model is a class which is being inherited
    #string, num date, time
    #email, url, file, image, boolean
    #choice, multiple choice, large text

    gender_choice=(("M","Male"), ( "F","Female"),("NS","Not Specified") )

    name = models.CharField(max_length=30)
    age= models.IntegerField(null=True, blank= True) #null= true for blank entry in database, blank=true for blank in form
    price= models.DecimalField(max_digits= 5, decimal_places=2)
    created_at= models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    timestamp= models.DateTimeField(auto_now_add=True)
    email= models.EmailField(max_length=254)
    url= models.URLField(max_length=200)
    file= models.FileField(upload_to='files/')
    avatar= models.ImageField(upload_to='avators/')
    is_active= models.BooleanField(default=True)
    gender= models.CharField(max_length=2, choices=gender_choice)
    description= models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    given_to= models.CharField(max_length=50)
    priorty= models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    
