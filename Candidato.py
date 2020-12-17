class Candidato:

    
    def __init__(self, nomeCandidato):
        self.nomeCandidato = nomeCandidato
        self.nomePartido   = None
        self.numPartido    = None


    def getNomeCandidato(self):
        return self.nomeCandidato

    def getNomePartido(self):
        return self.nomePartido

    def getNumPartido(self):
        return self.numPartido
    
    def setNomeCandidato(self, nomeCandidato):
        self.nomeCandidato = nomeCandidato

    def setNomePartido(self, nomePartido):
        self.nomePartido = nomePartido

    def setNumPartido(self, numPartido):
        self.numPartido = numPartido  

    def validar_candidato(self):
        #while True:
        if self.nomeCandidato == None:
            input("Nome do candidato nulo!")
        
        if len(self.numPartido) != 2:
            input("Nº do partido precisa ter 2 dígitos!")
            #break
        if self.numPartido == None: 
            input("Nº do partido nulo!")
            #break
        else:
            return True
            return False

    # Método para retornar todos os dados da lista, sempre que for necessário
    '''def imprimir(self):
        print("Candidato: " + self.nomeCandidato)
        print("Partido: " + self.nomePartido)
        print("Nº do Partido: " + self.numPartido)'''
    def __str__(self):
        return  str(self.nomeCandidato)+" -   "+str(self.nomePartido)+"  -    "+str(self.numPartido)


#---------------------------------------------------------------------------------------------------------------------------------

def cad_prefeito():
    nome = input("Nome: ")
    #partido = input("Partido: ")
    #numPartido = input("Nº partido: ")
    if not nome: 
        input("Nome de candidato nulo! [Enter]")
    elif prefeito_repetido(nome):
        input("Candidato já existe! [Enter]")
        cad_prefeito()
    else: 
        cand_dig = Candidato(nome) 
        cand_dig.setNomePartido(input("Partido: "))
        cand_dig.setNumPartido(input("Nº do partido: "))
        if cand_dig.validar_candidato():
            input("Candidato cadastrado com sucesso! [Enter]")
            return cand_dig 

def cad_vereador():
    nome = input("Nome: ")
    #partido = input("Partido: ")
    #numPartido = input("Nº partido: ")
    if not nome: 
        input("Nome de candidato nulo! [Enter]")
    elif prefeito_repetido(nome):
        input("Candidato já existe! [Enter]")
        cad_prefeito()
    else: 
        cand_dig = Candidato(nome) 
        cand_dig.setNomePartido(input("Partido: "))
        cand_dig.setNumPartido(input("Nº do partido: "))
        if cand_dig.validar_candidato():
            input("Candidato cadastrado com sucesso! [Enter]")
            return cand_dig

               
def add_dados_lista():
    op = '''
    Menu
        1 - Prefeito
        2 - Vereador
    Escolha: '''
    
    if op in ('1','2'): 
        return op 
    input("Opção inválida! [Enter]")

    escolhaTipoCand = input(op)
    if escolhaTipoCand == "1":
        lst_cand_prefeito.append(cad_prefeito())
    if escolhaTipoCand == "2":
        lst_cand_vereador.append(cad_vereador())

def relatorio_cand_prefeitos():
    print("Nome  Partido NumPartido")
    for x in lst_cand_prefeito: # Para cada objeto da lista lst_sala (sala, andar, capacidade)
        print(x) # Mostra a sala e seus dados
    input("[Enter p/ continuar]")

def relatorio_cand_vereadores():
    print("Nome  Partido NumPartido")
    for x in lst_cand_vereador: # Para cada objeto da lista lst_sala (sala, andar, capacidade)
        print(x) # Mostra a sala e seus dados
    input("[Enter p/ continuar]")

def prefeito_repetido(nome):
    for i in lst_cand_prefeito:
        if i.getNomeCandidato() == nome:
            input("Candidato já existente!")
    return False

def vereador_repetido(nome):
    for i in lst_cand_vereador:
        if i.getNomeCandidato() == nome:
            return True
    return False 

# Declaração das listas necessárias
lst_cand_prefeito  = []
lst_cand_vereador = []
lst_nome_partido = []
lst_num_partido = []
lst_categoria = []
lst_projeto = []
        
            # Método para apresentar as opções do menu principal
def menu_principal():
    opcao = input(""" 

            MENU

            0 - Finalizar Programa
            1 – Cadastrar Candidato/Partido
            2 – Cadastrar Projeto/Categoria
            3 – Relatório de Candidatos
            4 – Relatório de Candidatos por Partido
            5 – Relatório de Projetos
            6 – Relatório de Projetos por Categoria
            7 – Vincular Projeto a um Candidato
            8 – Excluir Candidato
            9 – Excluir Projeto
            10 – Avaliar um Projeto
            11 – Relatório de Projetos por Nota

            Escolha: """) # Grande string com as opções do menu

    if opcao in ('0','1','2','3','4','5','6','7','8','9','10','11'):
        return opcao 
    input("Opção inválida! [Enter]")



        # Programa principal
while True: 
    resp = menu_principal()
    if resp == '0':
        break 
    elif resp == '1':
        #pass
        add_dados_lista()
    elif resp == '2':
        pass
        #cadastrar_projeto()
    elif resp == '3':
        escolha = input ('''
           MENU

           1 - Prefeito
           2 - Vereador

            Escolha: '''
        )
        
        if escolha == '1':
            relatorio_cand_prefeitos()
        elif escolha == '2':
            relatorio_cand_vereadores() 
       
    elif resp == '4':
        pass
        #relatorio_cand_partido()
    elif resp == '5':
        pass
        #relatorio_projetos()
    elif resp == '6':
        pass
        #relatorio_proj_categoria()
    elif resp == '7':
        #vincular_projeto_candidato()
        pass
    elif resp == '8':
        #excluir_candidato()
        pass
    elif resp == '9':
        #excluir_projeto()
        pass
    elif resp == '10':
        #avaliar_projeto()
        pass
    elif resp == '11':
        #relatorio_projetos_nota()
        pass
    print("Fim")
        