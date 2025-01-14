import asyncio
import discord
import csv
import random
from dotenv import load_dotenv
import os
from discord.ext import commands

emoji = {
    "Water": "<:water:1031677118163189851>",
    "Fire": "<:fire2:1031677040224653332>",
    "Thunder": "<:thunder:1031677087691587614>",
    "Dragon": "<:dragon2:1031677165030346792>",
    "Ice": "<:ice:1031677068523614308>",
    "None": ""
}
color = {
    "Fire":0xFF4500,
    "Water": 0xADD8E6,
    "Dragon": 0x8A2BE2,
    "Ice": 0x87CEFA,
    "Thunder": 0xFFFF00,
    "None": 0x9F9F9F
}

left = '⏪'
right = '⏩'

newcolor = {
    "0x008000": 0x008000,
    "0xFFA500": 0xFFA500,
    "0x1E90FF": 0x1E90FF,
    "0xADD8E6": 0xADD8E6,
    "0xB0C4DE": 0xB0C4DE,
    "0x32CD32": 0x32CD32,
    "0xD2B48C": 0xD2B48C,
    "0xFF0000": 0xFF0000
}
datamap=[]
with open('Maps.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        datamap.append(row)


datamonster=[]
with open('Monsters.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        datamonster.append(row)


bot=commands.Bot(command_prefix="^^", intents= discord.Intents.all())

@bot.event
async def on_ready():
    print('yep')
    await bot.change_presence(
        activity=discord.Game('Monster Hunter 4 Ultimate'))



class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value= None
    @discord.ui.button(label=left,style=discord.ButtonStyle.grey)
    async def button_left(self, interaction: discord.Interaction, button:discord.ui.Button):
        name= interaction.message.embeds[0].title[:-4][-4:]
        name2= interaction.message.embeds[0].title[:4]
        for i in range(len(datamap)):
            if ((datamap[i][0].lower())[-4:] == name.lower() or (datamap[i][1].lower())[-4:] == name.lower() or datamap[i][0].lower()[:4] == name2.lower() or datamap[i][1].lower()[:4] == name2.lower()):
                if ((datamap[i-1][0].lower())[-4:] == datamap[i][0].lower()[-4:] or (datamap[i-1][1].lower())[-4:] == datamap[i][1].lower()[-4:] or (datamap[i-1][0].lower())[:4] == datamap[i][0].lower()[:4] or (datamap[i-1][1].lower())[:4] == datamap[i][1].lower()[:4]):
                    embed = discord.Embed(
                        title=f'{datamap[i-1][0]} Map',
                        url='https://kiranico.com/en/mh4u',
                        description=None,
                        color=newcolor[datamap[i-1][3]]

                    )

                    embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                                     icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

                    embed.set_image(url=f'{datamap[i-1][2]}')

                    await interaction.response.edit_message(embed=embed, content='')
            else:
                pass

        name = interaction.message.embeds[0].title[9:]
        for j in range(len(datamonster)):
            if ((datamonster[j][1].lower()) == name.lower()):
                if ((datamonster[j-1][1].lower())[-4:] == datamonster[j][1].lower()[-4:]):
                    ele = f'{datamonster[j-1][2]} {emoji[datamonster[j-1][2]]}'
                    if datamonster[j-1][3] != '0':
                        ele = ele + f' & {datamonster[j-1][3]} {emoji[datamonster[j-1][3]]}'

                    weak = f'{datamonster[j-1][4]} {emoji[datamonster[j-1][4]]}'
                    if datamonster[j-1][5] != '0':
                        weak = weak + f' & {datamonster[j-1][5]} {emoji[datamonster[j-1][5]]}'
                        if datamonster[j-1][9] != '0':
                            weak = weak + f' & {datamonster[j-1][9]} {emoji[datamonster[j-1][9]]}'

                    embed = discord.Embed(
                        title=f'Monster: {datamonster[j-1][1]}',
                        url='https://mogapedia.fandom.com/fr/wiki/Monster_Hunter_4_Ultimate',
                        description=datamonster[j-1][10],
                        color=color[datamonster[j-1][2]]
                    )
                    embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                                     icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

                    embed.set_image(url=f'{datamonster[j-1][8]}')

                    embed.add_field(
                        name="Element",
                        value=ele
                    )
                    embed.add_field(
                        name="Weakness",
                        value=weak
                    )

                    embed.add_field(
                        name="Weakness part",
                        value=f'{datamonster[j-1][6]}',
                        inline=False
                    )

                    embed.add_field(
                        name="(Base) Health Points",
                        value=f'{datamonster[j-1][7]} '
                    )

                    await interaction.response.edit_message(embed=embed, content='')
            else:
                pass
        await asyncio.sleep(30)
        self.value= False
        self.stop()

    @discord.ui.button(label=right,style=discord.ButtonStyle.grey)
    async def button_right(self, interaction: discord.Interaction, button:discord.ui.Button ):
        name= interaction.message.embeds[0].title[:-4][-4:]
        name2= interaction.message.embeds[0].title[:4]
        for i in range(len(datamap)):
            if (datamap[i][0].lower()[-4:] == name.lower() or datamap[i][1].lower()[-4:] == name.lower() or datamap[i][0].lower()[:4] == name2.lower() or datamap[i][1].lower()[:4] == name2.lower()):
                if ((datamap[i + 1][0].lower())[-4:] == datamap[i][0].lower()[-4:] or (datamap[i + 1][1].lower())[-4:] == datamap[i][1].lower()[-4:] or (datamap[i + 1][0].lower())[:4] == datamap[i][0].lower()[:4] or (datamap[i + 1][1].lower())[:4] == datamap[i][1].lower()[:4]):
                    embed = discord.Embed(
                        title=f'{datamap[i + 1][0]} Map',
                        url='https://kiranico.com/en/mh4u',
                        description=None,
                        color=newcolor[datamap[i + 1][3]]

                    )

                    embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                                     icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

                    embed.set_image(url=f'{datamap[i + 1][2]}')

                    await interaction.response.edit_message(embed=embed, content='')
            else:
                pass

        name = interaction.message.embeds[0].title[9:]
        for j in range(len(datamonster)):
            if ((datamonster[j][1].lower()) == name.lower()):
                if ((datamonster[j + 1][1].lower())[-4:] == datamonster[j][1].lower()[-4:]):
                    ele = f'{datamonster[j + 1][2]} {emoji[datamonster[j + 1][2]]}'
                    if datamonster[j + 1][3] != '0':
                        ele = ele + f' & {datamonster[j+1][3]} {emoji[datamonster[j + 1][3]]}'

                    weak = f'{datamonster[j + 1][4]} {emoji[datamonster[j + 1][4]]}'
                    if datamonster[j + 1][5] != '0':
                        weak = weak + f' & {datamonster[j + 1][5]} {emoji[datamonster[j + 1][5]]}'
                        if datamonster[j + 1][9] != '0':
                            weak = weak + f' & {datamonster[j + 1][9]} {emoji[datamonster[j + 1][9]]}'

                    embed = discord.Embed(
                        title=f'Monster: {datamonster[j + 1][1]}',
                        url='https://mogapedia.fandom.com/fr/wiki/Monster_Hunter_4_Ultimate',
                        description=datamonster[j + 1][10],
                        color=color[datamonster[j + 1][2]]
                    )
                    embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                                     icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

                    embed.set_image(url=f'{datamonster[j + 1][8]}')

                    embed.add_field(
                        name="Element",
                        value=ele
                    )
                    embed.add_field(
                        name="Weakness",
                        value=weak
                    )

                    embed.add_field(
                        name="Weakness part",
                        value=f'{datamonster[j + 1][6]}',
                        inline=False
                    )

                    embed.add_field(
                        name="(Base) Health Points",
                        value=f'{datamonster[j + 1][7]} '
                    )
                    await interaction.response.edit_message(embed=embed, content='')
            else:
                pass

        await asyncio.sleep(30)
        self.value = False
        self.stop()

class Menu2(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value= None
    @discord.ui.button(label=left,style=discord.ButtonStyle.grey)
    async def button_left(self, interaction: discord.Interaction, button:discord.ui.Button):
        name = interaction.message.embeds[0].description[-5:]
        if name == 'itaur':
            t=15
        if name == 'cylla':
            t=30
        if name == 'agala':
            t=45
        if name == 'nogre':
            t=60
        stop = True
        monsterlist = ''
        for j in datamonster:
            if (j[1] == datamonster[t-14][1]):
                stop = False
            if (j[1] != 'Monster' and stop == False):
                monsterlist = monsterlist + '''
                    ''' + '-' + j[1]
            if (j[1] == datamonster[t][1]):
                stop = True

        embed = discord.Embed(
            title='Monsters are:',
            url='https://mogapedia.fandom.com/fr/wiki/Monster_Hunter_4_Ultimate',
            description=monsterlist,
            color=0x00FFFF
        )
        embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                         icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

        await interaction.response.edit_message(embed=embed, content='')

        await asyncio.sleep(30)
        self.value = False
        self.stop()


    @discord.ui.button(label=right,style=discord.ButtonStyle.grey)
    async def button_right(self, interaction: discord.Interaction, button:discord.ui.Button):
        name = interaction.message.embeds[0].description[-5:]
        if name == 'ablos':
            t=30
        if name == 'itaur':
            t=45
        if name == 'cylla':
            t=60
        if name == 'agala':
            t=75
        stop = True
        monsterlist = ''
        for j in datamonster:
            if (j[1] == datamonster[t-14][1]):
                stop = False
            if (j[1] != 'Monster' and stop == False):
                monsterlist = monsterlist + '''
                    ''' + '-' + j[1]
            if (j[1] == datamonster[t][1]):
                stop = True

        embed = discord.Embed(
            title='Monsters are:',
            url='https://mogapedia.fandom.com/fr/wiki/Monster_Hunter_4_Ultimate',
            description=monsterlist,
            color=0x00FFFF
        )
        embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                         icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

        await interaction.response.edit_message(embed=embed, content='')

        await asyncio.sleep(30)
        self.value = False
        self.stop()

@bot.command(aliases=['l','listmonster','listmonsters'])
async def list(ctx):
    view=Menu2()
    t= 15
    stop= False
    monsterlist = ''
    for j in datamonster:
        if (j[1] != 'Monster' and stop==False):
            monsterlist = monsterlist + '''
            ''' + '-' + j[1]
        if (j[1] == datamonster[t][1]):
            stop= True

    embed = discord.Embed(
        title='Monsters are:',
        url='https://mogapedia.fandom.com/fr/wiki/Monster_Hunter_4_Ultimate',
        description=monsterlist,
        color=0x00FFFF
    )
    embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                     icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

    await ctx.send(embed=embed, view=view)

@bot.command(aliases=['c','command'])
async def commands(ctx):
    view=Menu()
    embed = discord.Embed(
        title = 'List of commands',
        description = '''^^list : Print the list of all Monsters
        ^^m Monster_Name : Print infos about the Monster
        ^^wiki : The place where the Data Base come from
        ^^listmap : Print the list of all Maps
        ^^map Map_Name : Print the Map
        ^^about : Just a random about
        ''',
        color = 0x00FFFF
        )
    await ctx.send(embed=embed)

@bot.command(aliases=['a'])
async def about(ctx):
    view=Menu()
    embed = discord.Embed(
            title='Hey thank you for using my bot! :D',
            url='https://twitter.com/_Trgh_',
            description="""This bot has been created to help people who searches infos and stats about the Monster Hunter 4 Ultimate game.
                        It can be cool to have infos for your next hunting party, and I think as a player of mh4u that remembering all weaknesses of each monster can be really compliacted.
                        So I decided to make a discord bot to search infos for me x)""",

            color=0x7F00FF
            )
    embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                             icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

    embed.set_image(url="https://pbs.twimg.com/profile_banners/1247234539728109569/1640297166/1080x360")

    await ctx.reply(embed=embed)


@bot.command()
async def map(ctx,*name):
    view=Menu()
    name = " ".join(name)
    for row in datamap:
        if (row[0].lower() == name.lower() or row[1].lower() == name.lower()):
            embed = discord.Embed(
                title=f'{row[0]} Map',
                url='https://kiranico.com/en/mh4u',
                description=None,
                color=newcolor[row[3]]

            )

            embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                             icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

            embed.set_image(url=f'{row[2]}')

            await ctx.send(embed=embed, view=view)

@bot.command()
async def m(ctx, *name):
    view=Menu()
    name = " ".join(name)
    for row in datamonster:
        if (row[0].lower() == name.lower() or row[1].lower() == name.lower()):

            ele = f'{row[2]} {emoji[row[2]]}'
            if row[3] != '0':
                ele = ele + f' & {row[3]} {emoji[row[3]]}'

            weak = f'{row[4]} {emoji[row[4]]}'
            if row[5] != '0':
                weak = weak + f' & {row[5]} {emoji[row[5]]}'
                if row[9] != '0':
                    weak = weak + f' & {row[9]} {emoji[row[9]]}'

            embed = discord.Embed(
                title=f'Monster: {row[1]}',
                url='https://mogapedia.fandom.com/fr/wiki/Monster_Hunter_4_Ultimate',
                description=row[10],
                color=color[row[2]]
            )
            embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805',
                         icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

            embed.set_image(url=f'{row[8]}')

            embed.add_field(
                name="Element",
                value=ele
            )
            embed.add_field(
                name="Weakness",
                value=weak
            )

            embed.add_field(
                name="Weakness part",
                value=f'{row[6]}',
                inline=False
            )

            embed.add_field(
                name="(Base) Health Points",
                value=f'{row[7]} '
            )
            await ctx.send(embed=embed, view=view)

@bot.event
async def on_message(message):
    if '^^' == message.content:
        await message.channel.send("Hey what's up? If you search for something type '^^s'")

    if 'mh4u' in message.content:
        if message.author == bot.user:
            return
        mes = random.choice(
            ['mh4u, I love that :D', 'mh4u, it reminds me something...', 'mh4u? The best game on 3ds in my book',
             'if you need infos on mh4u im here :)'])
        await message.channel.send(mes)

    if 'cya' in message.content or 'Cya' in message.content:
        if message.author == bot.user:
            return
        await message.reply('cya chad!')

    if 'uwu' in message.content or 'UwU' in message.content:
        if message.author == bot.user:
            return
        await message.channel.send('UwU')
    await bot.process_commands(message)




@bot.command(aliases=['menus'])
async def menu(ctx):
    view=Menu()
    view.add_item(discord.ui.Button(label="URL Button", style=discord.ButtonStyle.link, url="https://www.google.com/search?q=button+discord+bot+python&oq=button+discord+bot+python&aqs=chrome..69i57.9501j0j1&sourceid=chrome&ie=UTF-8#kpvalbx=_eVaXY5qyGOzHkdUP7pEC_78"))
    await ctx.reply("yo ma boy", view=view)

@bot.command(aliases=['search'])
async def s(ctx):
    await ctx.send("""yo
maybe you're searching for a monster stat? in this case type '^^m' followed by the name of the monster!
if you are searching for anything else, you should type '^^commands'""")

@bot.command(aliases=['w','wikis'])
async def wiki(ctx):
    view=Menu()
    await ctx.send('''All stats come from https://www.fandom.com/ and https://kiranico.com/en/mh4u
Go support them :D''')

@bot.command(aliases=['listmaps','lm'])
async def listmap(ctx):
    view=Menu()
    maplist = ''
    for j in datamap:
        if (j[0] != 'Maps name' and j[0] != 'volcanic hollow'):
            maplist = maplist + '''
            '''  + '-' + j[0]
        if j[0] == 'volcanic hollow':
            maplist = maplist + '''
            '''  + '-' + j[0]

    embed = discord.Embed(
        title='Maps are:',
        url='https://mogapedia.fandom.com/fr/wiki/Monster_Hunter_4_Ultimate',
        description=maplist,
        color=0x00FFFF
    )
    embed.set_footer(text='Infos by Kiranico and Fandom || By Trgh ツ#6805', icon_url='https://cdn.discordapp.com/avatars/479397397605384212/8f2cf01c4ad6df265fe19591183537a9.png?size=1024')

    await ctx.send(embed=embed)


@bot.command()
async def Monster_Name(ctx):
    view = Menu()
    await ctx.reply('No not like that, just type the name of the monster after the prefixe xD')
@bot.command()
async def Map_Name(ctx):
    view = Menu()
    await ctx.reply('No not like that, just type the name of the map after the prefixe xD')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)