
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

def av_encefalopatia(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[2] == 1:
        total += 1
    if sinais_clinicos[5] == 1:
        total += 1
    if sinais_clinicos[8] == 1:
        total += 1
    if sinais_clinicos[13] == 1:
        total += 1
    if sinais_clinicos[19] == 1:
        total += 1
    if sinais_clinicos[23] == 1:
        total += 1
    if sinais_clinicos[24] == 1:
        total += 1
    if sinais_clinicos[25] == 1:
        total += 1
    if sinais_clinicos[42] == 1:
        total += 1
    if sinais_clinicos[52] == 1:
        total += 1
    if sinais_clinicos[55] == 1:
        total += 1
    if sinais_clinicos[67] == 1:
        total += 1
    if sinais_clinicos[69] == 1:
        total += 1
    if sinais_clinicos[70] == 1:
        total += 1
    if sinais_clinicos[77] == 1:
        total += 1
    if sinais_clinicos[90] == 1:
        total += 1
    if sinais_clinicos[92] == 1:
        total += 1
    if sinais_clinicos[96] == 1:
        total += 1
    if sinais_clinicos[97] == 1:
        total += 1
    if sinais_clinicos[98] == 1:
        total += 1
    if sinais_clinicos[104] == 1:
        total += 1
    if sinais_clinicos[106] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[110] == 1:
        total += 1
    if sinais_clinicos[115] == 1:
        total += 1
    if sinais_clinicos[116] == 1:
        total += 1
    if sinais_clinicos[124] == 1:
        total += 1
    if sinais_clinicos[126] == 1:
        total += 1
    if sinais_clinicos[145] == 1:
        total += 1


    total = (total/29)*100
    return total
