
class MCHHeroData:

    def __init__(self):
        self.data = None
        self.type_data = None


    def set_data(self, metadata):
        self.data = metadata


    def set_type_data(self, metadata):
        self.type_data = metadata


    def get_lv(self):
        if self.data is None:
            return None
        else:
            return self.data['attributes']['lv']


    def get_rarity(self):
        if self.data is None:
            return None
        else:
            return self.data['attributes']['rarity']


    def get_url(self):
        if self.data is None:
            return None
        else:
            return self.data['external_url']


    def get_type(self):
        if self.data is None:
            return None
        else:
            return self.data['extra_data']['hero_type']


    def get_name_ja(self):
        if self.type_data is None:
            return None
        else:
            return self.type_data['name']['ja']


    def get_type_rarity(self):
        if self.type_data is None:
            return None
        else:
            return self.type_data['rarity']
