
cadastros = [
{
        "id":1042,
        "perfil":{
            "nome": "Beatriz Souza",
            "email": "beatrizsouza@gmail.com"
    }
    },
    {
        "id":1042,
        "perfil":{
            "nome": "Carlos Henrique",
            "email": "carloshr@gmail.com"
        }
    },
]
for item in cadastros: 
    id_formulario = item.get("id")
    perfil_extraido = item.get("perfil")
    nome_usuario = perfil_extraido.get("nome")
    telefone_usuario = perfil_extraido.get("telefone")

    print(f"ID: {id_formulario} | Usuario: {nome_usuario} | Telefone: {telefone_usuario}")  