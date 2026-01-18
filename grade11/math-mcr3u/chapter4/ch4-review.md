Based on **Chapter 4 (Exponential Functions)** from your textbook, I have created a comprehensive review guide to help you prepare for your unit test.

This guide breaks down the chapter into its core concepts, formulas, and the specific skills you need to master.

---

### **1. Exponent Laws (Sections 4.2 & 4.3)**
Before tackling functions, you must master the mechanics of exponents.

**The Basics:**
*   **Product Rule:** $x^a \cdot x^b = x^{a+b}$
*   **Quotient Rule:** $\frac{x^a}{x^b} = x^{a-b}$
*   **Power of a Power:** $(x^a)^b = x^{a \cdot b}$

**The "Tricky" Ones (Need to Know):**
*   **Zero Exponent:** $x^0 = 1$ (provided $x \neq 0$).
*   **Negative Exponent:** $x^{-n} = \frac{1}{x^n}$.
    *   *Tip:* If you have a fraction, flip it: $(\frac{a}{b})^{-n} = (\frac{b}{a})^n$.
*   **Rational (Fraction) Exponents:**
    *   $x^{\frac{1}{n}} = \sqrt[n]{x}$
    *   $x^{\frac{m}{n}} = (\sqrt[n]{x})^m$ or $\sqrt[n]{x^m}$
    *   *Memory Aid:* Flower Power — The **roots** are at the bottom (denominator), the **power** is at the top (numerator).

**Common Test Task:**
*   Simplify an algebraic expression containing radicals and negative exponents and express the final answer with **positive exponents**.

---

### **2. Characteristics of Exponential Functions (Section 4.5)**
You need to recognize what an exponential function looks like in an equation, a table, and a graph.

**The Parent Function:** $f(x) = b^x$
*   **Base ($b$):** Must be positive ($b > 0$) and not equal to 1.
*   **Domain:** $\{x \in \mathbb{R}\}$ (All real numbers).
*   **Range:** $\{y \in \mathbb{R} \mid y > 0\}$ (y is always positive, never touches 0).
*   **Asymptote:** There is a horizontal asymptote at **$y = 0$** (the x-axis).
*   **Y-Intercept:** Always **$(0, 1)$** because $b^0 = 1$.

**Growth vs. Decay:**
*   **Exponential Growth:** $b > 1$ (Graph goes up to the right).
*   **Exponential Decay:** $0 < b < 1$ (Graph goes down to the right).

**Recognizing Data (Table of Values):**
*   **Linear:** First differences are constant (add/subtract same amount).
*   **Quadratic:** Second differences are constant.
*   **Exponential:** The **ratio** of consecutive y-values is constant (you multiply by the same number to get the next term).

---

### **3. Transformations (Section 4.6)**
You must be able to graph and analyze the transformed equation:
$$g(x) = a(b)^{k(x-d)} + c$$

**What each letter does:**
*   **$c$ (Vertical Translation):** Moves the graph Up/Down.
    *   *Crucial:* This determines your **Horizontal Asymptote**. The new asymptote is **$y = c$**.
*   **$d$ (Horizontal Translation):** Moves the graph Left/Right.
    *   Remember to flip the sign: $(x - 3)$ moves Right 3; $(x + 3)$ moves Left 3.
*   **$a$ (Vertical Stretch/Reflection):**
    *   If $a < 0$: Reflection in the **x-axis**.
    *   $|a| > 1$: Vertical Stretch.
    *   $0 < |a| < 1$: Vertical Compression.
*   **$k$ (Horizontal Stretch/Reflection):**
    *   If $k < 0$: Reflection in the **y-axis**.
    *   Note: The factor is $\frac{1}{k}$. (e.g., if $k=2$, it is a horizontal compression by $\frac{1}{2}$).

**Test Task:**
*   Given an equation like $y = -2(3)^{x+1} + 4$, state the domain, range, asymptote, and sketch the graph.
    *   *Asymptote:* $y = 4$
    *   *Range:* $y < 4$ (because of the negative '$a$' reflection).

---

### **4. Real-World Applications (Section 4.7)**
Word problems usually fall into two categories: Growth or Decay.

**The General Formula:**
$$A(t) = A_0 (b)^{\frac{t}{P}}$$
*   **$A(t)$:** Final amount.
*   **$A_0$:** Initial amount (at $t=0$).
*   **$b$:** Growth/Decay factor.
*   **$t$:** Total time elapsed.
*   **$P$:** The period (how long it takes for the growth/decay to happen once).

**Scenario 1: Doubling or Half-Life**
*   **Doubling:** $A(t) = A_0 (2)^{\frac{t}{d}}$ (where $d$ is doubling time).
*   **Half-Life:** $A(t) = A_0 (\frac{1}{2})^{\frac{t}{h}}$ (where $h$ is half-life).

**Scenario 2: Percentage Growth/Decay**
*   **Growth:** $b = 1 + r$ (e.g., grows by 5% $\rightarrow b = 1.05$).
*   **Decay:** $b = 1 - r$ (e.g., depreciates by 12% $\rightarrow b = 0.88$).
*   **Formula:** $A(t) = A_0 (1 \pm r)^n$

**Test Task:**
*   "A bacteria culture starts with 500 cells and doubles every 3 hours. How many are there after 10 hours?"
    *   $y = 500(2)^{\frac{10}{3}}$

---

### **Study Checklist: Can you...?**
1.  [ ] Evaluate $27^{-2/3}$ without a calculator? (Answer: $1/9$)
2.  [ ] Simplify $\frac{(2x^3y^{-2})^2}{8x^{-1}y^3}$?
3.  [ ] Sketch $y = 3^x$ and $y = (\frac{1}{3})^x$ on the same grid?
4.  [ ] Identify the asymptote and range of $y = 5(2)^x - 3$? (Asymptote: $y=-3$, Range: $y > -3$)
5.  [ ] Solve for $x$ if $2^x = 32$ and if $9^{x+1} = 27^{2x}$? (Common base method).
6.  [ ] Write an equation for a car purchased for $\$20,000$ that loses $15\%$ of its value every year? ($V = 20000(0.85)^t$).

**Common Pitfall to Avoid:**
*   **Order of Operations:** In $y = -2(3)^x$, do **NOT** multiply $-2 \times 3$ to get $(-6)^x$. The exponent applies *only* to the base (3). The $-2$ is a vertical stretch applied *after* the exponent.