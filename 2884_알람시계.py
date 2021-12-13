# h = int(input())
# m = int(input())
#
# early = 45
# one_hour = 60
# hours = 24
#
# def setAlarm(h, m):
#     if (0 <= h <= 23 and 0 <= m <= 59):
#         if m >= early:
#             print(h , (m - early))
#
#         elif (m <= early and h <= 0):
#             print((hours-1) , (one_hour + m - early))
#
#         elif m <= early:
#             print((h - 1), (one_hour + m - early))
#
# setAlarm(h,m)

H, M = map(int, input().split())

if M > 44:
    print(H,M-45)
elif M < 45 and H > 0:
    print(H-1,M+15)
else:
    print(23,M+15)