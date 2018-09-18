import gym
from gym import error, spaces, utils
from gym.utils import seeding
from snake_gym.envs.modules import *
from snake_gym.envs.snake_env import SnakeEnv
import numpy as np


class SnakeEnvTiled(SnakeEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super().__init__()

    def step(self, action):
        state, reward, done, info = self._s.step(action)
        state = SnakeEnvTiled._process(state)
        return state, reward, done, info

    def reset(self):
        super().reset()

    def render(self, mode='human', close=False):
        super().render()

    @staticmethod
    def _equals(arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

    @staticmethod
    def _process(img):
        ret = list(map(list, np.zeros((GRID_HEIGHT, GRID_WIDTH))))
        ret = list(map(lambda x: list(map(int, x)), ret))
        for i in range(0, SCREEN_HEIGHT, GRIDSIZE):
            for k in range(0, SCREEN_WIDTH, GRIDSIZE):
                if SnakeEnvTiled._equals(img[i][k], [255, 0, 0, 255]):
                    ret[int(i / 15)][int(k / 15)] = 2
                elif SnakeEnvTiled._equals(img[i][k], [0, 0, 0, 255]):
                    ret[int(i / 15)][int(k / 15)] = 1
            print(ret[int(i / 15)])
        return ret
