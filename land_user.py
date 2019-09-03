import mch_apis

mch = mch_apis.MCHAPI()

value = mch.get_land_info('5')

for x in value['citizens']:
    info = mch.get_user_info(x)
    print(info['user_data']['name'])
#    print(info)
