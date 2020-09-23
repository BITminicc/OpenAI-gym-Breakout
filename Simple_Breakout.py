import gym
import keyboard
import numpy as np
import time

total_reward = 0
env = gym.make('Breakout-v0')
state = env.reset()
action = 0
def preprocess(img):
    img_temp = img.mean(axis = 2)
    x = -1
    y = -1
    if len(np.where((img_temp[100:189,8:152])!= 0)[0]) != 0:
        x = np.where((img_temp[100:189,8:152])!= 0)[0][0]
        y = np.where((img_temp[100:189,8:152])!= 0)[1][0]
    if len(np.where((img_temp[193:,8:152])!= 0)[0]) != 0:
        x = -2
        y = -2
    p = int(np.where(img_temp[191:193,8:152])[1].mean() - 7.5)
    #return img_temp
    return (x,y,p)
def key(x):
    global action
    if x.event_type == "down" and x.name == '0':
        action = 0
    elif x.event_type == "down" and x.name == '1':
        action = 3
    elif x.event_type == "down" and x.name == '2':
        action = 2
    elif x.event_type == "down" and x.name == '3':
        action = 1
    elif x.event_type == "down" and (action == 4 or x.name == '4'):
        action = 4
    elif action != 4:
        action = 0
keyboard.hook(key)
total_reward = 0
for j in range(1000):
    env.render()
    while action == 4:
        time.sleep(0.1)
    if action == 4:
        action = 0
    next_state,reward,done,_ = env.step(action)
    total_reward += reward
    (x2,y2,p2) = preprocess(next_state)
    #print(action,total_reward,done,x2,y2,p2)
    time.sleep(0.1)
    if done:
        break
keyboard.wait()
