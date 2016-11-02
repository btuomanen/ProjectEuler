from pylab import *

nums = array(range(1,101,1))

print ( abs(sum(nums)**2 - sum(nums*nums)) )