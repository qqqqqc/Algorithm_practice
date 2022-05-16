# 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。


# 第一个版本


def longgestCommonPrefix01(dataList):
    res = ""
    for i in range(len(dataList)):
        isComm = True
        commStr = dataList[0][i]
        for j in range(1,len(dataList)):
            if i < len(dataList[j]) and dataList[j][i] != commStr:
                isComm = False
                break
        if isComm:
            res += commStr
        else:
            break
    return res

# 第二个版本
def longgestCommonPrefix02(dataList):
    a = min(dataList)
    b = max(dataList)

    for s in range(len(dataList)):
        if a[s] != b[s]:
            return a[:s]
    return dataList


dataList = ["flower","flow","flight"]
print(longgestCommonPrefix01(dataList))
print(longgestCommonPrefix02(dataList))