# 코드 처리하기

def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for check in nums:
        numbers = numbers.replace(check, str(nums.index(check)))

    answer = int(numbers)

    return answer

print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))
print(solution("oneoneone"))