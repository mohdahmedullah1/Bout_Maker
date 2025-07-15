# Bout_Maker
A Python script to simulate MMA-style tournament matchups based on weight classes and age groups. Fighters are entered with basic info, grouped into brackets, and matched manually — with medals awarded based on wins.

Features
Weight Class Assignment (Flyweight to Heavyweight)
Age Group Division (Under 16, Under 18, 18+)
Smart grouping of fighters into brackets (default: 5 per group)
Medals awarded based on performance (Gold, Silver, Bronze)
Ranked results for the entire tournament
How It Works
Input Fighters: Name, weight, age, training experience, and fight history
Auto Classification: Fighters are classified by age group and weight class
Bout Simulation: Fighters in each group fight up to 4 matches, winners entered manually
Medal Distribution: Top 3 in each group receive medals
Final Ranking: All fighters are listed by total wins and losses
Running the Code
python mma_tournament.py
You'll be prompted to enter fighter information, and for each match, input the winner's name.

  Example Interaction
Enter the number of fighters: 4
Enter fighter's name: Ayaan
Enter weight in kg: 68.5
Enter number of months trained: 12
Enter age: 18
Enter number of fights fought: 3

Match: Ayaan vs Zaid
Enter the winner of Ayaan vs Zaid: Zaid
Weight Class Categories
Class	Weight (kg)
Flyweight	< 56.7
Bantamweight	< 61.2
Featherweight	< 65.8
Lightweight	< 70.3
Welterweight	< 77.1
Middleweight	< 83.9
Light Heavyweight	< 93.0
Heavyweight	≥ 93.0
Age Groups
Under 16
Under 18
18 or Above
  File Structure
mma_tournament.py   # Main logic for bout creation and result processing
README.md           # Documentation
Ideas for Future Enhancements
Auto-decide winners based on skill stats or probabilities
Export results to Excel/CSV
Add GUI or web interface (using Streamlit or Flask)
Use AI to generate match outcomes or predict rankings
License
This project is open source under the MIT License.

-- Contributing
PRs and forks are welcome! This project can grow into a full-featured fight bracket simulator for martial arts tournaments or gaming leagues.
