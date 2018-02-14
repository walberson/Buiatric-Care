
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

def av_babesiose(sinais_clinicos):


    total = 0
    if sinais_clinicos[2] == 1:
        total += 1
    if sinais_clinicos[8] == 1:
        total += 1
    if sinais_clinicos[11] == 1:
        total += 1
    if sinais_clinicos[14] == 1:
        total += 1
    if sinais_clinicos[25] == 1:
        total += 1
    if sinais_clinicos[27] == 1:
        total += 1
    if sinais_clinicos[38] == 1:
        total += 1
    if sinais_clinicos[42] == 1:
        total += 1
    if sinais_clinicos[43] == 1:
        total += 1
    if sinais_clinicos[55] == 1:
        total += 1
    if sinais_clinicos[62] == 1:
        total += 1
    if sinais_clinicos[83] == 1:
        total += 1
    if sinais_clinicos[94] == 1:
        total += 1
    if sinais_clinicos[106] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[121] == 1:
        total += 1
    if sinais_clinicos[135] == 1:
        total += 1
    if sinais_clinicos[147] == 1:
        total += 1
    if sinais_clinicos[155] == 1:
        total += 1
    if sinais_clinicos[160] == 1:
        total += 1
    if sinais_clinicos[169] == 1:
        total += 1
    if sinais_clinicos[171] == 1:
        total += 1
    if sinais_clinicos[191] == 1:
        total += 1
    if sinais_clinicos[194] == 1:
        total += 1
    if sinais_clinicos[195] == 1:
        total += 1
    if sinais_clinicos[197] == 1:
        total += 1
    if sinais_clinicos[203] == 1:
        total += 1


    total = (total/27)*100
    return total
