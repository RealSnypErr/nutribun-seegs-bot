from utils import utils
from discord.ext import commands
from traceback import format_exc
from random import randint, choice
from discord import Embed, colour
from datetime import timedelta
list_of_retards = []


class command(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    async def sex(self, ctx, *, user: str):
        try:
            result = await utils.query_database(f'SELECT bodycount FROM seegs WHERE user = {ctx.author.id}')

            if result:
                    current_count = result[0]
            else:
                    current_count = 0
            new_count = current_count + 1

            if result:
                await utils.update_database(f'UPDATE seegs SET bodycount = {new_count} WHERE user = {ctx.author.id}')
            else:
                await utils.update_database(f'INSERT INTO seegs (user, bodycount) VALUES ({ctx.author.id}, {new_count})')

            await ctx.send(f"**{user} has been sexed by <@{ctx.author.id}>!**")
        except:
            await utils.error_report(format_exc(1), ctx.channel.id)

    @commands.hybrid_command()
    async def swordfight(self, ctx, *, user: str):

        rand = randint(1,100)
        try:
            result = await utils.query_database(f'SELECT bodycount, swordfights, swordfight_win, swordfight_loss FROM seegs WHERE user = {ctx.author.id}')

            if result:
                current_count = result[0] if result[0] is not None else 0
                current_swordfights = result[1] if result[1] is not None else 0
                current_win_count = result[2] if result[2] is not None else 0
                current_loss_count = result[3] if result[3] is not None else 0
            else:
                current_count, current_swordfights, current_win_count, current_loss_count = 0, 0, 0, 0

            new_count = current_count + 1
            new_swordfights = current_swordfights + 1

            if result:
                await utils.update_database(f'UPDATE seegs SET bodycount = {new_count}, swordfights = {new_swordfights} WHERE user = {ctx.author.id}')
            else:
                await utils.update_database(f'INSERT INTO seegs (user, swordfights, bodycount) VALUES ({ctx.author.id}, {new_swordfights}, {new_count})')

            if rand >= 50: #implement that check
                await ctx.send(f"**<@{ctx.author.id}> dared {user} to a swordfight. {user} won and fucked <@{ctx.author.id}> in the ass.**")
                new_loss_count = current_loss_count + 1
                await utils.update_database(f'UPDATE seegs SET swordfight_loss = {new_loss_count} WHERE user = {ctx.author.id}')
                return
            elif rand < 50:
                await ctx.send(f"**<@{ctx.author.id}> dared {user} to a swordfight. <@{ctx.author.id}> won and fucked {user} in the ass.**")
                new_win_count = current_win_count + 1
                await utils.update_database(f'UPDATE seegs SET swordfight_win = {new_win_count} WHERE user = {ctx.author.id}')
                return
        except:
            await utils.error_report(format_exc(1), ctx.channel.id)

    @commands.hybrid_command()
    async def impregnate(self,ctx,*, user: str):
        try:
            succ = [f"**{user} became pregnant with <@{ctx.author.id}>'s child! \nCongratulations, it's a boy!**",f"**{user} became pregnant with <@{ctx.author.id}>'s child! \nCongratulations, it's a ~~girl~~ abortion!**",f"**{user} became pregnant with <@{ctx.author.id}>'s child! \nCongratulations, it's a femboy!**", f"**<@{ctx.author.id}> unsuccessfully tried to impregnate {user}.**",f"**{user} became pregnant with <@{ctx.author.id}>'s child, but soon suffered a miscarriage.**",f"**<@{ctx.author.id}> tried to impregnate {user}, but was reported to the police and was arrested.**"]
            randomizer = randint(0,len(succ))
            succ = succ[randomizer]
            result = await utils.query_database(f'SELECT bodycount, boys, girls, femboys, unsuccessful, miscarriage FROM seegs WHERE user = {ctx.author.id}')

            if result:
                current_count = result[0] if result[0] is not None else 0
                current_boy = result[1] if result[1] is not None else 0
                current_girl = result[2] if result[2] is not None else 0
                current_femboy = result[3] if result[3] is not None else 0
                current_unsuc = result[4] if result[4] is not None else 0
                current_mis = result[5] if result[5] is not None else 0
            else:
                current_count, current_boy, current_girl, current_femboy, current_unsuc, current_mis= 0, 0, 0, 0, 0, 0

            new_count = current_count + 1
                        
            if result:
                await utils.update_database(f'UPDATE seegs SET bodycount = {new_count} WHERE user = {ctx.author.id}')
            else:
                await utils.update_database(f'INSERT INTO seegs (user, bodycount) VALUES ({ctx.author.id}, {new_count})')

            match randomizer:
                case 0:
                    await utils.update_database(f'UPDATE seegs SET boys = {current_boy + 1} WHERE user = {ctx.author.id}')
                case 1:
                    await utils.update_database(f'UPDATE seegs SET girls = {current_girl + 1} WHERE user = {ctx.author.id}')
                case 2:
                    await utils.update_database(f'UPDATE seegs SET femboys = {current_femboy + 1} WHERE user = {ctx.author.id}') 
                case 3:
                    await utils.update_database(f'UPDATE seegs SET unsuccessful = {current_unsuc + 1} WHERE user = {ctx.author.id}')        
                case 4:
                    await utils.update_database(f'UPDATE seegs SET miscarriage = {current_mis + 1} WHERE user = {ctx.author.id}')     
                case _:
                    await utils.update_database(f'UPDATE seegs SET unsuccessful = {current_unsuc + 1} WHERE user = {ctx.author.id}')

            await ctx.send(f"**{succ}**")
        except:
            await utils.error_report(format_exc(1), ctx.channel.id)

    @commands.hybrid_command()
    async def threesome(self, ctx, user: str, user2: str):
        try:
            result = await utils.query_database(f'SELECT bodycount FROM seegs WHERE user = {ctx.author.id}')

            if result:
                    current_count = result[0] if result[0] is not None else 0
            else:
                    current_count = 0

            new_count = current_count + 2

            if result:
                    await utils.update_database(f'UPDATE seegs SET bodycount = {new_count} WHERE user = {ctx.author.id}')
            else:
                    await utils.update_database(f'INSERT INTO seegs (user, bodycount) VALUES ({ctx.author.id}, {new_count})')

            await ctx.send(f"**{user} and {user2} has been sexed by <@{ctx.author.id}>!**")

        except:
                await utils.error_report(format_exc(1), ctx.channel.id)

    @commands.hybrid_command()
    async def sniff(self, ctx, *, user: str):
        try:
            result = await utils.query_database(f'SELECT sniff FROM seegs WHERE user = {ctx.author.id}')

            if result:
                    current_count = result[0] if result[0] is not None else 0
            else:
                    current_count = 0

            new_count = current_count + 1

            if result:
                    await utils.update_database(f'UPDATE seegs SET sniff = {new_count} WHERE user = {ctx.author.id}')
            else:
                    await utils.update_database(f'INSERT INTO seegs (user, sniff) VALUES ({ctx.author.id}, {new_count})')

            await ctx.send(f"**<@{ctx.author.id}> sniffed {user}'s PE clothes!**")
        except:
            await utils.error_report(format_exc(1), ctx.channel.id)
    
    @commands.hybrid_command()
    async def cbt(self, ctx, *, user: str):
        await ctx.send(f"**<@{ctx.author.id}> cock and ball tortured {user}!**")

    @commands.hybrid_command()
    async def feminize(self, ctx, user: str):
        feminize_list = ["654323314201985044", "749446330132463706", "762500367812132894", "1142430617577979985", "1151540222585212948"]
        if any(id in user for id in feminize_list):
            await ctx.send(f"**{user} has been successfully feminized, welcome to your new femboy life! :3**")
            await ctx.send("https://tenor.com/view/gender-bender-gender-mtf-anime-gif-22298021")
        else:
            await ctx.send(f"{user} does not fulfill the requirements for feminization. :(")

    @commands.hybrid_command()
    async def rape(self, ctx, user: str):
        if self.client.block_commands == False:
            rand = randint(2,10) if "859360668826337291" in user else randint(1,10)
            if rand <= 3:
                await ctx.send(f"**<@{ctx.author.id}> tried to rape {user}, but was caught by the police!**")
                try:
                    await ctx.author.timeout(timedelta(seconds=30))
                except:
                    await ctx.send(f"I do not have permissions to mute <@{ctx.author.id}>!")

            elif rand >= 2:
                await ctx.send(f"**<@{ctx.author.id}> raped {user} and is now wanted by the police!**")
        else:
             await ctx.reply("https://tenor.com/view/pnp-police-raid-philippines-gif-18307264")

    @commands.hybrid_command()
    async def jakol(self, ctx):
         await ctx.send(f"**Nagjakol si <@{ctx.author.id}>!**")  

    @commands.hybrid_command()
    async def stats(self,ctx):   
        try:  
            result = await utils.query_database(f'SELECT bodycount, swordfights, swordfight_win, swordfight_loss, boys, girls, femboys, unsuccessful, miscarriage, gex, sniff FROM seegs WHERE user = {ctx.author.id}')

            if result:
                bodycount = result[0]
                swordfights = result[1] if result[1] is not None else 0
                swordfight_win = result[2] if result[2] is not None else 0
                swordfight_loss = result[3] if result[3] is not None else 0
                boys = result[4] if result[4] is not None else 0
                girls = result[5] if result[5] is not None else 0
                femboys = result[6] if result[6] is not None else 0
                unsuccessful = result[7] if result[7] is not None else 0
                miscarriage = result[8] if result[8] is not None else 0
                gex = result[9] if result[9] is not None else 0
                sniff = result[10] if result[10] is not None else 0
            else:
                bodycount, swordfights, swordfight_win, swordfight_loss, boys, girls, femboys, unsuccessful, miscarriage, gex, sniff = 0,0,0,0,0,0,0,0,0,0,0

            embed = await utils.construct_statsembed(ctx.author.name, ctx.author.avatar, bodycount, swordfights, swordfight_win, swordfight_loss, boys, girls, femboys, unsuccessful, miscarriage, gex, sniff)
            await ctx.send(embed=embed)
        except:
            await utils.error_report(format_exc(1), ctx.channel.id)

    @commands.hybrid_command()
    async def leaderboard(self,ctx):
        try:
            footer_msg = []
            with open("footer_message.txt", "rt") as f:
                footer_msg.clear()
                for line in f:
                    footer_msg.append(line.strip())
                f.close() 
            rpt = 1

            data = await utils.query_database_fetchall("SELECT user, bodycount FROM seegs ORDER BY bodycount DESC;")
            embed = Embed(title="Sex leaderboard for this server", color=colour.Color.red())

            for row in data:          
                name, stats = row
                embed.add_field(name=f"", value=f"{rpt}. <@{name}> • {stats}", inline=False)
                rpt += 1

                if rpt > 10:
                    break 
            embed.set_author(name=ctx.author.nick, icon_url=ctx.author.avatar.url)
            embed.set_footer(text=f"{choice(footer_msg)}")
            await ctx.send(embed=embed)
        except:
            await utils.error_report(format_exc(1), ctx.channel.id)

#    @commands.hybrid_command()
#    async def test_error(self, ctx):
#        await utils.error_report("Test error", ctx.channel.id)

async def setup(client):
    await client.add_cog(command(client))
    
