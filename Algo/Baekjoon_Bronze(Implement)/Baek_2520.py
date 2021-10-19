hour, minute = map(int, input().split())
plus_time = int(input())

new_time = (hour * 60) + minute + plus_time

new_hour = (new_time // 60) % 24
new_minute = new_time % 60

print(new_hour, new_minute)