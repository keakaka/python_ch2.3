
def f():
    l_a = 2
    l_b = '마이콜'
    print(locals())

class MyClass:
    x = 10
    y = 20

g_a = 1
g_b = '둘리'
# f()
print(globals())

# 1. 정의된 함수
f.k = 'hello'
print(f.__dict__)

# 2. 클래스 객체
MyClass.z = 10
# print(MyClass.__dict__)

# 내장함수 -> 심볼 테이블 X 확장 X
# print.z = 10
# print(print.__dict__)

# 내장 클래스 -> 심볼 테이블은 O 확장 X
# str.z = 10
# print(str.__dict__)

# 내장 클래스로 생성된 객체 -> 심볼 테이블 X 확장 X
# print(g_a.__dict__)

# 사용자 정의 클래스로 생성된 객체 -> 심볼 테이블 O 확장 O
o = MyClass()
o.z = 55
print(o.__dict__)

