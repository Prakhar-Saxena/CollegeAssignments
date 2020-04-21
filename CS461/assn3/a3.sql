-- CREATE TABLE nba (player varchar(50), salary integer, season char(7), season_end integer, season_start integer, team varchar(50), primary key (player, team, season));

-- COPY nba(player, salary, season, season_end, season_start, team) FROM 'S:\workspace\CollegeAssignments\CS461\assn3\nba.csv' DELIMITER ',' CSV HEADER;

-- this is for Q1

SELECT COUNT(DISTINCT(team)) FROM nba WHERE season_start >= 2017 AND season_end <= 2018;

-- OR

SELECT COUNT(DISTINCT(team)) FROM nba WHERE season = '2017-18';



-- this is for Q2

SELECT player, salary FROM nba ORDER BY salary DESC LIMIT 1;


-- this is for Q3

SELECT player, salary, team, season FROM nba ORDER BY salary ASC LIMIT 1;


-- this is for Q4

SELECT player, COUNT(DISTINCT(season)) AS "Seasons" FROM nba WHERE team = 'Philadelphia 76ers' GROUP BY player HAVING COUNT(DISTINCT(season)) > 5;

-- this is for Q5

SELECT player, team, salary, season FROM nba WHERE player = 'Allen Iverson' ORDER BY season;


-- this is for Q6

-- I wasn't sure what you meant by 'the year of their first season' so I printed both the season adn the season_start

SELECT player, COUNT(DISTINCT(season)) AS "Seasons", MIN(season) AS "First Season", MIN(season_start) AS "Year of First Season" FROM nba GROUP BY player HAVING COUNT(DISTINCT(season)) > 20;


-- this is for Q7

SELECT team, MIN(season_start) AS "first", MAX(season_end) AS "last", COUNT(DISTINCT(season)) AS "no_years" FROM nba GROUP BY team ORDER BY "no_years", team;


-- this is for Q8

SELECT team, MIN(season_start) AS "first" FROM nba GROUP BY team ORDER BY "first" DESC LIMiT 1;


-- this is for Q9

SELECT team, COUNT(DISTINCT(player)) AS "no_player" from nba GROUP BY team ORDER BY "no_player" DESC LIMIT 1;


-- this is for Q10

SELECT player, COUNT(DISTINCT(TEAM)) AS "no_teams" from nba GROUP BY player ORDER BY "no_teams" DESC;