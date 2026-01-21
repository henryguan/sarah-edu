**Transformation Mapping**

---

# Comprehensive Guide to Transformation Mapping

**Applicable to Ontario Curriculum (MCR3U / MHF4U)**

## 1. The General Theory
Any parent function $f(x)$ can be transformed using the general equation:
$$y = a f [k (x - d)] + c$$

**The Pointwise Mapping Formula**

To find the new coordinates of any point from the parent function, apply the following rule:
$$(x, y) \rightarrow \left( \frac{x}{k} + d, \text{ } ay + c \right)$$

### Parameter Breakdown

| Parameter | Transformation Type | Mathematical Action |
| :--- | :--- | :--- |
| $a$ | Vertical Stretch / Compression / Reflection | Multiply $y$ by $a$ |
| $k$ | Horizontal Stretch / Compression / Reflection | Divide $x$ by $k$ |
| $d$ | Horizontal Translation (Phase Shift) | Add $d$ to $x$ |
| $c$ | Vertical Translation | Add $c$ to $y$ |

---

## 2. Quadratic Functions

**Parent Function:**  $f(x) = x^2$

**Key Points:** $(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)$

### Example: $y = -2(x + 4)^2 - 3$

* **Identify:**  $a = -2, k = 1, d = -4, c = -3$
* **Mapping Rule:**  $(x, y) \rightarrow (x - 4, -2y - 3)$

| Parent Point | Calculation | Transformed Point |
| :--- | :--- | :--- |
| $(0, 0)$ | $(0-4, -2(0)-3)$ | $(-4, -3)$ (Vertex) |
| $(1, 1)$ | $(1-4, -2(1)-3)$ | $(-3, -5)$ |
| $(2, 4)$ | $(2-4, -2(4)-3)$ | $(-2, -11)$ |

---

## 3. Exponential Functions

**Parent Function:**   $f(x) = b^x$ (e.g., $2^x$)

**Key Points:** $(-1, 0.5), (0, 1), (1, 2)$

**Horizontal Asymptote (HA):** $y = 0$

### Example:   $y = 3(2)^{2x} + 1$

* **Identify:** $a = 3, k = 2, d = 0, c = 1$
* **Mapping Rule:**  $(x, y) \rightarrow (\frac{x}{2}, 3y + 1)$
* **New Asymptote:** $y = c \rightarrow \mathbf{y = 1}$

| Parent Point | Calculation | Transformed Point |
| :--- | :--- | :--- |
| $(0, 1)$ | $(0/2, 3(1)+1)$ | $(0, 4)$ ($y$-intercept) |
| $(1, 2)$ | $(1/2, 3(2)+1)$ | $(0.5, 7)$ |

---

## 4. Trigonometric Functions

**Parent Function:** $f(x) = \cos(x)$

**Key Points:** $(0^\circ, 1), (90^\circ, 0), (180^\circ, -1), (270^\circ, 0), (360^\circ, 1)$

### Example: 

* **Identify:** $y = 0.5 \cos[3(x - 60^\circ)] + 2$
* **Mapping Rule:** $(x, y) \rightarrow (\frac{x}{3} + 60^\circ, 0.5y + 2)$

| Parent Point | Calculation | Transformed Point |
| :--- | :--- | :--- |
| $(0^\circ, 1)$ | $(0/3+60, 0.5(1)+2)$ | $(60^\circ, 2.5)$ (Max) |
| $(90^\circ, 0)$ | $(90/3+60, 0.5(0)+2)$ | $(90^\circ, 2)$ (Midline) |
| $(180^\circ, -1)$ | $(180/3+60, 0.5(-1)+2)$ | $(120^\circ, 1.5)$ (Min) |

---

## 5. Critical Pro-Tips

1. **Always Factor :** If the equation looks like , you **must** rewrite it as  before identifying .
2. **Order of Operations:** The mapping formula automatically handles the correct order (Stretches/Reflections before Translations).
3. **The -Logic:** Remember that  and  always perform the **inverse** operation of what is written in the bracket. If it says , you add . If it says , you divide by .

---