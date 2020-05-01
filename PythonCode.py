def range_data():                           #to find range od different alphabets
    low1=low[-1]+(range_check[-1]*lows)
    high1=low[-1]+(range_check[-1]*highs)
    single_msg.append(low1)
    single_msg.append(high1)
    single_msg.append(high1-low1)
    coded_msg.append(single_msg)
    low.append(low1)
    high.append(high1)
    range_check.append(high1-low1)


input_message=input()
'''n=len(input_message)                  #alternative method to find probabilities
prob={}
msg=set(input_message)
for i in msg:
    z=input_message.count(i)
    y=float(z)/n
    prob[i]=y'''

prob={'B':0.1,'I':0.1,'L':0.2,'G':0.1,'A':0.1,'T':0.1,'E':0.1,'S':0.1,' ':0.1}
data=list(prob.keys())                  #to store all the alphabets
data.sort()
range_prob=[]                           #to store range of probabilities of all alphabets
for i in range(len(data)):
    data_prob=[]                        #to store single alphabet probability range
    data_prob.append(data[i])
    if i==0:
        data_prob.append(0)
        data_prob.append(prob[data_prob[0]])
        range_prob.append(data_prob)
    else:
        data_prob.append(range_prob[i-1][2])
        data_prob.append(data_prob[-1]+prob[data_prob[0]])
        range_prob.append(data_prob)
  
low=[]                                  #to store all low values
high=[]                                 #to store all high values
range_check=[]                          #to store all ranges
low.append(0)
high.append(1)
range_check.append(1)
coded_msg=[]                            #to store alphabet, low, high and range

for x in input_message:
    for i in range(len(range_prob)):
        if x==range_prob[i][0]:
            lows=range_prob[i][1]       #to get low of symbol from range of prob for each alphabet
            highs=range_prob[i][2]      #to get high of symbol from range of prob for each alphabet
            break
    single_msg=[]                   #to store alphabet, low_new, high_new, final range for each alphabet
    single_msg.append(x)
    range_data()
print(coded_msg)
