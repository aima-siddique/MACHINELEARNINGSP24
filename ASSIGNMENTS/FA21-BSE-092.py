#12/3/24
#CSC354 – Assignment1 – ML – Concept Learning 
# Aimah Siddique 
# fa21-bse-092
# The code tries to learn patterns from examples by guessing and refining its guesses based on whether it's right or wrong. It starts with a guess about what a certain thing might look like, then adjusts that guess as it sees more examples. At the end, it gives its best guess about what the thing is like.








def learn(concepts, target):
    specific_h = concepts[0].copy()
    print("\nInitialization of specific_h and general_h")
    print(specific_h)

    general_h = [['?' for _ in range(len(specific_h))] for _ in range(len(specific_h))]
    print(general_h)

    for i, h in enumerate(concepts):

        if target[i] == "yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        if target[i] == "no":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?' if general_h[x][x] != specific_h[x] else specific_h[x]

        print("\nSteps of Candidate Elimination Algorithm", i + 1)
        print(specific_h)
        print(general_h)
    return specific_h, general_h

data = [
    ['small', 'red', 'circle'],
    ['big', 'red', 'circle'],
    ['small', 'red', 'triangle'],
    ['big', 'blue', 'circle'],
    ['small', 'blue', 'circle'],
]

output = ["yes", "no", "no", "no", "yes"]

sFinal, gFinal = learn(data, output)
print("\nFinal Specific_h:")
print(sFinal)
print("\nFinal General_h:")
print(gFinal)
