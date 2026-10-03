funcionarios = {
    101: {
        "nome": "Iago",
        "cargo": "Desenvolvedor",
        "habilidades": ["Python", "C##", "PHP"]
    },
    102: {
        "nome": "Sofia",
        "cargo": "gerente de projetos",
        "habilidades": ["Scrum", "Gestão"]
    }
}

print(funcionarios[101]["cargo"])
print(funcionarios.get(102,{}).get("nome"))