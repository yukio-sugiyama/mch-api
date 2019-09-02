import mch_apis

mch = mch_apis.MCHAPI()

value = mch.get_hero_metadata(50010001)
print(value)

value = mch.get_hero_type_metadata(5001)
print(value)

value = mch.get_extension_metadata(50010001)
print(value)

value = mch.get_extension_type_metadata(5001)
print(value)

value = mch.get_skill_metadata(1)
print(value)

value = mch.get_referral_history('0x96c4c9CD98eB02ba00F2731e4ffB965Fa2A41923')
print(value)

value = mch.get_hero_asset('0x96c4c9CD98eB02ba00F2731e4ffB965Fa2A41923')
print(value)

value = mch.get_extension_asset('0x96c4c9CD98eB02ba00F2731e4ffB965Fa2A41923')
print(value)

value = mch.get_user_info('10043')
print(value)

value = mch.get_land_info('05')
print(value)

value = mch.get_hero_asset_info('10043')
print(value)
