
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

def av_hipocalcemia(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[14] == 1:
        total += 1
    if sinais_clinicos[19] == 1:
        total += 1
    if sinais_clinicos[20] == 1:
        total += 1
    if sinais_clinicos[32] == 1:
        total += 1
    if sinais_clinicos[33] == 1:
        total += 1
    if sinais_clinicos[42] == 1:
        total += 1
    if sinais_clinicos[43] == 1:
        total += 1
    if sinais_clinicos[52] == 1:
        total += 1
    if sinais_clinicos[56] == 1:
        total += 1
    if sinais_clinicos[58] == 1:
        total += 1
    if sinais_clinicos[80] == 1:
        total += 1
    if sinais_clinicos[96] == 1:
        total += 1
    if sinais_clinicos[97] == 1:
        total += 1
    if sinais_clinicos[100] == 1:
        total += 1
    if sinais_clinicos[105] == 1:
        total += 1
    if sinais_clinicos[106] == 1:
        total += 1
    if sinais_clinicos[138] == 1:
        total += 1
    if sinais_clinicos[159] == 1:
        total += 1
    if sinais_clinicos[162] == 1:
        total += 1
    if sinais_clinicos[167] == 1:
        total += 1
    if sinais_clinicos[175] == 1:
        total += 1
    if sinais_clinicos[177] == 1:
        total += 1
    if sinais_clinicos[192] == 1:
        total += 1
    if sinais_clinicos[194] == 1:
        total += 1
    if sinais_clinicos[197] == 1:
        total += 1
    if sinais_clinicos[199] == 1:
        total += 1
    if sinais_clinicos[201] == 1:
        total += 1
    if sinais_clinicos[203] == 1:
        total += 1


    total = (total/28)*100
    return total
