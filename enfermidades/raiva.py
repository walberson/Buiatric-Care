
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

def av_raiva(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[2] == 1:
        total += 1
    if sinais_clinicos[7] == 1:
        total += 1
    if sinais_clinicos[19] == 1:
        total += 1
    if sinais_clinicos[20] == 1:
        total += 1
    if sinais_clinicos[24] == 1:
        total += 1
    if sinais_clinicos[35] == 1:
        total += 1
    if sinais_clinicos[37] == 1:
        total += 1
    if sinais_clinicos[38] == 1:
        total += 1
    if sinais_clinicos[43] == 1:
        total += 1
    if sinais_clinicos[47] == 1:
        total += 1
    if sinais_clinicos[51] == 1:
        total += 1
    if sinais_clinicos[67] == 1:
        total += 1
    if sinais_clinicos[70] == 1:
        total += 1
    if sinais_clinicos[85] == 1:
        total += 1
    if sinais_clinicos[96] == 1:
        total += 1
    if sinais_clinicos[97] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[112] == 1:
        total += 1
    if sinais_clinicos[114] == 1:
        total += 1
    if sinais_clinicos[118] == 1:
        total += 1
    if sinais_clinicos[128] == 1:
        total += 1
    if sinais_clinicos[139] == 1:
        total += 1
    if sinais_clinicos[147] == 1:
        total += 1
    if sinais_clinicos[153] == 1:
        total += 1
    if sinais_clinicos[154] == 1:
        total += 1
    if sinais_clinicos[155] == 1:
        total += 1
    if sinais_clinicos[156] == 1:
        total += 1
    if sinais_clinicos[160] == 1:
        total += 1
    if sinais_clinicos[166] == 1:
        total += 1
    if sinais_clinicos[172] == 1:
        total += 1
    if sinais_clinicos[177] == 1:
        total += 1
    if sinais_clinicos[186] == 1:
        total += 1
    if sinais_clinicos[190] == 1:
        total += 1
    if sinais_clinicos[191] == 1:
        total += 1
    if sinais_clinicos[192] == 1:
        total += 1
    if sinais_clinicos[203] == 1:
        total += 1
    total = (total/36)*100
    return total
