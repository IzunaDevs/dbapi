# coding=utf-8
"""
dbapi
~~~~~~~~~~~~~~~~~~~

Discord Bots API for Discord Bots.

:copyright: (c) 2017 Decorater
:license: MIT, see LICENSE for more details.

"""

__all__ = ['DBAPI', 'DBAPIRequestError']


class DBAPIRoute:
    """
    Resolves the route to Discord Bots API urls.
    """
    BASE = 'https://bots.discord.pw'

    def __init__(self, method, path):
        self.path = path
        self.method = method
        if self.BASE not in self.path:
            self.url = self.BASE + self.path
        else:
            self.url = self.path


class DBAPIPayload:
    """
    Payload stuff to send to the
    Discord Bots API.
    """
    def __init__(self, server_count, shard_id=None,
                 shard_count=None):
        self.payload = {
            'server_count': server_count
        }
        if shard_id is not None:
            self.payload['shard_id'] = shard_id
        if shard_count is not None:
            self.payload['shard_count'] = shard_count


class DBAPIRequestError(Exception):
    pass


class DBAPI:
    """
    Discord Bots API Class.

    :param bot: Bot client initialization instance.
    :param api_token: User generated API Token.
    """
    def __init__(self, bot, api_token):
        # barrow discord.py's aiohttp
        # ClientSession instance.
        self.session = bot.http.session
        self.token = api_token

    def authorize(self):
        """
        handles creating the
        authorization header.
        """
        headers = {}
        headers['Authorization'] = self.token
        return headers

    async def request(self, route, *args, **kwargs):
        """
        Sends requests to the Discord Bots API.
        """
        await self.session.request(
            route.method, route.url, *args, **kwargs)

    async def send_stats(self, server_count,
                         bot_id, **kwargs):
        """
        Sends Bot stats with server count.
        And Shard information if present.

        :param server_count: Required. Number
            of Servers the bot is in.
        :param bot_id: Required. The Bot's user id.
        :param shard_id: Optional. Shard in use?
        :param shard_count: Optional. Total
            number of shards the bot is using.
        :raises: DBAPIRequestError on Failure.
        """
        headers = self.authorize()
        payloadclass = DBAPIPayload(server_count, **kwargs)
        payload = payloadclass.payload
        r = await self.request(
            DBAPIRoute(
                'POST',
                '/api/bots/{0}/stats'.format(bot_id)
            ),
            json=payload,
            headers=headers)
        if r is not None:
            # avoid AttributeError here.
            resp = r.json()
            # seems every time the response is not None that
            # an error occured somewhere and is
            # returned by the json response.
            raise DBAPIRequestError(resp['error'])

    async def get_stats(self, bot_id):
        """
        gets the bot's stats.

        :param bot_id: Required. The Bot's user id.
        """
        headers = self.authorize()
        r = await self.request(
            DBAPIRoute(
                'GET',
                '/api/bots/{0}/stats'.format(bot_id)
            ),
            headers=headers)
        return r.json()

    async def get_bot_info(self, bot_id):
        """
        gets the bot's information.

        :param bot_id: Required. The Bot's user id.
        """
        headers = self.authorize()
        r = await self.request(
            DBAPIRoute(
                'GET',
                '/api/bots/{0}'.format(bot_id)
            ),
            headers=headers)
        return r.json()

    async def get_all_bot_infos(self):
        """
        gets information on all bots.
        """
        headers = self.authorize()
        r = await self.request(
            DBAPIRoute(
                'GET',
                '/api/bots'
            ),
            headers=headers)
        return r.json()

    async def get_user_info(self, user_id):
        """
        gets information on a user.
        :param user_id: Required. The user id.
        """
        headers = self.authorize()
        r = await self.request(
            DBAPIRoute(
                'GET',
                '/api/users/{0}'.format(user_id)
            ),
            headers=headers)
        return r.json()
