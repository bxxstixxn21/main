import discord
from discord.ext import commands

class Willkommen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("Command Willkommens command  geladen")
        role = discord.utils.get(member.guild.roles, name='👋🏽 ▪ Besucher',)
        await member.add_roles(role)
        embed = discord.Embed(
            title="Willkommen!",
            color=discord.Color.random(),

    )
        embed.add_field(name="** **",
                        value=f"Willkommen {member.mention} auf Internet Treffpunkt", inline=False)
        embed.add_field(name="** **",
                        value="Bitte schau in <#1031204438737682536>", inline=False)
        embed.add_field(name="** ** ",
                        value=" Du kannst dich Verifizieren brauchst du aber nicht du kannst auch den Server so nutzen", inline=False)
        embed.add_field(name="** **",
                        value="Wir wünschen dir viel Spaß auf dem Server", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"© 2022 | Internet Treffpunkt | Alle Rechte vorbehalten!")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1038640114773020756/1045492838755999835/willkommen.png")
        channel = await self.bot.fetch_channel(1036820949850394700)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Willkommen(bot))