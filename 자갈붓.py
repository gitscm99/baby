import discord
import random
import time
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("--------------------")
    await client.change_presence(game=discord.Game(name='!명령어 7호기', type=0))

@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕, 나는 자갈봇 이야!")

    if message.content.startswith('!따라해'):
        learn = message.content.replace('!따라해', "")
        await client.send_message(message.channel, learn + ':heart: ')

    if message.content.startswith('!핑'):
        before = time.monotonic()
        msg = await client.send_message(message.channel, ':ping_pong: 퐁!')
        ping = (time.monotonic() - before) * 1000
        text = "퐁!  {0}ms ".format((round(ping, 1)))
        await client.edit_message(msg, text)

    if message.content.startswith('!주사위'):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(1, int(rolld[0]) + 1):
            dice += random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))

    if message.content.startswith('!뭐먹지?'):
        food = "밥 치밥 피자 치킨 떡볶이"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber - 1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('!투표'):
        vote = message.content[4:].split("/")
        await client.send_message(message.channel, "★투표- " + vote[0])
        for i in range(1, len(vote)):
            choose = await client.send_message(message.channel, "```" + vote[i] + "```")
            await client.add_reaction(choose, '✔')

    if message.content.startswith('!서버'):
        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.channel, '\n'.join(list))

    if message.content.startswith("!수"):
        content_list = message.content.split(" ")
        content_list = content_list[1:]
        for i in range(0, len(content_list)):
            content_list[i] = int(content_list[i])
        content_list = sorted(content_list)
        await client.send_message(message.channel, content_list[-2])

    if message.content.startswith('!게임'):
        food = "좀비고등학교 마인크래프트 브롤스타즈 클래시로얄 로블록스"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('!시간'):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        await client.send_message(message.channel, str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 입니다!")

    if message.content.startswith('!정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(coler=0x00ffbb)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버이름", value=message.author.display_name, inline=True)
        embed.add_field(name="계정생성일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
