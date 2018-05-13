class MemberFunc(object):
    """docstring for MemberFunc."""
    def __init__(self):
        super(MemberFunc, self).__init__()

    def leftTrapezoid(self,x,tomin,candidate):
        if x <= candidate[2]:
            return min(tomin,1)
        elif candidate[2] < x < candidate[3]:
            has = (candidate[2]-x)/(candidate[3]-candidate[2]);
            return min(tomin,abs(has))
        elif x >= candidate[3]:
            return min(tomin,0)
        else:
            return 0

    def rightTrapezoid(self,x,tomin,candidate):
        # print(x)
        if x <= candidate[0]:
            return min(tomin,0)
        elif candidate[0] < x < candidate[1]:
            has = (x-candidate[0])/(candidate[1]-candidate[0]);
            return min(tomin,abs(has))
        elif x >= candidate[1]:
            return min(tomin,1)
        else:
            return 0

    def centerTriangular(self,x,tomin,candidate):
        if x <= candidate[0]:
            return min(tomin,0)
        elif candidate[0] < x <= candidate[1]:
            has = (x-candidate[0])/(candidate[1]-candidate[0]);
            return min(tomin,abs(has))
        elif candidate[1] < x < candidate[3]:
            has = (candidate[3]-x)/(candidate[3]-candidate[1]);
            return min(tomin,abs(has))
        elif x >= candidate[3]:
            return min(tomin,0)
        else:
            return 0`
