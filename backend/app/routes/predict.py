from fastapi import APIRouter
from app.injury_scraper import scrape_nba_injuries
from app.db import get_db_connection
from app.routes.players import get_players
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

router = APIRouter()

@router.get("/{team_name1}-{team_name2}")
def getPredict(team_name1: str, team_name2: str):

    team_name1 = team_name1.upper()
    team_name2 = team_name2.upper()

    conn = get_db_connection()
    cursor = conn.cursor()

    # Get team stats per game for both sides
    query = 'SELECT * FROM "Team Stats Per Game" WHERE abbreviation = ?' 

    cursor.execute(query, (team_name1,))
    home_team = cursor.fetchone()

    cursor.execute(query, (team_name2,))
    away_team = cursor.fetchone()

    conn.close()

    # Convert home and away to dictionaries for easier manipulation
    home_team = dict(home_team)
    away_team = dict(away_team)

    # Prep the data to be put into logistic regression model
    df = {
        "fg_pct_home": home_team.get("fg_percent", 0),
        "fg3_pct_home": home_team.get("x3p_percent", 0), 
        "oreb_home": home_team.get("orb_per_game", 0), 
        "dreb_home": home_team.get("drb_per_game", 0), 
        "reb_home": home_team.get("trb_per_game", 0),
        "ast_home": home_team.get("ast_per_game", 0),
        "stl_home": home_team.get("stl_per_game", 0), 
        "blk_home": home_team.get("blk_per_game", 0),
        "tov_home": home_team.get("tov_per_game", 0),
        # input the away teams
        "fg_pct_away": away_team.get("fg_percent", 0),
        "fg3_pct_away": away_team.get("x3p_percent", 0), 
        "oreb_away": away_team.get("orb_per_game", 0), 
        "dreb_away": away_team.get("drb_per_game", 0), 
        "reb_away": away_team.get("trb_per_game", 0),
        "ast_away": away_team.get("ast_per_game", 0),
        "stl_away": away_team.get("stl_per_game", 0), 
        "blk_away": away_team.get("blk_per_game", 0),
        "tov_away": away_team.get("tov_per_game", 0),
    }

    df["fta_home"] = home_team.get("fta_per_game", 0)
    df["fga_home"] = home_team.get("fga_per_game", 0)
    df["pts_home"] = home_team.get("pts_per_game", 0)

    df["fta_away"] = away_team.get("fta_per_game", 0)
    df["fga_away"] = away_team.get("fga_per_game", 0)
    df["pts_away"] = away_team.get("pts_per_game", 0)

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