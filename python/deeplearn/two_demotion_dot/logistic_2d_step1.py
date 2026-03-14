import numpy as np
import matplotlib.pyplot as plt

#保持结果一致，设立随机数种子
np.random.seed(42)

#随机生成两类特征二维点,一类在(2,2),一类在(5,5)
class0 = np.random.randn(100,2)*0.8 + np.array([2,2])
class1 = np.random.randn(100,2)*0.8 + np.array([5,5])

#将数据集总结并贴上标签

#拼接数据集
point = np.vstack([class0,class1])
point_label = np.vstack([np.zeros((100,1)), np.ones((100,1))])

print("point", point.shape)
print("point_label", point_label.shape)


#作图

#确定大小
plt.figure(figsize=(6,6))

#画点
plt.scatter(class0[:,0],class0[:,1],label="class0",alpha=0.8)
plt.scatter(class1[:,0],class1[:,1],label="class1",alpha=0.8)

#写注释
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("2D Binary Classification Dataset")

#结尾
plt.grid(True)
plt.legend()
plt.show()


# #向前学习
# # z = w1*x1 + w2*x2 + b

# #初始化参数
# w = np.zeros((2,1))#可以理解为一个2*1的矩阵
# b = 0

# #定义sigmoid函数
# def sigmoid(z):
#     return 1/(1+np.exp(-z))


# for i in range(1000):
#     z = point@w + b

#     # 算出概率
#     a = sigmoid(z)

#     #反向传播

#     #计算loss

#     #获取样本数量
#     m = point_label.shape[0] #shape输出的是矩阵形状

#     #loss
#     loss = -(point_label*np.log(a) + (1-point_label)*(1-np.log(a)))

#     #cost
#     cost = np.sum(loss)/m

#     # =====================
#     # 梯度下降
#     # =====================

#     learning_rate = 0.1

#     dz = a - point_label

#     dw = (point.T @ dz) / m
#     db = np.sum(dz) / m

#     w = w - learning_rate * dw
#     b = b - learning_rate * db

# =====================
# 训练逻辑回归
# =====================

# 初始化参数
w = np.zeros((2, 1))
b = 0.0

# 学习率
learning_rate = 0.1

# 训练轮数
epochs = 1000

# 记录每一轮的cost，后面画图用
cost_history = []

# sigmoid函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 开始训练
for i in range(epochs):
    # 1. 前向传播
    z = point @ w + b
    a = sigmoid(z)

    # 2. 计算loss / cost
    m = point.shape[0]
    loss = -(point_label * np.log(a + 1e-8) + (1 - point_label) * np.log(1 - a + 1e-8))
    cost = np.sum(loss) / m

    # 3. 反向传播（求梯度）
    dz = a - point_label
    dw = (point.T @ dz) / m
    db = np.sum(dz) / m

    # 4. 更新参数
    w = w - learning_rate * dw
    b = b - learning_rate * db

    # 记录cost
    cost_history.append(cost)

    # 每100轮打印一次
    if i % 100 == 0:
        print(f"第{i}轮, cost = {cost:.6f}")

print("训练结束")
print("w =")
print(w)
print("b =", b)


# =====================
# 画loss曲线
# =====================
plt.figure(figsize=(6, 4))
plt.plot(cost_history)
plt.xlabel("epoch")
plt.ylabel("cost")
plt.title("Loss Curve")
plt.grid(True)
plt.show()

# =====================
# 画分类直线
# =====================

x_values = np.array([0, 7])

y_values = -(w[0]*x_values + b) / w[1]

plt.figure(figsize=(6,6))

plt.scatter(class0[:,0],class0[:,1],label="class0",alpha=0.8)
plt.scatter(class1[:,0],class1[:,1],label="class1",alpha=0.8)

plt.plot(x_values, y_values, color="red", label="decision boundary")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Logistic Regression Decision Boundary")

plt.legend()
plt.grid(True)
plt.show()