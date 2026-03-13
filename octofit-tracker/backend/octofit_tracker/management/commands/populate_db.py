from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Limpando dados antigos...')
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Criando times...')
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write('Criando usuários...')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        peter = User.objects.create(name='Peter Parker', email='peter@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        diana = User.objects.create(name='Diana Prince', email='diana@dc.com', team=dc)

        self.stdout.write('Criando atividades...')
        Activity.objects.create(user=tony, type='Corrida', duration=30, date='2023-01-01')
        Activity.objects.create(user=peter, type='Natação', duration=45, date='2023-01-02')
        Activity.objects.create(user=steve, type='Ciclismo', duration=60, date='2023-01-03')
        Activity.objects.create(user=clark, type='Corrida', duration=50, date='2023-01-01')
        Activity.objects.create(user=bruce, type='Natação', duration=40, date='2023-01-02')
        Activity.objects.create(user=diana, type='Ciclismo', duration=70, date='2023-01-03')

        self.stdout.write('Criando treinos...')
        w1 = Workout.objects.create(name='Treino Força', description='Supino, agachamento, levantamento terra')
        w2 = Workout.objects.create(name='Treino Cardio', description='Corrida, bike, HIIT')
        w1.suggested_for.set([tony, clark, diana])
        w2.suggested_for.set([peter, steve, bruce])

        self.stdout.write('Criando leaderboard...')
        Leaderboard.objects.create(user=tony, points=120)
        Leaderboard.objects.create(user=peter, points=110)
        Leaderboard.objects.create(user=steve, points=100)
        Leaderboard.objects.create(user=clark, points=130)
        Leaderboard.objects.create(user=bruce, points=125)
        Leaderboard.objects.create(user=diana, points=140)

        self.stdout.write('Garantindo índice único em email...')
        with connection.cursor() as cursor:
            cursor.execute('''db.get_collection('users').createIndex({ "email": 1 }, { unique: true })''')

        self.stdout.write(self.style.SUCCESS('Banco populado com sucesso!'))
