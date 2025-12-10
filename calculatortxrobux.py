print('---------Olá , seja bem vindo a calculator of taxas ROBUX (para os criadores)---------')
Taxas = {
  "roupas": 0.30,
  "game-pass": 0.30,
  "open-view": 0.30
}
categorias = ["roupas", "game-pass", "open-view"]

def cal_liquido(preço_bruto, taxa):
  return preço_bruto * (1 - taxa)

def cal_bruto(preço_liquido, taxa):
  bruto = preço_liquido / (1  - taxa)
  return bruto

def main():
 print(f"Categorias disponiveis: {categorias} ")
 categoria = str(input("Escolha uma categoria: ")).strip().lower()
  
 if categoria not in Taxas:
    print("Categoria invalida, ESSA CATEGORIA NAO ESTA DISPONIVEL OU NAO EXISTE!")
    return


 taxa = Taxas[categoria]
 while True:
  print("\n1 - Informar preço Bruto")
  print("2 - Calcular quanto quer receber")
  modo = int(input("Digite sua escolha: "))

  if modo == 1:
   preço_bruto = float(input("Qual o Preço bruto do Robux:")) 
   liquido = cal_liquido(preço_bruto, taxa)
   print(f'Liquido que foi recebido: {liquido:.2f} Robux')
  
  elif modo == 2:
   preço_liquido = float(input("Quanto voce quer receber:"))
   bruto = cal_bruto(preço_liquido, taxa)
   print(f'Preço Bruto necessario: {bruto:.2f} Robux')
  
  else:
   print("Opção Invalida")
main()


# Neste programa fizemos uma calculadora de taxas de robux que é de 30% para o roblox, você tem que informar o valor de robux exemplo 79, não o preço do robux... ESPERO que gostem criadores muito obrigado...