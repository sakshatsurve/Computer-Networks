class Tree:
    def __init__(self, d):
        self.dict = d
        self.stack = []
    def dfs(self,n,x):
        for i in range(len(self.dict[n])):
            self.stack.append(self.dict[n][i])
            if self.dict[n][i] in self.dict:
                self.dfs(self.dict[n][i],x)
            if x == self.stack[-1]:
                return
            self.stack.pop(-1)
        return
    def print_dfs(self,n,x):
        self.stack = []
        self.stack.append(n)
        y = self.dfs(n,x)
        return self.stack
    def least_common_ancestor(self,a,b):
        i=0
        j=0
        while(i in range(len(a)) and j in range(len(b))):
            if a[i] == b[j]:
                i+=1
                j+=1
                continue
            return a[i - 1]
        return -1
t = Tree({0: [1, 2, 3], 1: [4, 5, 6], 2: [7], 3: [8, 9], 4: [10], 5: [11], 6: [12]})
x = t.print_dfs(0,10)
y = t.print_dfs(0,12)
print(x,y)
print(t.least_common_ancestor(x,y))


#print(y)