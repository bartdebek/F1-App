from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    flag = models.ImageField(upload_to='images/flags/')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    wikipedia_link = models.CharField(max_length=200)
    twitter_handle = models.CharField(max_length=20,null=True)
    logo = models.ImageField(upload_to='images/logos/')
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    number_of_championships = models.PositiveIntegerField(default=0)
    first_race_date = models.DateField(null=True)
    first_race = models.CharField(max_length=200,null=True)
    other_achievements = models.TextField()
    total_races = models.PositiveIntegerField(default=0)
    total_podiums = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    
class Driver(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    wikipedia_link = models.CharField(max_length=200)
    twitter_handle = models.CharField(max_length=20,null=True)
    photo = models.ImageField(upload_to='images/drivers/')
    nationality = models.ForeignKey(Country,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    number_of_championships = models.PositiveIntegerField(default=0)
    first_race_date = models.DateField(null=True)
    first_race = models.CharField(max_length=200,null=True)
    last_race = models.CharField(max_length=200,null=True)
    date_of_birth = models.DateField()
    other_achievements = models.TextField()
    total_races = models.PositiveIntegerField(default=0)
    total_podiums = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_flag(self):
        return self.nationality.flag

    def get_logo(self):
        return self.team.logo
