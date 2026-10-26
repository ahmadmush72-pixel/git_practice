


def calculate_input():
  try:
    x = int(input("Please Enter a number: "))
    y = 1 / x
    print(y)
  except:
    print("An error occurred")
    raise

calculate_input()


try:
    age = int(input("Enter a number: "))

    if age < 0:
        raise ValueError("Age cannot be less than 0")

    print("Your age is:", age)

except ValueError as error:
    print("Error:", error)

print("practice of restore")

print("")