
### 1. Proof of: $\tan x + \frac{\cos x}{1 + \sin x} = \frac{1}{\cos x}$

**Step 1:** Convert $\tan x$ to sine and cosine.
$$LHS = \frac{\sin x}{\cos x} + \frac{\cos x}{1 + \sin x}$$

**Step 2:** Find a common denominator, which is $\cos x(1 + \sin x)$.
$$= \frac{\sin x(1 + \sin x) + \cos x(\cos x)}{\cos x(1 + \sin x)}$$

**Step 3:** Distribute and simplify the numerator.
$$= \frac{\sin x + \sin^2 x + \cos^2 x}{\cos x(1 + \sin x)}$$

**Step 4:** Apply the Pythagorean identity $\sin^2 x + \cos^2 x = 1$.
$$= \frac{\sin x + 1}{\cos x(1 + \sin x)}$$

**Step 5:** Cancel the common term $(1 + \sin x)$.
$$= \frac{1}{\cos x}$$
**Result:** $LHS = RHS$

---

### 2. Proof of: $\tan^2 x + 1 = \sec^2 x$

**Step 1:** Convert $\tan^2 x$ to sine and cosine.
$$LHS = \frac{\sin^2 x}{\cos^2 x} + 1$$

**Step 2:** Find a common denominator.
$$= \frac{\sin^2 x + \cos^2 x}{\cos^2 x}$$

**Step 3:** Apply the Pythagorean identity $\sin^2 x + \cos^2 x = 1$.
$$= \frac{1}{\cos^2 x}$$

**Step 4:** Use the definition of secant.
$$= \sec^2 x$$
**Result:** $LHS = RHS$

---

### 3. Proof of: $\frac{1}{1 - \sin x} - \frac{1}{1 + \sin x} = 2 \tan x \sec x$

**Step 1:** Find a common denominator, which is $(1 - \sin x)(1 + \sin x) = 1 - \sin^2 x$.
$$LHS = \frac{(1 + \sin x) - (1 - \sin x)}{1 - \sin^2 x}$$

**Step 2:** Simplify the numerator and the denominator.
$$= \frac{2 \sin x}{\cos^2 x}$$

**Step 3:** Separate the fraction into factors.
$$= 2 \cdot \frac{\sin x}{\cos x} \cdot \frac{1}{\cos x}$$

**Step 4:** Convert to tan and sec.
$$= 2 \tan x \sec x$$
**Result:** $LHS = RHS$

---

### 4. Proof of: $\tan x + \cot x = \sec x \csc x$

**Step 1:** Convert to sine and cosine.
$$LHS = \frac{\sin x}{\cos x} + \frac{\cos x}{\sin x}$$

**Step 2:** Find a common denominator.
$$= \frac{\sin^2 x + \cos^2 x}{\sin x \cos x}$$

**Step 3:** Apply the Pythagorean identity.
$$= \frac{1}{\sin x \cos x}$$

**Step 4:** Separate factors.
$$= \frac{1}{\cos x} \cdot \frac{1}{\sin x} = \sec x \csc x$$
**Result:** $LHS = RHS$

---

### 5. Proof of: $\frac{1 + \tan^2 x}{1 - \tan^2 x} = \frac{1}{\cos^2 x - \sin^2 x}$

**Step 1:** Substitute $1 + \tan^2 x$ with $\sec^2 x$ (Pythagorean identity).
$$LHS = \frac{\sec^2 x}{1 - \frac{\sin^2 x}{\cos^2 x}}$$

**Step 2:** Simplify the denominator by finding a common denominator of $\cos^2 x$.
$$= \frac{\sec^2 x}{\frac{\cos^2 x - \sin^2 x}{\cos^2 x}}$$

**Step 3:** Rewrite $\sec^2 x$ as $1/\cos^2 x$.
$$= \frac{\frac{1}{\cos^2 x}}{\frac{\cos^2 x - \sin^2 x}{\cos^2 x}}$$

**Step 4:** Multiply by the reciprocal.
$$= \frac{1}{\cos^2 x} \cdot \frac{\cos^2 x}{\cos^2 x - \sin^2 x}$$

