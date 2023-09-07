# Question 1
# http://www.pythonchallenge.com/pc/def/map.html

code =  "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

'''
HINT
K->M
O->Q
E->G
'''

# print(ord('M'))
# print(chr(ord('M')))
# 97-122

def trans(code):
    code = list(code)
    for i in range(len(code)):

        if code[i] in " ()'/." :
            pass
        else:
            iid = ord(code[i])
            if iid +2 > 122:
                iid -= 24
            else:
                iid +=2
            code[i] = chr(iid)
    return ''.join(code)
print(trans(code))

url = 'http://www.pythonchallenge.com/pc/def/map.html'
print(trans('map'))
ans_url = 'http://www.pythonchallenge.com/pc/def/ocr.html'