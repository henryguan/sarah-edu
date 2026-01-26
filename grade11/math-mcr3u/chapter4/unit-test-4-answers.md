# Answers to Unit Test 4: Exponential Functions

Here are the step-by-step solutions, explained simply!

---

## 1. Simplify

### c) $\left(\frac{3 x^{2}}{y^{-3}}\right)^{-5}$

**Step 1: The "Shower" Rule**
Imagine the exponent $-5$ outside the brackets is like water from a shower. It has to sprinkle onto *everything* inside the house (the brackets).
$\rightarrow$ The $3$ gets a $-5$.
$\rightarrow$ The $x^2$ gets a $-5$.
$\rightarrow$ The $y^{-3}$ gets a $-5$.

**Step 2: Multiply the Exponents**
When an exponent meets another exponent across a bracket (like $(x^2)^{-5}$), they multiply.
*   For x: $2 \times -5 = -10$
*   For y: $-3 \times -5 = +15$ (Two negatives make a positive!)

So now we have:
$$ \frac{3^{-5} x^{-10}}{y^{15}} $$

**Step 3: Fix the Negative Exponents**
Negative exponents are like unhappy people. To make them happy (positive), you have to move them to the other floor.
*   $3^{-5}$ is unhappy upstairs, so move it downstairs: $3^5$.
*   $x^{-10}$ is unhappy upstairs, so move it downstairs: $x^{10}$.
*   $y^{15}$ is already happy (+15) downstairs, so it stays there.

**Final Answer:**
$$ \frac{1}{3^5 x^{10} y^{15}} $$
*(Note: $3^5 = 243$)*
$$ \frac{1}{243 x^{10} y^{15}} $$

### d) $\left[\left(2 x^{2}\right)^{-2}\right]^{-3}$

**Step 1: Simplify the Outside First**
We have a $-3$ outside and a $-2$ inside. Let's combine them first by multiplying.
$-2 \times -3 = 6$.
So the problem becomes just: $(2 x^2)^6$

**Step 2: Share the Power**
Give the power of 6 to everyone inside.
*   The number $2$ gets the power of 6 $\rightarrow 2^6$.
*   The $x^2$ gets the power of 6 $\rightarrow (x^2)^6$.

**Step 3: Calculate**
*   $2^6 = 64$
*   $x^{2 \times 6} = x^{12}$

**Final Answer:**
$$ 64x^{12} $$

---

## 2. Function Properties

Equation: $y = 2\left(3^{-\frac{1}{2}(x-2)}\right)-4$

**i) Base Function**
Strip away all the extra numbers and shifts. What is the core engine? It is the base number with an exponent.
**Answer:** $f(x) = 3^x$

**ii) Asymptote**
Exponential functions normally flatten out at $y=0$ (the floor). But look at the $-4$ at the very end. That pulls the whole building down 4 floors.
**Answer:** $y = -4$

**iii) Y-intercept**
The y-intercept is where the graph crosses the vertical line. This happens when $x$ is 0.
Let's plug in 0 for $x$:
1.  Look at the exponent: $-\frac{1}{2}(0 - 2) = -\frac{1}{2}(-2) = 1$.
2.  So we have $3^1$, which is just 3.
3.  Multiply by the front number 2: $2 \times 3 = 6$.
4.  Subtract 4: $6 - 4 = 2$.
**Answer:** $(0, 2)$

**iv) Transformation Form**
We just need to match the parts to the template $y=a \cdot f(b(x-c))+d$.
*   $a = 2$ (Vertical stretch)
*   $b = -1/2$ (Horizontal reflection and stretch)
*   $c = 2$ (Shift right 2)
*   $d = -4$ (Shift down 4)

**Answer:** $y = 2 f(-0.5(x-2)) - 4$

---

## 3. Graphing

**The Mapping Formula (Pointwise)**
We take points $(x, y)$ from the simple parent function $y=3^x$ and transform them.
**New x:** Divide old x by $b$, then add $c$. $\rightarrow \frac{x}{-0.5} + 2 \rightarrow -2x + 2$
**New y:** Multiply old y by $a$, then add $d$. $\rightarrow 2y - 4$

**Let's transform 3 key points:**

1.  **Point (-1, 1/3)**
    *   New x: $-2(-1) + 2 = 4$
    *   New y: $2(1/3) - 4 = -3.33$
    *   **Plot:** $(4, -3.33)$

2.  **Point (0, 1)**
    *   New x: $-2(0) + 2 = 2$
    *   New y: $2(1) - 4 = -2$
    *   **Plot:** $(2, -2)$

3.  **Point (1, 3)**
    *   New x: $-2(1) + 2 = 0$
    *   New y: $2(3) - 4 = 2$
    *   **Plot:** $(0, 2)$ (The y-intercept!)

**Don't forget the Asymptote:** Draw a dashed line at $y = -4$. The curve will get closer and closer to this line but never touch it.

---

## 4. Computer Value Application

Model: $V(m)=1500(0.95)^{m}$

**(a) Initial Value**
"Initial" means at the very start, when time is zero ($m=0$).
Anything to the power of 0 is 1.
So, $1500 \times 1 = 1500$.
**Answer:** The computer cost **$1500**.

**(b) Rate of Depreciation**
Look at the multiplier $0.95$.
This means every month, the computer keeps 95% of its value.
If it keeps 95%, how much did it lose?
$100\% - 95\% = 5\%$.
**Answer:** It loses **5%** value per month.

**(c) Value after 2 years**
Be careful with units! The formula uses months ($m$), but the question says 2 *years*.
2 years = 24 months.
Plug 24 into the machine:
$V = 1500(0.95)^{24}$
Using a calculator: $0.95^{24} \approx 0.292$
$1500 \times 0.292 \approx 438$.
**Answer:** The value is approximately **$438.00**.

**(d) When does it fall below $900?**
We need to find when the value hits 900.
$1500(0.95)^m = 900$
1.  Divide by 1500: $0.95^m = 0.6$
2.  Use "Trial and Error" or Logarithms.
    *   Try $m=9$: $1500(0.95)^9 \approx \$945$ (Still too high)
    *   Try $m=10$: $1500(0.95)^{10} \approx \$898$ (Dropped below!)

Since it drops below 900 between month 9 and month 10, it happens **during the 10th month**.
**Answer:** In the **10th month**.
