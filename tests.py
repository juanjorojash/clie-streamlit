import pandas as pd

areas = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/areas.csv")
cursos = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/cursos/cursos_malla.csv")
rasgos = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/rasgos.csv")
saberes = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/saberes.csv")
cursos_rasgos = pd.read_csv("https://raw.githubusercontent.com/EIEM-TEC/CLIE/refs/heads/main/cursos/cursos_rasgos.csv")

nomArea = areas["nombre"].head(1).item()



codArea = areas[areas["nombre"]==nomArea]["codArea"].item()
saberes = saberes[saberes["codArea"]==codArea]

#"Codigo de area:", codArea

nomCurso = cursos[cursos["area"]==codArea]["nombre"].head(1).item()

codCurso = cursos[cursos["nombre"]==nomCurso]["codigo"].item()
idCurso = cursos[cursos["nombre"]==nomCurso]["id"].item()

codSaber = cursos_rasgos[cursos_rasgos["id"]==idCurso]["codSaber"].str.split(';', expand=False).item()

for index in range(len(codSaber)):
    print(codSaber[index])



