#定義Pen的類別
class Pen:
    #初始化物件的屬性
    def __init__(self, id, money, color):
        self._id = id
        self._money = money
        self._color = color

# 創建pen的物件
s1 = Pen('f0001', '25', 'black')
print("筆s1編號=", s1._id)
print("筆s1價錢=", s1._money)
print("筆s1顏色=", s1._color)

s2 = Pen('f0002', '25', 'blue')
print("筆s2編號=", s2._id)
print("筆s2價錢=", s2._money)
print("筆s2顏色=", s2._color)

s3 = Pen('f0003', '25', 'red')
print("筆s3編號=", s3._id)
print("筆s3價錢=", s3._money)
print("筆s3顏色=", s3._color)

class Pen(object):
    #副函式定義，名稱為method1，參數有a,b,c
    def method1(self, id, money, color):
        # 副函式程式內容，計算3個數字相乘的積
        return id*money*color
           
 
#呼叫副函式，先建立類別物件
obj1 = Pen()
#再利用建立好的類別物件obj1呼叫副函式method1
id=1
money=2
color=3
result = obj1.method1(id, money, color) #呼叫副函式method1，將結果存入變數result中
print(result) #列印結果
 