**Step 5:** Cancel $\cos^2 x$.
$$= \frac{1}{\cos^2 x - \sin^2 x}$$
**Result:** $LHS = RHS$

---

### 6. Proof of: $\tan^2 x - \sin^2 x = \tan^2 x \sin^2 x$

**Step 1:** Convert $\tan^2 x$ to sine and cosine.
$$LHS = \frac{\sin^2 x}{\cos^2 x} - \sin^2 x$$

**Step 2:** Factor out $\sin^2 x$.
$$= \sin^2 x \left(\frac{1}{\cos^2 x} - 1\right)$$

**Step 3:** Recognize that $\frac{1}{\cos^2 x} = \sec^2 x$.
$$= \sin^2 x (\sec^2 x - 1)$$

**Step 4:** Use the identity $\sec^2 x - 1 = \tan^2 x$.
$$= \sin^2 x \tan^2 x$$
**Result:** $LHS = RHS$

---

### 7. Proof of: $\frac{1 - \cos x}{\sin x} + \frac{\sin x}{1 - \cos x} = 2 \csc x$

**Step 1:** Find a common denominator $\sin x(1 - \cos x)$.
$$LHS = \frac{(1 - \cos x)^2 + \sin^2 x}{\sin x(1 - \cos x)}$$

**Step 2:** Expand the numerator.
$$= \frac{1 - 2\cos x + \cos^2 x + \sin^2 x}{\sin x(1 - \cos x)}$$

**Step 3:** Use $\cos^2 x + \sin^2 x = 1$.
$$= \frac{1 - 2\cos x + 1}{\sin x(1 - \cos x)} = \frac{2 - 2\cos x}{\sin x(1 - \cos x)}$$

**Step 4:** Factor the numerator.
$$= \frac{2(1 - \cos x)}{\sin x(1 - \cos x)}$$

**Step 5:** Cancel common terms.
$$= \frac{2}{\sin x} = 2 \csc x$$
**Result:** $LHS = RHS$

---

### 8. Proof of: $\frac{\sec x - 1}{\sec x + 1} = \frac{1 - \cos x}{1 + \cos x}$

**Step 1:** Rewrite $\sec x$ as $1/\cos x$.
$$LHS = \frac{\frac{1}{\cos x} - 1}{\frac{1}{\cos x} + 1}$$

**Step 2:** Multiply numerator and denominator by $\cos x$ to clear fractions.
$$= \frac{\cos x(\frac{1}{\cos x} - 1)}{\cos x(\frac{1}{\cos x} + 1)}$$

**Step 3:** Distribute.
$$= \frac{1 - \cos x}{1 + \cos x}$$
**Result:** $LHS = RHS$

---

### 9. Proof of: $1 + \cot^2 x = \csc^2 x$

**Step 1:** Convert $\cot^2 x$ to cosine and sine.
$$LHS = 1 + \frac{\cos^2 x}{\sin^2 x}$$

**Step 2:** Find a common denominator.
$$= \frac{\sin^2 x + \cos^2 x}{\sin^2 x}$$

**Step 3:** Apply Pythagorean identity.
$$= \frac{1}{\sin^2 x}$$

**Step 4:** Definition of cosecant.
$$= \csc^2 x$$
**Result:** $LHS = RHS$

---

### 10. Proof of: $\frac{\csc^2 x - 1}{\csc^2 x} = \cos^2 x$

**Step 1:** Use the identity $\csc^2 x - 1 = \cot^2 x$.
$$LHS = \frac{\cot^2 x}{\csc^2 x}$$

**Step 2:** Convert to sine and cosine.
$$= \frac{\frac{\cos^2 x}{\sin^2 x}}{\frac{1}{\sin^2 x}}$$

**Step 3:** Multiply by the reciprocal.
$$= \frac{\cos^2 x}{\sin^2 x} \cdot \frac{\sin^2 x}{1}$$

**Step 4:** Cancel $\sin^2 x$.
$$= \cos^2 x$$
**Result:** $LHS = RHS$

---

### 11. Proof of: $\frac{\cot x - 1}{\cot x + 1} = \frac{1 - \tan x}{1 + \tan x}$

