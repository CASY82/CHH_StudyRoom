hour, minute, seconds = map(int, input().split())
new_time = int(input())

hour = hour * 3600
minute = minute * 60

result = hour + minute + seconds + new_time

new_hour = (result // 3600) % 24
new_minute = (result % 3600) // 60
new_seconds = (result % 3600) % 60

print(new_hour, new_minute, new_seconds, end=' ')