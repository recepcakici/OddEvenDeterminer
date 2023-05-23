import os
import importlib.util
import random
import time
number = int(input("Enter a number to determine if it is odd or even: "))
isOdd = True

fakeModule = str(random.randint(1000000000000, 9999999999999))

# Create the module file in the current directory
module_path = os.path.join(os.getcwd(), f"{fakeModule}.py")
fake_module = open(module_path, "w+", encoding="utf-8")
fake_module.write("def isNumberOdd(number):\n")
for x in range(int(number+1)):
    fake_module.write(f"    if number == {x}: return {isOdd}\n")
    isOdd = False if isOdd == True else True
fake_module.close()

# Import the module dynamically
spec = importlib.util.spec_from_file_location(f"{fakeModule}", module_path)
fake_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fake_module)

# Call the function from the imported module
odd_or_even = 'even' if fake_module.isNumberOdd(number) else 'odd'
print(f"The entered number is {odd_or_even}.")

time.sleep(10)
# Remove the module file
os.remove(module_path)
