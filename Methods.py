# def sonlar():
#     for son in range(1, 101):
#         yield son
# gen=sonlar()
# for son in sonlar():
#     if son>50:
#         gen.throw(ValueError)
#     print(next(gen))


# def my_generator():
#     value = yield 1
#     print(f"Akrom: {value}")
#     yield 2
#
# gen = my_generator()
# next_value = next(gen)
# gen.send("Ishda")

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
gen.close()
print(next(gen))

