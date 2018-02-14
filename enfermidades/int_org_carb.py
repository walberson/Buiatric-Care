
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

def av_int_org_carb(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[2] == 1:
        total += 1
    if sinais_clinicos[15] == 1:
        total += 1
    if sinais_clinicos[16] == 1:
        total += 1
    if sinais_clinicos[19] == 1:
        total += 1
    if sinais_clinicos[23] == 1:
        total += 1
    if sinais_clinicos[31] == 1:
        total += 1
    if sinais_clinicos[32] == 1:
        total += 1
    if sinais_clinicos[38] == 1:
        total += 1
    if sinais_clinicos[41] == 1:
        total += 1
    if sinais_clinicos[42] == 1:
        total += 1
    if sinais_clinicos[43] == 1:
        total += 1
    if sinais_clinicos[49] == 1:
        total += 1
    if sinais_clinicos[62] == 1:
        total += 1
    if sinais_clinicos[70] == 1:
        total += 1
    if sinais_clinicos[95] == 1:
        total += 1
    if sinais_clinicos[99] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[112] == 1:
        total += 1
    if sinais_clinicos[130] == 1:
        total += 1
    if sinais_clinicos[140] == 1:
        total += 1
    if sinais_clinicos[156] == 1:
        total += 1
    if sinais_clinicos[159] == 1:
        total += 1
    if sinais_clinicos[188] == 1:
        total += 1
    if sinais_clinicos[191] == 1:
        total += 1
    if sinais_clinicos[193] == 1:
        total += 1
    if sinais_clinicos[198] == 1:
        total += 1
    if sinais_clinicos[199] == 1:
        total += 1
    if sinais_clinicos[201] == 1:
        total += 1
    if sinais_clinicos[203] == 1:
        total += 1
    if sinais_clinicos[208] == 1:
        total += 1


    total = (total/30)*100
    return total
