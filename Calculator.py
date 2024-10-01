def basic_calculator():
  """A basic calculator that performs addition, subtraction, multiplication, and division."""

  while True:
    try:
      num1 = float(input("Enter the first number: "))
      operator = input("Enter the operator (+, -, *, /): ")
      num2 = float(input("Enter the second number: "))

      if operator == "+":
        result = num1 + num2
      elif operator == "-":
        result = num1 - num2
      elif operator == "*":
        result = num1 * num2
      elif operator == "/":
        result = num1 / num2
      else:
        print("Invalid operator. Please choose +, -, *, or /.")
        continue

      print("Result:", result)

      choice = input("Do you want to perform another calculation? (yes/no): ")
      if choice.lower() != "yes":
        break

    except ValueError:
      print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
  basic_calculator()
