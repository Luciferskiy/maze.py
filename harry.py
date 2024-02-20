from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

knowlegde = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore)
    Not(And(hagrid, dumbledore)),
    dumbledore,
)

print(sentence.formula())
