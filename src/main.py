import pdftotext
from entities.cliente import Cliente
from entities.cobertura import Cobertura
from entities.resultado import Resultado

pdf_path = "assets/João Rodrigues_Vida Viva_2023_10_16.pdf"
pdf_converted_path = pdf_path.replace("assets/", "assets/out/").replace(".pdf", ".txt")

# Abre o arquivo PDF
with open(pdf_path, "rb") as f:
  pdf = pdftotext.PDF(f)


# Escreve os dados do PDF em um txt
with open(pdf_converted_path, "w") as t:
  t.write("")
  for page in pdf:
    t.write(page)
  t.close()


# Recupera os dados do cliente
dados_cliente = []

with open(pdf_converted_path, "r") as file:
  linhas = file.readlines()
  for linha in linhas:
    if linha.find("Cliente:") != -1:
      string = linha.replace("Cliente:", "")
      string = string.replace("Idade do Cônjuge:", "")
      string = string[: len(string) - 3]
      string = string.strip()
      dados_cliente = string.split(", ")

nome = dados_cliente[0]
idade = int(dados_cliente[1])
cliente = Cliente(nome, idade)


# Recupera os dados da tabela Resultados
string = ""

with open(pdf_converted_path, "r") as file:
  linhas = file.readlines()
  linha_inicial = False
  for linha in linhas:
    if linha.find("PRÊMIO TOTAL") != -1:
      break
    if linha_inicial:
      string += linha
    if linha.find("R$") != -1:
      linha_inicial = True

string = string.strip()
tabela = string.split("\n")


# Ajustando erros da tabela
aux = False
tabela_aux = []

for item in tabela:
  if aux:
    texto = "Despesas Médicas Hospitalares e Odontológicas por Acidente    " + item.strip()
    tabela_aux.append(texto)
    aux = False
    continue
  if item.find("Despesas Médicas Hospitalares e") != -1:
    aux = True
    continue
  if item.find("Odontológicas por Acidente") == -1:
    tabela_aux.append(item.strip())


# Removendo espaços entre os dados das linhas
dados_tabela = []

for linha in tabela_aux:
  linha_final = ""

  while True:
    if linha.find("  ") == -1:
      linha_final += linha
      dados_tabela.append(linha_final)
      break

    for i in range(len(linha)):
      if linha[i] == " " and linha[i + 1] == " ":
        final_index = i
        linha_final += linha[0:final_index]
        linha_final += ";"

        for j in range(i, len(linha)):
          if linha[j] != " ":
            linha = linha[j : len(linha)]
            break
        break

"""
TODO: implementar conexão com banco de dados
"""

# Instancia os objetos
resultados = []
coberturas = []

for linha in dados_tabela:
  dados_resultado = linha.split(";")

  cobertura = Cobertura(dados_resultado[0])
  coberturas.append(cobertura)

  capital = float(dados_resultado[1].replace(".", "").replace(",", "."))
  premio_mensal = float(dados_resultado[2].replace(".", "").replace(",", "."))
  premio_anual = float(dados_resultado[3].replace(".", "").replace(",", "."))

  resultado = Resultado(cliente, cobertura, capital, premio_mensal, premio_anual)
  resultados.append(resultado)


# Salva dados em um arquivo txt
dados_path = "assets/out/dados.txt"

with open(dados_path, "w") as t:
  t.write("")
  t.write(f"{str(cliente)}\n")

  for res in resultados:
    t.write(f"{str(res)}\n")

print(f"Dados convertidos e salvos em: '{dados_path}'")
