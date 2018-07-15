import sys
from EulerAnswer import EulerQuestion

print('Select Question (Enter Question number betweeb 1 to 3)')

question=int(input().strip())

ans = EulerQuestion(question)

print('The answer for your question is:')
print(ans)
