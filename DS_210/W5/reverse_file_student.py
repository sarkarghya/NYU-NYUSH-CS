from array_stack_student import ArrayStack

def reverse_file(input_filename, output_filename):
  """Overwrite given file with its contents line-by-line reversed.
     Use with open(.) construct to read and write files as provided.
     Think about how to use ArrayStack to help you.
     You cannot use other data structures like Python List to complete this question.
  """
  # TODO
  S = ArrayStack()
  with open(input_filename, 'r') as F:
    for line in F:
      line = line.rstrip('\n')
      # TODO
      S.push(line)


  # now we overwrite with contents in LIFO order
  with open(output_filename, 'w') as F:
    # TODO
    while not S.is_empty():
      F.write(S.pop()+'\n')

if __name__ == '__main__':
  reverse_file('DSSyllabus.txt', 'DSSyllabus_reverse.txt')
