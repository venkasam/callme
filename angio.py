import csv
import plotly.express as px 
import pandas as pd
import plotly.graph_objects as go

a=pd.read_csv("io.csv")
b=a.loc[a["student_id"]=="TRL_987"]
print(b.groupby("level")["attempt"].mean())
h=go.Figure(go.Bar(x=b.groupby("level")["attempt"].mean(),y=["Level 1","Leve 2","Level 3","Level 4"],orientation="h"))
h.show()
