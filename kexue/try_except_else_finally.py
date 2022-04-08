#!/usr/bin/python
import math

print '===================================='
try:
    math.sqrt(-1)
except ValueError, e:
    print 'ValueError: %s' % e
except AttributeError, e:
    print 'AttributeError: %s' % e
except:
    print 'Other Exception: %s' % e
else:
    print 'No error found'
finally:
    print 'Finally. #1\n'


print '===================================='
try:
    None.get('a')
except ValueError, e:
    print 'ValueError: %s' % e
except AttributeError, e:
    print 'AttributeError: %s' % e
except:
    print 'Other Exception: %s' % e
else:
    print 'No error found'
finally:
    print 'Finally. #2\n'


print '===================================='
try:
    1 + 1
except ValueError, e:
    print 'ValueError: %s' % e
except AttributeError, e:
    print 'AttributeError: %s' % e
except:
    print 'Other Exception: %s' % e
else:
    print 'No error found'
finally:
    print 'Finally. #3\n'
