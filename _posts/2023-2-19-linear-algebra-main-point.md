# 线性代数大纲



## 行列式

方阵，用$i,j$不表示行和列。

### 格式

$$
D=
\left|\begin{array}{ccc} 
    a_{11}	&	\cdots	&	a_{1n} \\
    \vdots	&			&	\vdots \\
    a_{n1} &	\cdots	&	a_{nn} 
\end{array}\right|
$$

### 性质

p8

### 计算

#### 对角线

只适用于二/三阶；正对角线（撇）之和减去副对角线（捺）之和。

#### 三角行列式

1. 根据行列式性质，将行列式化为上（下）三角行列式；
2. 根据上（下）三角行列式结论（其值等于对角线）计算。

#### 全排列

$$
\sum(-1)^{t}a_{1p_1}a_{2p_2}...a_{np_n}
$$

1. $t$表示$\{p_1, p_2...p_n\}$的逆序数；
2. $\{p_1, p_2...p_n\}$表示$\{1, 2...n\}$的全排列。

#### 按行（列）展开

按行展开，行数不变。

$D=a_{i1}A_{i1}+a_{i2}A_{i2}+\cdots+a_{in}A_{in}$

按列展开，列数不变。

$D=a_{1j}A_{1j}+a_{2j}A_{2j}+\cdots+a_{nj}A_{nj}$

$A_{ij}$表示代数余子式，顺便一提，$M_{ij}$表示余子式，两者都是行列式。

### 知识点

拉普拉斯定理；

范德蒙德行列式，通过拉普拉斯定理推导。

## 矩阵

$m \times n$

### 格式

$$
A = 
\left[\begin{array}{ccc} 
    a_{11}	&	\cdots	&	a_{1n} \\ 
    \vdots	&			&	\vdots \\ 
    a_{m1} &	\cdots	&	a_{mn} 
\end{array}\right]
$$

### 运算

#### 加减

$$
\mathbf{A}+\mathbf{B} =
\left[
\begin{array}{ccc}
	a_{11}+b_{11}&	a_{12}+b_{12}&	\cdots&	a_{1n}+b_{1n}	\\
	a_{21}+b_{21}&	a_{22}+b_{22}&	\cdots&	a_{2n}+b_{2n}	\\
	\vdots&			\vdots&			&		\vdots		 	\\
	a_{m1}+b_{m1}&	a_{m2}+b_{m2}&	\cdots&	a_{mn}+b_{mn}	\\
\end{array}
\right]
$$

#### 转置

略

#### 数乘

$$
\lambda\mathbf{A}=\mathbf{A}\lambda=
\left[
\begin{array}{ccc}
	\lambda a_{11}&	\lambda a_{12}&	\cdots&	\lambda a_{1n}	\\
	\lambda a_{21}&	\lambda a_{22}&	\cdots&	\lambda a_{2n}	\\
	\vdots&			\vdots&			&		\vdots		 	\\
	\lambda a_{m1}&	\lambda a_{m2}&	\cdots&	\lambda a_{mn}	\\
\end{array}
\right]
$$


#### 矩阵乘法（矩阵x矩阵）

略

应用于线性方程组、线性变换

#### 运算律

矩阵相加满足加法交换律：

$\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A}$

转置和数乘加法分配律：

$(\mathbf{A}+\mathbf{B})^\mathrm{T}=\mathbf{A}^\mathrm{T}+\mathbf{B}^\mathrm{T}$

$c(\mathbf{A}+\mathbf{B})=c\mathbf{A}+c\mathbf{B}$

矩阵乘法

结合律：$(\mathbf{AB})\mathbf{C}=\mathbf{A}(\mathbf{BC})$

左分配律：$(\mathbf{A}+\mathbf{B})\mathbf{C}=\mathbf{AC}+\mathbf{BC}$

右分配律：$\mathbf{C}(\mathbf{A}+\mathbf{B})=\mathbf{CA}+\mathbf{CB}$ 

数乘和转置满足的分配律：

$c(\mathbf{AB})=(c\mathbf{A})\mathbf{B}=\mathbf{A}(c\mathbf{B})$

$(\mathbf{AB})^\mathrm{T}=\mathbf{B}^\mathrm{T}\mathbf{A}^\mathrm{T}$

### 知识点

克拉默法则，用来求解线性方程组



矩阵初等行变换（定义类比线性方程组，比如矩阵可以两行互换，线性方程组也可以两行互换）

里面涉及了**行最简**和**标准形**，P60



矩阵的秩

最高阶的非零子式

## 向量

