from django.db import models

class Matches(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    city = models.CharField(max_length=20)
    date = models.DateField()
    team1 = models.CharField(max_length=40)
    team2 = models.CharField(max_length=40)
    toss_winner = models.CharField(max_length=40)
    toss_decision = models.CharField(max_length=20)
    result = models.CharField(max_length=15)
    dl_applied = models.IntegerField()
    winner = models.CharField(max_length=30)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=20)
    venue = models.CharField(max_length=20)
    umpire1 = models.CharField(max_length=20)
    umpire2 = models.CharField(max_length=20)
    umpire3 = models.CharField(max_length=20)

    def __str__(self):
        return f'match {self.id}'


class Deliveries(models.Model):
    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=30)
    bowling_team = models.CharField(max_length=30)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=20)
    non_striker = models.CharField(max_length=20)
    bowler = models.CharField(max_length=20)
    is_super_over = models.IntegerField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=30)
    dismissal_kind = models.CharField(max_length=30)
    fielder = models.CharField(max_length=30)

    def __str__(self):
        return f'delivery {self.match_id}'