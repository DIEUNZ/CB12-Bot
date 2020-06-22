import asyncio

import discord

client = discord.Client()

autoroles = {
    721820930736783371: {'memberroles': [722069911828168774], 'botroles': [722069910351773697]}

}


###############################################################################################

# DEFAULT: 0,
# AQUA: 1752220,
# GREEN: 3066993,
# BLUE: 3447003,
# PURPLE: 10181046,
# GOLD: 15844367,
# ORANGE: 15105570,
# RED: 15158332,
# GREY: 9807270,
# DARKER_GREY: 8359053,
# NAVY: 3426654,                          -------------------------------> EmbedColor-Codes
# DARK_AQUA: 1146986,
# DARK_GREEN: 2067276,
# DARK_BLUE: 2123412,
# DARK_PURPLE: 7419530,
# DARK_GOLD: 12745742,
# DARK_ORANGE: 11027200,
# DARK_RED: 10038562,
# DARK_GREY: 9936031,
# LIGHT_GREY: 12370112,
# DARK_NAVY: 2899536,
# LUMINOUS_VIVID_PINK: 16580705,
# DARK_VIVID_PINK: 12320855

#####



@client.event
async def on_ready():
    print('Wir sind eingeloggt als {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('GrieferGames.net'), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('$help'), status=discord.Status.online)
        await asyncio.sleep(20)
        await client.change_presence(activity=discord.Game('bei Problemen melde dich bei DIE_UNZ '), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('$help'), status=discord.Status.online)
        await asyncio.sleep(20)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith('$problem'):
        embed = discord.Embed(title="$problem", color=15158332)
        embed.add_field(name="Falls du ein Problem mit dem Discord hast",
                        value="Schreibe einen Supporter/Owner auf Discord an @Co-Owner , @Owner , @Supporter \r\n oder öffne ein ticket im #ticket-erstellen chanel!")

        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)


    #Clan

    if message.content.startswith('$clan'):
        embed = discord.Embed(title="$clan", color=1752220)
        embed.add_field(name="Es gibt akutell 5 Clans auf dem CB12-Discord",
                            value=" __***$0P-info***__ \r\n__***$Buddy-info***__ \r\n __***$CB12-info***__ \r\n __***$LAZ-info***__ \r\n __***$RED-info***__ ")


        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)


    #Clan info RED

    if message.content.startswith('$RED-info'):
        embed = discord.Embed(title='$RED-info', color=10038562)
        embed.add_field(name="RED", value=" Der RED-Clan wird aktuell durch 7 Member auf dem CB12 Discord Vertreten! \r\n \r\n __***Owner: DIE_UNZ***__ \r\n \r\n Member: Freakie \r\n Member: Juli_King1010 \r\n Member: Mr_Schlappe \r\n Member: Nadudi \r\n Member: Nuff_Nuff \r\n Member: Orangensaft1408")


        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)


    #Clan info LAZ

    if message.content.startswith('$LAZ-info'):
        embed = discord.Embed(title='$LAZ-info', color=15158332)
        embed.add_field(name="LAZ", value=" Der LAZ-Clan wird aktuell durch 6 Member auf dem CB12 Discord Vertreten! \r\n \r\n __***Owner: LAZ_TV61***__ \r\n \r\n Member: aragon \r\n Member: homersimpsons322 \r\n Member: LAZ_Exotic \r\n Member: Laz_fighting03 \r\n Member: LAZ_Robin \r\n Member: LAZ_Shadow \r\n Member: Laz_staphan \r\n Member: Meine13zzzzzz \r\n Member: webbbe ")

        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)


    #Clan info CB12

    if message.content.startswith('$CB12-info'):
        embed = discord.Embed(title='$CB12-info', color=15105570)
        embed.add_field(name="CB12", value=" Der CB12-Clan wird aktuell durch 2 Member auf dem CB12 Discord Vertreten! \r\n \r\n __***Owner: MaybeThegreat***__ \r\n \r\n Member: Broken_Moritz \r\n Member: Brunzzessin \r\n Member: Dagus \r\n Member: GinTonic1 \r\n Member: littleisland89 \r\n Member: The_Dark_Lurch \r\n Member: Xallesia ")

        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)



    #Clan info Buddy

    if message.content.startswith('$Buddy-info'):
        embed = discord.Embed(title='$Buddy-info', color=3447003)
        embed.add_field(name="CB12", value=" Der Buddy-Clan wird aktuell durch 1 Member auf dem CB12 Discord Vertreten! \r\n \r\n __***Owner: FAL_Vinni***__ \r\n \r\n  Member: 1Alex \r\n Member: 1Dxnnis \r\n Member: EinWildesNiko \r\n Member: Gamerfedex \r\n Member: Greenboll \r\n Member: Niki1234 \r\n Member: Onealius \r\n Member: Seyko54 \r\n Member: SimCor \r\n Member: Verhandelbar \r\n Member: vinnecin ")

        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)

    #Clan info 0P

    if message.content.startswith('$0P-info'):
        embed = discord.Embed(title='$0P-info', color=3066993)
        embed.add_field(name="0P", value=" Der 0P-Clan wird aktuell durch 2 Member auf dem CB12 Discord vertreten \r\n \r\n __***Owner: NKOTB12***__ \r\n \r\n Member: Ankurion \r\n Member: ByChidori \r\n Member: Code_404 \r\n Member: Der_Folk \r\n Member: Harry_Potter_42 \r\n Member: Hr_Pascalovice \r\n Member: JohannaPlayer \r\n Member: KingDeltaOne \r\n Member: Lord_Bierkrug \r\n Member: Loruam \r\n Member: Mabexx \r\n Member: MasterLou1007 \r\n Member: NicreyyFrispi \r\n Member: Noel_playzz \r\n Member: Xrelax")


        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)


    #MM liste

    if message.content.startswith('$MM-liste'):
        embed = discord.Embed(title='$MM-liste', color=3066993)
        embed.add_field(name="MM-liste", value=" Diese Folgenden Spieler sind aus der Sicht des Teams Scammfreie MM's : \r\n \r\n __***1Alex***__ [/p h MMBuddy (CB 12)] \r\n __***MasterLou1007***__ [/p h Lou-MM (Cb12)] \r\n __***MaybetheGreat***__ [/p h maybeMM (CB12)]  \r\n __***Meine13zzzzz***__ [/p h Meine13MM (CB12 & CB4)] \r\n __***Nuff_Nuff_ ***__   [/p h CB12_MM (CB12)]  \r\n __***Tre_Bullet***__ [/p h TRE_MM (CB12)]\r\n __***Webbbe***__     [/p h webbbeMM (CB12)] \r\n \r\n **Wir übernehemn keine Haftung bei Scamm!** ")


        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)






    #Help

    if message.content.startswith('$help'):
        embed = discord.Embed(title="$help", color=15158332)
        embed.add_field(name="Auf dem CB12-Discord gibt es aktuell folgenden Befehle",
                        value="$help - Zeigt diese Hilfe an\r\n $problem - Zeigt dir wie du schnellstmöglich Hilfe bekommmst \r\n $clan - Welche Clan auf dem Discord zu finden sind \r\n $MM-liste - Zeigt euch 'Trusted MM' \r\n $update - Zeigt euch die Letzten Updates \r\n $toplist - zeigt die GrieferGames Toplist der Clans ")


        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)



    #update

    if message.content.startswith('$update'):
        embed = discord.Embed(title="$update", color=1752220)
        embed.add_field(name="Beim letzten update am 21.06.2020 wurden folgende Befehle geändert\r\n \r\n",
                        value="\r\n Update vom 21.06.2020 \r\n \r\n \r\nDer 0P Clan wurde auf dem CB-12 hinzugefügt und ist jetzt mit **$0P-info** zu finden \r\n \r\n Die Clanliste von Buddy wurde geupdatet (3 Member entfernt) \r\n \r\n $toplist wurde hinzugefügt, dieser Befehl zeigt eine, unter GrieferGames als /Clan Toploist bekannnte, Tabelle der Reichten Clans \r\n \r\n Der LAZ hat jetzt 6 Member auf dem Cb12 Discord! \r\n \r\n Die Memberliste von RED wurde geupdatet[1 Member entfernt] \r\n \r\n Der Befehl __***$update***__ wurde hinzugefügt! \r\n \r\n In allen Clans wurden die Member dem Alphabet nach geordnet \r\n \r\n Die Rolle ScammFrei wurde erstell aber NUR manuel von **DIE_UNZ** verteilt! \r\n \r\n \r\n **Vorraussichtliches nächstes Update am 24.06.2020**")


        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)


    #toplist

    if message.content.startswith('$toplist'):
        embed = discord.Embed(title='$topliste', color=3066993)
        embed.add_field(name="Die Clan Toplist vom 21.06.2020 ; 12:13", value=" \r\n \r\n__***1***__ DieAlphaWölfe - [**Alpha**] - 153.428.164,02$ \r\n \r\n __***2***__ LaPetiteMort - [**LPM**] - 103.103.809,71$ \r\n \r\n__***3***__ FUSION - [**FUSION**] - 73.295.726,17$ \r\n \r\n__***4***__ MillionäreInternationalBuissines - [**MIB**] - 68.133.947,89$ \r\n \r\n__***5***__ PresidetialDelegates [**#PD**] - 49.724.983$ **CB12-Clan** \r\n \r\n __***6***__ DevilArmy - [**DvA**] - 40.476.714,42$ \r\n \r\n __***7***__ Reborn - [**Reborn**] - 39.498.085,17$ \r\n \r\n __***8***__ OldGeneration - [**-OG-**] - 39.478.534,22$ \r\n \r\n__***9***__ FaithFul - [**#Faith**] - 38.726.468,1$ \r\n \r\n__***10***__ FireAndLight - [**Buddy**] - 36.249.731,86$ **CB12-Clan** \r\n \r\n__***11***__ Tactical_Riot_Economics - [**TRE**] - 35.778.309,21$ **CB12-Clan** \r\n \r\n__***12***__ Sensei - [**ZEN**] - 34.168.320,87$ \r\n \r\n__***13***__ 2k - [**2K**] - 32.049.965,36 \r\n \r\n__***14***__ pro-player - [**prp**] - 31.917.673,54$ \r\n \r\n__***15***__ Wir-Scammen-nicht - [**#WSN**] - 31.212.805,03$")


        embed.set_footer(text="CB12-Bot Codet by unz")

        await message.channel.send(embed=embed)






@client.event
async def on_member_join(member):
    guild: Guild = member.guild
    if not member.bot:
        channel = discord.utils.get(member.guild.channels, name="join-leave")
        embed = discord.Embed(title="CB12-Bot",
                              description=f"Hey {member.mention} \n"
                                          f"Willkommen auf dem CB12 Discordserver! \n"
                                          f"Du bist der `{len(list(member.guild.members))}`. Member!",
                              color=discord.Colour.green())

        embed.set_footer(text="[CB12-Bot Codet by unz]")
        embed.set_thumbnail(url=f"{member.avatar_url}")
        mess = await channel.send(embed=embed)
        guild: Guild = member.guild

        autoguild = autoroles.get(member.guild.id)
        if autoguild and autoguild['memberroles']:
            for roleId in autoguild['memberroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)
    else:
        autoguild = autoroles.get(member.guild.id)
        if autoguild and autoguild['botroles']:
            for roleId in autoguild['botroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)



client.run('NzIyNDExNDg1MDkwOTM4OTQy.Xujj1A.CcbWEuYn-K8ce0jm7B5KWRp6MfU')