# from collections import deque
# import matplotlib.pyplot as plt

# from env import TreasureHuntEnv
# from q_learning import QLearningAgent


# def train():
#     # 实例化环境和智能体
#     env = TreasureHuntEnv()
#     agent = QLearningAgent(action_dim=4, alpha=0.4, gamma=0.99, epsilon=0.5)

#     # 训练轮数
#     episodes = 50000

#     # ===== 可视化数据 =====
#     plot_every = 1000            # 每多少轮更新一次图
#     window_size = 200            # 滑动平均窗口

#     x_data = []
#     reward_avg_data = []
#     steps_avg_data = []
#     chest_avg_data = []
#     success_rate_data = []       # 成功拿到2个宝箱的比例

#     recent_rewards = deque(maxlen=window_size)
#     recent_steps = deque(maxlen=window_size)
#     recent_chests = deque(maxlen=window_size)
#     recent_success = deque(maxlen=window_size)

#     # 打开交互模式
#     plt.ion()
#     fig, axes = plt.subplots(2, 2, figsize=(12, 8))
#     ax1, ax2 = axes[0]
#     ax3, ax4 = axes[1]

#     for episode in range(episodes):
#         # 重置环境
#         state = env.reset()
#         total_reward = 0
#         last_info = {"steps": 0, "collected_chests": 0}

#         # 一轮训练
#         while not env.done:
#             action = agent.choose_action(state)
#             next_state, reward, done, info = env.step(action)
#             agent.update(state, action, reward, next_state, done)

#             state = next_state
#             total_reward += reward
#             last_info = info

#         # 统计当前轮结果
#         chests = last_info["collected_chests"]
#         steps = last_info["steps"]
#         success = 1 if chests == 2 else 0

#         recent_rewards.append(total_reward)
#         recent_steps.append(steps)
#         recent_chests.append(chests)
#         recent_success.append(success)

#         # 控制台打印
#         if (episode + 1) % 1000 == 0:
#             print(
#                 f"Episode {episode + 1}, "
#                 f"total_reward = {total_reward}, "
#                 f"steps = {steps}, "
#                 f"chests = {chests}, "
#                 f"success_rate({window_size}) = {sum(recent_success) / len(recent_success):.2%}"
#             )

#         # 更新图像
#         if (episode + 1) % plot_every == 0:
#             x_data.append(episode + 1)
#             reward_avg_data.append(sum(recent_rewards) / len(recent_rewards))
#             steps_avg_data.append(sum(recent_steps) / len(recent_steps))
#             chest_avg_data.append(sum(recent_chests) / len(recent_chests))
#             success_rate_data.append(sum(recent_success) / len(recent_success))

#             ax1.clear()
#             ax2.clear()
#             ax3.clear()
#             ax4.clear()

#             ax1.plot(x_data, reward_avg_data)
#             ax1.set_title(f"Average Reward (last {window_size})")
#             ax1.set_xlabel("Episode")
#             ax1.set_ylabel("Reward")

#             ax2.plot(x_data, steps_avg_data)
#             ax2.set_title(f"Average Steps (last {window_size})")
#             ax2.set_xlabel("Episode")
#             ax2.set_ylabel("Steps")

#             ax3.plot(x_data, chest_avg_data)
#             ax3.set_title(f"Average Chests (last {window_size})")
#             ax3.set_xlabel("Episode")
#             ax3.set_ylabel("Chests")

#             ax4.plot(x_data, success_rate_data)
#             ax4.set_title(f"Success Rate = Get 2 Chests (last {window_size})")
#             ax4.set_xlabel("Episode")
#             ax4.set_ylabel("Rate")
#             ax4.set_ylim(0, 1.05)

#             plt.tight_layout()
#             plt.pause(0.01)

#     # 保存Q表
#     agent.save("q_table.pkl")
#     print("训练完成，Q表已保存到 q_table.pkl")

#     # 关闭交互模式，最终停留图像
#     plt.ioff()
#     plt.show()


# if __name__ == "__main__":
#     train()