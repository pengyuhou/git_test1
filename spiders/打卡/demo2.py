import re

s = 'ASP.NET_SessionId=sh1c1eftwobqxa245oa1trn3; __RequestVerificationToken=2QVja35zdIL40lhMfA9q83LhLslfJ4SPso-P7jcCjlwlRM1RGfbm7vGfBmZ50zQTU47cYRAaZSaJz8nxU4ltaxM1qCy1bF5cA8goKzbsm8E1; .ASPXFORMSAUTHYZY=C8F14161AC03A35F0F12638E29E37C6F906B58C35A4E01BEEAECB9125AB82503EE44710CFE464EFE8AF7510AC3C0BE3F7E5536288AEEE95D0B5514C199EBEB7A53836FD462B124B0363BF0E00E4CE8B7B74FB9C7D0F44A4BA97017DBB9759C032582D94C9C0873DE20F34BA2BAAB2163'
s = list(s)
ret = []
for i in s:
    if i != ' ':
        ret.append(i)
s = ''.join(ret)

reg = re.compile('[=;]')

res = re.split(reg, s)

key = []
value = []
for i in range(len(res)):
    if i % 2:
        value.append(res[i])
    else:
        key.append(res[i])

ret = [(i, j) for i, j in zip(key, value)]
print(dict(ret))
