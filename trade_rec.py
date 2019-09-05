import logging
import get_data
import time
import datetime
import schedule

data = get_data.GetOwnedAssets()

def trade_rec():

    now = datetime.datetime.now()
    old = now - datetime.timedelta(hours=24)

    since = int(old.timestamp())
    until = int(now.timestamp())

    hero_sold_set = data.get_hero_sold_csv(since, until)

    f_hero = open('hero.csv','a')

    for x in hero_sold_set:
        hero_csv = []

        hero_csv.append(x['trade_id'])
        hero_csv.append(x['hero_id'])
        hero_csv.append(x['sold_at'])
        hero_csv.append(x['price'])
        hero_csv.append(x['ce'])
        hero_csv.append(x['seller_id'])
        hero_csv.append(x['buyer_id'])
        hero_csv.append(x['sold_time'])
        hero_csv.append('\n')

        f_hero.write(','.join(map(str, hero_csv)))

    f_hero.close()

    exte_sold_set = data.get_exte_sold_csv(since, until)

    f_exte = open('exte.csv','a')

    for x in exte_sold_set:
        exte_csv = []

        exte_csv.append(x['trade_id'])
        exte_csv.append(x['extension_id'])
        exte_csv.append(x['sold_at'])
        exte_csv.append(x['price'])
        exte_csv.append(x['ce'])
        exte_csv.append(x['seller_id'])
        exte_csv.append(x['buyer_id'])
        exte_csv.append(x['sold_time'])
        exte_csv.append('\n')

        f_exte.write(','.join(map(str, exte_csv)))

    f_exte.close()


# 毎日稼働ジョブの設定
schedule.every().day.at('16:30').do(trade_rec)


while True:

    schedule.run_pending()

    time.sleep(5)
