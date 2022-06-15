from sympy import Function, dsolve, Eq, exp, symbols, pretty

# f'(x) = f(x) + e^x
x = symbols('x')
f = Function('f')
dfdx = f(x).diff(x)
eq = Eq(dfdx, f(x) + exp(x))
initial_value_condition = {f(0): 1}
ans = dsolve(eq, f(x), ics=initial_value_condition)
print(pretty(ans))
# => f(x) = (1 + x) * e^x
