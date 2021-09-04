hh, mm, ss = map(int, input().split(":"))
nh, nm, ns = map(int, input().split(":"))
ti=0
nti=0
ti += (hh * 3600)
ti += (mm * 60)
ti += ss

nti += (nh * 3600)
nti += (nm * 60)
nti += ns

nti -= ti

if nti < 0:
    nti += 86400

print("%02d:%02d:%02d" % (nti / 3600,(nti%3600)/60, nti % 60))