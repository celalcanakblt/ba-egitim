def outer_func(arg_outer):
    def inner_func(arg_inner):
        return arg_outer + arg_inner
    return inner_func

func1 = outer_func(5)
print(type(func1)) #<class 'function'>
print(func1(4))

func2 = outer_func(8)
print(type(func2))
func2(2)

print(outer_func(5)(5))