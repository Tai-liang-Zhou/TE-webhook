# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:41:23 2019

@author: Tom
"""
from langconv import Converter
import requests
import codecs

def SendMessage_TE(message):
    url =  'http://61.216.75.236:8096/v1/openapi'
    payload = {"text" : Converter('zh-hans').convert(message)}
    headers = {
            'content-type': 'application/json',
            'appId' : '02632665ccf24c44a7cd4de0c3556fef',
            'userId' : 'tom',
            'sessionId' : 'ga0953166069'
            }
    r = requests.post(url, json=payload, timeout=float(4), headers=headers)
    r_obj = r.json()
    return r_obj['data'][0]['value']


with codecs.open('test_dialogue/dialogue_output.csv', 'a', 'utf-8') as dialogue_output_f:
    with codecs.open('test_dialogue/dialogue.csv', 'r', 'utf-8') as dialogue_f:
        for request in dialogue_f:
            request = request.split(',')
            for index in range(len(request)):
                messages = request[index].strip('\n').strip('\r')
                dialogue_output_f.write(messages + '\n' + SendMessage_TE(messages) + '\n')
                print('Request  : %s\nResponse : %s\n' %(messages, SendMessage_TE(messages)))
            dialogue_output_f.write('----------------------------------------------------\n')


with codecs.open('test_dialogue/dialogue.csv', 'r', 'utf-8') as dialogue_f:
    dialogue = []
    for request in dialogue_f:
        request = request.split(',')
        dialogue.append(request)

dialogue[0]
with codecs.open('test_dialogue/dialogue_output.csv', 'a', 'utf-8') as dialogue_output_f:
    for index in range(len(dialogue[1])):
        messages = request[index].strip('\n').strip('\r')
        response = SendMessage_TE(messages)
        dialogue_output_f.write(messages + '\n' + response + '\n')
        print('Request  : %s\nResponse : %s\n' %(messages, response))
    dialogue_output_f.write('----------------------------------------------------\n')







print('Request  : %s\nResponse : %s\n' %("ga", SendMessage_TE("ga")))
print('Request  : %s\nResponse : %s\n' %("0953166069 周", SendMessage_TE("0953166069 周")))
print('Request  : %s\nResponse : %s\n' %("两大一小", SendMessage_TE("两大一小")))
print('Request  : %s\nResponse : %s\n' %('下禮拜二下午五點', SendMessage_TE('下禮拜二下午五點')))
print('Request  : %s\nResponse : %s\n' %("对", SendMessage_TE("对")))
print('Request  : %s\nResponse : %s\n' %("我要两张", SendMessage_TE("我要两张")))
print('Request  : %s\nResponse : %s\n' %("我要靠窗的位置", SendMessage_TE("我要靠窗的位置")))
print('Request  : %s\nResponse : %s\n' %("不要", SendMessage_TE("不要")))
print('Request  : %s\nResponse : %s\n' %('改为下礼拜五下午五点半', SendMessage_TE('改为下礼拜五下午五点半')))
print('Request  : %s\nResponse : %s\n' %("姓周", SendMessage_TE("姓周")))
print('Request  : %s\nResponse : %s\n' %("好", SendMessage_TE("好")))
print('Request  : %s\nResponse : %s\n' %("不要", SendMessage_TE("不要")))
print('Request  : %s\nResponse : %s\n' %("$exit", SendMessage_TE("$exit")))




print('Request  : %s\nResponse : %s\n' %("ga", SendMessage_TE("ga")))
print('Request  : %s\nResponse : %s\n' %("0953166069 周", SendMessage_TE("0953166069 周")))
print('Request  : %s\nResponse : %s\n' %("兩個", SendMessage_TE("兩個")))
print('Request  : %s\nResponse : %s\n' %('下禮拜五六點', SendMessage_TE('下禮拜五六點')))
print('Request  : %s\nResponse : %s\n' %("是", SendMessage_TE("是")))
print('Request  : %s\nResponse : %s\n' %("我要靠窗的位置", SendMessage_TE("我要靠窗的位置")))
print('Request  : %s\nResponse : %s\n' %("不要", SendMessage_TE("不要")))
print('Request  : %s\nResponse : %s\n' %('那我要改成明天晚上七點', SendMessage_TE('那我要改成明天晚上七點')))
print('Request  : %s\nResponse : %s\n' %("我姓林", SendMessage_TE("我姓林")))
print('Request  : %s\nResponse : %s\n' %("是", SendMessage_TE("是")))


print('Request  : %s\nResponse : %s\n' %("不要", SendMessage_TE("不要")))
print('Request  : %s\nResponse : %s\n' %("$exit", SendMessage_TE("$exit")))



 # person-name
 hour_str  =  '晚上七点半'
    payload = {
    "id": "chrono",
    "hasContext": True,
    "arguments": {
        "orientation": "future",
        "timePoint": {
            "onlyOne": "last",
            "distinguishType": False
        },
        "duration": {
            "extract": False,
            "onlyOne": "last"
        }
    },
    "query": hour_str,
    }
    payload = json.dumps(payload, ensure_ascii=False)
    payload = payload.encode('utf-8')
    headers = {'content-type': 'application/json'}
    r = requests.post(constants.TDE_URL, payload, timeout=float(constants.REQUEST_TIMEOUT), headers=headers)
    r_obj = r.json()
    r_obj
    r_obj['informs'][0]['value']['chrono']['time']['items'][0]['hour']
    r_obj['informs'][0]['value']['chrono']['time']['items'][0]['minute']
   
    
    
    time_judge = re.compile(u'(早|晚|凌晨|上午|中午|下午|晚上)').search('七点十分晚上')
    
    if time_judge is not None:
        time_judge = time_judge.group(1)
        
     if time_judge in [u'晚',u'中午',u'下午',u'晚上']:
            if exact_hour < 12:
                exact_hour += 12
