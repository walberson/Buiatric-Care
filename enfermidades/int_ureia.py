
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

def av_int_ureia(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[2] == 1:
        total += 1
    if sinais_clinicos[16] == 1:
        total += 1
    if sinais_clinicos[19] == 1:
        total += 1
    if sinais_clinicos[24] == 1:
        total += 1
    if sinais_clinicos[34] == 1:
        total += 1
    if sinais_clinicos[38] == 1:
        total += 1
    if sinais_clinicos[42] == 1:
        total += 1
    if sinais_clinicos[44] == 1:
        total += 1
    if sinais_clinicos[62] == 1:
        total += 1
    if sinais_clinicos[63] == 1:
        total += 1
    if sinais_clinicos[64] == 1:
        total += 1
    if sinais_clinicos[72] == 1:
        total += 1
    if sinais_clinicos[96] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[112] == 1:
        total += 1
    if sinais_clinicos[113] == 1:
        total += 1
    if sinais_clinicos[127] == 1:
        total += 1
    if sinais_clinicos[128] == 1:
        total += 1
    if sinais_clinicos[134] == 1:
        total += 1
    if sinais_clinicos[144] == 1:
        total += 1
    if sinais_clinicos[147] == 1:
        total += 1
    if sinais_clinicos[184] == 1:
        total += 1
    if sinais_clinicos[189] == 1:
        total += 1
    if sinais_clinicos[191] == 1:
        total += 1
    if sinais_clinicos[192] == 1:
        total += 1
    if sinais_clinicos[193] == 1:
        total += 1
    if sinais_clinicos[194] == 1:
        total += 1
    if sinais_clinicos[195] == 1:
        total += 1
    if sinais_clinicos[199] == 1:
        total += 1


    total = (total/29)*100
    return total
