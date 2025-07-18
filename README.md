<pre>
<h1>🥋 Bout Maker: MMA Tournament Simulator</h1>

<p>A Python script to simulate MMA-style tournament matchups based on weight classes and age groups. Fighters are entered with basic info, grouped into brackets, and matched manually — with medals awarded based on wins.</p>

<h2>🚀 Features</h2>
• Weight Class Assignment (Flyweight to Heavyweight)  
• Age Group Division (Under 16, Under 18, 18+)  
• Smart grouping of fighters into brackets (default: 5 per group)  
• Medals awarded based on performance (Gold, Silver, Bronze)  
• Ranked results for the entire tournament  

<h2>🔧 How It Works</h2>
<b>Input Fighters:</b> Name, weight, age, training experience, and fight history  
<b>Auto Classification:</b> Fighters are classified by age group and weight class  
<b>Bout Simulation:</b> Fighters in each group fight up to 4 matches, winners entered manually  
<b>Medal Distribution:</b> Top 3 in each group receive medals  
<b>Final Ranking:</b> All fighters are listed by total wins and losses  

<h2>🖥️ Running the Code</h2>
To run the program, execute:  
<code>python mma_tournament.py</code>  
You’ll be prompted to enter fighter information, and for each match, input the winner’s name.

<h2>✍️ Example Interaction</h2>
Enter the number of fighters: 4  
Enter fighter's name: Ayaan  
Enter weight in kg: 68.5  
Enter number of months trained: 12  
Enter age: 18  
Enter number of fights fought: 3  

Match: Ayaan vs Zaid  
Enter the winner of Ayaan vs Zaid: Zaid  

<h2>🧠 Weight Class Categories</h2>
<table border="1">
  <tr><th>Class</th><th>Weight (kg)</th></tr>
  <tr><td>Flyweight</td><td>&lt; 56.7</td></tr>
  <tr><td>Bantamweight</td><td>&lt; 61.2</td></tr>
  <tr><td>Featherweight</td><td>&lt; 65.8</td></tr>
  <tr><td>Lightweight</td><td>&lt; 70.3</td></tr>
  <tr><td>Welterweight</td><td>&lt; 77.1</td></tr>
  <tr><td>Middleweight</td><td>&lt; 83.9</td></tr>
  <tr><td>Light Heavyweight</td><td>&lt; 93.0</td></tr>
  <tr><td>Heavyweight</td><td>&ge; 93.0</td></tr>
</table>

<h2>🎂 Age Groups</h2>
• Under 16  
• Under 18  
• 18 or Above  

<h2>📁 File Structure</h2>
mma_tournament.py   — Main logic for bout creation and result processing  
README.md           — Documentation  

<h2>💡 Ideas for Future Enhancements</h2>
🤖 Auto-decide winners based on skill stats or probabilities  
📈 Export results to Excel/CSV  
🌐 Add GUI or web interface (using Streamlit or Flask)  
🧠 Use AI to generate match outcomes or predict rankings  

<h2>📜 License</h2>
This project is open source under the <b>MIT License</b>.

<h2>🤝 Contributing</h2>
Pull Requests and forks are welcome! This project can grow into a full-featured fight bracket simulator for martial arts tournaments or gaming leagues.
</pre>
