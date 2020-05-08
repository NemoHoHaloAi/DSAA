# 编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。
# 
# IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；
# 
# 同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。
# 
# IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。比如,  2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。
# 而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。
# 所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。
# 
# 然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。
# 
# 同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。
# 
# 说明: 你可以认为给定的字符串里没有空格或者其他特殊字符。
# 
# 链接：https://leetcode-cn.com/problems/validate-ip-address

class Solution:
    def checkIPv4(self, ip):
        items = [item for item in ip.split('.') if item and len(item)>0]
        print(items)
        if not items or len(items)!=4:
            return False
        try:
            # 开头不能有负号
            if len([item for item in items if item.startswith('-')]) > 0:
                return False
            # 开头不能有0
            if len([item for item in items if item != '0' and item.startswith('0')]) > 0:
                return False
            for item in items:
                if int(item)<0 or int(item)>255:
                    return False
        except Exception:
            return False
        return True
                
    
    def checkIPv6(self, ip):
        items = [item for item in ip.split(':') if item and len(item)>0]
        print(items)
        if not items or len(items)!=8:
            return False
        try:
            # 长度不能超过4个字符
            if len([item for item in items if len(item)>4]) > 0:
                return False
            # 开头不能有负号
            if len([item for item in items if item.startswith('-')]) > 0:
                return False
            # 开头最多只能连续有1个0
            # if len([item for item in items if item.startswith('00') or item.startswith('000') or item.startswith('0000')]) > 0:
                # return False
            for item in items:
                if int(item,16)<0:
                    return False
        except Exception:
            return False
        return True
    
    def validIPAddress(self, IP):
        if not IP or len(IP)<=0:
            return 'Neither'
        if IP.count('.')==3 and self.checkIPv4(IP):
            return 'IPv4'
        if IP.count(':')==7 and self.checkIPv6(IP):
            return 'IPv6'
        return 'Neither'

case = "01.01.01.01" 
res = Solution().validIPAddress(case)
print(res)

case = "1081:db8:85a3:01:-0:8A2E:0370:7334" 
res = Solution().validIPAddress(case)
print(res)

case = "172.16.254.1" 
res = Solution().validIPAddress(case)
print(res)

case = "2001:0db8:85a3:0:0:8A2E:0370:7334" 
res = Solution().validIPAddress(case)
print(res)

case = "256.256.256.256" 
res = Solution().validIPAddress(case)
print(res)

case = "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 
res = Solution().validIPAddress(case)
print(res)

case = "02001:0db8:85a3:0000:0000:8a2e:0370:7334" 
res = Solution().validIPAddress(case)
print(res)

# print(int('2001',16))
# print(int('0db8',16))
# print(int('0000',16))
# print(int('8A2E',16))