'''
Data cleaning for email.csv
Delete all message heads, and removed all noisy text including meaningless file names.
'''

import pandas as pd
import re

train = pd.read_csv('emails.csv')

# Create index column recording ending index of string we do not need
train['index'] = train['message'].str.find('X-FileName:')

# Create a list to store all index
msg = []
for i in train['index']:
    msg.append(i)

# Create another list to store strings after deleting non-sense info
i=0
list1 = []
for value in train['message']:
    element = value[msg[i]+24:].replace('-','').replace('-Privileged).pst','').replace('>','').replace('Privileged).pst','').replace('\n','').replace('  ','').strip('\"')
    text = re.sub(r'[^A-Za-z. ]', '', element)
    text = text.lower()
    list1.append(text)
    i += 1

# Create msg column and drop old columns
train['msg'] = list1
train = train.drop(columns=['file','message','index'])

# Create a new .csv file from train dataframe
train.to_csv('text.csv')