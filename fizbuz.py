import sys

# %%


def fizz_buzz(n):
    fizzer = 3
    buzzer = 5
    for i in range(1, n+1):
        if i % fizzer == 0 and i >= fizzer and i % buzzer == 0 and i >= buzzer:
            print('FizzBuzz')
        elif i % fizzer == 0 and i >= fizzer and i % buzzer != 0 and i >= buzzer or i == fizzer:
            print('Fizz')
        elif i % fizzer != 0 and i >= fizzer and i % buzzer == 0 and i >= buzzer or i == buzzer:
            print('Buzz')
        else:
            print(i)


# %%
fizz_buzz(15)

# %%
