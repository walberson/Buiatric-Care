
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

def av_listeriose(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[8] == 1:
        total += 1
    if sinais_clinicos[27] == 1:
        total += 1
    if sinais_clinicos[29] == 1:
        total += 1
    if sinais_clinicos[38] == 1:
        total += 1
    if sinais_clinicos[43] == 1:
        total += 1
    if sinais_clinicos[46] == 1:
        total += 1
    if sinais_clinicos[48] == 1:
        total += 1
    if sinais_clinicos[50] == 1:
        total += 1
    if sinais_clinicos[51] == 1:
        total += 1
    if sinais_clinicos[53] == 1:
        total += 1
    if sinais_clinicos[59] == 1:
        total += 1
    if sinais_clinicos[75] == 1:
        total += 1
    if sinais_clinicos[83] == 1:
        total += 1
    if sinais_clinicos[84] == 1:
        total += 1
    if sinais_clinicos[88] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[128] == 1:
        total += 1
    if sinais_clinicos[147] == 1:
        total += 1
    if sinais_clinicos[148] == 1:
        total += 1
    if sinais_clinicos[150] == 1:
        total += 1
    if sinais_clinicos[156] == 1:
        total += 1
    if sinais_clinicos[158] == 1:
        total += 1
    if sinais_clinicos[162] == 1:
        total += 1
    if sinais_clinicos[164] == 1:
        total += 1
    if sinais_clinicos[174] == 1:
        total += 1
    if sinais_clinicos[182] == 1:
        total += 1
    if sinais_clinicos[191] == 1:
        total += 1
    if sinais_clinicos[197] == 1:
        total += 1
    if sinais_clinicos[202] == 1:
        total += 1
    if sinais_clinicos[203] == 1:
        total += 1
    if sinais_clinicos[206] == 1:
        total += 1


    total = (total/31)*100
    return total
