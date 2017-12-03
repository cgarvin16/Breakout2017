variable = open("highScores.txt", "a")
name = input("Add 3 initials: ")
score = 0
variable.write("{0}. . . . .{1}\n".format(name, score))
variable.close()