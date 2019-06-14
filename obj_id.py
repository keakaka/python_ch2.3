import sys

i1 = 10
i2 = 10
print(hex(id(i1)), hex(id(i2)))

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

# is (동일 레퍼런스 비교
print(i1 is i2)  # immutable
print(l1 is l2)  # mutable
print(s1 is s2)  # immutable

# ?????
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(sys.getrefcount(t1), sys.getrefcount(t2))  # 왜 5 왜 5 왜 5 왜5 왜5
print(t1 is t2)

# 리터럴로 생성하면 같은 객체가 생성되나 명시하여 생성하면 다른 객체가 생성된다.
t3 = tuple(range(1, 4))
print(sys.getrefcount(t3))
print(t1 is t3)

# 슬라이싱으로 생성해도 다른 객체이다.
t4 = (0, 1, 2, 3)[1:]
print(t1 is t4)

