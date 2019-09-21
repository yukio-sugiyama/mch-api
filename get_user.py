from pprint import pprint
import mch_apis

api = mch_apis.MCHAPI()

for i in range(9):

    land = api.get_land_info(i+1)
    print('{0} {1}'.format(land['name'], len(land['citizens'])))
