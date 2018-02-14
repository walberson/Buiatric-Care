
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

def av_int_prosopis(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[11] == 1:
        total += 1
    if sinais_clinicos[20] == 1:
        total += 1
    if sinais_clinicos[21] == 1:
        total += 1
    if sinais_clinicos[50] == 1:
        total += 1
    if sinais_clinicos[51] == 1:
        total += 1
    if sinais_clinicos[53] == 1:
        total += 1
    if sinais_clinicos[56] == 1:
        total += 1
    if sinais_clinicos[59] == 1:
        total += 1
    if sinais_clinicos[65] == 1:
        total += 1
    if sinais_clinicos[67] == 1:
        total += 1
    if sinais_clinicos[103] == 1:
        total += 1
    if sinais_clinicos[108] == 1:
        total += 1
    if sinais_clinicos[109] == 1:
        total += 1
    if sinais_clinicos[129] == 1:
        total += 1
    if sinais_clinicos[154] == 1:
        total += 1
    if sinais_clinicos[156] == 1:
        total += 1
    if sinais_clinicos[191] == 1:
        total += 1

    total = (total/17)*100
    return total
