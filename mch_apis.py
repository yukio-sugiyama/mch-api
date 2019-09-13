import logging
import requests, json

class MCHAPI:

    def __init__(self):

        # METADATA API URL
        self.hero_metadata = 'https://www.mycryptoheroes.net/metadata/hero/'
        self.hero_type_metadata = 'https://www.mycryptoheroes.net/metadata/heroType/'
        self.extension_metadata = 'https://www.mycryptoheroes.net/metadata/extension/'
        self.extension_type_metadata = 'https://www.mycryptoheroes.net/metadata/extensionType/'
        self.skill_metadata = 'https://www.mycryptoheroes.net/metadata/skill/'

        # ETH PROXY API URL
        self.referral_history = 'https://www.mycryptoheroes.net/referrer/history/'
        self.hero_asset = 'https://www.mycryptoheroes.net/api/proxy/HeroAsset/heroes/'
        self.extension_asset = 'https://www.mycryptoheroes.net/api/proxy/ExtensionAsset/extensions/'

        # MCH PROXY API
        self.user_info = 'https://www.mycryptoheroes.net/api/proxy/mch/users/'
        self.land_info = 'https://www.mycryptoheroes.net/api/proxy/mch/lands/'
        self.hero_asset_info = 'https://www.mycryptoheroes.net/api/proxy/mch/heroes/'
        self.extension_asset_info = 'https://www.mycryptoheroes.net/api/proxy/mch/extensions/'
        self.hero_sold_trades = 'https://www.mycryptoheroes.net/api/proxy/mch/trades/heroes/sold'
        self.extension_sold_trades = 'https://www.mycryptoheroes.net/api/proxy/mch/trades/extensions/sold'

        # logger set
        # Prints logger info to terminal
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
        self.ch = logging.StreamHandler()
        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # add formatter to ch
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.ch)


    # 指定したHeroIDを持つHeroのMetadataを取得する
    # id = HeroID
    def get_hero_metadata(self, id):
        try:
            req = self.hero_metadata + str(id)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # 指定したHeroTypeIDを持つHeroTypeのMetadataを取得する
    # id = HeroTypeID
    def get_hero_type_metadata(self, id):
        try:
            req = self.hero_type_metadata + str(id)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # 指定したExtensionIDを持つエクステンションのMetadataを取得する
    # id = ExtensionID
    def get_extension_metadata(self, id):
        try:
            req = self.extension_metadata + str(id)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # 指定したextensionTypeIdを持つExtensionTypeのMetadataを取得する
    # id = ExtensionTypeID
    def get_extension_type_metadata(self, id):
        try:
            req = self.extension_type_metadata + str(id)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # 指定したskillTypeIDを持つスキルのMetadataを取得する
    # id = SkillTypeID
    def get_skill_metadata(self, id):
        try:
            req = self.skill_metadata + str(id)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # リファラル報酬の履歴一覧を取得する
    # address = EthAddress
    def get_referral_history(self, address):
        try:
            req = self.referral_history + str(address)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # EthNetworkに存在するオリジナルヒーローのID一覧を取得する
    # address = EthAddress
    def get_hero_asset(self, address):
        try:
            req = self.hero_asset + str(address)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # EthNetworkに存在するオリジナルエクステンションのID一覧を取得する
    # address = EthAddress
    def get_extension_asset(self, address):
        try:
            req = self.extension_asset + str(address)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # 指定したIDを持つユーザーに関する情報を取得する
    # また、idの部分をそのユーザーのEthアドレスに置き換えることでも取得することが可能
    # （ゲーム内でEthアドレスを公開しているユーザーのみ）
    # id = UserID or EthAddress
    def get_user_info(self, id):
        try:
            req = self.user_info + str(id)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # 指定したLandTypeのLand情報を取得する
    # id = LandType
    def get_land_info(self, id):
        try:
            req = self.land_info + str(id)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # 指定したIDのユーザーが所持するオリジナルヒーローのID一覧を取得する
    # id = UserID
    def get_hero_asset_info(self, id):
        try:
            req = self.hero_asset_info + str(id)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # 指定したIDのユーザーが所持するオリジナルヒーローのID一覧を取得する
    # id = UserID
    def get_extension_asset_info(self, id):
        try:
            req = self.extension_asset_info + str(id)
            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # トレード済みのHero一覧を取得を取得する
    # 最大で24時間分のデータが取得できます。since、untilで期間を指定してください。
    # since = start time(unix), until = end time(unix)
    def get_hero_sold_trades(self, since = '', until = ''):
        try:
            req = self.hero_sold_trades

            if since != '' and until == '':
                req = req + '?since=' + str(since)

            elif since == '' and until != '':
                req = req + '?until=' + str(until)

            elif since != '' and until != '':
                req = req + '?since=' + str(since) + '&until=' + str(until)

            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None


    # トレード済みのExtension一覧を取得を取得する
    # 最大で24時間分のデータが取得できます。since、untilで期間を指定してください。
    # since = start time(unix), until = end time(unix)
    def get_extension_sold_trades(self, since = '', until = ''):
        try:
            req = self.extension_sold_trades

            if since != '' and until == '':
                req = req + '?since=' + str(since)

            elif since == '' and until != '':
                req = req + '?until=' + str(until)

            elif since != '' and until != '':
                req = req + '?since=' + str(since) + '&until=' + str(until)

            res = requests.get(req)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            self.logger.error(e)
            return None
