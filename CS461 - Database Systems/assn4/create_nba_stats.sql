-- delete the table if it exists

DROP TABLE teams;
DROP TABLE players;
DROP TABLE game_details;

-- create the nba games tables

CREATE TABLE teams (
    league_id integer,
    team_id integer,
    min_year integer,
    max_year integer,
    abbreviation varchar(50),
    team_name varchar(50),
    yearfounded integer,
    city varchar(50),
    arena varchar(50),
    arenacapacity integer,
    owner varchar(50),
    general_manager varchar(50),
    head_coach varchar(50),
    league_affiliation varchar(50)
);

CREATE TABLE players (
    player_name varchar(50),
    team_id integer,
    player_id integer,
    season integer
);

CREATE TABLE game_details (
    game_id integer,
    team_id integer,
    team_abbreviation varchar(50),
    team_city varchar(50),
    player_id integer,
    player_name varchar(50),
    player_position varchar(50),
    comment varchar(50),
    min varchar(50),
    fgm numeric(3),
    fga numeric(3),
    fg_pct numeric(3),
    fg3m numeric(3),
    fg3a numeric(3),
    fg3_pct numeric(3),
    ftm numeric(3),
    fta numeric(3),
    ft_pct numeric(3),
    oreb numeric(3),
    dreb numeric(3),
    reb numeric(3),
    ast numeric(3),
    stl numeric(3),
    blk numeric(3),
    tovr numeric(3),
    pf numeric(3),
    pts numeric(3),
    plus_minus numeric(3)
);

-- load table

\copy teams FROM 'S:\workspace\CollegeAssignments\CS461\assn4\teams.csv' DELIMITER ',' CSV HEADER;
\copy players FROM 'S:\workspace\CollegeAssignments\CS461\assn4\players.csv' DELIMITER ',' CSV HEADER;
\copy game_details FROM 'S:\workspace\CollegeAssignments\CS461\assn4\game_details.csv' DELIMITER ',' CSV HEADER;

--psql -d nba_stats -a -f 'S:/workspace/CollegeAssignments/CS461/assn4/create_nba_stats.sql'
--psql -d nba_stats -a -f 'S:\workspace\CollegeAssignments\CS461\assn4\create_nba_stats.sql'
--psql postgres -f 'S:/workspace/CollegeAssignments/CS461/assn4/create_nba_stats.sql'
--psql postgres -f 'S:\workspace\CollegeAssignments\CS461\assn4\create_nba_stats.sql'