#
'''
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

file = open("newfile.txt", "w")
file.write(""" i am sowrav """)
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
'''
'''
txt = input()
c = txt.split(' ')
d = 0
e = None
for i in c:
    if len(i) >= d:
        d = len(i)
        e = i
print(e)
'''
'''

print((lambda x: x**2 + 5*x + 4) (-4))
'''
'''
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x + 5, nums))
print(result)
'''
'''
def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)
'''
'''
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
'''
'''
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(numbers(20)))
'''
'''
def countdown(i):
    while i > 0:
        yield i
        i -= 1

for i in countdown(6):
    print(i)
'''
'''
def make_word():
    word = ""
    for ch in "spam":
        word +=ch
        yield word

print(list(make_word()))
'''
'''
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap
@decor
def print_text():
    print("Hello world!")
print_text()
'''









