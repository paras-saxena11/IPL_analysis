import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('matches.csv')
ipl_df.info()
ipl_df.shape
# The .describe method gives us the overview of our data i.e data in rows and columns
ipl_df.describe()
ipl_df

ipl_df.drop(columns=['umpire1', 'umpire2', 'umpire3'], inplace=True)

ipl_df.columns

ipl_df.Season.unique()

ipl_df.team1.unique()
ipl_df.city.unique()
# We will use the .replace() method for the above mentioned cleaning
ipl_df.team1.replace({'Rising Pune Supergiants': 'Rising Pune Supergiant',
                     'Delhi Daredevils': 'Delhi Capitals', 'Pune Warriors': 'Rising Pune Supergiant'}, inplace=True)
ipl_df.team2.replace({'Rising Pune Supergiants': 'Rising Pune Supergiant',
                     'Delhi Daredevils': 'Delhi Capitals', 'Pune Warriors': 'Rising Pune Supergiant'}, inplace=True)
ipl_df.toss_winner.replace({'Rising Pune Supergiants': 'Rising Pune Supergiant',
                           'Delhi Daredevils': 'Delhi Capitals', 'Pune Warriors': 'Rising Pune Supergiant'}, inplace=True)
ipl_df.winner.replace({'Rising Pune Supergiants': 'Rising Pune Supergiant',
                      'Delhi Daredevils': 'Delhi Capitals', 'Pune Warriors': 'Rising Pune Supergiant'}, inplace=True)
ipl_df.city.replace({'Bangalore': 'Bengaluru'}, inplace=True)
ipl_df.team1.unique()
ipl_df.team2.unique()
ipl_df.city.unique()
# we can use .isnull() to set Null values to True and then use .sum() to calculate all the null values
ipl_df.isnull().sum().sum()
null_df = ipl_df[ipl_df.isna().any(axis=1)]
print(null_df)
ipl_df.loc[460:470]
ipl_df.loc[[461, 462, 466, 468, 469, 474, 476], 'city'] = "Dubai"
# Lets See the Changed Values
ipl_df.loc[461:480]
# Now lets Confirm if we have any NaN values in City Field
ipl_df.city.isnull().any()
# Lets Check if any any other COlumns Have NaN values
ipl_df.isna().any()[lambda x: x]
# Lets find total Number of Matches Played from 2008 - 2019
ipl_df.id.count()


# YAHA SE M BOLRA HU
# Now Lets Find Total Number Of Matches Where Result Was normal i.e Not A Tie
regular_matches = ipl_df[ipl_df.result == 'normal'].count()
regular_matches.result

winner_df = ipl_df.groupby('winner')[['id']].count()
winner_df = winner_df.sort_values('id', ascending=False).reset_index()
winner_df.rename(columns={'id': 'wins', 'winner': 'Teams'}, inplace=True)
print(winner_df)

# Plotting Wins vs Teams
# We will be using colour code of teams jersey to make it easily understandable
plt.figure(figsize=(20, 10))
plt.legend(winner_df.Teams, loc=1)
plt.xlabel('Teams', fontsize=10)
plt.ylabel('Wins', fontsize=10)
plt.tick_params(labelsize=20)
plt.xticks(rotation=90)
plt.title('Matches Won By Each Team', fontweight='bold', fontsize=30)
plt.bar(winner_df.Teams, winner_df.wins, color=['blue', '#FFD801', '#461B7E', '#C11B17',
        '#F660AB', '#000080', '#F535AA', '#F87217', '#BCC6CC', '#2C04A2', '#E04F16', '#632B72'])

# YAHA TAK M BOLRA HU

season_df = ipl_df.groupby('Season')[['id']].count()
season_df = season_df.sort_values('Season', ascending=False).reset_index()
season_df.rename(columns={'id': 'Matches', 'Season': 'Year'}, inplace=True)
print(season_df)

plt.figure(figsize=(20, 10))
plt.title("Mathes Played In Each Season", fontweight='bold', fontsize=30)
plt.xlabel('Season', fontweight='bold', fontsize=30)
plt.ylabel('Total Matches', fontweight='bold', fontsize=30)
plt.xticks(rotation='60')
plt.tick_params(labelsize=20)
plt.bar(season_df.Year, season_df.Matches, color=['#98AFC7', '#6D7B8D'])

ipl_df


