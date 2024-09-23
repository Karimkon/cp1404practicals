from musician import Musician
from guitar import Guitar
from band import Band

def main():
    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.add_instrument(Guitar("Washburn N4", 1990, 2499.95))
    band.add_musician(nuno)

    # Add more musicians
    band.add_musician(Musician("Gary Cherone"))
    band.add_musician(Musician("Pat Badger"))
    pat = Musician("Pat Badger")
    pat.add_instrument(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))
    band.add_musician(pat)

    band.add_musician(Musician("Kevin Figueiredo"))

    # Play the band
    print(band)
    band.play()

if __name__ == '__main__':
    main()
