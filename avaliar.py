

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


from enfermidades.aujeszky import av_aujeszky
from enfermidades.babesiose import av_babesiose
from enfermidades.botulismo import av_botulismo
from enfermidades.cetose import av_cetose
from enfermidades.def_cobre import av_def_cobre
from enfermidades.encefalopatia import av_encefalopatia
from enfermidades.febre_catarral_maligna import av_febre_catarral_maligna
from enfermidades.hipocalcemia import av_hipocalcemia
from enfermidades.int_aspergillus import av_int_aspergillus
from enfermidades.int_chumbo import av_int_chumbo
from enfermidades.int_claviceps import av_int_claviceps
from enfermidades.int_equisetum import av_int_equisetum
from enfermidades.int_ipomoea_asarifolia import av_int_ipomoea_asarifolia
from enfermidades.int_ipomoea_carnea import av_int_ipomoea_carnea
from enfermidades.int_marsdenia import av_int_marsdenia
from enfermidades.int_org_carb import av_int_org_carb
from enfermidades.int_phalaris import av_int_phalaris
from enfermidades.int_polygala import av_int_polygala
from enfermidades.int_prosopis import av_int_prosopis
from enfermidades.int_ricinus import av_int_ricinus
from enfermidades.int_sida import av_int_sida
from enfermidades.int_solanum import av_int_solanum
from enfermidades.int_sternocarpella import av_int_sternocarpella
from enfermidades.int_ureia import av_int_ureia
from enfermidades.leucose import av_leucose
from enfermidades.listeriose import av_listeriose
from enfermidades.meningoencefalite import av_meningoencefalite
from enfermidades.poliencefalomalacia import av_poliencefalomalacia
from enfermidades.raiva import av_raiva
from enfermidades.tetano import av_tetano



def avaliar_sinais_clinicos(sinais_clinicos):
    #passar lista para cada doença cadastrada
    #lista vai armazenar os valores correspondentes a cada doenca
    enfermidades = [ ]

    # ordem na lista de doencas
    # raiva, aujezky, febre_catarral_maligna, meningoencefalite_BHV5,
    # encefalopatia, botulismo , tetano
    aujeszky = av_aujeszky(sinais_clinicos)
    enfermidades.append(aujeszky)

    babesiose = av_babesiose(sinais_clinicos)
    enfermidades.append(babesiose)

    botulismo = av_botulismo(sinais_clinicos)
    enfermidades.append(botulismo)

    cetose = av_cetose(sinais_clinicos)
    enfermidades.append(cetose)

    def_cobre = av_def_cobre(sinais_clinicos)
    enfermidades.append(def_cobre)

    encefalopatia = av_encefalopatia(sinais_clinicos)
    enfermidades.append(encefalopatia)

    febre_catarral_maligna = av_febre_catarral_maligna(sinais_clinicos)
    enfermidades.append(febre_catarral_maligna)

    hipocalcemia = av_hipocalcemia(sinais_clinicos)
    enfermidades.append(hipocalcemia)

    int_aspergillus = av_int_aspergillus(sinais_clinicos)
    enfermidades.append(int_aspergillus)

    int_chumbo = av_int_chumbo(sinais_clinicos)
    enfermidades.append(int_chumbo)

    int_claviceps = av_int_claviceps(sinais_clinicos)
    enfermidades.append(int_claviceps)

    int_equisetum = av_int_equisetum(sinais_clinicos)
    enfermidades.append(int_equisetum)

    int_ipomoea_asarifolia = av_int_ipomoea_asarifolia(sinais_clinicos)
    enfermidades.append(int_ipomoea_asarifolia)

    int_ipomoea_carnea = av_int_ipomoea_carnea(sinais_clinicos)
    enfermidades.append(int_ipomoea_carnea)

    int_marsdenia = av_int_marsdenia(sinais_clinicos)
    enfermidades.append(int_marsdenia)

    int_org_carb = av_int_org_carb(sinais_clinicos)
    enfermidades.append(int_org_carb)

    int_phalaris = av_int_phalaris(sinais_clinicos)
    enfermidades.append(int_phalaris)

    int_polygala = av_int_polygala(sinais_clinicos)
    enfermidades.append(int_polygala)

    int_prosopis = av_int_prosopis(sinais_clinicos)
    enfermidades.append(int_prosopis)

    int_ricinus = av_int_ricinus(sinais_clinicos)
    enfermidades.append(int_ricinus)

    int_sida = av_int_sida(sinais_clinicos)
    enfermidades.append(int_sida)

    int_solanum = av_int_solanum(sinais_clinicos)
    enfermidades.append(int_solanum)

    int_sternocarpella = av_int_sternocarpella(sinais_clinicos)
    enfermidades.append(int_sternocarpella)

    int_ureia = av_int_ureia(sinais_clinicos)
    enfermidades.append(int_ureia)

    leucose = av_leucose(sinais_clinicos)
    enfermidades.append(leucose)

    listeriose = av_listeriose(sinais_clinicos)
    enfermidades.append(listeriose)

    meningoencefalite = av_meningoencefalite(sinais_clinicos)
    enfermidades.append(meningoencefalite)

    poliencefalomalacia = av_poliencefalomalacia(sinais_clinicos)
    enfermidades.append(poliencefalomalacia)

    raiva = av_raiva(sinais_clinicos)
    enfermidades.append(raiva)

    tetano = av_tetano(sinais_clinicos)
    enfermidades.append(tetano)




    return enfermidades
