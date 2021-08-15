import pandas as pd 
import plotly.graph_objects as pg 

df  = pd.read_csv("c-107csv.csv")
studentdf = df.loc[df["student_id"] == "TRL_abc"]
groupmean = studentdf.groupby("level")["attempt"].mean()
graph = pg.Figure(pg.Bar(x=["Level 1","Level 2","Level 3","Level 4"], y=groupmean))
graph.show()