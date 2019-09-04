import datetime

import mch_apis
import mch_heroe
import mch_extension

class GetOwnedAssets:

    def __init__(self):
        self.mch = mch_apis.MCHAPI()
        self.hero = mch_heroe.MCHHeroeData()
        self.exte = mch_extension.MCHExtensionData()


    def get_eth(self, user_id):
        res = self.mch.get_user_info(user_id)
        return res['user_data']['eth']


    def get_hero_ids_eth(self, eth):
        res = self.mch.get_hero_asset(eth)
        return res['hero_ids']


    def get_hero_ids_crypto(self, user_id):
        res = self.mch.get_hero_asset_info(user_id)
        return res['hero_ids']


    def get_extension_ids_eth(self, eth):
        res = self.mch.get_extension_asset(eth)
        return res['extension_ids']

    def get_hero_ids(self, user_id):
        hero_asset = []

        eth = self.get_eth(user_id)

        hero_asset.extend(self.get_hero_ids_eth(eth))
        hero_asset.extend(self.get_hero_ids_crypto(user_id))
        hero_asset.sort()

        return hero_asset

    def get_extension_ids(self, user_id):
        extension_asset = []

        eth = self.get_eth(user_id)

        extension_asset.extend(self.get_extension_ids_eth(eth))
        extension_asset.sort()

        return extension_asset


    def get_hero_metadata(self, id):

        return self.mch.get_hero_metadata(id)


    def get_hero_type_metadata(self, id):

        return self.mch.get_hero_type_metadata(id)


    def get_exte_metadata(self, id):

        return self.mch.get_extension_metadata(id)


    def get_exte_type_metadata(self, id):

        return self.mch.get_extension_type_metadata(id)


    def get_user_name(self, user_id):
        res = self.mch.get_user_info(user_id)
        if 'name' in res['user_data']:
            return res['user_data']['name']
        else:
            return ''


    def get_owned_assets(self, user_id):
        hero_ids = self.get_hero_ids(user_id)
        extension_ids = self.get_extension_ids(user_id)

        hero_data_set = []

        for id in hero_ids:

            hero_metadata = self.get_hero_metadata(id)
            self.hero.set_data(hero_metadata)

            type = self.hero.get_type()

            hero_type_metadata = self.get_hero_type_metadata(type)
            self.hero.set_type_data(hero_type_metadata)

            rarity = self.hero.get_rarity()
            name = self.hero.get_name_ja()
            id = self.hero.get_id()
            lv = self.hero.get_lv()
            url = self.hero.get_url()

            hero_data = {'rarity':rarity, 'name':name, 'id':id, 'lv':lv}

            hero_data_set.append(hero_data)

        return hero_data_set

    def get_hero_sold(self, since = '', until = ''):

        hero_sold = self.mch.get_hero_sold_trades(since, until)

        hero_sold_set = []
        for x in hero_sold:
            id = x['hero_id']
            time = x['sold_at']
            sold_price = x['price']
            ce = x['ce']
            seller_id = x['seller_id']
            buyer_id = x['buyer_id']

#            seller_name = self.get_user_name(seller_id)
#            buyer_name = self.get_user_name(buyer_id)


            sold_time = datetime.datetime.fromtimestamp(time)

            hero_metadata = self.get_hero_metadata(id)
            self.hero.set_data(hero_metadata)

            type = self.hero.get_type()

            hero_type_metadata = self.get_hero_type_metadata(type)
            self.hero.set_type_data(hero_type_metadata)

            name = self.hero.get_name_ja()

            hero_sold = {'sold_time':sold_time
                        , 'name':name
                        , 'sold_price':sold_price
                        , 'ce':ce
                        , 'seller_id':seller_id
                        , 'buyer_id':buyer_id
                        }

            hero_sold_set.append(hero_sold)

#            print('{:0} {:1} 価格:{:2,} CE:{:3,} 売:{:4} 買:{:5}'.format(sold_time, name, sold_price, ce, seller_id, buyer_id))

        return hero_sold_set

    def get_exte_sold(self, since = '', until = ''):

        exte_sold = self.mch.get_extension_sold_trades(since, until)

        exte_sold_set = []
        for x in exte_sold:
            id = x['extension_id']
            time = x['sold_at']
            sold_price = x['price']
            ce = x['ce']
            seller_id = x['seller_id']
            buyer_id = x['buyer_id']

#            seller_name = self.get_user_name(seller_id)
#            buyer_name = self.get_user_name(buyer_id)


            sold_time = datetime.datetime.fromtimestamp(time)

            exte_metadata = self.get_exte_metadata(id)
            self.exte.set_data(exte_metadata)

            type = self.exte.get_type()

            exte_type_metadata = self.get_exte_type_metadata(type)
            self.exte.set_type_data(exte_type_metadata)

            name = self.exte.get_name_ja()

            exte_sold = {'sold_time':sold_time
                        , 'name':name
                        , 'sold_price':sold_price
                        , 'ce':ce
                        , 'seller_id':seller_id
                        , 'buyer_id':buyer_id
                        }

            exte_sold_set.append(exte_sold)

#            print('{:0} {:1} 価格:{:2,} CE:{:3,} 売:{:4} 買:{:5}'.format(sold_time, name, sold_price, ce, seller_id, buyer_id))

        return exte_sold_set
