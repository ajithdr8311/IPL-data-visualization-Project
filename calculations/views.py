from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Matches, Deliveries
from django.db.models import Sum, Count, Case, When, F, FloatField 
from django.db.models.functions import Cast
from json import dumps

# Create your views here.

def index(request):
    return render(request, 'calculations/index.html', {})


def matches_per_year(request):
    matches = Matches.objects.values('season').annotate(total_matches = Count('id'))
    
    context = {
        'categories': list(matches.values_list('season', flat=True)),
        'matches_played': list(matches.values_list('total_matches', flat=True))
    }
    contextJSON = dumps(context)
    return render(request, 'calculations/problem1.html', {'data': contextJSON})


def matches_won_per_team(request):
    matches = Matches.objects.only('winner', 'season')
    matches_won_per_team = {}
    for match in matches:
        teamWon = match.winner
        season = match.season

        if teamWon in matches_won_per_team:
            if season in matches_won_per_team[teamWon]:
                matches_won_per_team[teamWon][season] += 1
            else:
                matches_won_per_team[teamWon][season] = 1
        else:
            matches_won_per_team[teamWon] = {}
            matches_won_per_team[teamWon][season] = 1


    context = {
      'categories': list(range(2008, 2018)),
      'matches_won':  matches_won_per_team
    }
    contextJson = dumps(context)
        
    return render(request, 'calculations/problem2.html', {'data': contextJson})


def extra_runs_per_team(request):
    match_ids_2016 = Matches.objects.filter(season=2016).values_list('id')
    extra_runs_per_team = Deliveries.objects.filter(match_id__in=match_ids_2016).values('bowling_team').annotate(total_extra_runs=Sum('extra_runs'))
    extra_runs_per_team_per_year = {}

    for team in extra_runs_per_team:
        extra_runs_per_team_per_year[team['bowling_team']] = team['total_extra_runs']

    context = {
      'categories': list(extra_runs_per_team_per_year.keys()),
      'extras_per_team':  list(extra_runs_per_team_per_year.values())
    }
    contextJson = dumps(context)

    return render(request, 'calculations/problem3.html', {'data': contextJson})


def top_ten_econ_bowlers(request):
    match_ids_2015 = list(Matches.objects.filter(season=2015).values_list('id', flat=True))
    
    runs_conceded = {}
    overs_bowled = {}
    bowler_economy = {}

    deliveries = Deliveries.objects.filter(match_id__in=match_ids_2015)
    for delivery in deliveries:
        if delivery.match_id.id in match_ids_2015:
            bowler_name = delivery.bowler
            bye_runs = delivery.bye_runs
            legbye_runs = delivery.legbye_runs

            runs = delivery.total_runs - (bye_runs + legbye_runs)

            if bowler_name in runs_conceded:
                runs_conceded[bowler_name] += runs
            else:
                runs_conceded[bowler_name] = runs

            if int(delivery.wide_runs) or int(delivery.noball_runs):
                pass
            else:
                if bowler_name in overs_bowled:
                    overs_bowled[bowler_name] += 1
                else:
                    overs_bowled[bowler_name] = 1

    for bowler, balls in overs_bowled.items():
        overs_bowled[bowler] = balls / 6

    for bowler, balls in runs_conceded.items():
        bowler_economy[bowler] = round(balls / overs_bowled[bowler], 2)

    sorted_bowler_economy = dict((sorted(bowler_economy.items(), key=lambda x: x[1]))[:10])

    context = {
        'categories': list(sorted_bowler_economy.keys()),
        'economy': list(sorted_bowler_economy.values())
    }
    
    contextJson = dumps(context)
    return render(request, 'calculations/problem4.html', {'data': contextJson})