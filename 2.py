class Luggage:
    def __init__(self, id, weight, departure , destination , holder):
        self._id = id
        self._weight = weight
        self._departure  = departure 
        self._destination = destination
        self._holder = holder


class Luggage(object):
    #副函式定義，名稱為method1，參數有a,b,c
    def method1(self, id, weight, departure , destination , holder):
        # 副函式程式內容，計算3個數字相乘的積
        return id*weight*departure*destination*holder
           
 
#呼叫副函式，先建立類別物件
obj1 = Luggage()
#再利用建立好的類別物件obj1呼叫副函式method1
id=1
weight=2
departure=3
destination=4
holder=5
result = obj1.method1(id, weight, departure , destination , holder) #呼叫副函式method1，將結果存入變數result中
print(result) #列印結果
 
class  Ticket:
    def __init__(self, name, id, time, Number, location, luggage, luggageID):
        self._name = name
        self._id = id
        self._time = time
        self._Number = Number
        self._location = location
        self._luggage = luggage
        self._luggageID = luggageID

class Ticket(object):
    #副函式定義，名稱為method1，參數有a,b,c
    def method1(self, name, id, time, Number, location, luggage, luggageID):
        # 副函式程式內容，計算3個數字相乘的積
        return name*id*time*Number*location*luggage*luggageID
           
 
#呼叫副函式，先建立類別物件
obj1 = Ticket()
#再利用建立好的類別物件obj1呼叫副函式method1
name=1
id=2
time=3
Number=4
location=5
luggage=6
luggageID=7
result = obj1.method1(name, id, time, Number, location, luggage, luggageID) #呼叫副函式method1，將結果存入變數result中
print(result) #列印結果
 
