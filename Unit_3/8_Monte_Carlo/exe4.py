import random


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    redBallsGlob = 3
    greenBallsGlob = 3
    hitsGlob = 0

    def monteCarloSim(redBalls, greenBalls):
        """runs one simulation"""
        x = 6
        for i in range(3):
            draw = random.randint(1, x)
            if draw <= redBalls:
                redBalls -= 1
            else:
                greenBalls -= 1
            x -= 1
        if redBalls == 0 or greenBalls == 0:
            return True

    for i in range(numTrials):
        simResult = monteCarloSim(redBallsGlob, greenBallsGlob)
        if simResult:
            hitsGlob += 1
    return hitsGlob / numTrials


print(noReplacementSimulation(100000))
