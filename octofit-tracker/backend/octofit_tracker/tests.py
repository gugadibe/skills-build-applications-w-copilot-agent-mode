from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(str(team), 'Marvel')
    def test_create_user(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team=team)
        self.assertEqual(str(user), 'Clark Kent')
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2023-01-01')
        self.assertEqual(activity.type, 'Run')
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Peter Parker', email='peter@marvel.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
