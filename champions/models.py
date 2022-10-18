import uuid
from datetime import date, timedelta
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from environs import Env

from star_ratings.models import Rating
import tweepy

# Tweepy token settings
env = Env()
env.read_env()
client = tweepy.Client(bearer_token=env("TWITTER_TOKEN"))


class Country(models.Model):
    name = models.CharField(max_length=50)
    flag = models.ImageField(upload_to='images/flags/')

    def __str__(self):
        return self.name


class Team(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
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
    ratings = GenericRelation(Rating, related_query_name='teams')

    class Meta:
        ordering = ('-active',)

    def __str__(self):
        return self.name

    def get_flag(self):
        return self.country.flag

    def get_absolute_url(self):
        return reverse('team_detail',
                       args=[str(self.uuid)])

    def tweet_list(self):
        team = Team.objects.get(id=self.id)
        name = team.twitter_handle
        team_data = client.get_user(username=name)
        team_id = team_data.data.id
        tweets = client.get_users_tweets(id=team_id, 
                                        max_results=5,
                                        expansions=['attachments.media_keys'],
                                        tweet_fields=['created_at','public_metrics','attachments'],
                                        media_fields=['preview_image_url'],
                                    )
        return tweets.data

    
class Driver(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    wikipedia_link = models.URLField(max_length=200)
    twitter_handle = models.CharField(max_length=20,null=True,blank=True)
    photo = models.ImageField(upload_to='images/drivers/')
    nationality = models.ForeignKey(Country,on_delete=models.CASCADE)
    team = models.ManyToManyField(Team)
    number_of_championships = models.PositiveIntegerField(default=0)
    number_of_wins = models.PositiveIntegerField(default=0)
    first_race_date = models.DateField(null=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True,default=None,blank=True)
    total_races = models.PositiveIntegerField(default=0)
    total_podiums = models.PositiveIntegerField(default=0)
    # User rating
    ratings = GenericRelation(Rating, related_query_name='drivers')


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

    def get_absolute_url(self):
        return reverse('driver_detail',
                       args=[str(self.uuid)])

    def tweet_list(self):
        driver = Driver.objects.get(id=self.id)
        name = driver.twitter_handle
        driver_data = client.get_user(username=name)
        driver_id = driver_data.data.id
        tweets = client.get_users_tweets(id=driver_id, 
                                        max_results=5, 
                                        tweet_fields=['created_at','public_metrics'],)
        return tweets.data


class SeasonResults(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    date_updated = models.DateField(auto_now=True)
    points = models.FloatField(default=0,null=True,blank=True)

    def __str__(self):
        return f'{self.driver} {self.team} {self.points} points, updated on {self.date_updated}'
