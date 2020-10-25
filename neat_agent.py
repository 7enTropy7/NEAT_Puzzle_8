
import neat
import numpy as np
import pickle
import os
from puzzle8 import *

env = Puzzle8()

def run(config_path):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(main, n=5000) # n is no. of generations

def main(genomes,config):
    observation = env.reset()
    temp = observation
    for genome_id,genome in genomes:

        genome.fitness = 0.0

        net = neat.nn.FeedForwardNetwork.create(genome,config)

        # observation = env.reset()

        done = False
        t = 0
        while not done:

            flat_observation = np.ndarray.flatten(observation)
            action = net.activate(flat_observation)
            step = action.index(max(action))
            observation, reward, done = env.step(step)
            print(observation,reward,done)
            t += 1
            if done:
                print("{} <-- Episode _________ {} timesteps __________ {} counter __________ reward {} ".format(genome_id,t + 1,env.counter, env.reward))
                observation = temp
                break
        genome.fitness = reward
        print("Genome : {}  Fitness : {}".format(genome_id,genome.fitness))


if __name__=="__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,'config-feedforward.txt')
    run(config_path)