import discord
import datetime
import asyncio
from Dtime import Uptime
token = 'NzI5MjcyNzAyMDk0OTM0MDY2.XwKFYQ.tVtWlRlOd9zi8o8OWNzxYW6U2EI'
client = discord.Client()
Uptime.uptimeset()
@client.event
async def on_ready():
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message(message):
    if message.content == '도움말':
        embed=discord.Embed(color=0xff00, title=":notebook_with_decorative_cover: 도움말 모음 :notebook_with_decorative_cover:", description="*아래 항목들을\n채팅창에 적으세요.*", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name = '시간 명령어', value = '`!타이머\n!업타임`') 
        embed.add_field(name = '유저 명령어', value = '`!내정보`')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/682991051950391367/729680143789850654/12121.png?size=636")
        await message.channel.send(embed=embed)
    if message.content == '김형우':
        embed=discord.Embed(color=0xff00, title="김형우가 누구인가", description="사람", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content == '!내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"`{message.author}님입니다.`")
    if message.content == '!타이머':
        await message.channel.send('`타이머는 10초, 1분만 가능\n사용법 : ex) 타이머 10초`')
    if message.content == "타이머 10초":
        await message.channel.send('타이머 10초가 시작되었습니다.')
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}님 10초가 지났어요!")
    if message.content == "타이머 1분":
        await message.channel.send('타이머 1분이 시작되었습니다.')
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention}님 1분이 지났어요!")
    if message.content == '!업타임':
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await message.channel.send(f"{hours}시간 {minitues}분 {seconds}초")

client.run(token)
