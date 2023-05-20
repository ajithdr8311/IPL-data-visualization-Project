from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from calculations.models import Matches, Deliveries
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        csv_files = options['csv_file']
        for csv_file in csv_files:
            self.load_data(csv_file)

    @transaction.atomic
    def load_data(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            if(csv_file == 'matches.csv'):
                load_matches(reader)
            elif csv_file == 'deliveries.csv':
                load_deliveries(reader)


def load_matches(matches_reader):
    for matches in matches_reader:
        Matches(
            id = int(matches['id']),
            season = int(matches['season']),
            city = matches['city'],
            date = matches['date'],
            team1 = matches['team1'],
            team2 = matches['team2'],
            toss_winner = matches['toss_winner'],
            toss_decision = matches['toss_decision'],
            result = matches['result'],
            dl_applied = int(matches['dl_applied']),
            winner = matches['winner'],
            win_by_runs = int(matches['win_by_runs']),
            win_by_wickets = int(matches['win_by_wickets']),
            player_of_match = matches['player_of_match'],
            venue = matches['venue'],
            umpire1 = matches['umpire1'],
            umpire2 = matches['umpire2'],
            umpire3 = matches['umpire3']
        ).save()

def load_deliveries(deliveries_reader):
    for delivery in deliveries_reader:
        Deliveries(
            match_id_id = int(delivery['match_id']),
            inning = int(delivery['inning']),
            batting_team = delivery['batting_team'],
            bowling_team = delivery['bowling_team'],
            over = int(delivery['over']),
            ball = int(delivery['ball']),
            batsman = delivery['batsman'],
            non_striker = delivery['non_striker'],
            bowler = delivery['bowler'],
            is_super_over = int(delivery['is_super_over']),
            wide_runs = int(delivery['wide_runs']),
            bye_runs = int(delivery['bye_runs']),
            legbye_runs = int(delivery['legbye_runs']),
            noball_runs = int(delivery['noball_runs']),
            penalty_runs = int(delivery['penalty_runs']),
            batsman_runs = int(delivery['batsman_runs']),
            extra_runs = int(delivery['extra_runs']),
            total_runs = int(delivery['total_runs']),
            player_dismissed = delivery['player_dismissed'],
            dismissal_kind = delivery['dismissal_kind'],
            fielder = delivery['fielder']
        ).save()