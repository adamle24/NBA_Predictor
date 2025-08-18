from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.routes import player, players, predict, recent_predict, team_leaders

app = FastAPI(title="NBA Predictor")

# CORS between frontend and backend 
origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
    "https://nbapredictor.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player.router, prefix="/player", tags=["Player"])
app.include_router(players.router, prefix="/players", tags=["Players"])
app.include_router(predict.router, prefix="/predict", tags=["Prediction"])
app.include_router(recent_predict.router, prefix="/recentpredict", tags=["Predict"])
app.include_router(team_leaders.router, prefix="/team", tags=["Leaders"])