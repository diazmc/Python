def score():
    print "Scores and Grades"

    import random
    for x in range(10):
        random_num = random.randint(60,100)
        if random_num in range(60,70): print "Score:", random_num, "Your grade is D"
        if random_num in range(70,80): print "Score:", random_num, "Your grade is C"
        if random_num in range(80,90): print "Score", random_num, "Your grade is B"
        if random_num in range(90,101): print "Score", random_num, "Your grade is A"  
    print "End of the program. Bye!"
    
score ()

