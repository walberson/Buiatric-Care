
'''

Este arquivo é parte do programa Buiatric Care Neurology

Buiatric Care Neurology é um software livre; você pode redistribuí-lo e/ou
modificá-lo dentro dos termos da Licença Pública Geral GNU como
publicada pela Fundação do Software Livre (FSF); na versão 3 da
Licença, ou (a seu critério) qualquer versão posterior.

Este programa é distribuído na esperança de que possa ser  útil,
mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
Licença Pública Geral GNU para maiores detalhes.

Você deve ter recebido uma cópia da Licença Pública Geral GNU junto
com este programa, Se não, veja <http://www.gnu.org/licenses/>.

'''

def av_meningoencefalite(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[8] == 1:
        total += 1
    if sinais_clinicos[14] == 1:
        total += 1
    if sinais_clinicos[24] == 1:
        total += 1
    if sinais_clinicos[25] == 1:
        total += 1
    if sinais_clinicos[27] == 1:
        total += 1
    if sinais_clinicos[38] == 1:
        total += 1
    if sinais_clinicos[40] == 1:
        total += 1
    if sinais_clinicos[42] == 1:
        total += 1
    if sinais_clinicos[43] == 1:
        total += 1
    if sinais_clinicos[58] == 1:
        total += 1
    if sinais_clinicos[83] == 1:
        total += 1
    if sinais_clinicos[107] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[122] == 1:
        total += 1
    if sinais_clinicos[141] == 1:
        total += 1
    if sinais_clinicos[147] == 1:
        total += 1
    if sinais_clinicos[156] == 1:
        total += 1
    if sinais_clinicos[191] == 1:
        total += 1
    if sinais_clinicos[197] == 1:
        total += 1
    if sinais_clinicos[203] == 1:
        total += 1
    if sinais_clinicos[204] == 1:
        total += 1


    total = (total/21)*100
    return total
