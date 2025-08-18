from fastapi import APIRouter
import pandas as pd
import joblib
from app.recent_games import recent_games
from app.db import get_db_connection

router = APIRouter()

@router.get("/{team_name1}-{team_name2}")
def getRecentPredict(team_name1: str, team_name2: str):

    team_name1 = team_name1.upper()
    team_name2 = team_name2.upper()

    con = get_db_connection()

    cursor = con.cursor()

    query = 'SELECT team_name_home FROM "games" WHERE team_abbreviation_home = ?'

    cursor.execute(query, (team_name1,))
    home = cursor.fetchone()
    home_name = home[0]

    cursor.execute(query, (team_name2,))
    away = cursor.fetchone()
    away_name = away[0]

    data = recent_games()

    home_team = data[data["TEAM_NAME"] == home_name].iloc[0]
    away_team = data[data["TEAM_NAME"] == away_name].iloc[0]

    df = {
        # Home team stats
        "fg_pct_home": home_team["FG_PCT"],
        "fg3_pct_home": home_team["FG3_PCT"],
        "oreb_home": home_team["OREB"],
        "dreb_home": home_team["DREB"],
        "reb_home": home_team["REB"],
        "ast_home": home_team["AST"],
        "stl_home": home_team["STL"],
        "blk_home": home_team["BLK"],
        "tov_home": home_team["TOV"],
        "fta_home": home_team["FTA"],
        "fga_home": home_team["FGA"],
        "pts_home": home_team["PTS"],
        # Away team stats
        "fg_pct_away": away_team["FG_PCT"],
        "fg3_pct_away": away_team["FG3_PCT"],
        "oreb_away": away_team["OREB"],
        "dreb_away": away_team["DREB"],
        "reb_away": away_team["REB"],
        "ast_away": away_team["AST"],
        "stl_away": away_team["STL"],
        "blk_away": away_team["BLK"],
        "tov_away": away_team["TOV"],
        "fta_away": away_team["FTA"],
        "fga_away": away_team["FGA"],
        "pts_away": away_team["PTS"],
    }

    # Calculate offensive rating
    df["second_part"] = 0.44*df["fta_home"] - df["oreb_home"] + df["tov_home"]
    df["home_possessions"] = (df["fga_home"] + df["second_part"]) 
    df["offrtg_home"] = 100 * (df["pts_home"]/df["home_possessions"])


    # Calculate away offensive rating
    df["second_pt"] = 0.44*df["fta_away"] - df["oreb_away"] + df["tov_away"]
    df["away_possessions"] = (df["fga_away"] + df["second_pt"]) 
    df["offrtg_away"] = 100 * (df["pts_away"]/df["away_possessions"])

    # Calculate true shooting percentage for both sides
    df["ts_home"] = df["pts_home"] / (2 * (df["fga_home"] + 0.44 * df["fta_home"]) )
    df["ts_away"] = df["pts_away"] / (2 * (df["fga_away"] + 0.44 * df["fta_away"]) )

    df = pd.DataFrame([df])

    features = [
        "fg_pct_home", "fg3_pct_home", "oreb_home", "dreb_home", "reb_home", "ast_home", "stl_home", 
        "blk_home", "tov_home", "offrtg_home", "ts_home",

        "fg_pct_away", "fg3_pct_away", "oreb_away", "dreb_away", "reb_away", "ast_away", "stl_away", 
        "blk_away", "tov_away", "offrtg_away", "ts_away"
    ]

    x = df[features]
    
    # Scale x as the model was also scaled
    scaler = joblib.load("app/model/scaler2.pkl")
    model = joblib.load("app/model/logreg_model2.pkl")

    x_scaled = scaler.transform(x)
    home_winner = model.predict(x_scaled)[0]

    return {
        "home_winner": bool(home_winner),
        "predicted_winner": team_name1 if home_winner == 1 else team_name2,
        "stats": x.iloc[0].to_dict()
        }