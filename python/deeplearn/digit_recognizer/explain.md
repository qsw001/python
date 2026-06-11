# 深度学习demo，数字识别

## 1. layers

layers负责前后两层神经网络的工作，主要有:
- 正向传播 forward
- 反向传播 backward
- 归一化
- 激活函数 activity function

正向传播公式:
$$ Y = XW + b $$

反向传播公式:

$$G = \frac{\partial L}{\partial Y}$$

$$\frac{\partial L}{\partial W}=\frac{1}{m} X^{T}G$$

$$\frac{\partial L}{\partial b}=\frac{1}{m}\sum_{i=1}^{m} G_i$$

$$\frac{\partial L}{\partial X}=GW^{T}$$

$$X \in \mathbb{R}^{m \times d_{\text{in}}}$$

$$W \in \mathbb{R}^{d_{\text{in}} \times d_{\text{out}}}$$

$$b \in \mathbb{R}^{1 \times d_{\text{out}}}$$

$$Y \in \mathbb{R}^{m \times d_{\text{out}}}$$

$$G \in \mathbb{R}^{m \times d_{\text{out}}}$$