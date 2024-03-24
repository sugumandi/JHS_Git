#프로그램 명: NLP시스템
#학번:202021270
#이름:정희성
print('==========================================================')
print('          문장 유사도를 측정하는 프로그램입니다.')
print('==========================================================')
while 1:
    print('-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,')
    a=input('기존에 사용하는 문장을 이용하시겠습니까?(맞으면 1을 입력):')
    print('-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,')
    if a!='1': #사용자가 '1'이외에 아무값을 넣으면 문장 2개를 새로 입력하여 유사도 측정
        b=input('첫 번째 문장:') #첫 번째 문장 입력
        listb=list(b.split(' ')) #첫 번째 문장을 띄어쓰기를 기준으로 단어를 나누고, 나눈 단어를 리스트의 원소에 포함시킴
        c=input('두 번째 문장:') #두 번째 문장 입력
        listc=list(c.split(' ')) #두 번째 문장을 띄어쓰기를 기준으로 단어를 나누고, 나눈 단어를 리스트의 원소에 포함시킴
        print('-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,')
        d=(input('''- - - - - - - - - - - - - - - - - - - 
다음 중 원하는 알고리즘을 선택하시오.
- - - - - - - - - - - - - - - - - - -
*************************
1. Cosine Similarity
2. Jaccard Similarity
3. Pearson Similarity
*************************
알고리즘 선택 번호 입력(1,2,3):'''))
        if d=='1': #코사인 유사도
            dou=set(listb) & set(listc) #첫 문장의 리스트와 두 번째 문장의 리스트중 중복되는 원소를 1개로 추려내기 위해 집합으로 바꾸고 합집합을 구함
            doul=list(dou) # 윗 문장에서 만든 합집합을 다시 리스트로 바꿈
            sum, sum1, sum2=0,0,0
            l1=list(set(listb)) #첫 문장의 리스트를 집합으로 바꾸어 리스트 내의 중복 원소를 삭제한 후 다시 리스트로 변환함
            l2=list(set(listc)) #두 번째 문장도 윗줄과 같은 과정을 거침
            for i in range(len(doul)): #코사인 유사도 식의 분자인 내적을 구하기 위해 for함수를 사용함
                dot=(listb.count(doul[i]))*(listc.count(doul[i])) #첫 문장 단어 리스트 'listb'와 두 번째 리스트 'listc' 두 리스트에서 중복되는 원소의 개수를 곱하여 내적을 구함
                sum+=dot
            for j in range(len(set(listb))):
                #크기를 구하기 위해 for를 사용하여 첫 문장 단어 리스트에 있는 각 단어의 개수를 제곱하여 더함
                #len(set(listb))을 사용한 이유는 중복되는 단어 원소는 1개로 추려내기 위해 집합으로 바꿈,
                mit=(listb.count(l1[j]))**2 #첫 번째 문장의 단어 리스트 를 통해 구한 TF를 제곱함
                sum1+=mit #제곱한 TF를 더함
            for k in range(len(set(listc))):
                mit2=(listc.count(l2[k]))**2
                sum2+=mit2
                #바로 위 for문과 동일함
            import math #루트를 사용하기 위해 math 라이브러리를 가져옴
            cosine=sum/(math.sqrt(sum1)*math.sqrt(sum2)) #코사인 유사도 식에 앞서 구한 값들을 대입하고 계산(분모에서는 공식대로 루트를 씌워서 계산) 
            print('----------------비교 문장 확인----------------')
            print('첫 번째 문장: %s' %b)
            print('두 번째 문장: %s' %c)
            print('----------------------------------------------')
            print('두 문장의 Cosine Similarity:%.3f' %cosine) #코사인 유사도 결과 출력
            print('----------------------------------------------')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            qu=input('  프로그램을 종료하시겠습니까?(종료하려면 1입력) :')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            if qu=='1': #사용자가 1을 누르면 프로그램 종료('1'외에 아무값을 넣으면 while에 의해 반복)
                print('***********************')
                print('프로그램을 종료합니다.')
                print('***********************')
                break #break를 이용하여 while문 탈출
        elif d=='2': #자카드 유사도
            Jaccard=(len(set(listb).intersection(set(listc)))/len(set(listb).union(set(listc))))
            # 리스트로 만든 첫 번째, 두 번째 문장의 교집합의 원소의 개수를 두 집합의 합집합의 원소의 개수로 나눔
            print('----------------비교 문장 확인----------------')
            print('첫 번째 문장: %s' %b)
            print('두 번째 문장: %s' %c)
            print('----------------------------------------------')
            print('두 문장의 Jaccard Similarity:%.3f' %Jaccard) #자카인 유사도 결과 출력
            print('----------------------------------------------')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            qu=input('  프로그램을 종료하시겠습니까?(종료하려면 1입력) :')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            if qu=='1':#사용자가 1을 누르면 프로그램 종료('1'외에 아무값을 넣으면 while에 의해 반복)
                print('***********************')
                print('프로그램을 종료합니다.')
                print('***********************')
                break #break를 이용하여 while문 탈출
        elif d=='3':#피어슨 유사도
            dou=set(listb) | set(listc) #집합으로 변환한 첫 번째, 두 번째 문장의 리스트의 합집합을 구해 두 문장에서 사용된 모든 단어를 집합으로 추출함
            doul=list(dou) #윗줄에서 만들어진 집합을 리스트로 변환함
            sum,sum1,sum2,sum3,sum4=0,0,0,0,0
            for i in range(len(dou)):
                a=(listb.count(doul[i]))
                sum+=a #첫 문장 리스트에서 사용된 단어의 TF를 모두 더함
            avg1=sum/(len(doul)) #더한 값을 모든 단어의 개수로 나누어 첫 문장의 평균을 구함
            for j in range(len(dou)):
                bl=(listc.count(doul[j]))
                sum1+=bl
            avg2=sum1/(len(doul)) #첫 문장과 같은 방법으로 두 번째 문장의 평균을 구함
            for k in range(len(dou)): #분자
                cl=((listb.count(doul[k]))-avg1)*((listc.count(doul[k]))-avg2)
                sum2+=cl #첫 번째, 두 번째 문장에서 두 문장에 모두 쓰인 TF에 2개의 평균빼고 곱하여 더함 
            for l in range(len(dou)):#분모
                lb=((listb.count(doul[l]))-avg1)**2 #첫 번째 문장의 단어 리스트 를 통해 구한 TF를 제곱함
                sum3+=lb #제곱한 값을 모두 더함
            for m in range(len(dou)):
                lc=((listc.count(doul[m]))-avg2)**2
                sum4+=lc #두 번째 문장도 위와 같은 방법으로 제곱값을 모두 더함
            import math #루트를 사용하기 위해 math 라이브러리를 가져옴
            pearson=(sum2)/(math.sqrt(sum3)*math.sqrt(sum4)) #루트를 이용하여 피어슨 상관계수 공식에 수를 집어넣고 유사도를 구함
            print('----------------비교 문장 확인----------------')
            print('첫 번째 문장: %s' %b)
            print('두 번째 문장: %s' %c)
            print('----------------------------------------------')
            print('두 문장의 Pearson Similarity:%.3f' %pearson) #피어슨 유사도 결과 출력
            print('----------------------------------------------')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            qu=input('  프로그램을 종료하시겠습니까?(종료하려면 1입력) :')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            if qu=='1': #사용자가 1을 누르면 프로그램 종료('1'외에 아무값을 넣으면 while에 의해 반복)
                print('***********************')
                print('프로그램을 종료합니다.')
                print('***********************')
                break #break를 이용하여 while문 탈출
        else:
            print('번호를 잘못 입력하셨습니다. 다시 입력해주세요.')
            # 코사인 유사도, 자카드 유사도, 피어슨 유사도 외에 다른 것을 선택했을 경우 사용자가 다시 입력하게끔 함
    if a=='1': #사용자가 이전 유사도 측정 때 사용한 2개의 문장을 사용자가 다시 사용할 수 있게끔 함
        #2개의 문장이 이미 b와 c라는 변수에 저장되어있기 때문에 문장입력 함수는 없음.
        #이 밑으로는 a=='0'일 때와 동일한 유사도 측정
        d=(input('''- - - - - - - - - - - - - - - - - - - 
다음 중 원하는 알고리즘을 선택하시오.
- - - - - - - - - - - - - - - - - - -
*************************
1. Cosine Similarity
2. Jaccard Similarity
3. Pearson Similarity
*************************
알고리즘 선택 번호 입력(1,2,3):'''))
        if d=='1':
            dou=set(listb) & set(listc)
            doul=list(dou)
            sum, sum1, sum2=0,0,0
            l1=list(set(listb))
            l2=list(set(listc))
            for i in range(len(doul)):
                dot=(listb.count(doul[i]))*(listc.count(doul[i]))
                sum+=dot
            for j in range(len(set(listb))):
                mit=(listb.count(l1[j]))**2
                sum1+=mit
            for k in range(len(set(listc))):
                mit2=(listc.count(l2[k]))**2
                sum2+=mit2
            import math 
            cosine=sum/(math.sqrt(sum1)*math.sqrt(sum2))
            print('----------------비교 문장 확인----------------')
            print('첫 번째 문장: %s' %b)
            print('두 번째 문장: %s' %c)
            print('----------------------------------------------')
            print('두 문장의 Cosine Similarity:%.3f' %cosine)
            print('----------------------------------------------')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            qu=input('  프로그램을 종료하시겠습니까?(종료하려면 1입력) :')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            if qu=='1':
                print('***********************')
                print('프로그램을 종료합니다.')
                print('***********************')
                break
        elif d=='2':
            Jaccard=(len(set(listb).intersection(set(listc)))/len(set(listb).union(set(listc))))
            print('----------------비교 문장 확인----------------')
            print('첫 번째 문장: %s' %b)
            print('두 번째 문장: %s' %c)
            print('----------------------------------------------')
            print('두 문장의 Jaccard Similarity:%.3f' %Jaccard)
            print('----------------------------------------------')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            qu=input('  프로그램을 종료하시겠습니까?(종료하려면 1입력) :')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            if qu=='1':
                print('***********************')
                print('프로그램을 종료합니다.')
                print('***********************')
                break
        elif d=='3':
            dou=set(listb) | set(listc)
            doul=list(dou)
            sum,sum1,sum2,sum3,sum4=0,0,0,0,0
            for i in range(len(dou)):
                a=(listb.count(doul[i]))
                sum+=a
            avg1=sum/(len(doul))
            for j in range(len(dou)):
                bl=(listc.count(doul[j]))
                sum1+=bl
            avg2=sum1/(len(doul))
            for k in range(len(dou)):
                cl=((listb.count(doul[k]))-avg1)*((listc.count(doul[k]))-avg2)
                sum2+=cl
            for l in range(len(dou)):
                lb=((listb.count(doul[l]))-avg1)**2
                sum3+=lb
            for m in range(len(dou)):
                lc=((listc.count(doul[m]))-avg2)**2
                sum4+=lc
            import math
            pearson=(sum2)/(math.sqrt(sum3)*math.sqrt(sum4))
            print('----------------비교 문장 확인----------------')
            print('첫 번째 문장: %s' %b)
            print('두 번째 문장: %s' %c)
            print('----------------------------------------------')
            print('두 문장의 Pearson Similarity:%.3f' %pearson)
            print('----------------------------------------------')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            qu=input('  프로그램을 종료하시겠습니까?(종료하려면 1입력) :')
            print('* - * - * - * -* - * - * - * -* - * - * - * - * -')
            if qu=='1':
                print('***********************')
                print('프로그램을 종료합니다.')
                print('***********************')
                break
        else:
            print('번호를 잘못 입력하셨습니다. 다시 입력해주세요.')
