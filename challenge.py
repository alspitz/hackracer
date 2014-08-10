class Challenge(object):
  def __init__(self):
    self.text = ""
    self.fname = ""
    self.inputs = ""
    self.outputs = ""
    self.header = ""

  def get_errors(self, solution):
    try:
      exec(solution)
    except Exception, e:
      return "Does not compile: %s" % e

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
        return False, str(e)

      if ans != o:
        return False, "Input: %s; Expected: %s, received: %s" % (i, o, ans)
    return True,

# Challenge definitions
sum_squares = Challenge()
sum_squares.text = "Write a function sum_squares, that, given a list of integers, returns the sum of their squares."
sum_squares.fname = "sum_squares"
sum_squares.inputs = [[1, 2, 3, 4], [0, 1, 10]]
sum_squares.outputs = [30, 101]
sum_squares.header = "def sum_squares(x):\n"

palindrome = Challenge()
palindrome.text = "Write a function which, given a string, returns True iff that string is a palindrome."
palindrome.fname = "palindrome"
palindrome.inputs = ["", "test", "chocolate dolphin", "racecar", "tttttt", "asdsa", "let tel", "adjnvknkqj"]
palindrome.outputs = [True, False, False, True, True, True, True, False]
palindrome.header = "def palindrome(s):\n"

prime = Challenge()
prime.text = "Write a function called prime, which given an integer, return True if the integer is prime and False otherwise."
prime.fname = "prime"
prime.inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 97, 7*1341, 1019, 2347, 1399, 2341, 99, 11, 17, 12]
prime.outputs = [False, True, True, False, True, False, True, False, False, True, False, True, True, True, True, False, True, True, False]
prime.header = "def prime(x):\n"

challenges = []
challenges.append(sum_squares)
challenges.append(palindrome)
challenges.append(prime)
