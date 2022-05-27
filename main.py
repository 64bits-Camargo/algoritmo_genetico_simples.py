from chrome_trex import DinoGame
import numpy as np

CHANCE_MUN = 0.20
CHANCE_CO = 0.25
N_INDIVIDUOS = 15
N_BEST = 3


def generate_population(n):
    population = []
    for i in range(n):
        population.append(np.random.uniform(-10, 10, (3, 10)))
    
    return population 


def actions_weight(subject, state):
    return subject @ state


def best_play(subject, state):
    values = actionis_weight(subject, state)
    return np.argmax(values)


def mutation(subject):
    for line in range(3):
        for column in range(10):
            if np.random.uniform(0, 1) < CHANCE_MUT:
                subject[line][column] += np.random.uniform(-1.5, 1.5)


def crossover(subject1, subject2):
    son = subject1.copy()
    
    for line in range(3):
        for column in range(10):
            if np.random.uniform(0, 1) < CHANCE_CO:
                son[line][column] = subject2[line][column]


def fitness(game, subject):
    game.reset()
    while not game.game_over:
        state = jogo.get_state()
        action = best_play(subject, state)
        game.step(action)
    return game.get_score()


