from menu import Menu,MenuItem
from coffe_maker import  CoffeeMaker
from money_machine import MoneyMachine
money_machine=MoneyMachine()
coffe_maker=CoffeeMaker()
menu=Menu()


is_on=True



while is_on:
    options=menu.get_items()
    choise=input(f"What would you like? ({options})")
    if choise=="off":
        is_on=False
    elif choise=="report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choise)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee((drink))