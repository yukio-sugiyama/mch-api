# インストールした discord.py を読み込む
import discord
import get_data

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTM4NjExOTg0NjgyMzE5ODgy.XW4Xyg.5KpaMkTgMhRk4RehAL20oj2TT7g'

# 接続に必要なオブジェクトを生成
client = discord.Client()
data = get_data.GetOwnedAssets()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました {0.user}'.format(client))

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('asset:'):
        id = message.content.replace('asset:', '').strip()
        data_set = data.get_owned_assets(id)

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

        await message.channel.send(send_message)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)