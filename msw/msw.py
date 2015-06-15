##########################################################################
#
#   Name:           msq.py
#   Author:         Harrison Hubbell
#   Date:           06/15/2015
#   Description:    MagicSeaweed class for interacting with API
#
##########################################################################

import requests
from .spot import Spot, SpotDataUnavailableError

class MagicSeaweed(object):
    ENDPOINT = 'http://magicseaweed.com/api/{}/forecast/?spot_id={}'

    def __init__(self, key):
        self.key = key
        
    def get(self, spot_id):
        url = self.ENDPOINT.format(self.key, spot_id)
        r = requests.get(url)

        if r.status_code == 200:
            if type(r.json()) is dict and r.json().get('error_response', False):
                raise SpotDataUnavailableError(
                    spot_id,
                    url,
                    code=r.json()['error_response']['code'],
                    msg=r.json()['error_response']['error_msg']
                )
            else:
                return Spot(spot_id, r.json())
        else:
            raise MagicSeaweedUnavailableError(url)
        
class MagicSeaweedUnavailableError(Exception):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return 'Magic Seaweed is unavailable at the following url: {}'.format(
            str(self.url)
        )

    def __unicode__(self):
        return u'Magic Seaweed is unavailable at the following url: {}'.format(
            unicode(self.url)
        )
