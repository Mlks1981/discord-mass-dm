#Mlks1981
import discum

bot = discum.Client(token="INSERT TOKEN")

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

members = get_members('INSERT SERVER_ID', 'INSERT CHANNEL_ID')
memberslist = []

for memberID in members:
    memberslist.append(memberID)
    print(memberID)

f = open('ids.txt', "a")
for element in memberslist:
    f.write(element + '\n')
f.close()