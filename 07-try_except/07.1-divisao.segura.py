def dividir_seguro(x, y):
    resultado = x / y 
    return resultado

x = int(input("Digite um número: "))
y = float(input("Digite um número: "))

valor_resultado = dividir_seguro(x, y)
print(valor_resultado)