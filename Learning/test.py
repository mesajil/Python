
import module


with open(r"input.txt", "r") as f:
    matriz = [line.split("\n")[0].split(",") for line in f]

print ([[int(e) for e in row] for row in matriz])
