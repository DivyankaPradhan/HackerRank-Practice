def count_substring(string, sub_string):
    c=0
    for i in range(0,len(string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            c+=1       
    return c



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna