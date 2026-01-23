# Chapter 3 Unit Test – Solutions

## Question 1

**Solve the following quadratic equations:**

**(a) $(2x - 3)(x + 7) = 0$**

*Method:* Set each factor to zero.
1. $2x - 3 = 0 \Rightarrow 2x = 3 \Rightarrow x = 1.5$
2. $x + 7 = 0 \Rightarrow x = -7$

**Answer:** $x = 1.5, x = -7$

---

**(b) $2x^2 + 2.7x - 5.1 = 0$**

*Method:* Quadratic Formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
- $a = 2, b = 2.7, c = -5.1$

1. Find discriminant:
   $\Delta = (2.7)^2 - 4(2)(-5.1)$
   $\Delta = 7.29 + 40.8 = 48.09$

2. Solve for $x$:
   $x = \frac{-2.7 \pm \sqrt{48.09}}{4}$
   $\sqrt{48.09} \approx 6.935$

3. Two solutions:
   $x_1 = \frac{-2.7 + 6.935}{4} = \frac{4.235}{4} \approx 1.06$
   $x_2 = \frac{-2.7 - 6.935}{4} = \frac{-9.635}{4} \approx -2.41$

**Answer:** $x \approx 1.06, x \approx -2.41$

---

**(c) $2x^2 - 9x - 5 = 0$**

*Method:* Factoring (Decomposition)
Need two numbers that multiply to $a \cdot c = 2(-5) = -10$ and add to $b = -9$.
Numbers are $-10$ and $1$.

1. Rewrite middle term:
   $2x^2 - 10x + 1x - 5 = 0$

2. Group terms:
   $2x(x - 5) + 1(x - 5) = 0$

3. Factor out common binomial:
   $(2x + 1)(x - 5) = 0$

4. Solve:
   $2x + 1 = 0 \Rightarrow x = -0.5$
   $x - 5 = 0 \Rightarrow x = 5$

**Answer:** $x = -0.5, x = 5$

---

## Question 2

**Simplify:**

**(a) $\sqrt{108}$**
Look for largest perfect square factor ($36$).
$\sqrt{36 \cdot 3} = \sqrt{36} \cdot \sqrt{3} = 6\sqrt{3}$
**Answer:** $6\sqrt{3}$

**(b) $4\sqrt{12} - 3\sqrt{48}$**
Simplify radicals first:
$\sqrt{12} = \sqrt{4 \cdot 3} = 2\sqrt{3}$
$\sqrt{48} = \sqrt{16 \cdot 3} = 4\sqrt{3}$

Substitute back:
$4(2\sqrt{3}) - 3(4\sqrt{3})$
$= 8\sqrt{3} - 12\sqrt{3}$
$= -4\sqrt{3}$
**Answer:** $-4\sqrt{3}$

**(c) $(7\sqrt{2} + \sqrt{3})(7\sqrt{2} - \sqrt{3})$**
This is a difference of squares $(A+B)(A-B) = A^2 - B^2$.
$A = 7\sqrt{2}, B = \sqrt{3}$
$(7\sqrt{2})^2 - (\sqrt{3})^2$
$= (49 \cdot 2) - 3$
$= 98 - 3 = 95$
**Answer:** $95$

**(d) $(3 - 2\sqrt{7})^2$**
Expand $(A-B)^2 = A^2 - 2AB + B^2$.
$= 3^2 - 2(3)(2\sqrt{7}) + (2\sqrt{7})^2$
$= 9 - 12\sqrt{7} + (4 \cdot 7)$
$= 9 - 12\sqrt{7} + 28$
$= 37 - 12\sqrt{7}$
**Answer:** $37 - 12\sqrt{7}$

---

## Question 3

**Function:** $f(x) = -3(x + 4)^2 + 27$

**(a) Convert forms:**

**(i) Standard Form**
Expand the vertex form:
$f(x) = -3(x^2 + 8x + 16) + 27$
$f(x) = -3x^2 - 24x - 48 + 27$
**Answer:** $f(x) = -3x^2 - 24x - 21$

**(ii) Factored Form**
Factor the standard form $f(x) = -3x^2 - 24x - 21$:
Factor out -3:
$f(x) = -3(x^2 + 8x + 7)$
Factor trinomial (sum 8, product 7 $\rightarrow$ 7, 1):
**Answer:** $f(x) = -3(x + 7)(x + 1)$

**(b) State the properties:**

**(i) y-intercept**
Let $x=0$ in standard form:
$y = -21$
**Answer:** $(0, -21)$

**(ii) x-intercepts**
From factored form $-3(x+7)(x+1) = 0$:
**Answer:** $x = -7, x = -1$

**(iii) Vertex**
From vertex form $-3(x+4)^2 + 27$:
**Answer:** $(-4, 27)$

**(iv) Axis of symmetry**
Matches x-coordinate of vertex.
**Answer:** $x = -4$

**(v) Max or min**
Parabola opens down ($a = -3$ is negative), so it has a Maximum.
**Answer:** Maximum value is 27.

**(c) Graphing notes**
- Plot Vertex: $(-4, 27)$
- Plot Zeros: $(-7, 0)$ and $(-1, 0)$
- Plot Y-int: $(0, -21)$
- Draw smooth curve downwards through these points.

---

## Question 4

**Projectile Motion:** $h(t) = -5t^2 + 20t + 0.8$

**(a) Height when hit?**
Initial height at $t=0$:
$h(0) = 0.8$
**Answer:** 0.8 meters

**(b) Maximum height**
Find the vertex.
$t_{vertex} = \frac{-b}{2a} = \frac{-20}{2(-5)} = \frac{-20}{-10} = 2$ seconds.
Max height $h(2) = -5(2)^2 + 20(2) + 0.8$
$h(2) = -5(4) + 40 + 0.8 = -20 + 40 + 0.8 = 20.8$
**Answer:** 20.8 meters

**(c) When will it hit the ground?**
Solve $h(t) = 0$:
$-5t^2 + 20t + 0.8 = 0$
Quadratic formula:
$t = \frac{-20 \pm \sqrt{20^2 - 4(-5)(0.8)}}{2(-5)}$
$t = \frac{-20 \pm \sqrt{400 + 16}}{-10} = \frac{-20 \pm \sqrt{416}}{-10}$
$\sqrt{416} \approx 20.396$

$t_1 = \frac{-20 + 20.396}{-10} \approx \frac{0.396}{-10} \approx -0.04$ (reject negative time)
$t_2 = \frac{-20 - 20.396}{-10} \approx \frac{-40.396}{-10} \approx 4.04$
**Answer:** At approximately 4.04 seconds.

**(d) When does height = 4 meters?**
Solve $h(t) = 4$:
$-5t^2 + 20t + 0.8 = 4$
$-5t^2 + 20t - 3.2 = 0$

Quadratic formula:
$t = \frac{-20 \pm \sqrt{20^2 - 4(-5)(-3.2)}}{2(-5)}$
$\Delta = 400 - 64 = 336$
$t = \frac{-20 \pm \sqrt{336}}{-10}$
$\sqrt{336} \approx 18.33$

$t_1 = \frac{-20 + 18.33}{-10} = \frac{-1.67}{-10} = 0.167$
$t_2 = \frac{-20 - 18.33}{-10} = \frac{-38.33}{-10} = 3.833$

**Answer:** At approx 0.17 seconds (going up) and 3.83 seconds (coming down).