# We can see toss decision is either bat/field
ipl_df.toss_decision.unique()
decision_df = ipl_df.groupby('toss_decision')[['id']].count()
decision_df = decision_df.sort_values('id').reset_index()
decision_df.rename(
    columns={'id': 'Total', 'toss_decision': 'Decision'}, inplace=True)
print('The most preferres decision on winning toss')
print(decision_df)


field_df = ipl_df.loc[(ipl_df['toss_winner'] == ipl_df['winner']) & (
    ipl_df['toss_decision'] == 'field'), ['id', 'winner', 'toss_decision']]
field_df.winner.count()
bat_df = ipl_df.loc[(ipl_df['toss_winner'] == ipl_df['winner']) & (
    ipl_df['toss_decision'] == 'bat'), ['id', 'winner', 'toss_decision']]
bat_df.winner.count()
frames = [bat_df, field_df]
result_df = pd.concat(frames)
result_df = result_df.groupby('toss_decision')[['id']].count()
print('Which Decision has proved most beneficial i.e Field / Bat')
print(result_df)
print('The Most Preferred Decision After Winning Toss in the IPL Until 2019 has been "Choose to Field First"')
# As from Earlier Analysis we know out of 756 Toss that were tossed (2008 - 2019) "463 times toss winning Team Choose to Field First" and only "293 Times batting was choosen"
# Plot the New Understanding Regarding the Success of these decisions
result_df = result_df.sort_values('id').reset_index()
result_df.rename(
    columns={'id': 'Total', 'toss_decision': 'Decision'}, inplace=True)
result_df

# How many venues have hosted the Ipl Matches
ipl_df.venue.unique()
total_venue = list(ipl_df.venue.unique())
len(total_venue)
venue_df = ipl_df.groupby('venue')[['id']].count()
venue_df = venue_df.sort_values('id', ascending=False).reset_index()
venue_df.rename(columns={'id': 'Total', 'venue': 'Stadium'}, inplace=True)
labels = list(venue_df.Stadium)
print('Venue hosted the Most Number Of Matches')
print(venue_df)
plt.figure(figsize=(20, 20))
plt.title("Venues", fontweight='bold', fontsize=30)
plt.tick_params(labelsize=40)
plt.pie(venue_df.Total, labels=labels, textprops={'fontsize': 5})

# How many players have been awarded with player of the match award
len(ipl_df.player_of_match.unique())
player_df = ipl_df.groupby('player_of_match')[['id']].count()
player_df
player_df = player_df.sort_values('id', ascending=False).reset_index()
player_df
players_df = player_df.head(10).copy()
players_df.rename(columns={'id': 'Total_Awards',
                  'player_of_match': 'Man_Of_The_Match'}, inplace=True)
print(players_df)
plt.figure(figsize=(15, 8))
plt.title("Top 10 Players with Highest Man Of the Match Titles", fontweight='bold')
plt.xticks(rotation=90)
plt.yticks(ticks=np.arange(0, 25, 5))
plt.ylabel('No. of Awards')
plt.xlabel('Players')
x = players_df["Man_Of_The_Match"]
y = players_df["Total_Awards"]
plt.bar(x, y, color=("#40ff00", "#00ffbf", "#ff0000", "#ffff00",
        "#00ff00", "#4000ff", "#ff0000", "#bf00ff", "#00ffbf", "#00ffbf"))

final_df = ipl_df.groupby('Season').tail(1).copy()
final_df
# Sort The Data According to Seasons
final_df = final_df.sort_values('Season')
final_df
final_df.winner.unique()
dict1 = y.to_dict()

dd = dict1.keys()

ss = list(dd)

ff = dict1.values()

gg = list(ff)
print('Season Champions')
print(final_df['winner'].value_counts())
plt.figure(figsize=(20, 10))
plt.title("Season Champions", fontweight='bold', fontsize=20)
plt.xlabel('Teams', fontweight='bold', fontsize=30)
plt.ylabel('Total Seasons', fontweight='bold', fontsize=20)
plt.xticks(rotation='60')
plt.tick_params(labelsize=8)
# sns.countplot(x=final_df['winner'],palette=['#F535AA','#BCC6CC','yellow','#461B7E','blue','#F87217']);
plt.bar(ss, gg, color=['#F535AA', '#BCC6CC',
        'yellow', '#461B7E', 'blue', '#F87217'])

plt.show()
