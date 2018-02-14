
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

def av_botulismo(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[14] == 1:
        total += 1
    if sinais_clinicos[19] == 1:
        total += 1
    if sinais_clinicos[23] == 1:
        total += 1
    if sinais_clinicos[25] == 1:
        total += 1
    if sinais_clinicos[33] == 1:
        total += 1
    if sinais_clinicos[42] == 1:
        total += 1
    if sinais_clinicos[43] == 1:
        total += 1
    if sinais_clinicos[49] == 1:
        total += 1
    if sinais_clinicos[50] == 1:
        total += 1
    if sinais_clinicos[51] == 1:
        total += 1
    if sinais_clinicos[52] == 1:
        total += 1
    if sinais_clinicos[53] == 1:
        total += 1
    if sinais_clinicos[54] == 1:
        total += 1
    if sinais_clinicos[61] == 1:
        total += 1
    if sinais_clinicos[62] == 1:
        total += 1
    if sinais_clinicos[91] == 1:
        total += 1
    if sinais_clinicos[106] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[128] == 1:
        total += 1
    if sinais_clinicos[148] == 1:
        total += 1
    if sinais_clinicos[151] == 1:
        total += 1
    if sinais_clinicos[153] == 1:
        total += 1
    if sinais_clinicos[156] == 1:
        total += 1
    if sinais_clinicos[159] == 1:
        total += 1
    if sinais_clinicos[165] == 1:
        total += 1
    if sinais_clinicos[167] == 1:
        total += 1
    if sinais_clinicos[179] == 1:
        total += 1
    if sinais_clinicos[181] == 1:
        total += 1
    if sinais_clinicos[191] == 1:
        total += 1
    if sinais_clinicos[201] == 1:
        total += 1



    total = (total/30)*100
    return total
