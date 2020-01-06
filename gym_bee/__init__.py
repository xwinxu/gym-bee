from gym.envs.registration import register

register(
    id='bee-v0',
    entry_point='gym_foo.envs:BeeEnv',
)
register(
    id='bee-extrahard-v0',
    entry_point='gym-bee.envs:BeeExtraHardEnv',
)