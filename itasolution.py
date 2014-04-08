class ITASolution(object):
  def __init__(self, solution = None):
    self.solution = solution

  def minPrice(self):
    # remove 'USD' prefix
    return float(self.solution['minPrice'][3:])

  def __getitem__(self, index):
    return self.solution['solutions'][index]
