def EulerQuestionPt1(question):
    # Solving Euler question #1
    # Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler001
    if question == 1:
        print('Project Euler #1: Multiples of 3 and 5')
        print('Enter a number, and this function will solve the following problem:')
        print('What is the sum of all the multiples of 3 or 5 below N (Your Input).')
        n = int(input().strip())
        n=n-1
        i3=n//3
        ans1 = ((3 + i3*3)*(i3))//2
        i5=n//5
        ans2 = ((5 + i5*5)*(i5))//2
        i15=n//15
        ans3 = ((15 + i15*15)*(i15))//2
        ans = (ans1+ans2-ans3)
        return ans
    elif question == 2 :
    # Solving Euler question #2
    # Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler002
        print('Project Euler #2 Even Fibonacci Numbers')
        print('Enter a number, and this function will solve the following problem:')
        print('By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.')
        print('Input N:')
        n = int(input().strip())
        i=1
        j=1
        k=0
        h=0
        while k<=n:
            if k%2 == 0:
                h=h+k
            k=i+j
            j=i
            i=k    
        return h
    elif question ==3:
        print('Project Euler #3: Largest prime factor')
        print('Enter a number, and this function will solve the following problem:')
        print('The prime factors of 13195 are 5,7,13 and 29.')
        print('What is the largest prime factor of the given number N?')
        print('Input N:')
        n = int(input().strip())
        ans =n
        w=0
        p = 0
        f=3
        while w<1 :
            w=ans%2
            if ans ==2:
                break
            if w ==0:
                ans = ans/2
        
        if ans>2 and p == 0:
            while f < ans:
                p=ans%f
                if p ==0:
                    ans = ans/f
                else:
                    f=f+2
        
        return int(ans)