import random


class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb

    def get_listen_prob(self):
        return self.listen

    def get_sleep_prob(self):
        return self.sleep

    def get_fb_prob(self):
        return self.fb


def get_mean_and_std(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object

    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
             Where the first float represents the mean number of lectures it takes
             to have a lecture in which all 3 activities take place,
             And the second float represents the total width of the 95% confidence
             interval around that mean.
    '''
    def oneTrial():
        """runs one simulation"""
        listenProb = aLecture.get_listen_prob()
        sleepProb = aLecture.get_sleep_prob()
        fbProb = aLecture.get_fb_prob()
        numberOfLectures = 0
        while True:
            numberOfLectures += 1
            if random.random() <= listenProb and random.random() <= sleepProb and random.random() <= fbProb:
                break
        return numberOfLectures

    simulations = []
    for i in range(N):
        trialResult = oneTrial()
        simulations.append(trialResult)

    mean, std = get_mean_and_std(simulations)

    ciWidth = 2 * 1.96 * std

    return mean, ciWidth





# sample test cases
a = Lecture(1, 1, 1)
print(lecture_activities(100, a))
# the above test should print out (1.0, 0.0)

b = Lecture(1, 1, 0.5)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)

b = Lecture(0.9, 0.3, 0.8)
print(lecture_activities(100000, b))
# the above test should print out something reasonably close to (2.0, 5.516)

