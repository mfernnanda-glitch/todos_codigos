
#FORMULADO POR MIM

#
disciplina = 0
soma = 0
media  = 0
nota = 0
contador = 0
nota_materia = 0
aluna = {
    "nome_aluna": "Maria Fernnanda",
    "disciplina": {
        "nome": "",
        "notas": [], #Aqui pode ser um dicionário também
    }
}

aluna["disciplina"]["nome"] = input("Digite o nome da disciplina: ") #aqui faz mais sentido do que ter um dicionário "disciplina" recebendo nome
nota = float(input("Digite a sua nota ou '-1' para sair: "))
["notas"].append(nota)


while nota != -1:

    
        nota = float(input("Digite a sua nota ou '-1' para sair: "))
        ["notas"].append(nota)
        
    
        

print("Cadastro encerrado.")
 
 


#for disciplinas in ["notas"]:
    #soma = sum(aluna["disciplina"]["notas"])
    #print(f"Soma total da disciplina: {aluna}")


    #media = 
print("-"*50)
nota = 0
print("\n --- Relatório final: --- \n")

#for nome_a in aluna["nome_aluna"]: #serve para percorrer apartir da onde eu apontar para o ponteiro 

print("Nome da aluna: ", aluna["nome_aluna"]) #eu adicionei nome da aluna, dentro de "nome", ou seja, eu vou chamar "nome"

print("-"*50)

for disciplinas in aluna["disciplina"]:

 for disciplinas in ["nome"]: #observar se precisa dar espaçamento aqui, ou apenas no 1° for
      
      print("Disciplina: ", disciplinas)
 print("-"*50)

 for nota_materia in ["notas"]:

      print("Notas: ", nota_materia)
      contador +=1
      
 print("-"*50)


media = soma/len(aluna["notas"])
print("Total das notas: ", sum(aluna["notas"]))
print("Media das notas ", media)
print(f"Você adicionou {contador} nota(s)")
print("-"*50)


#=============================================================================


 #MODELO ALTERADO

soma = 0

aluna = {
    "nome": "Maria Fernnanda",
    "disciplina": {
        "notas": []
    }
}

disciplina_nome = input("Digite o nome da disciplina: ")
nota = float(input("Digite uma nota ou -1 para sair: "))

while nota != -1:
    aluna["disciplina"]["notas"].append(nota)
    nota = float(input("Digite outra nota ou -1 para sair: "))

print("Cadastro encerrado.")

for nota_registrada in aluna["disciplina"]["notas"]:
    soma += nota_registrada

if aluna["disciplina"]["notas"]:
    media = soma / len(aluna["disciplina"]["notas"])
    print(f"\nDisciplina: {disciplina_nome}")
    print(f"Soma total das notas: {soma}")
    print(f"Média das notas: {media}")
else:
    print("Nenhuma nota foi registrada.")


