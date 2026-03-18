#对于环境,我们首先要确定地图，
from copy import deepcopy

class Env:
    def __init__(self):
        self.orginmap = [
            ['S', '.', '.', '.', '.', 'C'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '.', '.', '.'],
            ['.', '.', '.', '#', '.', '.'],
            ['C', '.', '.', '.', '#', '.'],
            ['.', '.', '.', '.', '.', 'G']
        ]

        self.colMap = len(self.orginmap[0])
        self.rowMap = len(self.orginmap)

        self.actions = {
            0: (1,0),
            1: (0,1),
            2: (-1,0),
            3: (0,-1),
        }

        self.maxsteps = 100

        self.reset()

    def reset(self):
        self.map = deepcopy(self.orginmap)
        self.steps = 0
        self.posAgent = self.findPos('S')
        self.posGoal = self.findPos('G')
        self.posChest = self.findAllPos('C')
        self.done = False
        self.getChests = set()

        return self.getState()

    def getState(self):
        chest_state = tuple(
            1 if pos in self.getChests else 0
            for pos in self.posChest 
        )
        return (self.posAgent, chest_state)

    def findPos(self, target):
        for i in range(self.rowMap):
            for j in range(self.colMap):
                if self.orginmap[i][j] == target:
                    return (i,j)
        return None
    
    def findAllPos(self, target):
        result = []
        for i in range(self.rowMap):
            for j in range(self.colMap):
                if self.orginmap[i][j] == target:
                    result.append((i,j))
        return result
    
    #
    def step(self, action):
        if self.done:
            raise ValueError("回合已经结束，请先 reset()")
        
        #先写一定变化的状态
        self.steps += 1
        reward = -1

        #算出下一步的状态
        dx, dy = self.actions[action]
        x, y = self.posAgent
        nx, ny = x + dx, y + dy

        #判断各种情况

        if not (0 <= nx < self.rowMap and 0 <= ny < self.colMap):
            reward -= 5
            return self.getState(), reward, self.done, {
                "steps" : self.steps,
                "chests" : len(self.getChests)
            }
        
        if self.map[nx][ny] == '#':
            reward -= 5
            return self.getState(), reward, self.done, {
                "steps" : self.steps,
                "chests" : len(self.getChests)
            }
        
        #以上两种情况返回的位置与之前一致，即agent的位置不变

        self.posAgent = (nx, ny)

        # 错误写法，地图里的信息是不变的
        # if self.map[nx][ny] == 'C':
        #     self.getChests

        if self.posAgent in self.posChest and self.posAgent not in self.getChests:
            self.getChests.add(self.posAgent)
            reward += 50

        if self.posAgent == self.posGoal:
            if len(self.getChests) == len(self.posChest):
                reward += 100
                self.done = True
            else:
                reward -= 40
                self.done = True
        
        if self.steps >= self.maxsteps:
            self.done = True

        return self.getState(), reward, self.done, {
            "steps" : self.steps,
            "chests" : len(self.getChests)
        }

    def render(self):
        display = deepcopy(self.orginmap)

        for cx, cy in self.getChests:
            display[cx][cy] = '.'

        x, y = self.posAgent
        display[x][y] = 'A'

        for row in display:
            print(' '.join(row))
        print()