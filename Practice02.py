import random

course_code = dict()
course_list = []

submit_credit, archive_credit = 0.0, 0.0
submit_gpa, archive_gpa = 0.0, 0.0

def convert_score(grade):
    match grade:
        case "A+":
            score = 4.5
        case "A":
            score = 4.0
        case "B+":
            score = 3.5
        case "B":
            score = 3.0
        case "C+":
            score = 2.5
        case "C":
            score = 2.0
        case "D+":
            score = 1.5
        case "D":
            score = 1.0
        case "F":
            score = 0.0
    return score

def code_to_name(num):
    course_name = course_code[int(num)]
    return course_name


while True:
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 출력")
    print("3. 계산")

    user_value = int(input())

    match user_value:
        case 1:
            print("과목명을 입력하세요: ")
            user_course_name = input()
            code = random.randint(10000, 99999)
            course_code[code] = user_course_name

            print("학점을 입력하세요: ")
            user_credit = int(input())

            print("평점을 입력하세요: ")
            user_gpa = input()
            course_list.append((code, user_credit, user_gpa))

            print("입력되었습니다.")

        case 2:
            i = 0
            for i in range(len(course_list)):
                code_num = course_list[i][0]
                saved_name = code_to_name(code_num)

                print("[" + str(saved_name) + "] " + str(course_list[i][1]) + "학점: " + str(course_list[i][2]))

        case 3:
            t = 0
            for t in range(len(course_list)):

                gpa_num = convert_score(str(course_list[t][2]))
                credit = int(course_list[t][1])

                if gpa_num > 0:
                    submit_credit += credit
                    submit_gpa += gpa_num * credit

                archive_credit += credit
                archive_gpa += gpa_num * credit

            submit_gpa /= submit_credit
            archive_gpa /= archive_credit

            print("제출용: " + str(submit_credit) + " (GPA: " + str(submit_gpa) + ")")
            print("열람용: " + str(archive_credit) + " (GPA: " + str(archive_gpa) + ")")

            print("프로그램을 종료합니다.")
            break