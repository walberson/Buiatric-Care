
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

def av_tetano(sinais_clinicos):
    #lista de sintomas atual
    #salivacao , Opistótono , agressividade, bruxismo, convuncoes
    total = 0
    if sinais_clinicos[13] == 1:
        total += 1
    if sinais_clinicos[33] == 1:
        total += 1
    if sinais_clinicos[37] == 1:
        total += 1
    if sinais_clinicos[42] == 1:
        total += 1
    if sinais_clinicos[47] == 1:
        total += 1
    if sinais_clinicos[72] == 1:
        total += 1
    if sinais_clinicos[97] == 1:
        total += 1
    if sinais_clinicos[123] == 1:
        total += 1
    if sinais_clinicos[141] == 1:
        total += 1
    if sinais_clinicos[147] == 1:
        total += 1
    if sinais_clinicos[149] == 1:
        total += 1
    if sinais_clinicos[157] == 1:
        total += 1
    if sinais_clinicos[168] == 1:
        total += 1
    if sinais_clinicos[170] == 1:
        total += 1
    if sinais_clinicos[186] == 1:
        total += 1
    if sinais_clinicos[187] == 1:
        total += 1
    if sinais_clinicos[199] == 1:
        total += 1
    if sinais_clinicos[200] == 1:
        total += 1
    if sinais_clinicos[201] == 1:
        total += 1
    if sinais_clinicos[203] == 1:
        total += 1
    if sinais_clinicos[205] == 1:
        total += 1


    total = (total/21)*100
    return total
