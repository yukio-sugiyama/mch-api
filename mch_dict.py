import time
from pprint import pprint

from . import mch_apis

mch = mch_apis.MCHAPI()

COMM_HEAD = '10'
UNCO_HEAD = '20'
RARE_HEAD = '30'
EPIC_HEAD = '40'
LEGE_HEAD = '50'
LIMI_HEAD = '55'

COMM_HERO_IMPLE = 2
UNCO_HERO_IMPLE = 37
RARE_HERO_IMPLE = 40
EPIC_HERO_IMPLE = 46
LEGE_HERO_IMPLE = 23

COMM_HERO_SKIP = []
UNCO_HERO_SKIP = []
RARE_HERO_SKIP = [33]
EPIC_HERO_SKIP = []
LEGE_HERO_SKIP = []

COMM_EXTE_IMPLE = 63
UNCO_EXTE_IMPLE = 63
RARE_EXTE_IMPLE = 63
EPIC_EXTE_IMPLE = 63
LEGE_EXTE_IMPLE = 63
LIMI_EXTE_IMPLE = 61

COMM_EXTE_SKIP = [7, 33, 52, 53, 54, 62]
UNCO_EXTE_SKIP = []
RARE_EXTE_SKIP = [52, 53, 54]
EPIC_EXTE_SKIP = [52, 53, 54, 62]
LEGE_EXTE_SKIP = [7, 33, 52, 53, 54, 62]
LIMI_EXTE_SKIP = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61]

COMM = 'Common'
UNCO = 'Uncommon'
RARE = 'Rare'
EPIC = 'Epic'
LEGE = 'Legendary'
LIMI = 'LimitedLegendary'

nCOMM = '1.Common'
nUNCO = '2.Uncommon'
nRARE = '3.Rare'
nEPIC = '4.Epic'
nLEGE = '5.Legendary'
nLIMI = '6.LimitedLegendary'

def main():
    print(get_hero_dict())
    print(get_exte_dict())


def get_hero_dict():
    hero_d = {}

    hero_d.update(make_dict('hero', COMM_HEAD, COMM_HERO_IMPLE, COMM, nCOMM, COMM_HERO_SKIP))
    hero_d.update(make_dict('hero', UNCO_HEAD, UNCO_HERO_IMPLE, UNCO, nUNCO, UNCO_HERO_SKIP))
    hero_d.update(make_dict('hero', RARE_HEAD, RARE_HERO_IMPLE, RARE, nRARE, RARE_HERO_SKIP))
    hero_d.update(make_dict('hero', EPIC_HEAD, EPIC_HERO_IMPLE, EPIC, nEPIC, EPIC_HERO_SKIP))
    hero_d.update(make_dict('hero', LEGE_HEAD, LEGE_HERO_IMPLE, LEGE, nLEGE, LEGE_HERO_SKIP))

    return hero_d


def get_exte_dict():
    exte_d = {}

    exte_d.update(make_dict('exte', COMM_HEAD, COMM_EXTE_IMPLE, COMM, nCOMM, COMM_EXTE_SKIP))
    exte_d.update(make_dict('exte', UNCO_HEAD, UNCO_EXTE_IMPLE, UNCO, nUNCO, UNCO_EXTE_SKIP))
    exte_d.update(make_dict('exte', RARE_HEAD, RARE_EXTE_IMPLE, RARE, nRARE, RARE_EXTE_SKIP))
    exte_d.update(make_dict('exte', EPIC_HEAD, EPIC_EXTE_IMPLE, EPIC, nEPIC, EPIC_EXTE_SKIP))
    exte_d.update(make_dict('exte', LEGE_HEAD, LEGE_EXTE_IMPLE, LEGE, nLEGE, LEGE_EXTE_SKIP))
    exte_d.update(make_dict('exte', LIMI_HEAD, LIMI_EXTE_IMPLE, LIMI, nLIMI, LIMI_EXTE_SKIP))

    return exte_d


def make_dict(type, head, imple, rarity, nrarity, skip):
    return_d = {}

    for i in range(0, imple):

        d = {}
        meta = None
        id = head + str(i + 1).zfill(2)

        if i + 1 not in skip:
            if type == 'hero':
                meta = mch.get_hero_type_metadata(id)
            elif type == 'exte':
                meta = mch.get_extension_type_metadata(id)

        if meta:
            d['name_en'] = meta['name']['en']
            d['name_ja'] = meta['name']['ja']
            d['name_zh'] = meta['name']['zh']
            d['rarity'] = rarity
            d['nrarity'] = nrarity
            return_d[id] = d

    return return_d


if __name__ == "__main__":
    main()
