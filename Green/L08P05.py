numberOfMagnets = int(input())
numberOfGroups = 1
previousMagnet = int(input())
for counter in range(1, numberOfMagnets):
    currentMagnet = int(input())
    if currentMagnet != previousMagnet:
        numberOfGroups += 1
    previousMagnet = currentMagnet

print(numberOfGroups)
