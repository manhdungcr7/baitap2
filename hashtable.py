'''class Hashtable:
    def __init__(self, size=1000):
        self.__size = size
        self.__table = [None] * self.__size
        self.__len = 0

    def __hash(self, value: int) -> int:
        return value % self.__size

    def insert(self, value):
        h = self.__hash(value)
        if self.__table[h] == None:
            self.__table[h] == [value]
            self.__len += 1
            return
        if value in self.__table[h]:
            return
        else:
            self.__table[h].append(value)
            self.__len += 1
        # Load factor
        if self.__len / self.__size > 0.7:
            self.__size *= 2
            old_table = self.__table

            self.__table = [None] * self.__size
            self.__len = 0
        # Trong old table có gì thì add vào hashtable cái đó
            for x in old_table:
                for y in x:
                    self.insert(y)
    def debug(self):
        for idx, bucket in enumerate(self.__table):
            print(f'{idx}: {bucket}')

    def search(self, value) -> bool:
        h = self.__hash(value)
        if self.__table[h] == None:
            return False
        return value in self.__table[h]

    def remove(self, value):
        h = self.__hash(value)
        if self.__table[h] == None:
            return
        if value in self.__table[h]:
            self.__table[h].remove(value)


def main():
    ht = Hashtable(3)
    a = [1,2,3,4,5]
    for i in a:
        ht.insert(i)
    ht.debug()


main()'''

# chaining hash table
class hashtable:
    def __init__(self, size=1000):
        self.__size = size
        self.__table = [None] * size
        self.__len = 0

    def __hash(self, value: int) -> int:
        return value % self.__size

    def insert(self, value):
        h = self.__hash(value)
        if self.__table[h] == None:
            self.__table[h] = [value]
            self.__len += 1
            return
        if value in self.__table[h]:
            return

        elif value not in self.__table[h]:
            self.__table[h].append(value)
            self.__len += 1

        if self.__len / self.__size > 0.7:
            self.__size *= 2
            old_table = self.__table[:]
            self.__len = 0
            self.__table = [None] * self.__size
            for bucket in old_table:
                if bucket != None:
                    for v in bucket:
                        self.insert(v)

    def search(self, value) -> bool:
        h = self.__hash(value)
        if self.__table[h] == None:
            return False
        return value in self.__table[h]

    def remove(self, value):
        h = self.__hash(value)
        if self.__table[h] == None:
            return
        if value in self.__table[h]:
            self.__table[h].remove(value)
            return

    def debug(self):
        for idx, bucket in enumerate(self.__table):
            print(f'{idx}: {bucket}')
# python set
def search_set(value, a):
    return value in a
#python dict
def tao_dict( a):
    s = int(len(a)/0.7)
    dic = {}
    for x in a:
        h = x%s
        try:
            dic[h].add(x)
        except:
            dic[h] = {x}
    return dic, s
def search_dict(value, dic, s):
    h = value%s
    try:
        return value in dic[h]
    except:
        return False
# binary search tree

class unbalanced_tree:
    class __tree_node:
        def __init__(self, value:int):
            self.value =  value
            self.left = None
            self.right  = None
            self.size = 1
    def __init__(self):
        self.__root = None
        self.__size = 0

    def __len__(self):
        return self.__root.size

    def __insert(root: __tree_node,  value : int):
        if root == None:
            return unbalanced_tree.__tree_node(value), True
        elif root.value == value:
            return root, False
        elif value < root.value :
            root.left, inserted = unbalanced_tree.__insert(root.left, value)
        else:
            root.right, inserted = unbalanced_tree.__insert(root.right, value)
        if inserted: root.size += 1
        return root, inserted
    def insert(self, value:int):
        self.__root, inserted = unbalanced_tree.__insert(self.__root, value)
    def __search2(r : __tree_node, v : int):
        if r == None:
            return None
        while r is not None:
            if r.value == v:
                return r
            elif r.value < v :
                r = r.right
            else:
                r = r.left
    def __search(root : __tree_node, value : int):
        if root == None:
            return None
        elif value < root.value:
            return unbalanced_tree.__search(root.left, value)
        elif value ==  root.value:
            return root
        else:
            return unbalanced_tree.__search(root.right, value)
    def search(self, value : int):
        return unbalanced_tree.__search(self.__root, value) != None



#main
import random, timeit
n = 10**6
s = set()
h = hashtable()
a = []
b = unbalanced_tree()
for i in range(n):
    x = random.randint(-n,n)
    h.insert(x)
    b.insert(x)
    a.append(x)
    s.add(x)
dic,y = tao_dict(a)
k = random.randint(-n,n)
execution_time1 = timeit.timeit(lambda:h.search(k), number=1000)
print(f'Thời gian chạy ht: {execution_time1} giây')
execution_time2 = timeit.timeit(lambda: b.search(k), number=1000)
print(f'Thời gian chạy bst: {execution_time2} giây')
execution_time3 = timeit.timeit(lambda:search_set(k,s) , number=1000)
print(f'Thời gian chạy set: {execution_time3} giây')
execution_time4 = timeit.timeit(lambda:search_dict(k,dic,y) , number=1000)
print(f'Thời gian chạy dict: {execution_time4} giây')