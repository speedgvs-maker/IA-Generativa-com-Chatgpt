# 1. operador and (e) - retorna True apenas se todas as condições forem verdadeiro
tem_sol = True
tem_dinheiro= True
vai_praia = tem_sol and tem_dinheiro

print("vai a praia (and):", vai_praia)

# 2. operador or (ou) - Retorna True se pelomenos uma condição for verdadeira
tem_carro = input("vc tem carro? (sim/nao): ")
tem_bicicleta = input("vc tem bicicleta? (sim/nao) ")
pode_viajar = tem_carro == "sim" or tem_bicicleta == "sim"

print("Pode viajar (or)", pode_viajar)

# 3. operador not (não) ele apenas inverte o valor lógico
chovendo = False
fazer_caminhada = not chovendo
print("Fazer caminhada (NOT) ", fazer_caminhada)