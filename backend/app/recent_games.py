from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd
from datetime import datetime

def get_current_season():
    today = datetime.today()
    year = today.year
    month = today.month

    if month >= 10:
        starting_year = year
        ending_year = year + 1
    else:
        start_year = year - 1
        ending_year = year
    return f"{start_year}-{str(ending_year)[-2:]}"

def recent_games():
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season=get_current_season(),
        season_type_all_star="Regular Season",
        per_mode_detailed="PerGame",   
        last_n_games=15,        
    )

    df = stats.get_data_frames()[0]
    return df
