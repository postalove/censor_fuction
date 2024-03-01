'''
Discord-Bot-Module template. For detailed usages,
 check https://interactions-py.github.io/interactions.py/

Copyright (C) 2024  __retr0.init__

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import interactions
# Use the following method to import the internal module in the current same directory
from . import load_info

'''
Replace the ModuleName with any name you'd like
'''
class RoleManager(interactions.Extension):
    module_base: interactions.SlashCommand = interactions.SlashCommand(
        name="censor_role",
        description="Replace here for the base command descriptions"
    )
    module_group: interactions.SlashCommand = module_base.group(
        name="can",
        description="Replace here for the group command descriptions"
    )

    
    
    @module_group.subcommand("promote", sub_cmd_description="通过审核")
    @interactions.slash_option(
        name = "member",
        description='member you want to promote',
        required = True,
        opt_type = interactions.OptionType.USER
    )
    async def promote(self,ctx:interactions.SlashContext,member:interactions.Member):
        censor, allowed_roles, log_channel_id,guild_id = load_info.extract_bot_setup("bot_setup.json")
        if any(role.name in censor for role in ctx.author.roles):
            official_member_role = interactions.utils.get(ctx.guild.roles, name='正式成员')

        # Get the '临时成员' role
            temporary_member_role = interactions.utils.get(ctx.guild.roles, name='临时成员')
            prisoner_role = interactions.utils.get(ctx.guild.roles, name='囚犯')
            if prisoner_role in member.roles:
                await ctx.response.send(f'{member.mention} is a prisoner!')
                return
        # Check if the roles exist
            if official_member_role is None or temporary_member_role is None:
                await ctx.send("Roles not found. Please make sure '正式成员' and '临时成员' roles exist.")
                return
            await member.add_role(official_member_role)
            await member.remove_role(temporary_member_role)
            await ctx.send(f'{member.mention} has been promoted.')
        else:
            await ctx.send(f'你无权这么做')
    @module_group.subcommand("demote", sub_cmd_description="撤销通过审核")
    @interactions.slash_option(
        name = "member",
        description='member you want to demote',
        required = True,
        opt_type = interactions.OptionType.USER
    )
    async def demote(self,ctx:interactions.SlashContext,member:interactions.Member):
        censor, allowed_roles, log_channel_id,guild_id = load_info.extract_bot_setup("bot_setup.json")
        if any(role.name in censor for role in ctx.author.roles):
            official_member_role = interactions.utils.get(ctx.guild.roles, name='正式成员')

        # Get the '临时成员' role
            temporary_member_role = interactions.utils.get(ctx.guild.roles, name='临时成员')
            prisoner_role = interactions.utils.get(ctx.guild.roles, name='囚犯')
            if prisoner_role in member.roles:
                await ctx.response.send(f'{member.mention} is a prisoner!')
                return
        # Check if the roles exist
            if official_member_role is None or temporary_member_role is None:
                await ctx.send("Roles not found. Please make sure '正式成员' and '临时成员' roles exist.")
                return
            await member.remove_role(official_member_role)
            await member.add_role(temporary_member_role)
            await ctx.send(f'{member.mention} has been promoted.')
        else:
            await ctx.send(f'你无权这么做')