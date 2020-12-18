import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    if CURRENTRABBITPOP == 10:
        rabbitProb = 0
    else:
        rabbitProb = 1 - (CURRENTRABBITPOP / MAXRABBITPOP)

    babies = 0
    for i in range(CURRENTRABBITPOP):
        if random.random() <= rabbitProb:
            babies += 1

    CURRENTRABBITPOP += babies


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    foxEatProb = CURRENTRABBITPOP / MAXRABBITPOP

    babies = 0
    deathsRabbit = 0
    deathsFox = 0
    for i in range(CURRENTFOXPOP):
        if random.random() <= foxEatProb and (CURRENTRABBITPOP - deathsRabbit) > 10:
            deathsRabbit += 1
            if random.random() <= 1 / 3:
                babies += 1
        else:
            if random.random() <= 0.1 and (CURRENTFOXPOP - deathsFox) > 10:
                deathsFox += 1

    CURRENTFOXPOP += babies
    CURRENTFOXPOP -= deathsFox

    CURRENTRABBITPOP -= deathsRabbit


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = [CURRENTRABBITPOP]
    fox_populations = [CURRENTFOXPOP]

    for i in range(numSteps - 1):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

    return rabbit_populations, fox_populations


rabbs, foxes = runSimulation(200)

pylab.plot(foxes)
pylab.show()

# coeff = pylab.polyfit(range(len(rabbs)), rabbs, 2)
# coeffFoxes = pylab.polyfit(range(len(foxes)), foxes, 2)
# pylab.plot(pylab.polyval(coeff, range(len(rabbs))))
# pylab.plot(pylab.polyval(coeffFoxes, range(len(foxes))))
# pylab.show()
# coeff = pylab.polyfit(range(len(foxes)), foxes, 2)
# pylab.plot(pylab.polyval(coeff, range(len(foxes))))
# pylab.show()