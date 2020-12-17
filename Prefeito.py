from Candidato import Candidato

class Prefeito (Candidato):
    def __init__(self, nomeCandidato, nomePartido, numPartido, numUrna2dig):
        Candidato.__init__(self, nomeCandidato, nomePartido, numPartido)
        self.numUrna2Dig = numUrna2dig

    def getNumUrna2Dig(self):
        return self.numUrna2Dig

    def setNumUrna5Dig(self, numUrna2Dig):
        self.numUrna5Dig = numUrna2Dig

    def imprimir(self):
        Candidato.imprimir(self)
        print("Nº na urna (2 dígitos): " + self.numUrna2Dig)