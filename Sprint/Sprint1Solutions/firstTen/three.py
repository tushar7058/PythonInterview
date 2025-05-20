'''

3. **Validating Leap Years**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Date Handling  
   **Description**: Write a program to check if a given year is a leap year.  
   **Example**:  
   Input: `year = 2020`  
   Output: `Leap Year`  
   Explanation: 2020 is divisible by 4 but not by 100, or it is divisible by 400, so it is a leap year.  


'''
year = 2000
def findleapYear(year):
    if year%4 ==0 and year%400 == 0:
        print("Year is leap year")
    else:
        print("year is not leap year")

findleapYear(2026)