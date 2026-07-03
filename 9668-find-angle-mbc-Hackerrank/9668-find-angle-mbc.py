# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = float(input())
BC = float(input())
t_rad = math.atan(AB/BC)
t = round(math.degrees(t_rad))
print(f"{t}\u00b0")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna