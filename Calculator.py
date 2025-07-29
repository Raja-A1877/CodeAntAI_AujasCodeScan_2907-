def process_data(data):
    return data + 1  # ❌ TypeError if data is a string
 
print(process_data("123"))
 
eval("print('This is dangerous')")  # ❌ Security risk
 
def d(a, b): return a*b  # ❌ Bad function name, no docstring