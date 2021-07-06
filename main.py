
Student1 = Student("Name")
Student1.add_test_scores([90, 20, 56, 78])
Student1.add_quiz_scores([10, 5, 25])
Student1.add_hw_scores([100])

Student1.add_test_scores([100, 95, 97])





print(str(Student1.name) + "'s average test score is a " + str(Student1.get_avg_test()))

