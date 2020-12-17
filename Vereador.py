from Candidato import Candidato

class Vereador (Candidato):
    def __init__(self, nomeCandidato, nomePartido, numPartido, numUrna5dig):
        Candidato.__init__(self, nomeCandidato, nomePartido, numPartido)
        self.numUrna5Dig = numUrna5dig

    def getNumUrna5Dig(self):
        return self.numUrna5Dig

    def setNumUrna5Dig(self, numUrna5Dig):
        self.numUrna5Dig = numUrna5Dig

    def imprimir(self):
        Candidato.imprimir(self)
        print("Nº na urna (5 dígitos): " + self.numUrna5Dig)