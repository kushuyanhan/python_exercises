def is_a_party(apples, pizzas):
    if apples > 10 and pizzas > 10:
        return True
    else:
        return False

def throw_party():
    num_apples = input("How many apples do you have:")
    num_pizzas = input("How many pizzas do you have")

    if is_a_party(num_apples, num_pizzas):
        return "let 's party down"
    else:
        return "you should go to store first"

##test
print is_a_party(20,20)
print is_a_party(5,15)
print is_a_party(5,2)
print is_a_party(4,8)

print throw_party()