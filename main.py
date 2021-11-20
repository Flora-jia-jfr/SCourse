from SCourse1 import main1

lec_arr = []
dic_arr = []
quiz_arr = []
def check_conflict(section_list):
    for i in range(len(section_list)):
        for j in range(i+1, len(section_list)):
            p_i = section_list[i].get_period()
            p_j = section_list[j].get_period()
            if p_i.if_collision(p_j):
                return (i, j)
    # section_list.sort(key=lambda x: x.period.start_time)
    # for i in range(len(section_list) - 1):
    #     if section_list[i].get_period().if_collision(section_list[i + 1].get_period()):
    #         return (i, i+1)
    return []

def arrange_lecture(lecture_list):
    global lec_arr
    temp_arr = []
    for i in lecture_list:
        if len(i) == 0:
            return
        temp_arr.append(i[0])

    conflicted_classes = check_conflict(temp_arr)
    if len(conflicted_classes) == 0:
        lec_arr.append(temp_arr)
        # for i in range(len(lecture_list)):
        #     removed = lecture_list[i].pop(0)
        #     arrange_lecture(lecture_list)
        #     lecture_list[i].insert(0, removed)
    else:
        # this can definitely be optimized
        for i in conflicted_classes:
            removed = lecture_list[i].pop(0)
            arrange_lecture(lecture_list)
            lecture_list[i].insert(0, removed)

def arrange_discussion(discussion_list):
    global dic_arr
    global lec_arr
    temp_arr = []
    for i in discussion_list:
        if len(i) == 0:
            return
        temp_arr.append(i[0])

    for lec in range(len(lec_arr)):
        conflicted_classes = check_conflict(temp_arr + lec_arr[lec])
        if len(conflicted_classes) == 0:
            dic_arr.append(temp_arr)
        else:
            # this can definitely be optimized
            for i in conflicted_classes:
                if i < len(discussion_list):
                    removed = discussion_list[i].pop(0)
                    arrange_discussion(discussion_list)
                    discussion_list[i].insert(0, removed)

def arrange_quiz(quiz_list):
    global quiz_arr
    quiz_arr = []

def main(classes):
    class_list = []
    for i in classes:
        class_list.append(main1(i))

    lecture_list = []
    discussion_list = []
    lab_list = []
    quiz_list = []
    for c in class_list:
        lecture_list.append(c.get_lecture_list())
        if len(c.get_discussion_list()) != 0:
            discussion_list.append(c.get_discussion_list())
        if len(c.get_lab_list()) != 0:
            lab_list.append(c.get_lab_list())
        if len(c.get_quiz_list()) != 0:
            quiz_list.append(c.get_quiz_list())

    arrange_lecture(lecture_list)
    global lec_arr
    for i in lec_arr:
        print("\nAll lecture arrangement as follow: ")
        for j in i:
            print('\t'+str(j))

    arrange_discussion(discussion_list)
    global dic_arr
    print("\nAll discussion and lab arrangement as follow: ")
    if len(dic_arr) != 0:
        for i in dic_arr[0]:
            print('\t'+str(i))
    else:
        print("no lab or discussion")

    arrange_quiz(quiz_list)
    global quiz_arr
    print("\nAll quiz arrangement as follow: ")
    if len(quiz_arr) != 0:
        for i in quiz_arr[0]:
            print('\t'+str(i))
    else:
        print("no quiz")

    return_dic = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    for lec in lec_arr[0] + dic_arr[0]:
        print(lec)
        for day in lec.get_period().get_days_list():
            if day == 1:
                return_dic['Monday'].append(lec.get_dic_format())
            elif day == 2:
                return_dic['Tuesday'].append(lec.get_dic_format())
            elif day == 3:
                return_dic['Wednesday'].append(lec.get_dic_format())
            elif day == 4:
                return_dic['Thursday'].append(lec.get_dic_format())
            elif day == 5:
                return_dic['Friday'].append(lec.get_dic_format())
    print(return_dic)
    return return_dic
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()