import pandas as pd
train = pd.read_csv('emails.csv')

train['index'] = train['message'].str.find('X-FileName:')

msg = []
for i in train['index']:
    msg.append(i)


i=0
list1 = []
for value in train['message']:
    element = value[msg[i]+23:]
    list1.append(element)
    i += 1

train['msg'] = list1
train = train.drop(columns=['file','message','index'])

train.to_csv('msg.csv')
