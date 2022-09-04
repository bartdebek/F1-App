from datetime import date, timedelta
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    flag = models.ImageField(upload_to='images/flags/')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    wikipedia_link = models.URLField(max_length=200)
    twitter_handle = models.CharField(max_length=20,blank=True,null=True)
    logo = models.ImageField(upload_to='images/logos/')
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    number_of_championships = models.PositiveIntegerField(default=0)
    number_of_wins = models.PositiveIntegerField(default=0)
    first_race_date = models.DateField(null=True)
    total_races = models.PositiveIntegerField(default=0)
    total_podiums = models.PositiveIntegerField(default=0)
    # User rating
    average_rating = models.FloatField(default=0)
    number_of_ratings = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_flag(self):
        return self.country.flag

    
class Driver(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    wikipedia_link = models.URLField(max_length=200)
    twitter_handle = models.CharField(max_length=20,null=True,blank=True)
    photo = models.ImageField(upload_to='images/drivers/')
    nationality = models.ForeignKey(Country,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    number_of_championships = models.PositiveIntegerField(default=0)
    number_of_wins = models.PositiveIntegerField(default=0)
    first_race_date = models.DateField(null=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True,default=None,blank=True)
    total_races = models.PositiveIntegerField(default=0)
    total_podiums = models.PositiveIntegerField(default=0)
    # User rating
    average_rating = models.FloatField(default=0)
    number_of_ratings = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_flag(self):
        return self.nationality.flag

    def get_logo(self):
        return self.team.logo

    def get_age(self):
        today = date.today()
        birthday = self.date_of_birth
        if self.date_of_death:
            return (self.date_of_death - birthday) // timedelta(days=365.2425)
        else:
            return (today - birthday) // timedelta(days=365.2425)
            
    
    class Meta:
        ordering = ['-number_of_championships']

