from mockredis import MockRedis as _MockRedis

from .hash import HashCommandsMixin

__all__ = ['MockRedis']

class MockRedis(HashCommandsMixin):
    '''Fake high-level aioredis.Redis interface'''

    def __init__(self, connection=None, encoding=None):
        # Just for API compatibility
        self._conn = connection
        self._redis = _MockRedis()

        self._encoding = encoding


async def create_redis(address, *, db=None, password=None, ssl=None,
                       encoding=None, commands_factory=MockRedis,
                       loop=None):
    '''Create a fake high-level MockRedis interface

    This function is a coroutine
    '''
    return commands_factory(None, encoding=encoding)