from django.test import TestCase
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(team.name, 'Test Team')

class UserProfileModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(user.email, 'test@example.com')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, date='2026-02-27')
        self.assertEqual(activity.activity_type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='A test workout')
        self.assertEqual(workout.name, 'Test Workout')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        leaderboard = Leaderboard.objects.create(team=team, total_points=50)
        self.assertEqual(leaderboard.total_points, 50)
