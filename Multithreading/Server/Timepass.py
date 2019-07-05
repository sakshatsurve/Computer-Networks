'''
import collections
def deckRevealedIncreasing(deck):
    N = len(deck)
    index = collections.deque(range(N))
    ans = [None] * N

    for card in sorted(deck):
        ans[index.popleft()] = card
        if index:
            index.append(index.popleft())
        print(ans,index)



deckRevealedIncreasing([17,13,11,2,3,5,7])

str = 'aaaaaAAAbbbbbbcccccdddd'
a = list(str)
s = a[0]
count =  0
b = [a[0]]
for i in range(0,len(a)):
    if(a[i]==s):
        count+=1
    else:
        b.append(count)
        s = a[i]
        count=1
        b.append(a[i])
b.append(count)
#b = ' '.join(b)
print(b)

import heapq

list = [
    {'prod_id':123, 'number_of_times_bought': 10},
    {'prod_id':124, 'number_of_times_bought': 5},
    {'prod_id':125, 'number_of_times_bought': 18},
    {'prod_id':126, 'number_of_times_bought': 20},
    {'prod_id':127, 'number_of_times_bought': 15}
]
print(heapq.nlargest(2,list, key=lambda i:i['number_of_times_bought'])) '''
import sys

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = []
        self.pointer = -1

    def push(self, x: int) -> None:
        self.head.append(x)
        self.pointer += 1

    def pop(self) -> None:
        self.pointer -= 1

    def top(self) -> int:
        try:
            return self.head[self.pointer]
        except:
            return None

    def getMin(self) -> int:
        min = 99999
        for i in range(0,self.pointer+1):
            if self.head[i] < min:
                min = self.head[i]

        if min == 99999:
            return None
        return min
x = MinStack()
x.push(-2)
x.push(0)
x.push(-3)
x.push(1)
#x.pop()
print(x.getMin(),x.top())