# Machine-Vision
机器视觉课程实验

## Practicals
**01_FittingProbDistribs:**
- 实现三种概率分布拟合方法：最大似然估计（ML）、最大后验概率估计（MAP）和贝叶斯估计（Bayesian），拟合正态分布
  
**02_PracticalMixGauss:**
- 对皮肤和非皮肤像素数据拟合高斯分布模型，计算每个像素为皮肤像素的后验概率，实现皮肤/非皮肤像素的分类
- 使用期望最大化（E-M）算法，迭代拟合混合高斯分布模型

**03_PracticalRegress_Pose:**
- 使用最大似然估计（ML）、贝叶斯估计（Bayesian）来拟合线性回归模型
- 引入径向基函数（RBF）拟合非线性回归模型
- 基于高斯过程回归模型进行头部姿态估计

**04_Classification:**
- 实现线搜索法（line search）调整步长优化函数
- 应用最陡下降法（steepest descent）和牛顿法(Newton's method)解决Rosenbrock函数的非凸优化问题
- 训练逻辑回归模型作为二分类器实现人脸检测功能

**05_GraphicalModels_DynProgStereo:**
- 实现动态规划算法（dynamic programming），可应用于优化路径和匹配问题
- 基于动态规划算法解决密集立体匹配问题，即预测双目摄像头画面扫描线上的像素视差（disparity）

**06_Homographies:**
- 基于最小二乘法实现单应性变换估计算法
- 构建全景图像拼接器：利用对应关键点及单应性变换将多张图像拼接成全景图
- 利用图像空间点和对应的3D世界坐标点，计算相机的外参数矩阵
- 实现将3D立方体投影到图像空间的增强现实效果：通过计算变换矩阵，将立方体的基角与图像中的平面对应

**07_Condensation:**
- 实现因子采样算法，应用于运动系统中跟踪连续视频帧中轮胎的位置

**08_NeuralNets:**
- 构建多层感知机（MLP），利用crossentropy-softmax进行分类
- 训练一个自编码器（Autoencoder），生成手写数字图像，并探索潜在空间中的线性流形。使用PCA降维，实现数字在潜在空间主成分方向的平滑插值，生成连续变化的手写数字图像。

**10_CNN:**
- 对Caltech Camera Traps训练数据集进行数据预处理和数据增强操作，以提高模型的泛化能力
- 基于PyTorch框架，从头训练卷积神经网络（CNN）实现动物图像种类分类
- 利用迁移学习（transfer learning）技术，在预训练模型基础上基于该数据集进行微调，以提高预测准确率
- 可视化分析不同类别的分类准确率

## Coursework

**CW1:**
- 拟合高斯混合模型（Mixtures of Gaussians）以实现图像中的苹果和非苹果像素分割效果，绘制ROC曲线对结果进行量化评估。

**CW2:**
- 结合因子采样（Factored Sampling）和单应性变换（Homography），在视频中跟踪目标图案的四个角，并将3D立方体投影到图像空间，实现增强现实效果。

