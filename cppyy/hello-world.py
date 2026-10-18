# Code based on https://www.youtube.com/watch?v=ao105xyl1dk

import cppyy

# Define a simple cpp function for printing hello world
# We use double slashes before newline as we are in a string
cppyy.cppdef(
  """
  #include <iostream>

  void helloWorld()
  {
    std::cout << "Hello World from C++ code!\\n";
  }
  """
)

# Access the cpp function
from cppyy.gbl import helloWorld

helloWorld()

print("From Python!!!")
