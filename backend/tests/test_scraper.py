from app.injury_scraper import scrape_nba_injuries

def test_scraper():
    injuries = scrape_nba_injuries()
    assert isinstance(injuries, list)  # The function should return a list
    assert len(injuries) > 0  # Should contain injury reports
    assert all("player_name" in i for i in injuries)  # Each entry should have 'player_name'