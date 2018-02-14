
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

def av_cetose(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[4] == 1:
        total += 1
    if sinais_clinicos[6] == 1:
        total += 1
    if sinais_clinicos[7] == 1:
        total += 1
    if sinais_clinicos[8] == 1:
        total += 1
    if sinais_clinicos[16] == 1:
        total += 1
    if sinais_clinicos[17] == 1:
        total += 1
    if sinais_clinicos[19] == 1:
        total += 1
    if sinais_clinicos[25] == 1:
        total += 1
    if sinais_clinicos[27] == 1:
        total += 1
    if sinais_clinicos[40] == 1:
        total += 1
    if sinais_clinicos[42] == 1:
        total += 1
    if sinais_clinicos[43] == 1:
        total += 1
    if sinais_clinicos[55] == 1:
        total += 1
    if sinais_clinicos[57] == 1:
        total += 1
    if sinais_clinicos[66] == 1:
        total += 1
    if sinais_clinicos[67] == 1:
        total += 1
    if sinais_clinicos[73] == 1:
        total += 1
    if sinais_clinicos[74] == 1:
        total += 1
    if sinais_clinicos[86] == 1:
        total += 1
    if sinais_clinicos[97] == 1:
        total += 1
    if sinais_clinicos[98] == 1:
        total += 1
    if sinais_clinicos[101] == 1:
        total += 1
    if sinais_clinicos[104] == 1:
        total += 1
    if sinais_clinicos[106] == 1:
        total += 1
    if sinais_clinicos[118] == 1:
        total += 1
    if sinais_clinicos[129] == 1:
        total += 1
    if sinais_clinicos[142] == 1:
        total += 1
    if sinais_clinicos[143] == 1:
        total += 1
    if sinais_clinicos[147] == 1:
        total += 1
    if sinais_clinicos[169] == 1:
        total += 1
    if sinais_clinicos[178] == 1:
        total += 1
    if sinais_clinicos[191] == 1:
        total += 1
    total = (total/32)*100
    return total
