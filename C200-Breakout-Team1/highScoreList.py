variable = open("highScores.txt", "a")
name = input("Add 3 initials")
score = 0
variable.write("{0}_ _ _ _{1}".format(name, score))
variable.close()