import plotly.express as px

generos={
    "Drama": 30,
    "Suspense": 8,
    "Comédia": 52,
    "Aventura": 15
}

fig = px.pie(
    names=generos.keys(),
    values=generos.values(),
    title="Gráfico: Filmes por gênero"
)

fig.show()