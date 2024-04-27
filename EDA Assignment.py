#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


MD = pd.read_excel("Data/data.xlsx", sheet_name = 'Matches Data')
PTM = pd.read_excel("Data/data.xlsx", sheet_name = 'Player Team Mapping')


# In[3]:


PTM.rename(columns={'Player Name':'player_name'}, inplace=True)


# In[4]:


DF = pd.merge(MD,PTM, on='player_name', how='left')


# In[5]:


DF


# In[6]:


DF.isnull().sum()


# In[7]:


DF.dropna(inplace=True)


# In[8]:


DF.info()


# In[9]:


DF.head(10)


# In[10]:


DF.set_index("index").head(10)


# In[11]:


DF['match_date']=pd.to_datetime(DF['match_date'])
Filter_data = DF[DF['opposing_team'].isin(['Australia', 'New Zealand', 'England'])]
Filter_data = Filter_data[(Filter_data['match_date'].dt.year >= 2000) & (Filter_data['match_date'].dt.year <= 2022)]
Indian_Players = Filter_data[Filter_data['Team']=='India']
indian_players_runs = indian_players.groupby('player_name')['runs_scored'].sum().reset_index()
indian_players_runs = indian_players_runs.sort_values(by='runs_scored', ascending=False)
top_2_indian_players = indian_players_runs.head(2)
print(top_2_indian_players[['player_name', 'runs_scored']])


# In[ ]:


DF['match_date'] = pd.to_datetime(DF['match_date'], format='%d-%m-%Y')
indian_bowlers = DF[(DF['player_category'] == 'Bowler') & (DF['Team'] == 'India')]
matches_against_opponents = indian_bowlers[indian_bowlers['opposing_team'].isin(['USA', 'West Indies', 'Sri Lanka'])]
matches_in_period = matches_against_opponents[(matches_against_opponents['match_date'] >= '2000') & (matches_against_opponents['match_date'] <= '2022')]
matches_in_period['wicket_economy'] = matches_in_period['wickets_taken'] / matches_in_period['overs_bowled']
best_bowler = matches_in_period.loc[matches_in_period['wicket_economy'].idxmin()]

print("Best Indian bowler against USA, West Indies, and Sri Lanka combined in 2000–2022:")
print(best_bowler[['player_name', 'wicket_economy']])


# In[ ]:


DF['match_date'] = pd.to_datetime(DF['match_date'], format='%d-%m-%Y')
indian_players = DF[DF['Team'] == 'India']
matches_in_period = indian_players[(indian_players['match_date'] >= '2000') & (indian_players['match_date'] <= '2022')]
matches_in_period['strike_rate'] = matches_in_period['runs_scored'] / matches_in_period['balls_faced']
matches_in_period['wicket_economy'] = matches_in_period['wickets_taken'] / matches_in_period['overs_bowled']
matches_in_period['overall_score'] = (0.66 * matches_in_period['strike_rate']) + (0.34 * matches_in_period['wicket_economy'])
best_player = matches_in_period.loc[matches_in_period['overall_score'].idxmax()]
print("Best Indian player with the highest weighted overall score in years 2000-2022:")
print(best_player[['player_name', 'overall_score']])


# In[ ]:


december_matches = DF[(DF['match_date'].dt.month == 12) & (DF['match_date'].dt.year >= 2010) & (DF['match_date'].dt.year <= 2022)]
australian_players = december_matches[december_matches['Team'] == 'Australia']
english_players = december_matches[december_matches['Team'] == 'England']
december_matches['strike_rate'] = (december_matches['runs_scored'] / december_matches['balls_faced']) * 100
average_strike_rate = december_matches.groupby('Team')['strike_rate'].mean()

if average_strike_rate['Australia'] > average_strike_rate['England']:
    print("Australian players had a better strike rate than England players in December from 2010 to 2022.")
elif average_strike_rate['Australia'] < average_strike_rate['England']:
    print("England players had a better strike rate than Australian players in December from 2010 to 2022.")
else:
    print("Australian and England players had the same strike rate in December from 2010 to 2022.")


# In[ ]:


indian_batsmen = DF[(DF['player_category'] == 'Batsman') & 
                              (DF['Team'] == 'India') & 
                              (DF['match_date'].dt.year >= 2000) & 
                              (DF['match_date'].dt.year <= 2022)]
