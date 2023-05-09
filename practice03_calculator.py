class CourseHistory:
    course_code_set = set()
    for k in range(1, 100000):
        course_code_set.add(k)

    def __init__(self):
        self.course_dict = dict()
        self.use_grade = []
        self.no_use_grade = []

    @classmethod
    def get_gpa_score(cls, gpa):
        match gpa:
            case 'A+':
                return 4.5
            case 'A':
                return 4
            case 'B+':
                return 3.5
            case 'B':
                return 3
            case 'C+':
                return 2.5
            case 'C':
                return 2
            case 'D+':
                return 1.5
            case 'D':
                return 1
            case 'F':
                return 0

    def give_course_code(self, user_course_name):
        if user_course_name not in self.course_dict:
            code = CourseHistory.course_code_set.pop()
            self.course_dict[user_course_name] = code
            self.course_dict[code] = user_course_name
            return code
        else:
            code = self.course_dict[user_course_name]
            return code

    def input_process(self):
        user_course_name = input("과목명을 입력하세요: ")
        code = self.give_course_code(user_course_name)

        credit = int(input("학점을 입력하세요: "))

        gpa = input("평점을 입력하세요: ")

        decision = 0
        for i in range(len(self.use_grade)):
            if code == self.use_grade[i][0]:
                if self.get_gpa_score(gpa) >= self.get_gpa_score(self.use_grade[i][2]):
                    decision = 1
                else:
                    decision = 2
            else:
                decision = 0

        if decision == 0:
            self.use_grade.append((code, credit, gpa))

        elif decision == 1:
            retake = self.use_grade.pop(i)
            self.no_use_grade.append(retake)
            self.use_grade.append((code, credit, gpa))

        elif decision == 2:
            self.no_use_grade.append((code, credit, gpa))

        print("입력되었습니다.")

    def print_process(self):
        i = 0
        for i in range(len(self.use_grade)):
            saved_code = self.use_grade[i][0]
            saved_name = self.course_dict[saved_code]

            print("[" + str(saved_name) + "] " + str(self.use_grade[i][1]) + "학점: " + str(self.use_grade[i][2]))

        i = 0
        for i in range(len(self.no_use_grade)):
            saved_retake_code = self.no_use_grade[i][0]
            saved_retake_name = self.course_dict[saved_retake_code]

            print("[" + str(saved_retake_name) + "] " + str(self.no_use_grade[i][1]) + "학점: " + str(self.no_use_grade[i][2]))


    def query_process(self):
        course_name = input('과목명을 입력하세요: ')
        query_code = self.course_dict[course_name]

        i = 0
        for i in range(len(self.use_grade)):
            if query_code == self.use_grade[i][0]:
                print("[" + course_name + "] " + str(self.use_grade[i][1]) + "학점: " + str(self.use_grade[i][2]))

        j = 0
        for j in range(len(self.no_use_grade)):
            if query_code == self.no_use_grade[j][0]:
                print("[" + course_name + "] " + str(self.no_use_grade[j][1]) + "학점: " + str(self.no_use_grade[j][2]))

    def calculation_process(self):
        submit_credit, archive_credit = 0.0, 0.0
        submit_gpa, archive_gpa = 0.0, 0.0

        i = 0
        for i in range(len(self.use_grade)):

            gpa_num = self.get_gpa_score(str(self.use_grade[i][2]))
            credit_num = int(self.use_grade[i][1])

            if gpa_num > 0:
                submit_credit += credit_num
                submit_gpa += gpa_num * credit_num

            archive_credit += credit_num
            archive_gpa += gpa_num * credit_num

        submit_gpa /= submit_credit
        archive_gpa /= archive_credit

        print("제출용: " + str(submit_credit) + " (GPA: " + str(submit_gpa) + ")")
        print("열람용: " + str(archive_credit) + " (GPA: " + str(archive_gpa) + ")")

course_history = CourseHistory()

while True:
    print('작업을 선택하세요')
    print('1. 입력')
    print('2. 출력')
    print('3. 조회')
    print('4. 계산')
    print('5. 종료')

    user_input = str(input())

    match user_input:
        case '1':
            course_history.input_process()

        case '2':
            course_history.print_process()

        case '3':
            course_history.query_process()

        case '4':
            course_history.calculation_process()

        case '5':
            break

print('프로그램을 종료합니다.')
