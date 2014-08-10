class Challenge(object):
  def __init__(self, text, fname, inputs, outputs):
    self.text = text
    self.fname = fname
    self.inputs = inputs
    self.outputs = outputs

  def get_errors(self, solution):
    try:
      exec(solution)
    except:
      return "Does not compile."

    try:
      eval(self.fname)
    except:
      return "Function name incorrect."

    return False

  def check(self, solution):
    exec(solution)
    f = eval(self.fname)
    for i, o in zip(self.inputs, self.outputs):
      try:
        ans = f(i)
      except Exception, e:
        print e
        return False

      if ans != o:
        print "%s != %s (input=%s)" % (ans, o, i)
        return False
    return True

challenges = []
challenges.append(Challenge("Write a function sum_squares, that, given a list of integers, returns the sum of their squares", "sum_squares", [[1, 2, 3, 4], [0, 1, 10]], [30, 101]))
challenges.append(Challenge("Write a function called palindrome, which given a string, returns True iff that string is a palindrome", "palindrome", ["", "test", "chocolate dolphin", "racecar", "tttttt", "asdsa", "let tel", "adjnvknkqj"], [True, False, False, True, True, True, True, False]))
challenges.append(Challenge("Write a function called prime, which given an integer, return True if the integer is prime and False otherwise", "prime", \
[1, 2, 3, 4, 5, 6, 7, 8, 9, 97, 7*1341, 1019, 2347, 1399, 2341, 99, 11, 17, 12],\
[False, True, True, False, True, False, True, False, False, True, False, True, True, True, True, False, True, True, False]))

