import os
import random

import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channels = [channel for channel in guild.channels]
        roles = roles = [role for role in guild.roles]
        embed = discord.Embed(title=f"Bot just joined : {guild.name}", color=random.randint(0, 16777215))

        embed.set_thumbnail(url=guild.icon.url if guild.icon else "https://i.imgur.com/3ZUrjUP.png")

        embed.add_field(name="Server Name:", value=f"{guild.name}")
        embed.add_field(name="Server ID:", value=f"{guild.id}")
        embed.add_field(name="Server region:", value=f"{guild.region}")
        embed.add_field(
            name="Server Creation Date:",
            value=f"{discord.utils.format_dt(guild.created_at, style = 'd')}\n{discord.utils.format_dt(guild.created_at, style = 'T')}",
        )
        embed.add_field(name="Server Owner:", value=f"{guild.owner}")
        embed.add_field(name="Server Owner ID:", value=f"{guild.owner_id}")
        embed.add_field(name="Member Count:", value=f"{guild.member_count}")
        embed.add_field(name="Amount of Channels:", value=f"{len(channels)}")
        embed.add_field(name="Amount of Roles:", value=f"{len(roles)}")
        await self.bot.get_channel(852897595869233182).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channels = [channel for channel in guild.channels]
        roles = roles = [role for role in guild.roles]
        embed = discord.Embed(title=f"Bot just left : {guild.name}", color=random.randint(0, 16777215))

        embed.set_thumbnail(url=guild.icon.url if guild.icon else "https://i.imgur.com/3ZUrjUP.png")

        embed.add_field(name="Server Name:", value=f"{guild.name}")
        embed.add_field(name="Server ID:", value=f"{guild.id}")

        try:
            embed.add_field(name="Server region:", value=f"{guild.region}")

        except:
            pass

        embed.add_field(
            name="Server Creation Date:",
            value=f"{discord.utils.format_dt(guild.created_at, style = 'd')}\n{discord.utils.format_dt(guild.created_at, style = 'T')}",
        )
        embed.add_field(name="Server Owner:", value=f"{guild.owner}")
        embed.add_field(name="Server Owner ID:", value=f"{guild.owner_id}")
        try:
            embed.add_field(name="Member Count:", value=f"{guild.member_count}")
        except:
            pass
        embed.add_field(name="Amount of Channels:", value=f"{len(channels)}")
        embed.add_field(name="Amount of Roles:", value=f"{len(roles)}")
        await self.bot.get_channel(852897595869233182).send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is Ready")
        print(f"Logged in as {self.bot.user}")
        print(f"Id: {self.bot.user.id}")

    @commands.Cog.listener()
    async def on_message(self, message):
        test = await self.bot.get_context(message)

        if isinstance(message.channel, discord.DMChannel):
            if test.prefix is None or self.bot.user.mentioned_in(message):
                if message.author.id != self.bot.user.id and test.valid is False:
                    await message.channel.send(
                        "Ticket Support is coming soon. For now Contact our Developers: Shadi#9492 or JDJG Inc. Official#3493"
                    )

        if (test.valid) == False and test.prefix != None and test.command is None and test.prefix != "":

            embed_message = discord.Embed(
                title=f" {test.prefix}{test.invoked_with}",
                description=f"{discord.utils.format_dt(message.created_at, style = 'd')}{discord.utils.format_dt(message.created_at, style = 'T')}",
                color=random.randint(0, 16777215),
            )

            embed_message.set_author(
                name=f"{message.author} tried to excute invalid command:",
                icon_url=(message.author.display_avatar.url),
            )
            embed_message.set_footer(text=f"{message.author.id}")
            embed_message.set_thumbnail(url="https://i.imgur.com/bW6ergl.png")
            await self.bot.get_channel(852897595869233182).send(embed=embed_message)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(member)
        # currently wip btw

    @commands.Cog.listener()
    async def on_guild_available(self, guild):
        print(f"{guild} is avaible")

    @commands.Cog.listener()
    async def on_guild_unavailable(self, guild):
        print(f"{guild} is unavaible")


async def setup(bot):
    await bot.add_cog(Events(bot))
