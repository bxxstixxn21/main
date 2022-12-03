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
            color=discord.Color.random()

    )
        embed.add_field(name="Willkommen auf dem Internet Treffpunkt", value="Wir wünschen dir viel Spaß auf unserem Server", inline=False)
        embed.add_field(name="Regeln", value="Bitte lies dir die Regeln durch, bevor du dich auf dem Server bewegst", inline=False)
        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name="Support", value="Falls du Hilfe brauchst, kannst du dich gerne an einen Moderator wenden", inline=False)
        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name="Verifizierung", value="Du hast momentan den Rang ''Besucher'', damit kannst du dich auf dem Server umschauen, aber bitte verifiziere dich", inline=False)
        embed.set_footer(text=f"© 2022 | Internet Treffpunkt | Alle Rechte vorbehalten!")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1038640114773020756/1045492838755999835/willkommen.png")
        channel = await self.bot.fetch_channel(1036820949850394700)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Willkommen(bot))