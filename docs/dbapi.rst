dbapi is a python package that brings
the ability to access the Discord Bots
website API to python code for the sole
reason of requesting it from behalf of
a discord bot.

Without this package normal discord bots
would not be able to do this as
discord.py does not have this integrated.

Class DBAPI:
============


:class:`DBAPI`

Discord Bots API Class.

:param bot: Required. Bot client
    initialization instance.
:param api_token: Required. User generated
   API Token to the Discord Bots API.


:method:`send_stats`

Sends Bot stats with server count
and shard information if present.
    
:param server_count: Required. Number of
    Servers the bot is in.
:param bot_id: Required. The Bot's user id.
:param shard_id: Optional. Shard in use?
:param shard_count: Optional. Total
    number of shards the bot is using.
:raises: DBAPIRequestError on Failure.


:method:`get_stats`

Gets the bot's stats.

:param bot_id: Required. The Bot's user id.


:method:`get_bot_info`

Gets the bot's information.

:param bot_id: Required. The Bot's user id.


:method:`get_all_bot_infos`

Gets information on all bots.


:method:`get_user_info`

Gets information on a user.

:param user_id: Required. The user's
    discord id.


Class DBAPIRequestError:
========================


:class:`DBAPIRequestError`

This class is a error class when
there is a request error sent
from the API website.
