import time
import pandas as pd
import matplotlib.pyplot as plt
#https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html
import plotly.express as px
#https://plotly.com/python/plotly-express/

file_path = "archivo.csv"

def main():
    data = pd.read_csv(file_path)
    data.head()
    #print(data.tail(2))
    data.plot()
    fig = px.line_3d(data, x="x",y="y",z="z")   
    fig.show()

if __name__ == "__main__":
    main()
    