#sys.path.append("usr/local/lib/python3.7/site-packages/gym")
import gym
import bipedal
import atari
import mountaincar
import argparse

def parse_args():
  parser = argparse.ArgumentParser(...)

  parser.add_argument('--env', type=str, default='bee_env', help='the env to run')

if __name__ == "__main__":
  params = parse_args()
  env = mountaincar.Continuous_MountainCarEnv()
  env.reset()
  for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())  # take a random action
  env.close()