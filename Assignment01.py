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


submit_credit, archive_credit = 0.0, 0.0
submit_gpa, archive_gpa = 0.0, 0.0

while True:
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 계산")

    user_value = input()
    value = int(user_value)

    match value:
        case 1:
            print("학점을 입력하세요.")
            user_value = input()
            credit = int(user_value)

            print("평점을 입력하세요.")
            user_value = input()
            gpa = convert_score(user_value)

            if gpa > 0:
                submit_credit += credit
                submit_gpa += gpa * credit
            archive_credit += credit
            archive_gpa += gpa * credit

        case 2:
            submit_gpa /= submit_credit
            archive_gpa /= archive_credit

            print("제출용: " + str(submit_credit) + " (GPA: " + str(submit_gpa) + ")")
            print("열람용: " + str(archive_credit) + " (GPA: " + str(archive_gpa) + ")")

            break