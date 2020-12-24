#2
sec = int(input('Enter time by seconds: '))
hh = sec // 3600
mm = sec // 60 % 60
ss = sec % 60
print(f"Time: {hh}:{mm}:{ss}")