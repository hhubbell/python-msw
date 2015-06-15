##########################################################################
#
#   Name:           spot.py
#   Author:         Harrison Hubbell
#   Date:           06/15/2015
#   Description:    Representation of a spot
#
##########################################################################

from .forecast import Forecast

class Spot(object):
    def __init__(self, spot_id, forecast=None):
        self.spot_id = spot_id
        self.forecast = self.parse(forecast) if type(forecast) is list else {}

    def parse(self, forecast_json):
        fc = []

        for tf in forecast_json:
            fc.append(Forecast(**tf))

        return fc

class SpotDataUnavailableError(Exception):
    def __init__(self, spot_id, url, code=None, msg=None):
        self.spot_id = spot_id
        self.url = url
        self.code = code
        self.msg = msg

    def __str__(self):
        return 'Spot data for spot_id {} unavailable at the following url: {}. Additional information: code: {} msg: {}'.format(
            str(self.spot_id),
            str(self.url),
            str(self.code),
            str(self.msg)
        )

    def __unicode__(self):
        return u'Spot data for spot_id {} unavailable at the following url: {}. Additional information: code: {} msg: {}'.format(

            unicode(self.spot_id),
            unicode(self.url),
            unicode(self.code),
            unicode(self.msg)
        )
