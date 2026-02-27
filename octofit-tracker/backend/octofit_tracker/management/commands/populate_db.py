from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, UserProfile, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data in correct order to avoid unhashable errors
        for obj in Activity.objects.all():
            if obj.id:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.id:
                obj.delete()
        for obj in Leaderboard.objects.all():
            if obj.id:
                obj.delete()
        for obj in UserProfile.objects.all():
            if obj.id:
                obj.delete()
        for obj in Team.objects.all():
            if obj.id:
                obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc},
        ]
        user_objs = [UserProfile.objects.create(**u) for u in users]

        # Create Activities
        Activity.objects.create(user=user_objs[0], activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=user_objs[1], activity_type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=user_objs[2], activity_type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=user_objs[3], activity_type='Yoga', duration=40, date=timezone.now().date())

        # Create Workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=100)
        Leaderboard.objects.create(team=dc, total_points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
