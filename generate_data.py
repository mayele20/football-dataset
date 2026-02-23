import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration
np.random.seed(42)
random.seed(42)

# Listes de données réalistes
leagues = ['Premier League', 'La Liga', 'Serie A', 'Bundesliga', 'Ligue 1']
countries = ['England', 'Spain', 'Italy', 'Germany', 'France']

teams_by_league = {
    'Premier League': ['Manchester United', 'Liverpool', 'Chelsea', 'Arsenal', 'Manchester City', 
                       'Tottenham', 'Everton', 'Leicester City', 'West Ham', 'Newcastle'],
    'La Liga': ['Real Madrid', 'Barcelona', 'Atletico Madrid', 'Sevilla', 'Valencia', 
                'Villarreal', 'Real Sociedad', 'Athletic Bilbao', 'Real Betis', 'Getafe'],
    'Serie A': ['Juventus', 'AC Milan', 'Inter Milan', 'Roma', 'Napoli', 
                'Lazio', 'Atalanta', 'Fiorentina', 'Torino', 'Sassuolo'],
    'Bundesliga': ['Bayern Munich', 'Borussia Dortmund', 'RB Leipzig', 'Bayer Leverkusen', 'Wolfsburg',
                   'Eintracht Frankfurt', 'Borussia Monchengladbach', 'Stuttgart', 'Hoffenheim', 'Mainz'],
    'Ligue 1': ['PSG', 'Marseille', 'Lyon', 'Monaco', 'Lille', 
                'Nice', 'Rennes', 'Lens', 'Montpellier', 'Strasbourg']
}

# Générer les matchs
matches_data = []
match_id = 1

seasons = ['2018/2019', '2019/2020', '2020/2021', '2021/2022', '2022/2023', '2023/2024']

for season in seasons:
    year = int(season.split('/')[0])
    start_date = datetime(year, 8, 1)
    
    for league, country in zip(leagues, countries):
        teams = teams_by_league[league]
        
        # Chaque équipe joue contre chaque autre équipe 2 fois (domicile et extérieur)
        for i, home_team in enumerate(teams):
            for j, away_team in enumerate(teams):
                if i != j:
                    # Générer une date aléatoire dans la saison
                    days_offset = random.randint(0, 270)
                    match_date = start_date + timedelta(days=days_offset)
                    
                    # Générer des scores réalistes
                    # L'équipe à domicile a un léger avantage
                    home_goals = np.random.poisson(1.5)
                    away_goals = np.random.poisson(1.2)
                    
                    matches_data.append({
                        'match_id': match_id,
                        'league': league,
                        'country': country,
                        'season': season,
                        'date': match_date.strftime('%Y-%m-%d'),
                        'home_team': home_team,
                        'away_team': away_team,
                        'home_team_goal': home_goals,
                        'away_team_goal': away_goals
                    })
                    
                    match_id += 1

# Créer le DataFrame
df = pd.DataFrame(matches_data)

# Sauvegarder
df.to_csv('/home/claude/football_project/matches.csv', index=False)

print(f"✅ Dataset créé avec {len(df)} matchs")
print(f"📊 Saisons : {df['season'].unique()}")
print(f"🏆 Ligues : {df['league'].unique()}")
print(f"⚽ Nombre total de buts : {df['home_team_goal'].sum() + df['away_team_goal'].sum()}")
