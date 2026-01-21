That's a great idea! Learning the common LaTeX expressions is essential for writing math digitally. For high school math, you'll mostly need standard arithmetic, algebra, geometry, and calculus symbols.

Here is a table of common inline LaTeX expressions, along with their output, specifically tailored for high school topics. Remember that these expressions are typically enclosed in dollar signs, like `$\text{expression}$`, for inline display.

## 📐 Common High School Inline LaTeX Expressions

| Category | Description | LaTeX Code | Rendered Output (Inline) |
| :--- | :--- | :--- | :--- |
| **Basic Arithmetic** | Multiplication | `a \times b` | $a \times b$ |
| | Division (Fraction) | `\frac{a}{b}` or `a/b` | $\frac{a}{b}$ or $a/b$ |
| | Plus/Minus | `\pm` | $\pm$ |
| **Exponents/Indices** | Squared/Cubed/General | `x^2`, `y^3`, `z^{a+b}` | $x^2$, $y^3$, $z^{a+b}$ |
| **Roots** | Square Root | `\sqrt{x}` | $\sqrt{x}$ |
| | N-th Root | `\sqrt[n]{x}` | $\sqrt[n]{x}$ |
| **Sets & Logic** | Element of | `x \in A` | $x \in A$ |
| | Not equal to | `a \neq b` | $a \neq b$ |
| | Less than or equal to | `\leq` | $\leq$ |
| | Greater than or equal to | `\geq` | $\geq$ |
| **Geometry** | Angle measurement | `\angle ABC` | $\angle ABC$ |
| | Pi constant | `\pi` | $\pi$ |
| | Degree symbol | `90^\circ` | $90^\circ$ |
| | Parallel | `AB \parallel CD` | $AB \parallel CD$ |
| | Perpendicular | `AB \perp CD` | $AB \perp CD$ |
| **Algebra & Functions**| Absolute value | `|x|` | $|x|$ |
| | Piecewise function | `f(x) = \begin{cases} a & \text{if } x < 0 \\ b & \text{if } x \geq 0 \end{cases}` | $f(x) = \begin{cases} a & \text{if } x < 0 \\ b & \text{if } x \geq 0 \end{cases}$ |
| | Subscripts (for sequences) | `a_n` | $a_n$ |
| **Trigonometry** | Sine function | `\sin(\theta)` | $\sin(\theta)$ |
| | Cosine function | `\cos(\theta)` | $\cos(\theta)$ |
| | Tangent function | `\tan(\theta)` | $\tan(\theta)$ |
| **Calculus (Advanced High School)** | Limit | `\lim_{x \to 0}` | $\lim_{x \to 0}$ |
| | Derivative (prime notation) | `f'(x)` | $f'(x)$ |
| | First derivative (Leibniz) | `\frac{dy}{dx}` | $\frac{dy}{dx}$ |
| | Integral | `\int f(x) \, dx` | $\int f(x) \, dx$ |
| | Summation | `\sum_{i=1}^n` | $\sum_{i=1}^n$ |

### 📝 Key Tips for Inline Math

1.  **Use `{}` for Grouping:** Always use curly braces (`{}`) for exponents, subscripts, or expressions that contain more than one character.
    * **Good:** `x^{2y+1}` $\to x^{2y+1}$
    * **Bad:** `x^2y+1` $\to x^2y+1$
2.  **Special Functions:** Mathematical functions like $\sin$, $\cos$, $\log$, $\exp$, etc., should be prefixed with a backslash (`\`) to render them in the correct upright font (not italics).
    * **Good:** `\log(x)` $\to \log(x)$
    * **Bad:** `log(x)` $\to log(x)$
3.  **Plain Text:** If you need to include regular text *within* a math environment (e.g., in a piecewise function or formula description), use `\text{...}`.
    * Example: `x=0 \text{ is the solution}` $\to x=0 \text{ is the solution}$

Would you like to see how to write a full equation, like the **Quadratic Formula**, using display-style LaTeX?


`y=2*3^{-2(x+1)}-3`

$y=2*3^{-2(x+1)}-3$