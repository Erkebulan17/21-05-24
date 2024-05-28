find__max=[1,2,3,4,5,6,7,8,9,10]
max_number=max(find__max)
print("максималды сан",max_number)  

class Number_max:
    def __init__(self, Maximum):
        self.Maximum = Maximum
        self.max_Maximum = max(Maximum)
        print("максималды сан:", self.max_Maximum)

Maximum = (1,2,3,4,5,6,7,8,9,10)
number = Number_max(Maximum)

def find_max(list1):
    return max(list1)
find_ma = find_max([1,2,3,4,5,6,7,8,9,10])
print("максималды сан:",find_ma)

