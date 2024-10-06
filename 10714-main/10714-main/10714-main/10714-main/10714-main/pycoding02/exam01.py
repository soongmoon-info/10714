score = float(input('수학점수를 입력하세요:'))
score = float(input('국어점수를 입력하세요:')) + score
score = float(input('정보점수를 입력하세요:')) + score

standard  = int(score/3)

if standard >= int('90'):
  print('A')
elif standard >= int('80'):
  print('B')
else:
  print('C')