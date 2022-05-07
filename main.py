import data as dt
import requests
import json
import html

#Online.
js = requests.get(dt.url).text 
#Offline.
#js = dt.js

#Data conversion class, JSON to dictionary.
class Data(object):
    def __init__(self, js):
        self.js = js

    def conv(self):
        r = json.loads(self.js)
        del r['response_code']
        return r

#Trivia class.
class Trivia(object):
    def __init__(self, r, num, c = 0):
        self.r = r
        self.num = num
        self.c = c

    def quiz(self):
        for i in range(self.num):
            answer = html.unescape(self.r['results'][i]['question'])
            answer = input(f"Q{i+1}: {answer} (True/False)?: ")
            if answer == self.r['results'][i]['correct_answer']:
                print('Correct!')
                self.c += 1
            else:
                print('Wrong!')
                print(f"The correct answer was: {self.r['results'][i]['correct_answer']}")
            print(f'Your current store is: {self.c}/{self.num} \n\n\n')

    def results(self):
        print("RESULTS")
        print(f'Your score is: {self.c}/{self.num}')

d = Data(js)
r = d.conv()
num = len(r['results'])
tr = Trivia(r, num)
tr.quiz()
tr.results()