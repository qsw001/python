from copy import deepcopy

#定义了环境的行列行动等行为
class TreasureHuntEnv:
    def __init__(self):# 这里的init指的是构造函数,self指的是它本身
        self.original_map = [
            ['S', '.', '.', '#', '.', 'C'],
            ['.', '#', '.', '#', '.', '.'],
            ['.', '#', '.', '.', '.', '.'],
            ['.', '.', '#', '#', '.', '.'],
            ['C', '.', '.', '.', '#', '.'],
            ['.', '.', '.', '.', '.', 'G']
        ]#S为起点，G为终点，C为宝箱

        self.rows = len(self.original_map)
        self.cols = len(self.original_map[0])

        self.actions = {
            0: (-1, 0),  # 上
            1: (1, 0),   # 下
            2: (0, -1),  # 左
            3: (0, 1),   # 右
        }#动作编号等于坐标变化

        self.max_steps = 100

        self.reset()

    #在地图里找某一个目标字符第一次出现的位置。
    def find_pos(self, target):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.original_map[i][j] == target:
                    return (i, j)
        return None

    #这个和上面不同，它不是找第一个，而是找所有。
    def find_all_pos(self, target):
        result = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.original_map[i][j] == target:
                    result.append((i, j))
        return result

    #开始一局游戏，把所有的恢复到新的状态
    def reset(self):
        self.map = deepcopy(self.original_map)
        self.agent_pos = self.find_pos('S')
        self.goal_pos = self.find_pos('G')
        self.chest_positions = self.find_all_pos('C')
        self.collected_chests = set()
        self.steps = 0
        self.done = False
        return self.get_state()

    #设置状态，agent的位置和宝箱的状态(是否获得)
    def get_state(self):
        chest_state = tuple(
            1 if pos in self.collected_chests else 0
            for pos in self.chest_positions
        )
        return (self.agent_pos, chest_state)


    # def step(self, action):
    #     if self.done:
    #         raise ValueError("回合已经结束，请先 reset()")#raise主动触发错误，让进程停止

    #     self.steps += 1
    #     reward = -1

    #     dx, dy = self.actions[action]
    #     x, y = self.agent_pos
    #     nx, ny = x + dx, y + dy

    #     if not (0 <= nx < self.rows and 0 <= ny < self.cols):
    #         reward -= 5
    #         return self.get_state(), reward, self.done, {
    #             "steps": self.steps,
    #             "collected_chests": len(self.collected_chests)
    #         }

    #     if self.map[nx][ny] == '#':
    #         reward -= 5
    #         return self.get_state(), reward, self.done, {
    #             "steps": self.steps,
    #             "collected_chests": len(self.collected_chests)
    #         }

    #     self.agent_pos = (nx, ny)

    #     if self.agent_pos in self.chest_positions and self.agent_pos not in self.collected_chests:
    #         self.collected_chests.add(self.agent_pos)
    #         reward += 20

    #     if self.agent_pos == self.goal_pos:
    #         reward += 100
    #         self.done = True

    #     if self.steps >= self.max_steps:
    #         self.done = True

    #     return self.get_state(), reward, self.done, {
    #         "steps": self.steps,
    #         "collected_chests": len(self.collected_chests)
    #     }

    #传入当前状态和要移动的方向，来做出判断
    def step(self, action):
        if self.done:
            raise ValueError("回合已经结束，请先 reset()")
        
        self.steps += 1
        reward = -1  #走路有惩罚

        #开始移动,与之前定义的action有关,此处x为行，y为列
        dx, dy = self.actions[action]
        x, y = self.agent_pos
        nx, ny = x + dx, y + dy

        #判断如果出界
        if not (0 <= nx <= self.rows and 0 <= ny <= self.cols):
            reward -= 5
            return self.get_state(), reward, self.done, {
                "steps": self.steps,
                "collected_chests": len(self.collected_chests)
            }

        #如果撞到障碍物
        if self.map[nx][ny] == '#':
            reward -= 5
            return self.get_state(), reward, self.done, {
                "steps": self.steps,
                "collected_chests": len(self.collected_chests)
            }

        #以上两个不用移动agnet，否则更新位置
        self.agent_pos = (nx, ny)

        #吃到宝箱加分，并且更新搜集到的宝箱位置
        if self.agent_pos in self.chest_positions and self.agent_pos not in self.collected_chests:
            self.collected_chests.add(self.agent_pos)
            reward += 20

        #到达终点加分
        if self.agent_pos == self.goal_pos:
            reward += 100
            self.done = True

        #步数达到上限是结束
        if self.steps >= self.max_steps:
            self.done = True

        #返回
        return self.get_state(), reward, self.done, {
            "steps": self.steps,
            "collected_chests": len(self.collected_chests)
        }


    def render(self):
        display = deepcopy(self.original_map)

        for cx, cy in self.collected_chests:
            display[cx][cy] = '.'

        x, y = self.agent_pos
        display[x][y] = 'A'

        for row in display:
            print(' '.join(row))
        print()


# if __name__ == "__main__":
#     env = TreasureHuntEnv()

#     state = env.reset()
#     print("初始状态:", state)
#     env.render()

#     action_list = [3, 3, 1, 3]  # 右 右 下 下，随便试几步

#     for action in action_list:
#         next_state, reward, done, info = env.step(action)
#         print(f"动作: {action}")
#         print(f"下一状态: {next_state}")
#         print(f"奖励: {reward}")
#         print(f"结束: {done}")
#         print(f"信息: {info}")
#         env.render()