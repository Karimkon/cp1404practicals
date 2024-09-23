def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def main():
    with open("temps_input.txt", "r") as infile, open("temps_output.txt", "w") as outfile:
        for line in infile:
            fahrenheit = float(line.strip())
            celsius = fahrenheit_to_celsius(fahrenheit)
            outfile.write(f"{celsius}\n")

main()
