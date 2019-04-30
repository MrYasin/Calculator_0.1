"""





"""

def grade_calc(note):

    note = note[:-1]

    splitted = note.split(",")

    name = splitted[0]
    first_grade = int(splitted[1])
    second_grade = int(splitted[2])
    third_grade = int(splitted[3])

    average = first_grade * (3/10) + second_grade * (3/10) + third_grade * (4/10)


    if average >= 90:
        by_letter = "AA"
    elif average >= 80:
        by_letter = "BA"
    elif average >= 70:
        by_letter = "BB"
    elif average >= 60:
        by_letter = "CB"
    elif average >= 50:
        by_letter = "CC"
    elif average >= 40:
        by_letter = "DC"
    elif average >= 30:
        by_letter = "DD"
    else:
        by_letter = "FF"

    return name + " ------> " + by_letter + "\n"





with open("Ep_10/grades_file.txt","r",encoding="utf-8") as file:

    to_be_added = []


    for i in file:

        to_be_added.append(grade_calc(i))

    with open("Ep_10/grades_final.txt", "w", encoding="utf-8") as file_2:

        for grades in to_be_added:
            file_2.write(grades)
