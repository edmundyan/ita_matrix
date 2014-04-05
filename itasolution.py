class ITASolution(object):
  def __init__(self, solution = None):
    self.solution = solution

  def minPrice(self):
    return self.solution['minPrice']

  def __getitem__(self, index):
    return self.solution['solutions'][index]
