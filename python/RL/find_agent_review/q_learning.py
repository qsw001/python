from collections import defaultdict
import random

#agent需要的几个基本参数，gamma折扣率，越大越注重长远利益，alpha学习率，越小越稳定，epsilon探索率，action_dim行动方向,qtable
class QLearningAgent:
    def __init__(self, action_dim, alpha = 0.1, gamma = 0.99, epsilon = 0.2):
        self.action_dim = action_dim
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = defaultdict(lambda : [0.0] * action_dim)

    def greedy_action(self, state):
        q_value = self.q_table[state]
        q_max = max(q_value)
        best_actions = [i for i, j in enumerate(q_value) if q_max == j]
        return random.choice(best_actions)
    
    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0,self.action_dim-1)
        return self.greedy_action(state)
    
    def update(self, state, action, reward, next_state, done):
        current_q = self.q_table[state][action]
        next_max_q = 0 if done else max(self.q_table[next_state])
        target = reward + next_max_q * self.gamma
        self.q_table[state][action] = self.alpha * (target - current_q)

    

        