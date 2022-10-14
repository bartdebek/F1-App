import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from champions.models import Driver, Team, Country


class DriverTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.country = Country.objects.create(
            name = 'Poland',
        )   
        cls.team = Team.objects.create(
            name = 'Test Team',
            wikipedia_link = 'https://www.example.com',
            twitter_handle = '@example',
            country = Country.objects.get(id=1),
            number_of_championships = '10',
            number_of_wins = '1000',
            first_race_date = datetime.date(2010, 1, 1),
            total_races = '2000',
            total_podiums = '500',
            )

    def test_country_listing(self):
        self.assertEqual(f'{self.country.name}', 'Poland')

    def test_team_listing(self):
        self.assertEqual(f'{self.team.name}', 'Test Team')
        self.assertEqual(f'{self.team.country}', 'Poland')
        self.assertEqual(f'{self.team.total_races}', '2000')
