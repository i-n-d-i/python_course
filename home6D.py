import sys
import random

L = int(input())
#file = open("anna.txt", 'r')
#text = file.read().replace("\n    ", " @ ").split()
text = sys.stdin.read().replace("\n    ", " @ ").split()
num = len(text)
random_num = random.randint(0, num)
answer = (" ".join(text[random_num:random_num+L])).replace(" @ ", "\n    ")
print(answer)
