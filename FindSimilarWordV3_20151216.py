
# coding: utf-8

# ############使用說明###############
# #finalmethod((1),(2),(3))
# #(1)排序較高的(檔名)
# #(2)排序較低的(檔名)-->最後一筆資料一定要是0
# #(3)要輸出的檔(可自己取)
# ###***(1)與(2)的'第一筆資料'一定要一樣
# ###***(1)與(2)的資料長度不一樣沒關係,但(2)的最後一筆一定要是0
# ###***每筆資料只能在2~7個字之間(可自己修改,但超過七個字笑能會變很差)
# ###***只能兩兩比對,比對到第三個會無法新增別名下去
# ############使用說明##############
# 
# 1.先執行下面的方法
# 
# 2.再跑finalmethod方法

# In[1]:

###Original version
###字串比對--->生成一含有別名的 place3 ,但不含新的景點-->place3 = place + 別名
def firstpk(fileone,filetwo,filefinal):
    f = open(filefinal,'w')
    for line in open(fileone):
        for linetwo in open(filetwo):
            #都不符合 ->自己
            if linetwo.split(',')[0].strip() == '0' :
                f.write(line.split(',')[0].strip()+',\n')
            #符合[完全相同] ->自己
            elif findSimilarWord(line.split(',')[0].strip() , linetwo.split(',')[0].strip()) == "SAME":
                f.write(line.split(',')[0].strip()+',\n')
                #f.write('YYYYY\n')
                break
            #符合[相似] ->自己+別名
            elif findSimilarWord(line.split(',')[0].strip() , linetwo.split(',')[0].strip()) == "TRUE":
                f.write(line.split(',')[0].strip()+','+linetwo.split(',')[0].strip()+',\n')
                break
    f.close()     
###把有重複的存進tempnum裡面
def temp(filefinal,filetwo):
    tempnum=[]
    for line in open(filefinal):
        innum = 0
        for linetwo in open(filetwo):
            innum += 1
            if line.split(',')[1].strip(): #有別名的才會進來
                if line.split(',')[1].strip() == linetwo.split(',')[0].strip():
                    tempnum.append(innum)#把有出現別名的母樣本順序記下來
                    break
            else: #沒有別名的
                if line.split(',')[0].strip() == linetwo.split(',')[0].strip():  #出現一樣的名字
                    tempnum.append(innum)  #把出現一樣名字的記下來
                    break
    return tempnum

def final(tempnum,filefinal,filetwo):
    f = open(filefinal,'a')
    num = 0
    for linetwo in open(filetwo):
        num += 1
        if num not in tempnum:
            if linetwo.split(',')[0].strip() != '0':
                f.write(linetwo.strip()+"\n")
    f.close()
###別名比對方法

###使用說明：
#(1)符合相似--回傳-->TRUE
#(2)完全相符--回傳-->SAME
#(3)  不相符--回傳-->FALSE
#(4)長度不在2~7個字->OVER

##########################################

def findSimilarWord(Attraction,TestString):
    
###先問傳進的東西是不是一樣
    if Attraction == TestString:
        #print "This is the samething"
        return 'SAME'
    else:
        import itertools
        import re
        
###把字串拆開放進List
        s1 = Attraction.decode('utf-8')

        AttDic=[]
        for cnt in range(0,len(s1)):
            AttDic.append(s1[cnt])     
        s=[]
        for i in AttDic:
            s.append(i.encode('utf-8'))
###判斷輸入的字串長度(2-5個字-->從2個找 ; 6-7個字-->從3個找)
        if len(s) <= 7:
            xn = 3
            if len(s) in range(2,6):
                xn = 2
###把字串排列組合印出來-->寫到文件
        if len(s) in range(2,8):
            f = open('string.txt','w')
            for num in range(xn,len(s)+1):
                for i in list(itertools.permutations(s,num)):
                    for u in range(0,num):
                        f.write(i[u]+" ")
                    f.write('\n')
            f.close()        
###讀取文件--->放到list
            dic=[]
            f1 = open('string.txt','r')
            for line in f1:
                dic.append(line.strip())
            f1.close()    
###另存一個正規化的list
            redic=[]
            for i in dic:
                redic.append('(.*)'+'(.*)'.join(i.split())+'(.*)')
###檢視是否match
            correctnum = 0
            for ele in redic:
                if re.match(ele,TestString):
                    #print "match : "+TestString, " ; matchRegex is : "+ele
                    correctnum += 1
###如果correctnum > 0 (有任何一筆match) 回傳TRUE 反則就是FALSE                    
            if correctnum > 0:
                return 'TRUE'
            else:
                return 'FALSE'
        else:
            #print "Try insert 2 ~ 7 letters"
            return 'OVER'
##########################################
def finalmethod(place,place2,place3):
    firstpk(place,place2,place3)
    final(temp(place3,place2),place3,place2)


# In[4]:

finalmethod('place.txt','place2.txt','place3.txt')

