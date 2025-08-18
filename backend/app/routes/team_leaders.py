from fastapi import APIRouter, HTTPException
from app.db import get_db_connection

router = APIRouter()

stat_cats = ["PTS", "AST", "REB", "STL", "BLK", "3PT"]

def get_stat_value(player, stat):
    mapping = {
        "PTS" : ["pts_per_game", "PTS"],
        "AST" : ["ast_per_game", "AST"],
        "REB" : ["trb_per_game", "REB"],
        "STL" : ["stl_per_game", "STL"],
        "BLK" : ["blk_per_game", "BLK"],
        "3PT" : ["x3p_per_game", "3PT"],
    }

    for col in mapping.get(stat, []):
        if col in player and player[col] is not None:
            try:
                return float(player[col])
            except (ValueError, TypeError):
                return 0
    return 0

def get_leader(players, stat):
    def key(p):
        return get_stat_value(p, stat)

    top = max(players, key=key, default=None)
    if not top:
        return None

    value = get_stat_value(top, stat)

    return {
        "name": top.get("player"),
        "value": round(value, 3),
        "team": top.get("tm"),
        "position": top.get("pos"),
    }

@router.get("/leaders/{team_name}")
def get_team_leaders(team_name: str):
    con = get_db_connection()
    cursor = con.cursor()

    query = 'SELECT * FROM "Player Per Game" WHERE tm = ? AND season = 2025 AND mp_per_game > 10'

    # Convert team name to all capital
    team_name = team_name.upper()
    cursor.execute(query, (team_name,))

    rows = cursor.fetchall()

    if not rows:
        raise HTTPException(status_code=404)

    players = [dict(row) for row in rows]
    leaders = { stat: get_leader(players, stat) for stat in stat_cats }

    con.close()
    
    return leaders