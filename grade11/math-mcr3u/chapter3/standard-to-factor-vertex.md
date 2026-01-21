# Converting Quadratic Forms

## 1. Standard Form to Factored Form ($y = a(x-r)(x-s)$)

**Purpose:** To find the x-intercepts (roots/zeros) of the function.
**Method:** Factoring

To convert, you need to factor the quadratic expression. The method depends on the $a$ value.

### Simple Trinomial ($a = 1$):
*   Find two numbers that multiply to $c$ and add to $b$.
*   **Example:** $y = x^2 + 5x + 6$
*   Numbers that multiply to 6 and add to 5 are 2 and 3.
*   **Factored Form:** $y = (x + 2)(x + 3)$

### Complex Trinomial ($a \neq 1$):
*   Use decomposition or "slip and slide." Find two numbers that multiply to $(a \times c)$ and add to $b$.
*   **Example:** $y = 2x^2 + 7x + 3$
*   Multiply to 6 ($2 \times 3$) and add to 7 $\rightarrow$ 6 and 1.
*   $$y = 2x^2 + 6x + 1x + 3 \rightarrow 2x(x+3) + 1(x+3)$$
*   **Factored Form:** $y = (2x + 1)(x + 3)$

## 2. Standard Form to Vertex Form ($y = a(x-h)^2 + k$)

**Purpose:** To find the vertex $(h, k)$ and the maximum or minimum value.
**Method:** Completing the Square

This is a specific algebraic procedure used to create a perfect square trinomial.

**Steps:**
1.  Group the first two terms and factor out the '$a$' value.
2.  Calculate the magic number: take the new coefficient of $x$, divide by 2, and square it $[(b/2a)^2]$.
3.  Add and subtract that number inside the brackets.
4.  Move the subtracted number outside the brackets (remember to multiply it by '$a$' on the way out).
5.  Factor the perfect square trinomial inside the brackets.

**Example:** $y = 2x^2 - 12x + 7$
$$y = 2(x^2 - 6x) + 7$$
Magic number: $(-6/2)^2 = 9$
$$y = 2(x^2 - 6x + 9 - 9) + 7$$
$$y = 2(x^2 - 6x + 9) - 18 + 7$$
**Vertex Form:** $y = 2(x - 3)^2 - 11$
(The vertex is $(3, -11)$)

## Summary Table: What each form tells you

| Form | Equation | Key Information |
| :--- | :--- | :--- |
| Standard | $y = ax^2 + bx + c$ | $c$ is the y-intercept. |
| Factored | $y = a(x - r)(x - s)$ | $r$ and $s$ are the x-intercepts. |
| Vertex | $y = a(x - h)^2 + k$ | $(h, k)$ is the vertex. |

> **Pro-Tip:** The '$a$' value is the same in all three forms. If $a$ is positive, the parabola opens up; if it is negative, it opens down. If you convert and your '$a$' value changes, you've made an algebraic error!