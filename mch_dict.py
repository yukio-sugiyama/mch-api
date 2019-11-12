import time
from pprint import pprint

from . import mch_apis

mch = mch_apis.MCHAPI()

COMM_HEAD = '10'
UNCO_HEAD = '20'
RARE_HEAD = '30'
EPIC_HEAD = '40'
LEGE_HEAD = '50'

COMM_HERO_IMPLE = 2
UNCO_HERO_IMPLE = 34
RARE_HERO_IMPLE = 38
EPIC_HERO_IMPLE = 40
LEGE_HERO_IMPLE = 19

COMM_HERO_SKIP = []
UNCO_HERO_SKIP = []
RARE_HERO_SKIP = [33]
EPIC_HERO_SKIP = []
LEGE_HERO_SKIP = []

COMM_EXTE_IMPLE = 55
UNCO_EXTE_IMPLE = 55
RARE_EXTE_IMPLE = 55
EPIC_EXTE_IMPLE = 55
LEGE_EXTE_IMPLE = 55

COMM_EXTE_SKIP = [7, 33, 52, 53, 54]
UNCO_EXTE_SKIP = []
RARE_EXTE_SKIP = [52, 53, 54]
EPIC_EXTE_SKIP = [52, 53, 54]
LEGE_EXTE_SKIP = [7, 33, 52, 53, 54]

COMM = 'Common'
UNCO = 'Uncommon'
RARE = 'Rare'
EPIC = 'Epic'
LEGE = 'Legendary'

nCOMM = '1.Common'
nUNCO = '2.Uncommon'
nRARE = '3.Rare'
nEPIC = '4.Epic'
nLEGE = '5.Legendary'

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
