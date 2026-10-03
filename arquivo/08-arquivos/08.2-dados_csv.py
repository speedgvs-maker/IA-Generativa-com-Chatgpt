import csv

dados_tabela = [
    ["Nome", "Cargo", "Idade" "Linguagem de programação"],
    ["Iago", "dev", 26, "Python"],
    ["Sofia", "Analista de Cibersegurança", 24],
    ["Nicolly", "Desenvolvedora front end", 26],
]

with open("08.2-funcionarios.csv", "w" ,encoding="utf-8" ,newline="") as arquivo_csv:
    escrever = csv.writer(arquivo_csv)
    escrever.writerows(dados_tabela)
    print(escrever)

