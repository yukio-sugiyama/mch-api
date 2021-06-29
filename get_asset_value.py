from pprint import pprint
import mch_apis

api = mch_apis.MCHAPI()

asset_d = {}

def get_asset(id):
    global asset_d

    asset_d[id] = {'hero':{'1':0,'2':0,'3':0,'4':0,'5':0}, 'exte':{'1':0,'2':0,'3':0,'4':0,'5':0}}

    res = api.get_hero_asset_info(id)
    if res:
        for x in res['hero_ids']:
            asset_d[id]['hero'][str(x)[0:1]] = asset_d[id]['hero'][str(x)[0:1]] + 1

    res = api.get_extension_asset_info(id)
    if res:
        for x in res['extension_ids']:
            asset_d[id]['exte'][str(x)[0:1]] = asset_d[id]['exte'][str(x)[0:1]] + 1

def get_user_name(id):
    res = api.get_user_info(id)
    if res and res['user_data']['name']:
        return res['user_data']['name']
    else:
        return None

if __name__ == "__main__":
    user_l = [
                30782,
                20127,
                32200,
                49596,
                20601,
            ]

    for id in user_l:
        get_asset(id)

    for x in asset_d:
        name = get_user_name(x)

        asset_value = 0
        asset_value = asset_value + asset_d[x]['hero']['1'] * 1
        asset_value = asset_value + asset_d[x]['hero']['2'] * 2
        asset_value = asset_value + asset_d[x]['hero']['3'] * 3
        asset_value = asset_value + asset_d[x]['hero']['4'] * 4
        asset_value = asset_value + asset_d[x]['hero']['5'] * 5

        asset_value = asset_value + asset_d[x]['exte']['1'] * 1
        asset_value = asset_value + asset_d[x]['exte']['2'] * 2
        asset_value = asset_value + asset_d[x]['exte']['3'] * 3
        asset_value = asset_value + asset_d[x]['exte']['4'] * 4
        asset_value = asset_value + asset_d[x]['exte']['5'] * 5

        print(f"{x}, {name}, {asset_value}")
