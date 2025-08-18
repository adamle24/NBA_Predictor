from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

def preprocess(df):

    # Convert wl_home to 1/0 for won/lose at home
    df["wl_home"] = df["wl_home"].replace({"W": 1, "L":0}) 

    # Calculate offensive rating
    df["second_part"] = 0.4*df["fta_home"] - df["oreb_home"] + df["tov_home"]
    df["home_possessions"] = (df["fga_home"] + df["second_part"]) / 2
    df["offrtg_home"] = 100 * (df["pts_home"]/df["home_possessions"])


    # Calculate away offensive rating
    df["second_pt"] = 0.4*df["fta_away"] - df["oreb_away"] + df["tov_away"]
    df["away_possessions"] = (df["fga_away"] + df["second_pt"]) / 2
    df["offrtg_away"] = 100 * (df["pts_away"]/df["away_possessions"])

    # Calculate true shooting percentage for both sides
    df["ts_home"] = df["pts_home"] / (2 * (df["fga_home"] + 0.44 * df["fta_home"]) )
    df["ts_away"] = df["pts_away"] / (2 * (df["fga_away"] + 0.44 * df["fta_away"]) )

    features = [
        "fg_pct_home", "fg3_pct_home", "oreb_home", "dreb_home", "reb_home", "ast_home", "stl_home", 
        "blk_home", "tov_home", "offrtg_home", "ts_home",

        "fg_pct_away", "fg3_pct_away", "oreb_away", "dreb_away", "reb_away", "ast_away", "stl_away", 
        "blk_away", "tov_away", "offrtg_away", "ts_away"
    ]

    x = df[features]

    # Handle missing data
    imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
    imputer = imputer.fit(x)
    x = imputer.transform(x)
    
    y = df["wl_home"]

    # Normalize data for logistic regression model
    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    return x, y, scaler