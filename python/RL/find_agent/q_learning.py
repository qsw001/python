#通过训练得到一个q值表，该表得到在当前状况下，向哪里走得到的收益最高，并不是局部最高而是长期有效的值Q(s,a)
import random
import pickle
from collections import defaultdict

#强调一下这里面的state第一个值指的是当前位置的坐标，而第二个是一个包含宝箱是否被获取的元组(1,0)第一个已经得到了，第二个还没有得到

#state数据结构((位置),(宝箱情况))

class QLearningAgent:
    def __init__(self, action_dim, alpha=0.1, gamma=0.99, epsilon=0.2):
        self.action_dim = action_dim#动作数
        self.alpha = alpha#学习率，越小越稳定
        self.gamma = gamma#折扣因子，越大越看重长期收益
        self.epsilon = epsilon#探索率，随机程度
        self.q_table = defaultdict(lambda: [0.0] * action_dim)#lambda是匿名函数的意思,:后面为返回值; defaultdict的作用是当第一次访问时,if不存在相对应的key,赋值为0

#q_table的数据结构,{
# state1:[x,x,x,x]
# state2:[x,x,x,x]
#}

    #随机选择还是遵循训练的结果
    def choose_action(self, state):
        # if random.random() < self.epsilon:
        #     return random.randint(0, self.action_dim - 1)
        # return self.greedy_action(state)
        if random.random() < self.epsilon:#有0.2的概率进入随机事件
            return random.randint(0,self.action_dim)
        return self.greedy_action(state)

    def greedy_action(self, state):
        q_values = self.q_table[state],#得到4个值，为当前情况下向哪里走可能获得收益的可能性
        max_q = max(q_values)
        best_actions = [i for i, q in enumerate(q_values) if q == max_q]#enumerate的作用是获取索引和值,这句话的意思是如果存在多个一样的值，将他们总结道一起
        return random.choice(best_actions)#随机选择一个前进

    def update(self, state, action, reward, next_state, done):
        current_q = self.q_table[state][action]
        next_max_q = 0 if done else max(self.q_table[next_state])
        target = reward + self.gamma * next_max_q
        self.q_table[state][action] += self.alpha * (target - current_q)

    def save(self, path):
        with open(path, "wb") as f:
            pickle.dump(dict(self.q_table), f)

    def load(self, path):
        with open(path, "rb") as f:
            data = pickle.load(f)
        self.q_table = defaultdict(lambda: [0.0] * self.action_dim, data)