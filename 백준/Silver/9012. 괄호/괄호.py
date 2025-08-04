class Casually_Stack:
    def __init__(self):
        self.s = []
        
    def push(self,data):
        self.s.append(data)
        
    def pop(self):
        return self.s.pop() # list 의 이미 존재하는 pop 함수 이용 
        #return self.s[-1]  # 맨 마지막 값을 뺀다.

    def is_empty(self):
        return len(self.s) == 0
        
    def peek(self):
        # 비어 있으면 "비어 있습니다"
        # 비어 있지 않으면 가장 윗 값
        if self.is_empty() == 1:
            return "비어 있습니다"
        else:
            return self.s[-1]

    def __str__(self):
        return str(self.s)
    
T = int(input())
b_list = []
for i in range(T):
    b_list.append(input())

for test_case in b_list:
    is_valid = True
    b_stack = Casually_Stack()
    for b in test_case:
        if b == "(":
            b_stack.push(b)
        elif b == ")":
            if b_stack.is_empty():
                is_valid = False
                break
            if b_stack.pop() == "(":
                continue
            elif b == ")":
                is_valid = False
                break
            else: print("error")
        else: print("error") 
    
    
    if not b_stack.is_empty():
        is_valid = False
    print("YES" if is_valid else "NO")    

