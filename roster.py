import pandas as pd 

roster = ["High", "Cadeau", "Ryan", "Davis", "Bacot", "Trimble", "Wojcik", "Washington", "Leo", "Landry"]
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)