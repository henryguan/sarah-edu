# Chapter 6 Unit Test – Solutions

## Question 1

**State $y = \cos x$ in terms of sine.**

**Answer:**
$y = \sin(x + 90^\circ)$

*Reasoning:* The cosine graph is the same as the sine graph shifted to the left by $90^\circ$.

---

## Question 2

**For the trig function $f(x) = -2 \cos(3x - 120) - 1$, determine:**

First, factor the inner expression to identify the transformations:
$f(x) = -2 \cos[3(x - 40)] - 1$

**(a) The phase shift**
Right $40^\circ$.

**(b) The amplitude**
$a = |-2| = 2$.

**(c) The period**
Period $= \frac{360^\circ}{k} = \frac{360^\circ}{3} = 120^\circ$.

**(d) The axis**
$y = -1$.

**(e) The max value**
Max = Axis + Amplitude = $-1 + 2 = 1$.

**(f) The min value**
Min = Axis - Amplitude = $-1 - 2 = -3$.

---

## Question 3

**Sketch one period of the following functions.**

**(a) $f(x) = -2 \sin(x) + 2$**

*Analysis:*
- Parent: $\sin x$
- Reflection in x-axis (starts at axis, goes down).
- Amplitude: 2.
- Axis: $y = 2$ (Vertical shift up 2).
- Period: $360^\circ$.

*Key Points (every $90^\circ$):*
- $x=0^\circ$: Axis $\rightarrow y=2$.
- $x=90^\circ$: Minimum $\rightarrow y = 2 - 2 = 0$.
- $x=180^\circ$: Axis $\rightarrow y=2$.
- $x=270^\circ$: Maximum $\rightarrow y = 2 + 2 = 4$.
- $x=360^\circ$: Axis $\rightarrow y=2$.

**(b) $g(x) = \cos(2(x + 45))$**

*Analysis:*
- Parent: $\cos x$
- Period: $360^\circ / 2 = 180^\circ$.
- Quarter-points: Every $45^\circ$.
- Phase shift: Left $45^\circ$.
- Amplitude: 1.
- Axis: $y = 0$.

*Key Points (Starting at shift $x = -45^\circ$):*
- $x=-45^\circ$: Max $\rightarrow y=1$.
- $x=0^\circ$: Axis $\rightarrow y=0$.
- $x=45^\circ$: Min $\rightarrow y=-1$.
- $x=90^\circ$: Axis $\rightarrow y=0$.
- $x=135^\circ$: Max $\rightarrow y=1$.

*(Note: The sketch should label these coordinates.)*

---

## Question 4

**Write the following function in terms of sine:**
$f(x) = -2 \cos(3x - 120) - 1$

*Steps:*
1. Factor the argument: $f(x) = -2 \cos[3(x - 40)] - 1$.
2. Use the identity $\cos \theta = \sin(\theta + 90^\circ)$.
3. Substitute: $-2 \sin([3(x - 40)] + 90) - 1$.
4. Simplify angle: $3x - 120 + 90 = 3x - 30$.
5. Factor again: $3(x - 10)$.

**Answer:**
$f(x) = -2 \sin(3(x - 10)) - 1$

*(Alternate Answer using positive sine: $f(x) = 2 \sin(3(x - 70)) - 1$)*

---

## Question 5

**Analyzed from Graph (Question 5 Image):**
- **Axis (Vertical Shift):** The wave oscillates between $y=1$ (Max) and $y=-3$ (Min).
  Axis $c = \frac{1 + (-3)}{2} = -1$.
- **Amplitude:**
  $a = \frac{1 - (-3)}{2} = 2$.
- **Period:**
  The graph crosses the axis at $x=0$ and returns to the axis (completing half a cycle) at $x=2$.
  Full Period = 4.
  $k = \frac{360}{4} = 90$ (assuming degrees scaling for consistency).

**(a) State the:**
- (i) **Period:** 4
- (ii) **Amplitude:** 2
- (iii) **Equation of the axis:** $y = -1$

