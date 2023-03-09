
### 测试

设$\displaystyle\lim_{x\rightarrow a} \frac{f(x)-f(a)}{(x-a)^2}=1$，则在点$x=a$处（）

A. $f(x)$的导数存在，且$f'(a)\neq 0$
B. $f(x)$取得极大值
C. $f(x)$取得极小值
D. $f(x)$取导数不存在

**解**
左式展开：

$$
\begin{aligned}
\displaystyle\lim_{x\rightarrow a}\frac{f(x)-f(a)}{(x-a)^2}&=\displaystyle\lim_{x\rightarrow a}\frac{f(x)-f(a)}{(x+a)(x-a)}\\
&=\displaystyle\lim_{x\rightarrow a}\frac{1}{x+a}\cdot\displaystyle\lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}
\end{aligned}
$$

$\because\displaystyle\lim_{x\rightarrow a} \frac{f(x)-f(a)}{(x-a)^2}=1$
$\therefore \displaystyle\lim_{x\rightarrow a}\frac{1}{x+a}\cdot\displaystyle\lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}=1$
$\therefore\displaystyle\lim_{x\rightarrow a}\frac{f(x)-f(a)}{x-a}\neq 0$
$\therefore$导数存在且不为0，故选A。

---

求由方程$e^y+xy-e=0$所确定的因函数的导数$\frac{dy}{dx}$.
**解**
方程左式对$x$求导：

$$
\begin{aligned}
\frac{d(e^y+xy-e)}{dx}&=\frac{de^y+d(xy)-de}{dx}\\
&=\frac{e^ydy+dxy+xdy-0}{dx}\\
&=e^y\frac{dy}{dx}+y+x\frac{dy}{dx}
\end{aligned}
$$

方程右式对$x$求导：
$$
(0)'=0
$$

综上，
$$
\begin{aligned}
e^y\frac{dy}{dx}+y+x\frac{dy}{dx}&=0\\
(e^y+x)\frac{dy}{dx}&=-y\\
\frac{dy}{dx}&=-\frac{y}{e^y+x}
\end{aligned}
$$