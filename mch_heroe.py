
class MCHHeroeData:

    def __init__(self):
        self.hero_data = None
        self.type_data = None


    def set_hero_data(self, metadata):
        self.hero_data = metadata


    def set_hero_type_data(self, metadata):
        self.type_data = metadata


    def get_hero_id(self):
        if self.hero_data is None:
            return None
        else:
            return self.hero_data['attributes']['id']


    def get_hero_lv(self):
        if self.hero_data is None:
            return None
        else:
            return self.hero_data['attributes']['lv']


    def get_hero_rarity(self):
        if self.hero_data is None:
            return None
        else:
            return self.hero_data['attributes']['rarity']


    def get_hero_url(self):
        if self.hero_data is None:
            return None
        else:
            return self.hero_data['external_url']


    def get_hero_type(self):
        if self.hero_data is None:
            return None
        else:
            return self.hero_data['extra_data']['hero_type']


    def get_hero_name_ja(self):
        if self.type_data is None:
            return None
        else:
            return self.type_data['name']['ja']
