# Write your MySQL query statement below

select
    t.team_name as team_name,
    count(*) as matches_played,
    sum(
        if(
            team_id = home_team_id,
            case
                when home_team_goals > away_team_goals then 3
                when home_team_goals = away_team_goals then 1
                else 0
            end,
            case
                when home_team_goals < away_team_goals then 3
                when home_team_goals = away_team_goals then 1
                else 0
            end
        )
    ) as points,
    sum(if(team_id = home_team_id, home_team_goals, away_team_goals)) as goal_for,
    sum(if(team_id = home_team_id, away_team_goals, home_team_goals)) as goal_against,
    sum(if(team_id = home_team_id, home_team_goals, away_team_goals)) - sum(if(team_id = home_team_id, away_team_goals, home_team_goals)) as goal_diff
from
    Teams t
    join
    Matches m
    on (
        t.team_id = m.home_team_id
        or
        t.team_id = m.away_team_id
    )
group by t.team_id
order by points desc, goal_diff desc, team_name
