#함수
b=10
def allsum(): #함수를 정의만 한거여서 실행 x
  a=10
  print(a)

print(a+b)
allsum()

def numInput():
  a=int(input('숫자입력:'))
  return a

#함수내부 지역변수 , 전체는 전역변수

num = numInput()
print(num)
allsum

y=x