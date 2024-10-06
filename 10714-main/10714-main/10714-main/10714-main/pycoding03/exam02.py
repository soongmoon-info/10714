student = [['강호명','10100',36.6,67.1,55.4,'none'],   # [이름, 학번, 수학점수, 국어점수, 정보점수, 빈공간(삭제 필요)]
          ['이규래','10400',96.1,'none',75.2,87.3]]    # [이름, 학번, 수학점수, 빈공간(삭제 필요), 국어점수, 정보점수]

del(student[0][5])
del(student[1][3])


donglist = ['이준동','10700',87.4,22.7,97.9]

student.append(donglist)



print(student[2])

student[0].insert(2,'C')
student[1].insert(2,'B')
student[2].insert(2,'F')

print(student)

수학합 = int(student[0][2]+student[1][2]+student[2][2])
국어합 = int(student[0][3]+student[1][3]+student[2][3])
정보합 = int(student[0][4]+student[1][4]+student[2][4])

수학평균 = int(수학합/3)
국어평균 = int(국어합/3)
정보평균 = int(정보합/3)
print(수학평균,국어평균,정보평균)