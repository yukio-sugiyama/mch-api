from pprint import pprint
import mch_apis
import time

api = mch_apis.MCHAPI()

base = 10000
i = 0

n_ct = 0

res = api.get_user_info(37359)
print(res)

"""
for i in range(100):
    try:
        res = api.get_user_info(base + i)
    except Exception as e:
        print(f"res:{res}")
        print(f"e:{e}")
        res = None
    if res:
        print(res)
"""
#        n_ct = 0
#        res = res['user_data']
#        with open('user_info.csv', 'a') as f:
#            print(f"{res['uid']}, {res['name']}, {res['eth'] if 'eth' in res else ''}, {res['ema_levels'] if 'ema_levels' in res else ''}", file=f)

#    else:
#        n_ct += 1
#        if n_ct > 1:
#            break
