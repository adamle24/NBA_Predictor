from fastapi import APIRouter, HTTPException
from app.db import get_db_connection

router = APIRouter()

@router.get("/{team_name}")
def get_players(team_name: str):
    con = get_db_connection()
    cursor = con.cursor()

    query = 'SELECT * FROM "Player Per Game" WHERE tm = ? AND season = 2025'

    # Convert team name to all capital
    team_name = team_name.upper()
    cursor.execute(query, (team_name,))

    rows = cursor.fetchall()
    con.close()

    if rows is None:
        raise HTTPException(status_code=404)
    
    return [dict(row) for row in rows]