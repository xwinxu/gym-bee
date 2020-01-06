import gym
from gym import error, spaces, utils
from gym.utils import seeding

import math

VIEWPORT_W = 600
VIEWPORT_H = 400
SCALE = 30.0  # affects how fast-paced the game is, forces should be adjusted as well


class BeeEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.env = None
    self.viewer = None
    self.min_position = -10.0
    self.max_position = 

  def step(self, action):
    ...
    # one bee
    # if done dance, can move out of hive
    # collect flower
    # cannot leave boundaries of field
  def reset(self):
    ...

  def render(self, mode='human'):
    """
    Render environment
    """
    from gym.envs.classic_control import rendering

    flower_width = 10
    flower_height = 10
    bee_width = 10
    bee_height = 10

    if self.viewer is None:
      self.viewer = rendering.Viewer(VIEWPORT_W, VIEWPORT_H)
    self.viewer.set_bounds(self.scroll, VIEWPORT_W / SCALE + self.scroll, 0,
                           VIEWPORT_H / SCALE)

    # add the boundary b/t observing bees and observers
    self.boundary = rendering.make_polyline()

    self.viewer.draw_polygon([
        (0, 0),
        (VIEWPORT_W / SCALE, 0),
        (VIEWPORT_W / SCALE, VIEWPORT_H / SCALE),
        (0, VIEWPORT_H / SCALE),
    ],
                             color=(0.04, 0.196, 0.125))
    # draw out

  def close(self):
    if self.viewer:
      self.viewer.close()
    self.viewer = None


ACTION_MEANING = {0: 'LEFT', 1: 'RIGHT', 2: 'UP', 3: 'DOWN'}
