from fastapi import APIRouter 
from app.injury_scraper import scrape_nba_injuries

router = APIRouter()

@router.get("/")
def get_injuries():
    return scrape_nba_injuries()