**Step 1:** Rewrite $\cot x$ as $1/\tan x$.
$$LHS = \frac{\frac{1}{\tan x} - 1}{\frac{1}{\tan x} + 1}$$

**Step 2:** Multiply numerator and denominator by $\tan x$.
$$= \frac{\tan x(\frac{1}{\tan x} - 1)}{\tan x(\frac{1}{\tan x} + 1)}$$

**Step 3:** Distribute.
$$= \frac{1 - \tan x}{1 + \tan x}$$
**Result:** $LHS = RHS$

---

### 12. Proof of: $(\sin x + \cos x)(\tan x + \cot x) = \sec x + \csc x$

**Step 1:** Convert the second bracket to sine and cosine.
$$LHS = (\sin x + \cos x)\left(\frac{\sin x}{\cos x} + \frac{\cos x}{\sin x}\right)$$

**Step 2:** Combine fractions in the second bracket.
$$= (\sin x + \cos x)\left(\frac{\sin^2 x + \cos^2 x}{\sin x \cos x}\right)$$

**Step 3:** Simplify the numerator to 1.
$$= (\sin x + \cos x)\left(\frac{1}{\sin x \cos x}\right)$$

**Step 4:** Distribute the fraction.
$$= \frac{\sin x}{\sin x \cos x} + \frac{\cos x}{\sin x \cos x}$$

**Step 5:** Cancel terms.
$$= \frac{1}{\cos x} + \frac{1}{\sin x} = \sec x + \csc x$$
**Result:** $LHS = RHS$

---

### 13. Proof of: $\frac{\sin^3 x + \cos^3 x}{\sin x + \cos x} = 1 - \sin x \cos x$

**Step 1:** Factor the numerator as a sum of cubes ($a^3 + b^3 = (a+b)(a^2 - ab + b^2)$).
$$LHS = \frac{(\sin x + \cos x)(\sin^2 x - \sin x \cos x + \cos^2 x)}{\sin x + \cos x}$$

**Step 2:** Cancel the $(\sin x + \cos x)$ term.
$$= \sin^2 x - \sin x \cos x + \cos^2 x$$

**Step 3:** Group $\sin^2 x + \cos^2 x = 1$.
$$= 1 - \sin x \cos x$$
**Result:** $LHS = RHS$

---

### 14. Proof of: $\frac{\cos x + 1}{\sin^3 x} = \frac{\csc x}{1 - \cos x}$

**Step 1:** Rewrite LHS denominator $\sin^3 x$ as $\sin x \cdot \sin^2 x$.
$$LHS = \frac{1 + \cos x}{\sin x(1 - \cos^2 x)}$$

**Step 2:** Factor $(1 - \cos^2 x)$ as difference of squares.
$$= \frac{1 + \cos x}{\sin x(1 - \cos x)(1 + \cos x)}$$

**Step 3:** Cancel $(1 + \cos x)$.
$$= \frac{1}{\sin x(1 - \cos x)}$$

**Step 4:** Separate terms.
$$= \frac{1}{\sin x} \cdot \frac{1}{1 - \cos x} = \frac{\csc x}{1 - \cos x}$$
**Result:** $LHS = RHS$

---

### 15. Proof of: $\frac{1 + \sin x}{1 - \sin x} - \frac{1 - \sin x}{1 + \sin x} = 4 \tan x \sec x$

**Step 1:** Find a common denominator $(1 - \sin^2 x) = \cos^2 x$.
$$LHS = \frac{(1 + \sin x)^2 - (1 - \sin x)^2}{\cos^2 x}$$

**Step 2:** Expand the numerators.
$$= \frac{(1 + 2\sin x + \sin^2 x) - (1 - 2\sin x + \sin^2 x)}{\cos^2 x}$$

**Step 3:** Simplify numerator.
$$= \frac{4 \sin x}{\cos^2 x}$$

**Step 4:** Separate terms.
$$= 4 \cdot \frac{\sin x}{\cos x} \cdot \frac{1}{\cos x} = 4 \tan x \sec x$$
**Result:** $LHS = RHS$

---

