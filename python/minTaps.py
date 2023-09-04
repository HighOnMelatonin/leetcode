# Minimum number of taps to open to water a garden

class Solution(object):
    def minTaps(self, n = int(), ranges = list()) -> int:
        intervals = []
        for i in range(n + 1):
            interval = (i - ranges[i], i + ranges[i])
            if self.inRange(self, 0, interval) and self.inRange(self, n, interval):
                return 1
            
            else:
                intervals.append(interval)
                # How to check for lowest coverage


    def inRange(self, i = int(), interval = tuple()) -> bool:
        '''
        :param i:       Number to check if in range

        :param range:   Tuple with high and low (low, high)
        '''
        if i >= interval[0] and i <= interval[1]:
            return True
        
        else:
            return False


# not a working solution