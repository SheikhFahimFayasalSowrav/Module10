#
'''def count_char(text, char):
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

txt = input()
c = txt.split(' ')
d = 0
e = None
for i in c:
    if len(i) >= d:
        d = len(i)
        e = i
print(e)

print((lambda x: x**2 + 5*x + 4) (-4))


nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x + 5, nums))
print(result)

def is_even(x):
    if x%2==0:
        return x

def get_even():
    num = 44
    while True:
        if is_even(num):
            yield num
        print(num)

print(get_even())

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(numbers(11)))

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap
@decor
def print_text():
    print("Hello world!")

print_text()'''








