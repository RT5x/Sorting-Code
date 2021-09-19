class Student:
  def __init__(self, name):
    self.name = name
    self.test_scores_lst = []
    self.quiz_scores_lst = []
    self.hw_scores_lst = []

#define student scores
  def add_test_scores(self, lst):
    for score in lst:
      self.test_scores_lst.append(score)

  def add_quiz_scores(self, lst):
    for score in lst:
      self.quiz_scores_lst.append(score)

  def add_hw_scores(self, lst):
    for score in lst:
      self.hw_scores_lst.append(score)

  def average(self, num_lst):
    number_of_scores = 0
    total_sum = 0
    for number in num_lst:
      total_sum += number
      number_of_scores += 1

    return total_sum / number_of_scores

  def get_avg_test(self):
    return self.average(self.test_scores_lst)

  def get_avg_quiz(self):
    return self.average(self.quiz_scores_lst)

  def get_avg_hw(self):
    return self.average(self.hw_scores_lst)












