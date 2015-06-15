##########################################################################
#
#   Name:           forecast.py
#   Author:         Harrison Hubbell
#   Date:           06/15/2015
#   Description:    Make sure the module can propery query spots and
#                   handle spot_ids that are not valid.
#
##########################################################################

import inspect
import msw
from msw.spots.north_america import new_hampshire

def key():
    with open('util/key') as f:
        return f.read().strip()

def print_result(result):
    current = inspect.currentframe()
    caller = inspect.getouterframes(current, 2)

    callframe = caller[1][3]

    print('[{}]: {}'.format(callframe, "Pass" if result else "Fail"))

def test_valid_id(msw, spot_id):
    ok = False
    
    if msw.get(spot_id):
        ok = True
    
    print_result(ok)
    return ok

def test_invalid_id(m, spot_id):
    ok = False
    
    try:
        m.get(spot_id)
    except msw.SpotDataUnavailableError:
        # This is supposed to fail
        ok = True
    
    print_result(ok)
    return ok

def test_forecast(m, spot_id):
    ok = False

    s = m.get(spot_id)
    #test a bunch of things that should exist
    ok = (s.forecast and 
        s.forecast[0] and 
        s.forecast[0].swell.components.combined.direction and
        s.forecast[0].wind and
        s.forecast[0].condition.pressure)

    print_result(ok)
    return ok

if __name__ == '__main__':
    key = key() 
    m = msw.MagicSeaweed(key)

    test_valid_id(m, new_hampshire.THE_WALL)
    test_invalid_id(m, 2000)
    test_forecast(m, new_hampshire.THE_WALL)
