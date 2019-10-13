import jieba.analyse


with open("E:\\code\\PycharmProjects\\keywords\\waihuiba.txt", "r", encoding='utf-8') as f:
    s = f.read()
    f.close()

jieba.analyse.set_stop_words("E:\\code\\PycharmProjects\\keywords\\stop_words.txt")
tags = jieba.analyse.extract_tags(s, topK=2000, withWeight=True)
for v, n in tags:
    print(v + '\t' + str(n))
