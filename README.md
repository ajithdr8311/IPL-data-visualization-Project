# Django IPL Project

Performed Calculations on IPL dataset for the following queries.
1. Number of matches Played per season for all the seasons.
2. Number of matches won per team per season.
3. Extra runs conceded per team in the year 2016.
4. Top ten economical bowlers in the year 2015.

The Results are shown in the form of charts using HighCharts library.


- **Install required modules**
```
pip install -r requirements.txt
```

- **Command to load csv data into database**
```
python manage.py load_data <MATCHES_CSV_PATH> <DELIVERIES_CSV_PATH>
``` 

- **Command to start the server**
```
python manage.py runserver
```

- **How to see charts**
    - Start the server, go to https://localhost:<PORT>/charts/
    - https://localhost:<PORT>/charts/<problem_number>
    - <problem_number>: 1,2,3,4