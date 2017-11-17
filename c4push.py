import os
import re
from time import time as now

import requests
import znc

API_USER = os.getenv('API_USER')
API_TOKEN = os.getenv('API_TOKEN')

def debug(*args):
    with open('/tmp/c4push-debug.log', 'a') as log:
        log.write('[{}] {!r}\n'.format(now(), args))

def notify(message):
    requests.post('https://api.pushover.net/1/messages.json',
                  data = {'user': API_USER,
                          'token': API_TOKEN,
                          'message': message})

class c4push(znc.Module):
    module_types = [znc.CModInfo.NetworkModule]
    description = 'Send notifications when the C4 hackerspace opens its doors'

    def OnTopic(self, nick, channel, sTopic):
        nick = nick.GetNick()
        channel = channel.GetName()
        topic = str(sTopic)
        if channel == '#cccc':
            debug(nick, channel, topic)
            if re.search('Club ist offen', topic):
                notify('Club ist offen!')
