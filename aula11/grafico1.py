import plotly.express as px

cursos = {
    "ADS": 30,
    "Redes": 12,
    "Marketing": 20,
    "PMM": 8,
    "PG": 23
}

fig = px.bar(
    x=cursos.keys(),
    y=cursos.values(),
    title="Grafico: Nº Alunos por curso"
)

fig.show()