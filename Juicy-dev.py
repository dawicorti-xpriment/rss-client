import os
import sys


sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        'src'
    )
)

from juicy.client import JuicyClient

client = JuicyClient()
client.run()
