class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        n = list(time)
        if(n[0]=='?'):
            if(n[0]=='?' and int(n[1]>3)):
                n[0]='1'
            else:
                n[0]='2'
        if n [1]=='?':
            if n[0] == '2':
                n[1] = '3'
            else:
                n[1]='9'
        if n [3 ]=='?':
            n[3]='5'
        if n[4]=='?':
            n[4]='9'
        return ''.join(n)
