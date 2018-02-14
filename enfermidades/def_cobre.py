
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

def av_def_cobre(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[1] == 1:
        total += 1
    if sinais_clinicos[2] == 1:
        total += 1
    if sinais_clinicos[4] == 1:
        total += 1
    if sinais_clinicos[12] == 1:
        total += 1
    if sinais_clinicos[14] == 1:
        total += 1
    if sinais_clinicos[16] == 1:
        total += 1
    if sinais_clinicos[19] == 1:
        total += 1
    if sinais_clinicos[20] == 1:
        total += 1
    if sinais_clinicos[24] == 1:
        total += 1
    if sinais_clinicos[26] == 1:
        total += 1
    if sinais_clinicos[27] == 1:
        total += 1
    if sinais_clinicos[39] == 1:
        total += 1
    if sinais_clinicos[43] == 1:
        total += 1
    if sinais_clinicos[45] == 1:
        total += 1
    if sinais_clinicos[49] == 1:
        total += 1
    if sinais_clinicos[67] == 1:
        total += 1
    if sinais_clinicos[76] == 1:
        total += 1
    if sinais_clinicos[81] == 1:
        total += 1
    if sinais_clinicos[93] == 1:
        total += 1
    if sinais_clinicos[102] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[132] == 1:
        total += 1
    if sinais_clinicos[141] == 1:
        total += 1
    if sinais_clinicos[147] == 1:
        total += 1
    if sinais_clinicos[161] == 1:
        total += 1
    if sinais_clinicos[169] == 1:
        total += 1
    if sinais_clinicos[183] == 1:
        total += 1
    if sinais_clinicos[192] == 1:
        total += 1
    if sinais_clinicos[197] == 1:
        total += 1
    if sinais_clinicos[202] == 1:
        total += 1
    if sinais_clinicos[203] == 1:
        total += 1
    if sinais_clinicos[207] == 1:
        total += 1
    total = (total/32)*100
    return total
