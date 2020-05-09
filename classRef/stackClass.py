class Stack:
    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def isEmpty(self):
        return len(self.__data) == 0

    def push(self, e):
        self.__data.append(e)

    def top(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            return self.__data[self.__len__() - 1]

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            value = self.__data[self.__len__() - 1]
            del self.__data[self.__len__() - 1]
            return value