**(b) State a function in terms of cosine representing this graph:**
The minimum is at $x=1$. A negative cosine function starts at a minimum.
Using no phase shift for negative cosine relative to the minimum at $x=1$:
$y = -a \cos(k(x - d)) + c$
$y = -2 \cos(90(x - 1)) - 1$

**Answer:**
$f(x) = -2 \cos(90(x - 1)) - 1$

---

## Question 6

**The diameter of a car's tire is 60 cm. While the car is being driven, the tire picks up a nail.**

**(a) Graph and Trig Function**

*Setup:*
- **Diameter:** 60 cm $\rightarrow$ **Radius:** 30 cm.
- **Axis:** The center of the wheel is 30 cm off the ground. $y=30$.
- **Amplitude:** The nail moves from 0 to 60 cm. $a=30$.
- **Start:** Nail is picked up from the ground ($h=0$). This corresponds to a minimum.
- **Function Type:** Negative cosine (starts at min).
- **Period (Distance):** One rotation = Circumference = $\pi D = 60\pi \approx 188.5$ cm.
- **k value:** $k = \frac{360}{60\pi} = \frac{6}{\pi}$ (degrees per cm).

**Function:**
$h(d) = -30 \cos\left(\frac{6}{\pi} d\right) + 30$

**(b) Height after 1.2 km**

*Calculation:*
- $d = 1.2 \text{ km} = 1200 \text{ m} = 120,000 \text{ cm}$.
- Substitute $d$ into equation:
  $h = -30 \cos\left(\frac{6}{\pi} \times 120,000\right) + 30$
- Angle $\theta = \frac{720,000}{\pi}$ degrees.
- Number of full rotations = $\frac{120,000}{60\pi} \approx 636.61977$.
- Remainder fraction = $0.61977$.
- Angle in current cycle = $0.61977 \times 360^\circ \approx 223.1^\circ$.
- $\cos(223.1^\circ) \approx -0.73$.
- $h \approx -30(-0.73) + 30 = 21.9 + 30 = 51.9$.

**Answer:**
Approximately **51.9 cm** above the ground.

---

## Question 7

**Valve stem problem (Diagram 7).**
- **Wheel:** Outer height 12 cm $\rightarrow$ Radius 6 cm.
- **Valve Stem:** Indicated at 6 cm height (same as center).
- **Position:** Diagram shows it on the **left** (9 o'clock).
- **Motion:** Rolling right $\rightarrow$ clockwise rotation.
- **Movement:** From 9 o'clock, clockwise motion moves the valve **UP**.
- **Inner Radius:** Gap at bottom is 3 cm. Valve radius from center = $6 - 3 = 3$ cm.
- **Amplitude:** 3.
- **Axis:** Center height = 6.

**(a) Function of distance (with graph)**

- **Start:** At axis, going up $\rightarrow$ Positive Sine.
- **Period:** Circumference of tire = $12\pi$ cm.
- **k:** $k = \frac{360}{12\pi} = \frac{30}{\pi}$.

**Function:**
$h(d) = 3 \sin\left(\frac{30}{\pi} d\right) + 6$

**(b) Height after rolling 60 cm**

- $d = 60$.
- $\theta = \frac{30}{\pi} \times 60 = \frac{1800}{\pi} \text{ degrees} \approx 573^\circ$.
- $573^\circ - 360^\circ = 213^\circ$ (Quadrant 3).
- $h = 3 \sin(213^\circ) + 6$.
- $h \approx 3(-0.545) + 6 = -1.63 + 6 = 4.37$.

**Answer:**
Approximately **4.37 cm**.

**(c) Function of time**

- **Speed:** $v = 24\pi \text{ cm/s}$.
- Substitute $d = v \cdot t = 24\pi t$.
- $k_{time} = \frac{30}{\pi} \times 24\pi = 720$.

**Function:**
$h(t) = 3 \sin(720t) + 6$