yearly_runs = indian_batsmen.groupby(indian_batsmen['match_date'].dt.year)['runs_scored'].sum()
mean_yearly_runs = yearly_runs.mean()
variance_yearly_runs = yearly_runs.var()
print("Total runs scored every year by Indian batsmen from 2000 to 2022:")
print(yearly_runs)
print("\nMean yearly runs scored by Indian batsmen from 2000 to 2022:", mean_yearly_runs)
print("Variance of yearly runs scored by Indian batsmen from 2000 to 2022:", variance_yearly_runs)



# In[ ]:


matches_2000_to_2022 = DF[(DF['match_date'].dt.year >= 2000) & 
                                    (DF['match_date'].dt.year <= 2022)]
team_stats = matches_2000_to_2022.groupby('Team').agg({'runs_scored': ['mean', 'std'],
                                                        'wickets_taken': ['mean', 'std']})

team_stats['runs_scored_zscore'] = (team_stats['runs_scored']['mean'] - team_stats['runs_scored']['mean'].mean()) / team_stats['runs_scored']['std']
team_stats['wickets_taken_zscore'] = (team_stats['wickets_taken']['mean'] - team_stats['wickets_taken']['mean'].mean()) / team_stats['wickets_taken']['std']

plt.figure(figsize=(12, 6))
plt.plot(team_stats['runs_scored_zscore'], team_stats['wickets_taken_zscore'], color='blue')
plt.title('Z Scores of Runs Scored vs Wickets Taken by Teams (2000-2022)')
plt.xlabel('Z Score of Runs Scored')
plt.ylabel('Z Score of Wickets Taken')
for team, x, y in zip(team_stats.index, team_stats['runs_scored_zscore'], team_stats['wickets_taken_zscore']):
    plt.annotate(team, (x, y), textcoords="offset points", xytext=(0,10), ha='center')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()


# In[ ]:


matches_2010_to_2022 = DF[(DF['match_date'].dt.year >= 2010) & 
                                     (DF['match_date'].dt.year <= 2022)]

team_percentiles = matches_2010_to_2022.groupby('Team').agg({'runs_scored': lambda x: (x.quantile(0.25), x.quantile(0.5), x.quantile(0.75)),
                                                             'wickets_taken': lambda x: (x.quantile(0.25), x.quantile(0.5), x.quantile(0.75))})

print("Percentile runs scored and wickets taken by all teams from 2010 to 2022:")
for team in team_percentiles.index:
    runs_percentiles = team_percentiles.loc[team, 'runs_scored']
    wickets_percentiles = team_percentiles.loc[team, 'wickets_taken']
    print(f"\nTeam: {team}")
    print("25th percentile runs scored:", runs_percentiles[0])
    print("50th percentile runs scored (median):", runs_percentiles[1])
    print("75th percentile runs scored:", runs_percentiles[2])
    print("25th percentile wickets taken:", wickets_percentiles[0])
    print("50th percentile wickets taken (median):", wickets_percentiles[1])
    print("75th percentile wickets taken:", wickets_percentiles[2])


# In[ ]:


# DS


# In[ ]:


def f(x, y):
    return x * y**2 * np.sin(x) + 2 * x**3 * np.cos(y)

result = f(1, 1)
print("f(1, 1) =", result)


# In[ ]:


def f(x, y):
    return x * y**2 * np.sin(x) + 2 * x**3 * np.cos(y)

def gradient_f(x, y):
    df_dx = lambda x, y: y**2 * (np.sin(x) + x * np.cos(x)) + 6 * x**2 * np.cos(y)
    df_dy = lambda x, y: 2 * x * y * np.sin(x) - 2 * x**3 * np.sin(y)
    
    grad_x = df_dx(x, y)
    grad_y = df_dy(x, y)
    
    return (grad_x, grad_y)

# put the gradient of f(0, 1)
gradient = gradient_f(0, 1)
print("Gradient of f(0, 1) =", gradient)


# In[ ]:


# Given data
weights = np.array([50, 65, 89, 55, 77, 49, 66, 72, 79, 67])
heights = np.array([171, 165, 195, 154, 161, 151, 163, 178, 183, 185])

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(heights, weights)[0, 1]

print("Correlation Coefficient between height and weight:", correlation_coefficient)


# In[ ]:





# In[ ]:




