import mch_apis
import mch_heroe

class GetOwnedAssets:

    def __init__(self):
        self.mch = mch_apis.MCHAPI()
        self.hero = mch_heroe.MCHHeroeData()


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

    def get_owned_assets(self, user_id):
        hero_ids = self.get_hero_ids(user_id)
        extension_ids = self.get_extension_ids(user_id)

        hero_data_set = []

        for id in hero_ids:

            hero_metadata = self.get_hero_metadata(id)
            self.hero.set_hero_data(hero_metadata)

            type = self.hero.get_hero_type()

            hero_type_metadata = self.get_hero_type_metadata(type)
            self.hero.set_hero_type_data(hero_type_metadata)

            rarity = self.hero.get_hero_rarity()
            name = self.hero.get_hero_name_ja()
            id = self.hero.get_hero_id()
            lv = self.hero.get_hero_lv()
            url = self.hero.get_hero_url()

            hero_data = {'rarity':rarity, 'name':name, 'id':id, 'lv':lv}

            hero_data_set.append(hero_data)

        return hero_data_set
