#encoding=utf-8
import jieba
import jieba.analyse as fx
import xmnlp as xm

def test():
  jieba.set_dictionary("./extra_dict/dict.txt.big")
  doc = "我 将 网球 拍卖 给 需要 的 人 。"
#  doc = "卖给需要的人"
#  doc = "它适用于信息检索和提取，请求处理，问答系统。从英文文本中，它能提取出主动宾元组，形容词、名词和动词短语，人名、地名、事件，日期和时间等语义信息。"
  seg_list = jieba.lcut(doc, cut_all=False)
  slen=0
  for e in seg_list:
    slen += len(e)
  print("doc:"+str(len(doc))+" sge:"+str(slen)+" rate:"+str(len(doc)/slen))
  print("seg: "+str(seg_list))
  word_list = jieba.lcut(doc, cut_all=True)
  slen=0
  for e in word_list:
    slen += len(e)
  print("word:"+str(slen)+" rate:"+str(len(doc)/slen))
  print("word: "+str(word_list))
  print("="*20)

  result = jieba.tokenize(doc,mode='search')
  for tk in result:
      print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
  print("="*20)

  tags = fx.extract_tags(doc,topK=10,withWeight=True)
  for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
  print("="*20)
#  print(",".join(tags))
  words = jieba.posseg.cut(doc)
  for word, flag in words:
    print('%s %s' % (word, flag))
  print("="*20)
 
  tags = jieba.analyse.extract_tags(doc, topK=20, withWeight=False, allowPOS=('n'))
  print(tags)
#  print("xm:"+str(xm.seg(doc, hmm=True)))
#  print("xm:"+str(xm.keyword(doc)))

if __name__ == '__main__':
  test()
