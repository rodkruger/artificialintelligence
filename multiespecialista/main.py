#!/usr/bin/env python

from multiespecialista.blackboard.QuadroNegro import QuadroNegro
from multiespecialista.controlador.Controlador import Controlador
from multiespecialista.geradordeproduto.GeradorDeProduto import GeradorDeProduto
from multiespecialista.especialista.estacaoForja import estacaoForja
from multiespecialista.especialista.estacaoImpressao3D import estacaoImpressao3D
from multiespecialista.especialista.estacaoMontagem import estacaoMontagem
from multiespecialista.especialista.estacaoUsinagem import estacaoUsinagem
from multiespecialista.especialista.verificacaoFinal import verificacaoFinal

if __name__ == '__main__':

    quadro_negro = QuadroNegro()
    GeradorDeProduto = GeradorDeProduto(quadro_negro)

    quadro_negro.adicionaEspecialista( estacaoForja(quadro_negro) )
    quadro_negro.adicionaEspecialista( estacaoImpressao3D(quadro_negro) )
    quadro_negro.adicionaEspecialista( estacaoMontagem(quadro_negro) )

    quadro_negro.adicionaEspecialista( estacaoUsinagem(quadro_negro) )
    quadro_negro.adicionaEspecialista( verificacaoFinal(quadro_negro) )

    contribuicoes = Controlador(quadro_negro, GeradorDeProduto, 120).loop()

    for x in contribuicoes:
        print('\n',x[0],':\n',x[1])