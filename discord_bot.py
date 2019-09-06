# インストールした discord.py を読み込む
import discord
import datetime

import get_data

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTM4NjExOTg0NjgyMzE5ODgy.XXC-OQ.IRFI3isZYCu32hSXx54UHE-keTw'
ENABLE_CH = [618639034490552340]

# 接続に必要なオブジェクトを生成
client = discord.Client()
data = get_data.GetData()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました {0.user}'.format(client))

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    if message.channel.id in ENABLE_CH:

        if message.author == client.user:
            return

        if message.content.startswith('asset:'):
            id = message.content.replace('asset:', '').strip()
            user_name = data.get_user_name(id)

            send_message = '{0}さんのヒーロー情報取ってくるよ！'.format(user_name + '#' + id)
            await message.channel.send(send_message)

            data_set = data.get_hero_assets(id)

            old_rarity = None
            send_message = ''

            for x in data_set:
                rarity = x['rarity']
                name = x['name']
                id = x['id']
                lv = x['lv']

                if not old_rarity == rarity:
                    send_message = send_message + '\n----------\n{0}\n----------'.format(rarity)

                old_rarity = rarity
                send_message = send_message + '\n  {0} Lv.{1} '.format(name, lv)

                if 1800 < len(send_message):
                    await message.channel.send(send_message)
                    send_message = ''

            await message.channel.send(send_message)

            send_message = '次はエクステンション情報取ってくるよ！'
            await message.channel.send(send_message)

            data_set = data.get_exte_assets(id)

            old_rarity = None
            send_message = ''

            for x in data_set:
                rarity = x['rarity']
                name = x['name']
                id = x['id']
                lv = x['lv']

                if not old_rarity == rarity:
                    send_message = send_message + '\n----------\n{0}\n----------'.format(rarity)

                old_rarity = rarity
                send_message = send_message + '\n  {0} Lv.{1} '.format(name, lv)

                if 1800 < len(send_message):
                    await message.channel.send(send_message)
                    send_message = ''

            await message.channel.send(send_message)

            send_message = '取ってきました！'
            await message.channel.send(send_message)

        if message.content.startswith('asset HERO:'):
            id = message.content.replace('asset HERO:', '').strip()
            user_name = data.get_user_name(id)

            send_message = '{0}さんのヒーロー情報取ってくるよ！'.format(user_name + '#' + id)
            await message.channel.send(send_message)

            data_set = data.get_hero_assets(id)

            old_rarity = None
            send_message = ''

            for x in data_set:
                rarity = x['rarity']
                name = x['name']
                id = x['id']
                lv = x['lv']

                if not old_rarity == rarity:
                    send_message = send_message + '\n----------\n{0}\n----------'.format(rarity)

                old_rarity = rarity
                send_message = send_message + '\n  {0} Lv.{1} '.format(name, lv)

                if 1800 < len(send_message):
                    await message.channel.send(send_message)
                    send_message = ''

            await message.channel.send(send_message)

            send_message = '取ってきました！'
            await message.channel.send(send_message)

        if message.content.startswith('asset EXTE:'):
            id = message.content.replace('asset EXTE:', '').strip()
            user_name = data.get_user_name(id)

            send_message = '{0}さんのエクステンション情報取ってくるよ！'.format(user_name + '#' + id)
            await message.channel.send(send_message)

            data_set = data.get_exte_assets(id)

            old_rarity = None
            send_message = ''

            for x in data_set:
                rarity = x['rarity']
                name = x['name']
                id = x['id']
                lv = x['lv']

                if not old_rarity == rarity:
                    send_message = send_message + '\n----------\n{0}\n----------'.format(rarity)

                old_rarity = rarity
                send_message = send_message + '\n  {0} Lv.{1} '.format(name, lv)

                if 1800 < len(send_message):
                    await message.channel.send(send_message)
                    send_message = ''

            await message.channel.send(send_message)

            send_message = '取ってきました！'
            await message.channel.send(send_message)

        if message.content.startswith('trade:hero'):
            hero_sold_set = data.get_hero_sold()

            send_message = ''

            for x in hero_sold_set:
                sold_time = x['sold_time'].strftime("%Y/%m/%d %H:%M:%S")
                name = x['name']
                sold_price = '{:,}'.format(x['sold_price'])
                ce = '{:,}'.format(x['ce'])
                seller_id = x['seller_id']
                buyer_id = x['buyer_id']

                send_message = send_message + '\n{0} {1} 価格:{2} CE:{3} 売手:{4} 買手:{5}'.format(sold_time, name, sold_price, ce, seller_id, buyer_id)

                if 1800 < len(send_message):
                    await message.channel.send(send_message)
                    send_message = ''

            await message.channel.send(send_message)

        if message.content.startswith('trade:extension'):
            exte_sold_set = data.get_exte_sold()

            send_message = ''

            for x in exte_sold_set:
                sold_time = x['sold_time'].strftime("%Y/%m/%d %H:%M:%S")
                name = x['name']
                sold_price = '{:,}'.format(x['sold_price'])
                ce = '{:,}'.format(x['ce'])
                seller_id = x['seller_id']
                buyer_id = x['buyer_id']

                send_message = send_message + '\n{0} {1} 価格:{2} CE:{3} 売手:{4} 買手:{5}'.format(sold_time, name, sold_price, ce, seller_id, buyer_id)

                if 1800 < len(send_message):
                    await message.channel.send(send_message)
                    send_message = ''

            await message.channel.send(send_message)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
