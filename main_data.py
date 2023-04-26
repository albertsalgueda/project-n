import points_3d as points
import Write as wr
import time as time
import Read as rd

#PARAMETRES_2
hora_inici = time.time()
posicio_actual_temporal = [0,0,0,0]
pasos = 4
pas_maxim = 20
interval = 1

#TEMPS INICI
t_inici = time.time()

def main():
    punt = posicio_actual_temporal
    for i in range(pasos):
        punt = points.fer_pas_temporal(punt, hora_inici, pas_maxim)
        wr.functiondades(punt)
        time.sleep(interval)

def main_infinite():
    punt = posicio_actual_temporal
    while True:
        punt = points.fer_pas_temporal(punt, hora_inici, pas_maxim)
        wr.functiondades(punt)
        time.sleep(interval)


if __name__ == "__main__":
    #main()
    main_infinite()
    
    
    """
    import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random

# Inicializa la Dash APP

app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Graph(id='live-graph', animate=True),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # Intervalo en milisegundos (1 segundo)
        n_intervals=0
    )
])

@app.callback(Output('live-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph(n):
    # Simula datos en tiempo real
    x = list(range(10))
    y = [random.randint(1, 10) for _ in range(10)]

    # Crea el gráfico con los datos actualizados
    data = go.Scatter(
        x=x,
        y=y,
        mode='lines+markers'
    )

    return {'data': [data],
            'layout': go.Layout(xaxis=dict(range=[min(x), max(x)]),
                                yaxis=dict(range=[min(y), max(y)]))}

if __name__ == '__main__':
    app.run_server(debug=True)
"""
