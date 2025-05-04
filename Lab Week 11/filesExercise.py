def filesExercise():
    with open("scores.txt", "r") as scores:
        with open("students.txt", "r") as students:
            total = 0
            count = 0
            students_name = []
            students_id1 = []
            students_id2 = []
            assignment = []
            score = []
            score_content_list = []
            students_content_list = []
            students_content = students.read().split("\n")
            for i in range(1, len(students_content)):
                students_content_list.append(students_content[i].split(","))
            for x in range(0, len(students_content_list)):
                for y in range(0, len(students_content_list[0])):
                    if (y==0):
                        students_id1.append(students_content_list[x][y])
                    else:
                        students_name.append(students_content_list[x][y])
            score_content = scores.read().split("\n")
            for j in range(1, len(score_content)):
                score_content_list.append(score_content[j].split(","))
            for a in range(0, len(score_content_list)):
                for b in range(0, len(score_content_list[0])):
                    if(b == 0):
                        students_id2.append(score_content_list[a][b])
                    elif(b == 1):
                        assignment.append(score_content_list[a][b])
                    else:
                        score.append(score_content_list[a][b])
            grades_dict = {}
            grades_dict["Student ID"] = "Name", "Total Scores", "Sum of All Scores", "Score Average"
            for i in range(0, len(students_id1)):
                for j in range(0, len(students_id2)):
                    if(students_id1[i] == students_id2[j]):
                        count += 1
                        total += int(score[j])
                keys = grades_dict.keys()
                if keys not in students_name:
                    grades_dict[students_id1[i]] = students_name[i], count, total, (total/count)
                else:
                    grades_dict[students_id1[i]] = count, total, (total/count)
                total = 0
                count = 0
            return grades_dict
                        
def file_output(grades_dict):
    with open("grades.txt", "w") as file:
        keys = grades_dict.keys()
        for keys in grades_dict:
            file.write(keys)
            value = str(grades_dict[keys])
            file.write(value.replace("'", "").replace('(', ', ').replace(')', '')+"\n")

def main():
    grades_dict = filesExercise()
    file_output(grades_dict)

if __name__ == "__main__":
    main()