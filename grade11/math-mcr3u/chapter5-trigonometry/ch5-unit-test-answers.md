# 3U Trigonometry Test 1 - Answers & Solutions

---

## 1. Solve for all of the unknowns in the following right triangle.
*(Assumed: A right triangle where one acute angle is $29^\circ$, and the adjacent side (let's say $b$) is 37 units (or hypotenuse? Based on student working $z = 37/\sin(61)$, $z$ is Hypotenuse. If $z$ is hyp, then side 37 is opposite angle 61. Angle 61 is $B$. So $b=37$ is opposite $B$. $A=29$ is opposite $a$.)*

**Given:**
*   Right Triangle ($C=90^\circ$)
*   Angle $A = 29^\circ$
*   Side adjacent to A (or opposite B) = 37.

**Step 1: Find Missing Angle ($\beta$)**
The sum of angles in a triangle is $180^\circ$.
$$ \beta = 180^\circ - 90^\circ - 29^\circ = 61^\circ $$

**Step 2: Find Hypotenuse ($z$)**
Using Sine Law or SOH CAH TOA:
$$ \sin(61^\circ) = \frac{\text{Opposite}}{\text{Hypotenuse}} = \frac{37}{z} $$
$$ z = \frac{37}{\sin(61^\circ)} $$
$$ z \approx \frac{37}{0.8746} $$
$$ z \approx 42.3 $$
*(Note: Student answer 42.53 suggests they might have used $\cos(29)$ or similar with rounding diff, or original diagram labeled 37 differently. If 37 was adjacent to 29, $z = 37/\cos(29) \approx 42.3$ as well.)*

**Step 3: Find Remaining Side ($y$)**
Using Tangent:
$$ \tan(29^\circ) = \frac{y}{37} $$
$$ y = 37 \cdot \tan(29^\circ) $$
$$ y = 37 \cdot 0.5543 $$
$$ y \approx 20.5 $$

**Answers:**
*   $\beta = 61^\circ$
*   $y \approx 20.5$ (Student got 20.6)
*   $z \approx 42.3$ (Student got 42.53)

---

## 2. In $\Delta ABC$, sides $a = 26$ cm, $b = 63$ cm, and $c = 44$ cm. Determine all angles to 1 decimal place.

**Step 1: Find the largest angle first (Angle B, opposite side b=63) given SSS.**
Using Cosine Law: $b^2 = a^2 + c^2 - 2ac \cos B$
$$ 63^2 = 26^2 + 44^2 - 2(26)(44) \cos B $$
$$ 3969 = 676 + 1936 - 2288 \cos B $$
$$ 3969 = 2612 - 2288 \cos B $$
$$ 1357 = -2288 \cos B $$
$$ \cos B = -\frac{1357}{2288} \approx -0.5931 $$
$$ B = \cos^{-1}(-0.5931) \approx 126.4^\circ $$

**Step 2: Find Angle A using Sine Law**
$$ \frac{\sin A}{a} = \frac{\sin B}{b} $$
$$ \sin A = \frac{26 \cdot \sin(126.4^\circ)}{63} $$
$$ \sin A = \frac{26 \cdot 0.8049}{63} \approx 0.3323 $$
$$ A = \sin^{-1}(0.3323) \approx 19.4^\circ $$

**Step 3: Find Angle C**
$$ C = 180^\circ - (126.4^\circ + 19.4^\circ) $$
$$ C = 180^\circ - 145.8^\circ = 34.2^\circ $$

**Answers:**
*   $A = 19.4^\circ$
*   $B = 126.4^\circ$
*   $C = 34.2^\circ$

---

## 3. Determine all lengths and angles in $\Delta ABC$ where angle B is obtuse and $\angle A = 34^\circ$, $b = 5$ cm, $a = 4$ cm.

**Step 1: Check for Ambiguous Case (SSA)**
Height $h = b \sin A = 5 \sin(34^\circ) \approx 2.8$.
Since $h < a < b$ ($2.8 < 4 < 5$), there are two possible triangles (Acute B and Obtuse B).
Problem states **B is obtuse**.

**Step 2: Find Angle B**
Using Sine Law:
$$ \frac{\sin B}{5} = \frac{\sin 34^\circ}{4} $$
$$ \sin B = \frac{5 \sin 34^\circ}{4} \approx 0.699 $$
$$ B_{ref} = \sin^{-1}(0.699) \approx 44.3^\circ $$
Since B is obtuse:
$$ B = 180^\circ - 44.3^\circ = 135.7^\circ $$

**Step 3: Find Angle C**
$$ C = 180^\circ - (34^\circ + 135.7^\circ) $$
$$ C = 180^\circ - 169.7^\circ = 10.3^\circ $$

**Step 4: Find side c**
$$ \frac{c}{\sin 10.3^\circ} = \frac{4}{\sin 34^\circ} $$
$$ c = \frac{4 \sin 10.3^\circ}{\sin 34^\circ} \approx \frac{4(0.1788)}{0.559} \approx 1.3 \text{ cm} $$

**Answers:**
*   $B = 135.7^\circ$
*   $C = 10.3^\circ$
*   $c = 1.3$ cm

---

## 4. Determine x (and involved steps).

**Reconstructed Solution based on student work:**
The problem likely involves two triangles linked together.
**Step 1:** Calculate a missing side or angle.
Student used Cosine Law or similar to find a value $C \approx 21.83$. Assuming this is an angle based on later usage inside $\sin()$.

**Step 2:** Solve for $x$.
$$ \frac{x}{\sin 122^\circ} = \frac{25}{\sin 21.83^\circ} $$
$$ x = \frac{25 \sin 122^\circ}{\sin 21.83^\circ} $$
$$ x = \frac{25 (0.848)}{0.372} $$
$$ x \approx 57.0 $$
(Student answer 57.3 is reasonably close, likely due to intermediate rounding differences).

---

## 5. Point P(-3, -6)

**(a) Diagram**
*   Point P is in Quadrant 3 (both x and y are negative).
*   Triangle drawn to x-axis.

**(b) Exact Values**
$$ x = -3, y = -6 $$
$$ r = \sqrt{x^2 + y^2} = \sqrt{(-3)^2 + (-6)^2} = \sqrt{9 + 36} = \sqrt{45} = 3\sqrt{5} $$

Trig Ratios:
$$ \sin \theta = \frac{y}{r} = \frac{-6}{3\sqrt{5}} = \frac{-2}{\sqrt{5}} $$
$$ \cos \theta = \frac{x}{r} = \frac{-3}{3\sqrt{5}} = \frac{-1}{\sqrt{5}} $$
$$ \tan \theta = \frac{y}{x} = \frac{-6}{-3} = 2 $$

**(c) Angles**
Related Acute Angle $\alpha$:
$$ \tan \alpha = |2| \implies \alpha = \tan^{-1}(2) \approx 63.4^\circ $$
Principal Angle $\theta$ (Quadrant 3):
$$ \theta = 180^\circ + \alpha = 180^\circ + 63.4^\circ = 243.4^\circ $$

---

## 6. Determine exact value of $\sec(210^\circ)$

1.  **Quadrant:** $210^\circ$ is in Quadrant 3.
2.  **Related Acute Angle:** $210^\circ - 180^\circ = 30^\circ$.
3.  **Special Triangle:** 30-60-90.
    *   Sides for $30^\circ$: Opp = 1, Adj = $\sqrt{3}$, Hyp = 2.
    *   In Q3: $x = -\sqrt{3}, y = -1, r = 2$.
4.  **Secant Ratio:**
    $$ \sec \theta = \frac{r}{x} $$
    $$ \sec(210^\circ) = \frac{2}{-\sqrt{3}} = -\frac{2}{\sqrt{3}} $$

---

## 7. For $\cos(A) = -2/3$, $0^\circ \leq A \leq 360^\circ$

**(i) Sketch**
Cosine is negative in Quadrants 2 and 3. There are two terminal arms.

**(ii) Determine $\tan(A)$**
Given $x = -2, r = 3$. Find $y$.
$$ x^2 + y^2 = r^2 $$
$$ (-2)^2 + y^2 = 3^2 $$
$$ 4 + y^2 = 9 $$
$$ y^2 = 5 \implies y = \pm\sqrt{5} $$

*   **Quadrant 2 ($y$ is pos):** $\tan A = \frac{\sqrt{5}}{-2} = -\frac{\sqrt{5}}{2}$
*   **Quadrant 3 ($y$ is neg):** $\tan A = \frac{-\sqrt{5}}{-2} = \frac{\sqrt{5}}{2}$

**(iii) Angles**
$$ \alpha = \cos^{-1}(2/3) \approx 48.2^\circ $$
*   Q2: $A = 180^\circ - 48.2^\circ = 131.8^\circ$
*   Q3: $A = 180^\circ + 48.2^\circ = 228.2^\circ$

---

# Part 2: Proofs

## (a) Prove $\frac{1 - \sin x}{\cos x} = \frac{\cos x}{1 + \sin x}$

**Strategy: Multiply LS by conjugate $(1+\sin x)$**
$$ LS = \frac{1 - \sin x}{\cos x} \cdot \frac{1 + \sin x}{1 + \sin x} $$
$$ LS = \frac{1 - \sin^2 x}{\cos x(1 + \sin x)} $$
$$ \text{Identity: } 1 - \sin^2 x = \cos^2 x $$
$$ LS = \frac{\cos^2 x}{\cos x(1 + \sin x)} $$
$$ LS = \frac{\cos x}{1 + \sin x} $$
$$ LS = RS \quad \blacksquare $$

## (b) Prove $\tan x + \frac{\cos x}{1 + \sin x} = \frac{1}{\cos x}$

**Strategy: Convert tan to sin/cos and find common denominator**
$$ LS = \frac{\sin x}{\cos x} + \frac{\cos x}{1 + \sin x} $$
$$ LS = \frac{\sin x(1 + \sin x) + \cos x(\cos x)}{\cos x(1 + \sin x)} $$
$$ LS = \frac{\sin x + \sin^2 x + \cos^2 x}{\cos x(1 + \sin x)} $$
$$ \text{Identity: } \sin^2 x + \cos^2 x = 1 $$
$$ LS = \frac{\sin x + 1}{\cos x(1 + \sin x)} $$
$$ LS = \frac{(1 + \sin x)}{\cos x(1 + \sin x)} $$
$$ LS = \frac{1}{\cos x} $$
$$ LS = RS \quad \blacksquare $$
