#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 인수로 년을 넘겨받아 윤년, 평년을 판단해 윤년이면 True, 평년이면 False를 리턴하는 isLeapYear() 함수를 만든다.
# 논리값을 기억하는 변수는 논리값을 리턴하는 함수는 이름을 'is'로 시작하는 것이 관행이다.
def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# In[20]:


# 인수로 년, 월을 넘겨받아 그 달의 마지막 날짜를 리턴하는 lastDay() 함수를 만든다.
def lastDay(year, month):
    # 각 달의 마지막 날짜를 기억하는 리스트를 만든다.
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 인수로 넘겨받은 년도에 따른 2월의 마지막 날짜를 확정한다.
    # if isLeapYear(year):
        # m[1] = 29
    m[1] = 29 if isLeapYear(year) else 28
    # 마지막 날짜를 리턴시킨다.
    return m[month - 1]


# In[35]:


# 인수로 년, 월, 일을 넘겨받아 1년 1월 1일 부터 지난 날짜의 합계를 리턴하는 totalDay() 함수를 만든다.
def totalDay(year, month, day):
    # 인수로 넘어온 년도가 다 지나가지 않았으므로 1년 1월 1일 부터 전년도 12월 31일까지 지난 날짜를 계산한다.
    total = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    # 전년도 12월 31일까지 지난 날짜의 합계에 전달까지 지난 날짜를 더한다.
    for i in range(1, month):
        total += lastDay(year, i)
    # 전달까지 지난 날짜의 합계에 일을 더해서 리턴시킨다.
    return total + day


# In[39]:


# 일요일 => 0, 월요일 => 1, 화요일 => 2, 수요일 => 3, 목요일 => 4, 금요일 => 5, 토요일 => 6
# 인수로 년, 월, 일을 넘겨받아 요일을 계산해서 숫자로 리턴하는 weekDay() 함수를 만든다.
def weekDay(year, month, day):
    return totalDay(year, month, day) % 7


# In[40]:


print(isLeapYear(2021))
print(lastDay(2021, 6))
print(totalDay(2021, 6, 24))
print(weekDay(2021, 6, 24))


# In[ ]:





# In[ ]:




