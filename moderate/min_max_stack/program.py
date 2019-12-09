class MinMaxStack:
    def __init__(self):
        self.mins = []
        self.maxs = []
        self.stack = []
        
    def peek(self):
        # Write your code here.
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        self.mins.pop()
        self.maxs.pop()
        return self.stack.pop()

    def push(self, number):
        # Write your code here.
            
        if not self.maxs or self.maxs[-1] < number:
            self.maxs.append(number)
        else:
            self.maxs.append(self.maxs[-1])
        if not self.mins or self.mins[-1] > number:
            self.mins.append(number)
        else:
            self.mins.append(self.mins[-1])
        self.stack.append(number)

    def getMin(self):
        # Write your code here.
        return self.mins[-1]

    def getMax(self):
        # Write your code here.
        return self.maxs[-1]

