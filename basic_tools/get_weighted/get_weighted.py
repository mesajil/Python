




def get_weight_and_grades (line):
    list = [int(str) for str in line.replace(","," ").split()]
    return (list[0], list[1:])


def get_grades ():
    name = "D:\Github\python-2\\basic_tools\get_weighted\grades.txt"   
    f = open (name, "r")
    list = [get_weight_and_grades(line) for line in f]
    f.close()
    return list


def cal_average (grades):
    return sum(grades)/len(grades)

def calc_weighted (list_of_tuples):
    weights = [weight for weight,_ in list_of_tuples]
    return sum([weight*cal_average(grades) for weight,grades in list_of_tuples])/sum(weights)








if __name__ == '__main__':
    list_of_tuples = get_grades()
    average = calc_weighted(list_of_tuples)
    print ("Average: ", average)
