import os

from juicy.core.juicymq import JuicyMQ

path = os.path.abspath(
    os.path.dirname(__file__)
)

rootpath = os.path.join(
    path,
    'root'
)

assetspath = os.path.join(
    path,
    'assets'
)

homepath = os.path.join(
    os.path.expanduser('~'),
    '.juicy'
)

mq = JuicyMQ()
