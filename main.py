from data import nbadata
from compare_model import StatsBrain
from stat_organizer import ComparisonOrganizer

categories = ['Player', 'Team', 'G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT'
    , 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS▼', 'Trp-Dbl']

stats = []
for data in nbadata:
    player = data['Player']
    pts = data['PTS▼']
    stats.append(ComparisonOrganizer(player, pts))


nbagame = StatsBrain(stats)


nbagame.next_comparisons()
final_score = (nbagame.score/nbagame.attempts) * 100

print('\n')
print(f"You completed the Game!")
print(f"Your final score is: {nbagame.score}/{nbagame.attempts}")
print(f"You got {final_score}% of questions correct!")


