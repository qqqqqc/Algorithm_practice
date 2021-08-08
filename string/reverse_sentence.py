# 句子逆序
# 描述
# 将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
# 所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
#
# 输入描述：
# 输入一个英文语句，每个单词用空格隔开。保证输入只包含空格和字母。
#
# 输出描述：
# 得到逆序的句子
#
# 示例1
# 输入：
# I am a boy
# 输出：
# boy a am I


def reverse_sentence(sen):
    sen_list = sen.split()  # 可以关注下 split() 和 split(' ') 的区别
    out_sen = []
    for s  in sen_list[::-1]:
        out_sen.append(s)

    return " ".join(out_sen)

# print(reverse_sentence("I am a boy"))



# 升级版本
# 对字符串中的所有单词进行倒排。
# 说明：
# 1、构成单词的字符只有26个大写或小写英文字母；
# 2、非构成单词的字符均视为单词间隔符；
# 3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
# 4、每个单词最长20个字母；
#
# 输入描述：
# 输入一行以空格来分隔的句子
#
# 输出描述：
# 输出句子的逆序
#
# 示例1
# 输入：
# I am a student
# 输出：
# student a am I
# 示例2
# 输入：
# $bo*y gi!r#l
# 输出：
# l r gi y bo


def reverse_sentence_2(sen):

    for i in sen:
        if not i.isalpha():
            sen = sen.replace(i," ")
    res = []
    for i in sen.split():
        res.append(i)
    return " ".join(res[::-1])

print(reverse_sentence_2("$bo*y gi!r#l"))