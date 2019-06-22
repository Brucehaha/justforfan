
# -*- utf-8 -*-
import sys
print(sys.getdefaultencoding())

s ="你好"

s_to_gbk=s.encode("GBK")
print(s_to_gbk.decode("GBK").encode("utf-8"))
print(s.encode())
print(s_to_gbk)
