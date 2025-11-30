

## 📝 Unit Test Study Guide: Trigonometric Ratios

### 1. Algebraic Tools for Proofs
To prove trigonometric identities effectively, you often need to use standard algebraic expansions and factoring. These patterns allow you to substitute trigonometric ratios (like $\sin \theta$ or $\cos \theta$) into algebraic forms.

| Concept | Formula | Trigonometry Example |
| :--- | :--- | :--- |
| **Difference of Squares** | $a^2 - b^2 = (a+b)(a-b)$ | $\sin^2 x - \cos^2 x = (\sin x + \cos x)(\sin x - \cos x)$ |
| **Perfect Square (Addition)** | $(a+b)^2 = a^2 + 2ab + b^2$ | $(\sin x + 1)^2 = \sin^2 x + 2\sin x + 1$ |
| **Perfect Square (Subtraction)**| $(a-b)^2 = a^2 - 2ab + b^2$ | $(\tan x - 1)^2 = \tan^2 x - 2\tan x + 1$ |

***

### 2. Primary and Reciprocal Ratios (Right Triangles)

[cite_start]The reciprocal trigonometric ratios are defined as 1 divided by each of the primary trigonometric ratios[cite: 256].

| Ratio Name | Abbreviation | Definition | Relationship |
| :--- | :--- | :--- | :--- |
| **Sine** | $\sin~\theta$ | $\frac{\text{opposite}}{\text{hypotenuse}}$ | [cite_start]Primary Ratio [cite: 193] |
| **Cosine** | $\cos~\theta$ | $\frac{\text{adjacent}}{\text{hypotenuse}}$ | [cite_start]Primary Ratio [cite: 193] |
| **Tangent** | $\tan~\theta$ | $\frac{\text{opposite}}{\text{adjacent}}$ | [cite_start]Primary Ratio [cite: 193] |
| **Cosecant** | $\csc~\theta$ | $\frac{\text{hypotenuse}}{\text{opposite}}$ | [cite_start]$\csc~\theta = \frac{1}{\sin~\theta}$ [cite: 257] |
| **Secant** | $\sec~\theta$ | $\frac{\text{hypotenuse}}{\text{adjacent}}$ | [cite_start]$\sec~\theta = \frac{1}{\cos~\theta}$ [cite: 257] |
| **Cotangent** | $\cot~\theta$ | $\frac{\text{adjacent}}{\text{opposite}}$ | [cite_start]$\cot~\theta = \frac{1}{\tan~\theta}$ [cite: 257] |

#### Important Notes for Right Triangles:
* **Calculators:** Most calculators do not have buttons for $\csc, \sec, \cot$. [cite_start]To evaluate them, use the reciprocal of the primary ratio (e.g., for $\sec~20^{\circ}$, calculate $1 \div \cos~20^{\circ}$)[cite: 260].
* [cite_start]**Inverse Functions:** Use $\sin^{-1}$, $\cos^{-1}$, and $\tan^{-1}$ to determine the angle associated with a specific ratio[cite: 250].

***

### 3. Trigonometric Identities

[cite_start]A trigonometric identity is an equation involving trigonometric ratios that is true for all values of the variable[cite: 667].

#### [cite_start]A. Quotient Identities [cite: 669]
* $\tan~\theta = \frac{\sin~\theta}{\cos~\theta}$ (where $\cos~\theta \neq 0$)
* $\cot~\theta = \frac{\cos~\theta}{\sin~\theta}$ (where $\sin~\theta \neq 0$)

#### [cite_start]B. Reciprocal Identities [cite: 669]
* $\csc~\theta = \frac{1}{\sin~\theta}$ (where $\sin~\theta \neq 0$)
* $\sec~\theta = \frac{1}{\cos~\theta}$ (where $\cos~\theta \neq 0$)
* $\cot~\theta = \frac{1}{\tan~\theta}$ (where $\tan~\theta \neq 0$)

#### [cite_start]C. Pythagorean Identities [cite: 669]
* $\sin^2~\theta + \cos^2~\theta = 1$
* $1 + \tan^2~\theta = \sec^2~\theta$
* $1 + \cot^2~\theta = \csc^2~\theta$

#### [cite_start]Strategy for Proving Identities [cite: 670, 671]
1.  **Separate sides:** Work with the Left Side (L.S.) and Right Side (R.S.) independently.
2.  **Simplify:** Start with the more complicated side.
3.  **Rewrite:** Express tangent and reciprocal ratios in terms of sine and cosine.
4.  **Operations:** Use common denominators, factoring, or the Pythagorean identity to simplify expressions.

***

### 4. Solving Oblique (Non-Right) Triangles



#### [cite_start]A. The Sine Law [cite: 753]
In any triangle $\triangle ABC$, the ratios of each side to the sine of its opposite angle are equal.
$$\frac{a}{\sin~A} = \frac{b}{\sin~B} = \frac{c}{\sin~C}$$
* **When to Use:**
    * Two angles and any side (**AAS** or **ASA**).
    * Two sides and one angle opposite a given side (**SSA**).
* [cite_start]**The Ambiguous Case (SSA):** When given two sides and an angle opposite one of them (SSA), 0, 1, or 2 triangles may be possible depending on the side lengths and the angle size (acute vs. obtuse)[cite: 732, 755].

#### [cite_start]B. The Cosine Law [cite: 858]
* **To find a side (e.g., $a$):**
    $$a^2 = b^2 + c^2 - 2bc \cos~A$$
* **To find an angle (e.g., $\angle A$):**
    $$\cos~A = \frac{b^2 + c^2 - a^2}{2bc}$$
* **When to Use:**
    * Two sides and the contained angle (**SAS**).
    * All three sides (**SSS**).

#### [cite_start]Quick Selection Guide [cite: 941]
| Given Information | Law to Use |
| :--- | :--- |
| **SSA** (Side-Side-Angle) | **Sine Law** (Check for Ambiguous Case) |
| **ASA** or **AAS** (Two Angles, One Side) | **Sine Law** |
| **SAS** (Side-Angle-Side) | **Cosine Law** |
| **SSS** (Side-Side-Side) | **Cosine Law** |