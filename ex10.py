tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
food = "Cat food"
fish = "Fishies"
nip = "Catnip"
grass = "Grass"

fat_cat = '''
I'll do a list:
\t* %r
\t* %r
\t* %r\n\t* %r
''' % (food, fish, nip, grass)

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# text below creates an animated cursor looking thing

# while True:
#     for i in ["/", "-", "|", "\\", "|"]:
#         print "%s\r" % i,