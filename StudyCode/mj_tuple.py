def is_it_true(anything):
  if anything:
    print("yes, it's true")
  else:
    print("no, it's false")

is_it_true(())
is_it_true(('a', 'b'))
is_it_true((False,))
# type((False))
# type((False,))

# 2.5.2

