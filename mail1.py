class LinearEquation:
    def __init__(self, a=1.0, b=1.0, c=0.0):
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)

    def __repr__(self):
        if self.a>0 and self.b>0 and self.c>0:
            return "{}x + {}y = {}".format(self.a, self.b, self.c)
        elif self.a<0 and self.b>0 and self.c>0:
            return "-{}x + {}y = {}".format(abs(self.a), self.b, self.c)
        elif self.a>0 and self.b<0 and self.c>0:
            return "{}x - {}y = {}".format(self.a, abs(self.b), self.c)
        elif self.a>0 and self.b>0 and self.c<0:
            return "{}x + {}y = -{}".format(self.a, self.b, abs(self.c))
        elif self.a<0 and self.b<0 and self.c>0:
            return "-{}x - {}y = {}".format(abs(self.a), abs(self.b), self.c)
        elif self.a<0 and self.b>0 and self.c<0:
            return "-{}x + {}y = -{}".format(abs(self.a),self.b, abs(self.c))
        elif self.a>0 and self.b<0 and self.c<0:
            return "{}x - {}y = {}".format(self.a, abs(self.b), abs(self.c))
        else:
            return "-{}x - {}y = -{}".format(abs(self.a), abs(self.b), abs(self.c))
      

    def __str__(self):
      if self.a>0 and self.b>0 and self.c>0:
        return "{}x + {}y = {}".format(self.a, self.b, self.c)
      elif self.a<0 and self.b>0 and self.c>0:
        return "-{}x + {}y = {}".format(abs(self.a), self.b, self.c)
      elif self.a>0 and self.b<0 and self.c>0:
        return "{}x - {}y = {}".format(self.a, abs(self.b), self.c)
      elif self.a>0 and self.b>0 and self.c<0:
        return "{}x + {}y = -{}".format(self.a, self.b, abs(self.c))
      elif self.a<0 and self.b<0 and self.c>0:
        return "-{}x - {}y = {}".format(abs(self.a), abs(self.b), self.c)
      elif self.a<0 and self.b>0 and self.c<0:
        return "-{}x + {}y = -{}".format(abs(self.a),self.b, abs(self.c))
      elif self.a>0 and self.b<0 and self.c<0:
        return "{}x - {}y = {}".format(self.a, abs(self.b), abs(self.c))
      else:
        return "-{}x - {}y = -{}".format(abs(self.a), abs(self.b), abs(self.c))
      

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        return LinearEquation(a, b, c)

    def isparallel(self, other):
        return self.a/other.a == self.b/other.b and self.a/other.a != self.c/other.c

    def intersects(self, other):
        return self.a/other.a != self.b/other.b

    def overlaps(self, other):
        return self.a/other.a == self.b/other.b and self.a/other.a == self.c/other.c
eqn=LinearEquation(1,-1,1)
print(abs(eqn.b))
print(eqn.__repr__())