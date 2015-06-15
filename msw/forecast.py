##########################################################################
#
#   Name:           forecast.py
#   Author:         Harrison Hubbell
#   Date:           06/15/2015
#   Description:    Representation of a forecast and components
#
##########################################################################
    
class ForecastComponent(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems(): 
            if type(value) is dict:
                value = ForecastComponent(**value)
                
            setattr(self, key, value)

    def __str__(self):
        rep = ''
        for key, value in self.__dict__.iteritems():
            rep += '{}: {}\n'.format(key, value)

        return rep


class Forecast(ForecastComponent):
    """ 
    Forecast has the same base functionality as ForecastComponent,
    but additional methods will likely be included someday
    """
