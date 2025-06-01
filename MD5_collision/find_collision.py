# import hashlib
#
# res = hashlib.md5("elena".encode())
# print(res.hexdigest())
#
# res1 = hashlib.md5("admin".encode())
# print(res1.hexdigest())
#
# res2 = hashlib.md5("admin2".encode())
# print(res2.hexdigest())
#
#
from hashlib import md5
from difflib import ndiff

def showdiff(a, b):
    for i,s in enumerate(ndiff(a, b)):
        if s[0]==' ': continue
        elif s[0]=='-':
            print(u'Delete "{}" from position {}'.format(s[-1],i))
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))
                        # -
a = "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
b = "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"

showdiff(a, b)

ahash = md5(a.encode('utf-8')).hexdigest()
bhash = md5(b.encode('utf-8')).hexdigest()
assert(ahash == bhash)