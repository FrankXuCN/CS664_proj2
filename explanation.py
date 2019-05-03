#encoding=utf-8
import jieba
import jieba.analyse as fx


def explanation(doc):

  word_list = jieba.lcut(doc, cut_all=True)
  pos = jieba.posseg.cut(doc)
  slen=0
  for e in word_list:
    slen += len(e)

  posb_cut = []
  amb_key = []
  spart = ""
  lpart = []
  amb_flag = False
  if slen/len(doc) > 1:
    for e in word_list:
      if amb_flag :
        lpart.pop()
        spart = spart.replace(laste,'')
        if len([u for u in list(e) if u in list(laste)]) == 0:
          posb_cut.append(amb_key)
          return posb_cut

      spart += e
      lpart.append(e)
      if len(e)>1 :
        if spart in doc:
          tail = doc.replace(spart,'')
          l = [e for e in word_list if e not in lpart]
          if l == jieba.lcut(tail, cut_all=True):
            continue
          else:
            amb_flag = True
            amb_key.append(e)
            posb_cut.append(' '.join(lpart)+ ' ' + explanation(tail))
        else:
          continue
      laste = e
  else:
    return ' '.join(word_list)

def count(word, cut_lst):
  cnt = 0
  loop = 1
  if type(cut_lst[-1]) is list:
    loop = len(cut_lst.pop())

  for i in range(loop):
    l = jieba.lcut(cut_lst[i], cut_all=False)
    cnt += l.count(word)

  return cnt

if __name__ == '__main__':
  jieba.initialize()
  jieba.set_dictionary("./extra_dict/dict.txt.big")
  jieba.suggest_freq('网球拍', True)
#  doc = "我将网球拍卖给需要的人。"
#  doc = "我们研究所有东西"
#  doc = ["这个球拍很好", "我将网球拍卖给需要的人。","我们研究所有东西"]
#  doc = ["我们研究所建设了实验楼、办公楼、会客楼和娱乐馆。", "我们研究所有东西"]
#  doc = ["我有一只网球拍和很多网球。","网球的重要指标之一是弹性。","我的网球弹性很好，但是很旧了。","我将网球拍卖给需要的人。"]
  doc = ["网球的重要指标之一是弹性。","我的网球弹性很好，但是很旧了。","我将网球拍卖给需要的人。"]
  print("text is :"+doc[0]+doc[1]+doc[2])
  cut = []
  for cts in doc:
    l = explanation(cts)
    if type(l) is str:
      cut.append([l])
    else:
      cut.append(l)
  print("it could be :",format(cut))
  key = []
  for e in cut:
    if type(e[-1]) is list:
      key = e.pop()
  cnt = []
  c = 0
  if len(key) > 0:
    for e in key:
      for cts in cut:
        c += count(e,cts)
      cnt.append((e,c))
      c = 0
    print(cnt)

  print("="*30)
  print("POS will be showed:")
  for cts in cut:
    if len(cts) ==1 :
      words = jieba.posseg.cut(cts[0])
      for word, flag in words:
        print('%s %s' % (word, flag))
        
  else:
    print(len(cut))
