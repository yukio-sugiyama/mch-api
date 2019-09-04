import mch_apis
import datetime
import mch_heroe
import mch_extension

mch = mch_apis.MCHAPI()
hero = mch_heroe.MCHHeroeData()
exte = mch_extension.MCHExtensionData()

def get_hero_metadata(id):

    return mch.get_hero_metadata(id)


def get_hero_type_metadata(id):

    return mch.get_hero_type_metadata(id)


def get_extension_metadata(id):

    return mch.get_extension_metadata(id)


def get_extension_type_metadata(id):

    return mch.get_extension_type_metadata(id)


def get_user_name(user_id):
    res = mch.get_user_info(user_id)
    if 'name' in res['user_data']:
        return res['user_data']['name']
    else:
        return ''

hero_sold = mch.get_hero_sold_trades()

for x in hero_sold:
    id = x['hero_id']
    time = x['sold_at']
    sold_price = x['price']
    ce = x['ce']
    seller_id = x['seller_id']
    buyer_id = x['buyer_id']
    seller_name = get_user_name(seller_id)
    buyer_name = get_user_name(buyer_id)


    sold_time = datetime.datetime.fromtimestamp(time)

    hero_metadata = get_hero_metadata(id)
    hero.set_data(hero_metadata)

    type = hero.get_type()

    hero_type_metadata = get_hero_type_metadata(type)
    hero.set_type_data(hero_type_metadata)

    name = hero.get_name_ja()

    print('time:{:0} name:{:1} price:{:2,} ce:{:3,} 売手:{:4}{:5} 買手{:6}{:7}'.format(sold_time, name, sold_price, ce, seller_id, seller_name, buyer_id, buyer_name))

exte_sold = mch.get_extension_sold_trades()

for x in exte_sold:
    id = x['extension_id']
    time = x['sold_at']
    sold_price = x['price']
    ce = x['ce']
    seller_id = x['seller_id']
    buyer_id = x['buyer_id']
    seller_name = get_user_name(seller_id)
    buyer_name = get_user_name(buyer_id)


    sold_time = datetime.datetime.fromtimestamp(time)

    exte_metadata = get_extension_metadata(id)
    exte.set_data(exte_metadata)

    type = exte.get_type()

    exte_type_metadata = get_extension_type_metadata(type)
    exte.set_type_data(exte_type_metadata)

    name = exte.get_name_ja()

    print('time:{0} name:{1} price:{2} ce:{3} 売手:{4}{5} 買手{6}{7}'.format(sold_time, name, sold_price, ce, seller_id, seller_name, buyer_id, buyer_name))