### 16. Proof of: $\csc^4 x - \cot^4 x = \csc^2 x + \cot^2 x$

**Step 1:** Factor LHS as a difference of squares.
$$LHS = (\csc^2 x - \cot^2 x)(\csc^2 x + \cot^2 x)$$

**Step 2:** Apply identity $\csc^2 x - \cot^2 x = 1$.
$$= 1 \cdot (\csc^2 x + \cot^2 x)$$

**Step 3:** Simplify.
$$= \csc^2 x + \cot^2 x$$
**Result:** $LHS = RHS$

---

### 17. Proof of: $\frac{\sin^2 x}{\cos^2 x + 3\cos x + 2} = \frac{1 - \cos x}{2 + \cos x}$

**Step 1:** Replace $\sin^2 x$ with $1 - \cos^2 x$.
$$LHS = \frac{1 - \cos^2 x}{\cos^2 x + 3\cos x + 2}$$

**Step 2:** Factor numerator and denominator.
Numerator (Diff of squares): $(1 - \cos x)(1 + \cos x)$
Denominator (Quadratic factoring): $(\cos x + 1)(\cos x + 2)$

**Step 3:** Substitute back into fraction.
$$= \frac{(1 - \cos x)(1 + \cos x)}{(1 + \cos x)(2 + \cos x)}$$

**Step 4:** Cancel $(1 + \cos x)$.
$$= \frac{1 - \cos x}{2 + \cos x}$$
**Result:** $LHS = RHS$

---

### 18. Proof of: $\frac{\tan x + \tan y}{\cot x + \cot y} = \tan x \tan y$

**Step 1:** Rewrite denominator in terms of tangent.
$$LHS = \frac{\tan x + \tan y}{\frac{1}{\tan x} + \frac{1}{\tan y}}$$

**Step 2:** Combine fractions in the denominator.
$$= \frac{\tan x + \tan y}{\frac{\tan y + \tan x}{\tan x \tan y}}$$

**Step 3:** Multiply by reciprocal.
$$= (\tan x + \tan y) \cdot \frac{\tan x \tan y}{\tan x + \tan y}$$

**Step 4:** Cancel terms.
$$= \tan x \tan y$$
**Result:** $LHS = RHS$

---

### 19. Proof of: $\frac{1 + \tan x}{1 - \tan x} = \frac{\cos x + \sin x}{\cos x - \sin x}$

**Step 1:** Convert $\tan x$ to $\sin x / \cos x$.
$$LHS = \frac{1 + \frac{\sin x}{\cos x}}{1 - \frac{\sin x}{\cos x}}$$

**Step 2:** Multiply numerator and denominator by $\cos x$.
$$= \frac{\cos x(1 + \frac{\sin x}{\cos x})}{\cos x(1 - \frac{\sin x}{\cos x})}$$

**Step 3:** Distribute.
$$= \frac{\cos x + \sin x}{\cos x - \sin x}$$
**Result:** $LHS = RHS$

---

### 20. Proof of: $(\sin x - \tan x)(\cos x - \cot x) = (\sin x - 1)(\cos x - 1)$

**Step 1:** Factor out $\sin x$ from first term and $\cos x$ from second term.
First term: $\sin x - \frac{\sin x}{\cos x} = \sin x(1 - \frac{1}{\cos x})$
Second term: $\cos x - \frac{\cos x}{\sin x} = \cos x(1 - \frac{1}{\sin x})$

**Step 2:** Multiply them together.
$$LHS = \sin x \cos x \left(1 - \frac{1}{\cos x}\right)\left(1 - \frac{1}{\sin x}\right)$$

**Step 3:** Expand the brackets.
$$= \sin x \cos x \left(1 - \frac{1}{\sin x} - \frac{1}{\cos x} + \frac{1}{\sin x \cos x}\right)$$

**Step 4:** Distribute $\sin x \cos x$.
$$= \sin x \cos x - \cos x - \sin x + 1$$

**Step 5:** Factor by grouping.
$$= \sin x(\cos x - 1) - 1(\cos x - 1)$$
$$= (\sin x - 1)(\cos x - 1)$$
**Result:** $LHS = RHS$
