
import gym
env = gym.make("CartPole-v1")
observation = evn.reset()
for i in range(1000):
    env.render()
    action = env.action_space.sample()
    observation,reward, done, info = env.stop(action)
    if done:
        observation = env.reset()
env.close()
