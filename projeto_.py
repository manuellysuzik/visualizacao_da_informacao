import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly as py
import matplotlib.pyplot as plt

# ---------------BARRAS
paises = ['Noruega', 'Brasil', 'República Centro-Africana']

rank = [0.949, 0.754, 0.352]
plt.bar(paises, rank, color=['green', 'lightblue', 'red'], edgecolor='black')
plt.ylabel('Países', color='red')
plt.xlabel('IDH', color='red')
plt.title('Comparativo entre maior e o menor IDH no mundo com o Brasil')

plt.show()

# ---------------LINHAS
continentes = ['Noruega', 'Brasil', 'República Centro-Africana']
anos = ['1990-2000', ' 2000-2010', '2010-2015']

noruega = [0.77, 0.24, 0.21]
RCA = [-0.19, 1.41, -0.47]
Brasil = [1.15, 0.55, 0.83]

plt.plot(anos, noruega, "o-", color='blue')
plt.plot(anos, Brasil, "o-", color='red')
plt.plot(anos, RCA, "o-", color='orange')
plt.xticks(anos)
plt.title('Média de crescimento anual')
plt.ylabel('Média em Anos', color='red')
plt.legend(continentes, loc=3)
plt.grid(True)

plt.show()

df = pd.read_csv(r'C:/Users/manun/Desktop/projeto/HDI.csv')

paises = df.Country
IDH = df.HDI

fig = go.Figure(data=go.Choropleth(
 locations=paises ,# Nome do país
 z = IDH ,# Dados para o Choropleth
 locationmode = 'country names', # Tipo de identificção geográfica
 colorscale = 'RdBu', #escala contínua em tons de vermelho
 colorbar_title = "IDH",
))

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)
