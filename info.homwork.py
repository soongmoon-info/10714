#최종 리스트 내용 [이름, 학번, 등급, 수학점수, 국어점수, 정보점수, 총합, 평균]
student = [['강호명','10100',36.6,67.1,55.4],   # [이름, 학번, 수학점수, 국어점수, 정보점수]
          ['양정민','10300',100,0,0],             # [이름, 학번, (국어, 정보점수 입력 안됨)]      - 점수 입력 필요
          ['이규래','10400',96.1,75.2,87.3],    # [이름, 학번, 수학점수, 국어점수, 정보점수]
          ['김묵병','10500',0,0,0],             # [이름, 학번, (수학, 국어, 정보 점수 입력 안됨)] - 점수 입력 필요
          ['박주근','10600',0,96.7,0],             # [이름, 학번, (수학, 정보점수 입력 안됨)]     - 점수 입력 필요
          ['이준동','10700',87.4,45.6,97.9]]    # [이름, 학번, 수학점수, 국어점수, 정보점수]






def inputinput(x,y,z):
    for i in range(x,len(student)):
        for q in range(y,len(student[i])):
            student[i][q]=z
            break
        break

while True:
    x=int(input('점수를 추가할 학생 인덱스: '))
    y=int(input('점수를 추가할 위치: '))
    z=float(input('추가할 점수: '))
    if  x != -1 or y != -1 or z != -1: #-1을 입력하면 멈춤
        inputinput(x,y,z)
    else:
        break
    






for item in student: #다차원에서 두번째로 큰차원 item
    sum = 0
    count = 0
    avg = 0
    for score in item[2:5]:
        sum = sum + score
        count = count + 1
    avg = sum/count
    item.append(sum)
    item.append(avg)
    if avg >= 90:
        item.insert(2,"'A'")
    elif avg >= 80:
        item.insert(2,"'B'")
    elif avg >= 70:
        item.insert(2,"'C'")
    else:
        item.insert(2,"'F'")
print(student)


   