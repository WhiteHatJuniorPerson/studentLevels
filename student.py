import pandas as pd 
import plotly.graph_objects as pg

df = pd.read_csv("c-107csv.csv")
groupmean  = df.groupby("level")["attempt"].mean()
print(groupmean)
graph = pg.Figure(pg.Bar(x=["Level 1","Level 2","Level 3","Level 4"], y =groupmean))
graph.show()


