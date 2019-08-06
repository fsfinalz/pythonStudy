# 학생의 수를 1개의 변수에 담고 임의의 학생 5명의 이름을 5개의 변수에 담는다. 그리고 각 학생의 성적 또한 5개의 변수에 
# 담아서 이를 출력하는 프로그램을 작성하세요. (단, print는 총 6번만을 이용하여 다음의 결과를 만들며 학생의 성적은 소수점 첫째 자리까지만 표현합니다.)

student = 5

student_name1 = "MoonSungHoon"
student_name2 = "YoonJaeIl"
student_name3 = "JeongSujin"
student_name4 = "JeongByeongIn"
student_name5 = "ParkSooHyuk"

moonSungHoon_score = 74.7
yoonJaeIl_score = 89.3
jeongSujin_score = 98.9
jeongByeongIn_score = 92.4
parkSooHyuk_score = 87.1

print("******* %d students *******" %student)
# print(student_name1, "'s score is ", moonSungHoon_score)
print("%s 's score is %.1f" %(student_name1, moonSungHoon_score))
# print(student_name2, "'s score is ", yoonJaeIl_score)
print("%s 's score is %.1f" %(student_name2, yoonJaeIl_score))
# print(student_name3, "'s score is ", jeongSujin_score)
print("%s 's score is %.1f" %(student_name3, jeongSujin_score))
# print(student_name4, "'s score is ", jeongByeongIn_score)
print("%s 's score is %.1f" %(student_name4, jeongByeongIn_score))
# print(student_name5, "'s score is ", parkSooHyuk_score)
print("%s 's score is %.1f" %(student_name5, parkSooHyuk_score))

