#Very basic parser to see how they work
import parser
addy= "7+5"

print('Lets do some simple maths')
print(addy)

st=parser.expr(addy)
code=st.compile()
tot=eval(code)

print('\n')
print('And the answer is...')
print(tot)
