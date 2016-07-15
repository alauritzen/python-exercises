days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\nSep\nOct\nNov\nDec"
something = "something"
double_quotes = "double-quotes"
how_many = 4

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's %s going on here.
With the three %s.
We'll be able to type as much as we like.
Even %d lines if we want, or %d, or %d.
""" % (something, double_quotes, how_many, how_many+1, how_many+2)