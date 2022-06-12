import collections
from inspect import stack
from platform import node
from turtle import pos


class Node:
    def __init__(self,data) :
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        if self.data is None:
            self.data = data
        
        else:
            if data < self.data:
                if self.left is None:
                    self.left= Node(data)
                else:
                    self.left.insert(data)    
            
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)            
 
def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end=" ")
        inOrderPrint(r.right)

def preOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data,end=" ")
        preOrderPrint(r.left)
        preOrderPrint(r.right)                

def postOrderPrint(r):
    if r is None:
        return
    else:
        postOrderPrint(r.left)
        postOrderPrint(r.right)
        print(r.data,end=" ")
        
def makeLists(r):
    if r is None:
        return
    else:
        d[r.data]=[]
        
        makeLists(r.left)
        if r.left:
            d[r.data].append(r.left.data)
        if r.right:
            d[r.data].append(r.right.data)    
        makeLists(r.right)
    return d    
     
    # >>> d={}
    # >>> d[2]=[]
    # >>> d
    # {2: []}
     
    # >>> d[2].append(32)
    # >>> d
    # {2: [32]}     


#give Adjacency L ist as an input
#we need a queue(Queue) and a list(Visited List)
def bfs(al):
    queue=collections.deque('g')
    visited=[]
    
    #while queue is not empty
    while queue:
        #retrieve item from the queue
        node = queue.popleft()
        #append the node which we extracted from the queue
        visited.append(node)
        #take nodes into the queue from adjacency list
        
        # for x  in al[node]:
        #     queue.append(x)
        # OR
        [queue.append(x) for x in al[node]]
        
    print(visited)    
 
def dfs(al):
    stack= ['g']
    visited =[]
    while stack:
       node = stack.pop()
       if node not in visited:
           visited.append(node)
           [stack.append(x) for x in al[node]]
    print(visited)            
      
            
if __name__ == "__main__":
    root = Node("g")
    root.insert("c")
    root.insert("b") 
    root.insert("e")
    root.insert("a") 
    root.insert("e") 
    root.insert("d") 
    root.insert("f")            
    root.insert("i")
    root.insert("h") 
    root.insert("j") 
    root.insert("k") 

# printing all the nodes

inOrderPrint(root)
print("\n")
preOrderPrint(root)
print("\n")
postOrderPrint(root)
print("\n")

d={}
myl=makeLists(root)
# print(myl)

#adjacency list
for i in myl:
    print(f'{i}:{d[i]}')
    
# g:['c', 'i']
# c:['b', 'e']
# b:['a']
# a:[]
# e:['d', 'f']
# d:[]
# f:[]
# i:['h', 'j']
# h:[]
# j:['k']
# k:[]    

bfs(myl)
# ['g', 'c', 'i', 'b', 'e', 'h', 'j', 'a', 'd', 'f', 'k']

dfs(myl)