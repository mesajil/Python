




def get_weight_and_grades (str_line):
    list = [int(str) for str in str_line.replace(","," ").split()]
    return (list[0], list[1:])


def get_grades ():
    name = "D:\Github\python-2\\basic_tools\grades.txt"
    f = open (name, "r")
    list = [get_weight_and_grades(str_line) for str_line in f]
    f.close()
    return list


def cal_average (grades):
    return sum(grades)/len(grades)

def calc_weighted (list_of_tuple_weight_grades):
    weights = [weight for weight,_ in list_of_tuple_weight_grades]
    return sum([weight*cal_average(grades) for weight,grades in list_of_tuple_weight_grades])/sum(weights)








if __name__ == '__main__':
    list_of_tuple_weight_grades = get_grades()
    average = calc_weighted(list_of_tuple_weight_grades)
    print ("Average: ", average)
