class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            res = IP.split('.')
            if IP.count('.') == 3:
                for i in res:
                    if i.startswith('0') and i != '0':
                        return 'Neither'
                if '' in res:
                    return 'Neither'
                for i in res:
                    for j in i:
                        if j not in set('0123456789'):
                            return 'Neither'
                res = list(map(int, res))
                if all([0 <= i <= 255 for i in res]):
                    return "IPv4"
            return 'Neither'
        else:
            res = IP.split(':')
            if IP.count(':') == 7:
                if all([len(i) <= 4 for i in res]) and '' not in res:
                    for i in res:
                        for j in i:
                            if j not in set('0123456789abcdefABCDEF'):
                                return 'Neither'
                    return 'IPv6'
                else:
                    return 'Neither'
            else:
                return 'Neither'


if __name__ == "__main__":
    print(Solution().validIPAddress("1.0.1."))
