# 레퍼런스 복사
import copy

a = 1
b = a

a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = x

print(x)
print(y)
print(x is y)

# ShallowCopy(얕은 복사) - 복합 객체를 생성하고 원래 객체로부터 내용을 복사한다.
#                          새 객체를 생성 후 복사
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]

y = copy.copy(x)
print(x)
print(y)
print(x is y)
print(x[0] is y[0])  # x와 y가 같은 객체는 아니지만 얕은 복사를 통해 첫 단계의 값(객체)들은 같다.

# DeepCopy(깊은 복사)
y = copy.deepcopy(x)
print(x)
print(y)
print(x is y)
print(x[0] is y[0])  # deepcopy를 통해 모든 요소가 새로운 복합 객체에 담겼기 때문에 False

# 깊은 복사가 복합 객체만을 생성하기 때문에
# 복합 객체가 한개만 있을 경우 얕은 복사와 깊은 복사의 차이가 없다.
a = ['hello', 'world']
b = copy.copy(a)
print(a is b)   # F
print(a[0] is b[0])  # T   Correct !@!@!@

b = copy.deepcopy(a)
print(a is b)   # F
print(a[0] is b[0])  # T   /   IF 내부 요소가 복합 객체일 경우 F
# ( 트리를 생각하면 이해하기 쉽다. )
