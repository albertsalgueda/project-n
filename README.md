# project-n

------ FEEDBACK ----

Recomano fer servir pandas per llegir el csv i interactuar amb les dades. 
Exemple
`
import pandas as pd
file_path = "data.csv"
data = pd.read_csv(file_path)
`
Això crea un objecte que es diu pandas dataframe. Molt ràpid i fàcil de fer servir amb plotly, dash i altres llibreries de Data Science com TF...

Bona feina!
---------------------

 ## Concepte
 Visualitzar una posició tridimensional en una gràfica

 ## Calculs adicionals
Calcular la velocitat

## Visualització
El gràfic ha de veure's en una pagina web

## Passos a seguir
### 1 DONE
Github setup
### 2
Funcio per guardar punt
Fem servir import random, usant un range concret
exemple: posicio actual * index amb uns valors possibles maxims i minims
### 3
Funcio per guardar .csv
### 4
LLegir l'archiu csv i fer una grafica
import pandas as pd
pc.reac_csv(path)  : exemple de funcio d'us de csv com a dades per a un grafic
### 5
Funcio per calcular la velocitat
Importat el temps time.time()
Amb el temps i la variació de posició podem calcular la velocitat
### 6
Render
Plotly (minimo)         https://dash.gallery/dash-wind-streaming/
Dash   (objectivo chad) https://dash.gallery/dash-world-cell-towers/
                        https://dash.gallery/dash-opioid-epidemic/
                        https://dash.gallery/Portal/
