# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
s=str(input())
k=str(input())
m=re.compile(f'(?=({k}))')
n=list(m.finditer(s))
if not n:
    print((-1,-1))
else:
    for i in n:    
        print((i.start(),i.start()+len(k)-1))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna