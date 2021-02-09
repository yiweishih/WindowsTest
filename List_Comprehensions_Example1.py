#!/usr/bin/python3
"""
Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the dictionary tester. Do this using a list comprehension.
"""





import json

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
compri = []

"""
# print our data structure by json dumps:
dic_to_json = json.dumps(tester['info'], indent=2)
print(dic_to_json)
"""

inner_list = tester['info']
compri = [d['name'] for d in inner_list]
print(compri)

"""
# Traditional Way: 
for key in tester:
    for i in tester[key]:
        for sec_key in i:
            if sec_key == "name":
                compri.append(i[sec_key])

print(compri)
"""