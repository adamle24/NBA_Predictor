from fastapi import APIRouter
from app.db import get_db_connection

router = APIRouter()

@router.get("/{player_name}")
def get_player(player_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = 'SELECT * FROM "Player per Game" WHERE player = ? and season = 2025'
    
    # replace dash with a space to match name in the database
    player_name = player_name.replace("-", " ")

    cursor.execute(query, (player_name,))
    row = cursor.fetchone()
    conn.close()

    return dict(row)