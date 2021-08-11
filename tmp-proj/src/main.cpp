
/*
 * File: main.cpp
 * Author: So Chigusa
 * Date: MM/DD/YY
 * Description: some description here
 */

#include <iomanip>
#include <iostream>

/**
 * main program
 * @return status code
 */
int main()
{
  std::cout << std::setprecision(6) << std::scientific;

  try
  {
  }
  catch (std::string &error)
  {
    std::cerr << "Error: " << error << std::endl;
  }
  catch (const char *error)
  {
    std::cerr << "Error: " << error << std::endl;
  }
  return 0;
}
