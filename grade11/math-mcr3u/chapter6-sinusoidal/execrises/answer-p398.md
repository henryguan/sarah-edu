
## Question 1
The load on a trailer has shifted, causing the rear end of the trailer to swing left and right. The distance from one of the tail lights on the trailer to the curb varies sinusoidally with time. The graph models this behaviour.

    **a)** What is the equation of the axis of the function, and what does it represent in this situation?

    **b)** What is the amplitude of the function, and what does it represent in this situation?

    **c)** What is the period of the function, and what does it represent in this situation?

    **d)** Determine the equation and the range of the sinusoidal function.

    **e)** What are the domain and range of the function in terms of the situation?

    **f)** How far is the tail light from the curb at t = 3.2s?

Answer:

This problem involves analyzing a sinusoidal function from its graph, relating the function's parameters to a real-world scenario, and using the function to make a prediction.

The general equation for this sinusoidal graph is $f(t) = a \sin(k(t-d)) + c$ or $f(t) = a \cos(k(t-d)) + c$.

### **a) What is the equation of the axis of the function, and what does it represent in this situation?**

The equation of the axis ($y=c$) is the vertical center of the wave, calculated as the average of the maximum and minimum values.

* **Maximum Value ($f_{max}$):** The highest point on the graph is $2.0$ m.
* **Minimum Value ($f_{min}$):** The lowest point on the graph is $1.0$ m.

$$c = \frac{f_{max} + f_{min}}{2} = \frac{2.0 + 1.0}{2} = \frac{3.0}{2} = 1.5$$

* **Equation of the Axis:** $\mathbf{f(t) = 1.5}$ (or $y=1.5$).
* **Representation:** This represents the **average distance** of the tail light from the curb when the trailer is swinging.

### **b) What is the amplitude of the function, and what does it represent in this situation?**

The amplitude ($|a|$) is the vertical distance from the axis to the maximum (or minimum) value.

$$a = \frac{f_{max} - f_{min}}{2} = \frac{2.0 - 1.0}{2} = \frac{1.0}{2} = 0.5$$

* **Amplitude:** $\mathbf{0.5 \text{ m}}$.
* **Representation:** This represents the **maximum distance the tail light swings** (the maximum deviation) to the left or right *from* its average distance to the curb.

### **c) What is the period of the function, and what does it represent in this situation?**

The period ($P$) is the time it takes for one full cycle to complete. Observing the graph:
* The wave starts near $t=0$ and completes one cycle when it returns to the same height and slope direction.
* A maximum occurs at $t \approx 0.75$ s. The *next* maximum occurs at $t \approx 2.75$ s.
$$P = 2.75 - 0.75 = 2.0$$

* **Period:** $\mathbf{2.0 \text{ s}}$.
* **Representation:** This represents the **time it takes for the trailer to swing completely left and right once** and return to its initial swinging position.

### **d) Determine the equation and the range of the sinusoidal function.**

#### **i. Determine the Equation**

We have the parameters: $a=0.5$, $c=1.5$, and $P=2.0$.
We need $k$ and the phase shift $d$. Using the period formula:
$$k = \frac{2\pi}{P} = \frac{2\pi}{2.0} = \pi$$

**Choosing a Cosine Model:**
The basic cosine function starts at a maximum. The graph has a maximum at $t_{max} \approx 0.75$ s.
* **Phase Shift ($d$):** $d = 0.75$.
* **Equation (Cosine):** $f(t) = a \cos(k(t - d)) + c$
$$\mathbf{f(t) = 0.5 \cos(\pi(t - 0.75)) + 1.5}$$

#### **ii. Determine the Range**

The range is the set of all possible $f(t)$ values (vertical values). This is from the minimum distance to the maximum distance.

* **Range:** $\mathbf{\{f(t) \in \mathbb{R} \mid 1.0 \le f(t) \le 2.0\}}$ (or $[1.0, 2.0]$ in interval notation).

### **e) What are the domain and range of the function in terms of the situation?**

* **Domain:** The domain represents the time ($t$) over which the swinging motion is measured. Based on the graph, the domain is $\mathbf{\{t \in \mathbb{R} \mid 0 \le t \le 4\}}$ or perhaps $\mathbf{\{t \in \mathbb{R} \mid t \ge 0\}}$ if the motion continues indefinitely. Since the graph is only shown up to $t=4$ s, we will use that as the observed domain: $\mathbf{[0, 4] \text{ s}}$.
* **Range:** The range represents the possible distances of the tail light from the curb. $\mathbf{[1.0, 2.0] \text{ m}}$.

### **f) How far is the tail light from the curve at $t=3.2$ s?**

Substitute $t=3.2$ into the equation from part (d):
$$f(t) = 0.5 \cos(\pi(t - 0.75)) + 1.5$$
$$f(3.2) = 0.5 \cos(\pi(3.2 - 0.75)) + 1.5$$
$$f(3.2) = 0.5 \cos(2.45\pi) + 1.5$$

Using a calculator (in radian mode, since $k$ involves $\pi$):
$$\pi \approx 3.14159$$
$$2.45\pi \approx 7.6969$$
$$\cos(2.45\pi) \approx \cos(7.6969) \approx -0.8090$$

$$f(3.2) \approx 0.5 (-0.8090) + 1.5$$
$$f(3.2) \approx -0.4045 + 1.5$$
$$f(3.2) \approx 1.0955$$

Rounding to two decimal places (matching the precision of the graph):
* **Distance at $t=3.2$ s:** $\mathbf{1.10 \text{ m}}$.


##Question 2:

Don Quixote, a fictional character in a Spanish novel, attacked windmills because he thought they were giants. At one point, he got snagged by one of the blades and was hoisted into the air. The graph shows his height above ground in terms of time.

a) What is the equation of the axis of the function, and what does it represent in this situation?  
b) What is the amplitude of the function, and what does it represent in this situation?  
c) What is the period of the function, and what does it represent in this situation?  
d) If Don Quixote remains snagged for seven complete cycles, determine the domain and range of the function.  
e) Determine the equation of the sinusoidal function.  
f) If the wind speed decreased, how would that affect the graph of the sinusoidal function?

Answer:

This problem analyzes the height of Don Quixote on a windmill blade using a sinusoidal function graph.

The graph shows his height $f(t)$ in meters above the ground over time $t$ in seconds.

### **a) What is the equation of the axis of the function, and what does it represent in this situation?**

The equation of the axis ($y=c$) is the vertical center of the wave, calculated as the average of the maximum and minimum values.

* **Maximum Value ($f_{max}$):** The highest point on the graph is $17 \text{ m}$ (reading from the grid).
* **Minimum Value ($f_{min}$):** The lowest point on the graph is $3 \text{ m}$.

$$c = \frac{f_{max} + f_{min}}{2} = \frac{17 + 3}{2} = \frac{20}{2} = 10$$

* **Equation of the Axis:** $\mathbf{f(t) = 10}$ (or $y=10$).
* **Representation:** This represents the **height of the center** of the windmill blade's rotation above the ground.

### **b) What is the amplitude of the function, and what does it represent in this situation?**

The amplitude ($|a|$) is the vertical distance from the axis to the maximum (or minimum) value.

$$a = \frac{f_{max} - f_{min}}{2} = \frac{17 - 3}{2} = \frac{14}{2} = 7$$

* **Amplitude:** $\mathbf{7 \text{ m}}$.
* **Representation:** This represents the **length of the windmill blade**, specifically the radius of the circular path that Don Quixote travels.

### **c) What is the period of the function, and what does it represent in this situation?**

The period ($P$) is the time it takes for one full cycle to complete. Observing the graph:
* A minimum occurs at $t \approx 20 \text{ s}$. The *next* minimum occurs at $t \approx 40 \text{ s}$.
$$P = 40 - 20 = 20$$
* **Period:** $\mathbf{20 \text{ s}}$.
* **Representation:** This represents the **time it takes for the windmill blade to complete one full rotation**.

### **d) If Don Quixote remains snagged for seven complete cycles, determine the domain and range of the function.**

#### **i. Range**
The range is the set of all possible heights Don Quixote reaches. This is determined by the minimum and maximum height, which does not change based on the number of cycles.

* **Range:** $\mathbf{\{f(t) \in \mathbb{R} \mid 3 \le f(t) \le 17\}}$ (or $[3, 17] \text{ m}$ in interval notation).

#### **ii. Domain**
The domain represents the time ($t$) he is snagged. The motion starts at $t=0$.
* **Duration:** $7 \text{ cycles} \times 20 \frac{\text{s}}{\text{cycle}} = 140 \text{ s}$.
* **Domain:** The time interval is from $t=0$ to $t=140 \text{ s}$.
* **Domain:** $\mathbf{\{t \in \mathbb{R} \mid 0 \le t \le 140\}}$ (or $[0, 140] \text{ s}$ in interval notation).

### **e) Determine the equation of the sinusoidal function.**

We have the parameters: $a=7$, $c=10$, and $P=20$.

**1. Determine the $k$-value**
$$k = \frac{2\pi}{P} = \frac{2\pi}{20} = \frac{\pi}{10}$$

**2. Determine the Phase Shift ($d$)**
We can use a negative cosine model because the graph starts near a minimum at $t=5 \text{ s}$ (reading from the grid, the first minimum occurs at $t \approx 5 \text{ s}$). *Correction: The graph starts at $t=0$ at a height of 3. The first minimum is actually at $t=20 \text{ s}$. Let's re-examine the graph.*

The graph starts at $t=0$ at a height of $3 \text{ m}$, which is the **minimum height**.
* A basic **negative cosine** function, $y = -a \cos(kt) + c$, starts at its minimum when $t=0$. This is the simplest model.
* **Phase Shift ($d$):** $d = 0$.

**3. The Equation (Negative Cosine Model)**
$$f(t) = -a \cos(k(t - d)) + c$$
$$f(t) = -7 \cos\left(\frac{\pi}{10}(t - 0)\right) + 10$$

$$\mathbf{f(t) = -7 \cos\left(\frac{\pi}{10}t\right) + 10}$$

### **f) If the wind speed decreased, how would that affect the graph of the sinusoidal function?**

A decrease in wind speed would cause the windmill to **rotate more slowly**.

* This would **increase the period ($P$)** (it takes longer to complete one rotation).
* Since $k = \frac{2\pi}{P}$, an increase in the period ($P$) would lead to a **decrease in the $k$-value** (a horizontal stretch).

The **amplitude ($a$)** and the **equation of the axis ($c$)** would **remain the same** because the size of the windmill blades and the height of the axle above the ground are fixed physical properties.


## Question 4

The interior and exterior temperatures of an igloo were recorded over a 48 h period. The data were collected and plotted, and two curves were drawn through the appropriate points.

**a)** How are these curves similar? Explain how each of them might be related to this situation.

**b)** Describe the domain and range of each curve.

**c)** Assuming that the curves can be represented by sinusoidal functions, determine the equation of each function.

Answer:

This problem analyzes two sinusoidal curves representing the interior and exterior temperatures of an igloo over a 48-hour period.

### **a) How are these curves similar? Explain how each of them might be related to this situation.**

#### **Similarities**

The two curves are similar because they both represent **sinusoidal functions** and have the same **Period** ($P$).
* The blue (interior) curve completes one cycle in 24 hours (e.g., from $h=0$ to $h=24$).
* The pink (exterior) curve also completes one cycle in 24 hours (e.g., from $h=0$ to $h=24$).
* **Period $P = 24 \text{ h}$** for both. This makes sense as daily temperature cycles are tied to the 24-hour rotation of the Earth. 
#### **Relationship to the Situation**

* **Exterior Temperature (Pink Curve):** This curve is related to the daily cycle of solar heating and cooling.
    * The **minimum** temperature is approximately $-30^\circ\text{C}$ (coldest time of day/night).
    * The **maximum** temperature is approximately $-10^\circ\text{C}$ (warmest time of day/daylight).
* **Interior Temperature (Blue Curve):** This curve reflects the temperature inside the igloo, which is generally more stable than the exterior temperature.
    * The **minimum** temperature is approximately $15^\circ\text{C}$.
    * The **maximum** temperature is approximately $20^\circ\text{C}$.
    * The interior temperature has a much **smaller amplitude** (less extreme swings) and a **higher axis** (warmer overall) than the exterior temperature, illustrating the **insulating effect** of the igloo.

---

### **b) Describe the domain and range of each curve.**

#### **Domain**
The domain ($h$) represents the time over which the temperatures were recorded. Both curves are shown over the same 48-hour interval.

* **Domain:** $\mathbf{\{h \in \mathbb{R} \mid 0 \le h \le 48\}}$, or $[\mathbf{0, 48}]$ **hours**.

#### **Range**
The range ($T(h)$) represents the possible temperature values for each curve.

* **Exterior Temperature (Pink):**
    * $T_{min} = -30^\circ\text{C}$
    * $T_{max} = -10^\circ\text{C}$
    * **Range (Exterior):** $\mathbf{\{T \in \mathbb{R} \mid -30 \le T \le -10\}}$, or $[\mathbf{-30, -10}] \mathbf{^\circ\text{C}}$.
* **Interior Temperature (Blue):**
    * $T_{min} = 15^\circ\text{C}$
    * $T_{max} = 20^\circ\text{C}$
    * **Range (Interior):** $\mathbf{\{T \in \mathbb{R} \mid 15 \le T \le 20\}}$, or $[\mathbf{15, 20}] \mathbf{^\circ\text{C}}$.

---

### **c) Assuming that the curves can be represented by sinusoidal functions, determine the equation of each function.**

The general equation is $T(h) = a \cos(k(h - d)) + c$. Since the period $P=24$ for both:
$$k = \frac{2\pi}{P} = \frac{2\pi}{24} = \frac{\pi}{12}$$

#### **Exterior Temperature (Pink Curve)**

1.  **Axis ($c$):** $c = \frac{-10 + (-30)}{2} = \frac{-40}{2} = -20$
2.  **Amplitude ($a$):** $a = \frac{-10 - (-30)}{2} = \frac{20}{2} = 10$
3.  **Phase Shift ($d$):** The curve starts at a minimum ($T=-30$) at $h=0$. This is a perfect fit for a **negative cosine** function with $d=0$.
    * We use the form $T(h) = -a \cos(kh) + c$.
4.  **Equation:**
    $$\mathbf{T_{ext}(h) = -10 \cos\left(\frac{\pi}{12}h\right) - 20}$$

#### **Interior Temperature (Blue Curve)**

1.  **Axis ($c$):** $c = \frac{20 + 15}{2} = \frac{35}{2} = 17.5$
2.  **Amplitude ($a$):** $a = \frac{20 - 15}{2} = \frac{5}{2} = 2.5$
3.  **Phase Shift ($d$):** The curve starts at a medium value, going up. The first maximum is at $h \approx 12$. A basic cosine function starts at a maximum at $h=0$.
    * Let's use a standard **cosine function** and shift it to the right until the maximum is at $h=12$.
    * $d = 12$
4.  **Equation:**
    $$T(h) = a \cos(k(h - d)) + c$$
    $$\mathbf{T_{int}(h) = 2.5 \cos\left(\frac{\pi}{12}(h - 12)\right) + 17.5}$$
    * *Alternative (Sine Model):* The curve crosses the axis ($T=17.5$) going up at $h \approx 6$. A sine function $T(h) = a \sin(k(h - 6)) + c$ would also work: $T_{int}(h) = 2.5 \sin\left(\frac{\pi}{12}(h - 6)\right) + 17.5$.

## Question 5

Skyscrapers sway in high-wind conditions. In one case, at s, the top

At time \( t = 0 \), the top floor of a building swayed 30 cm to the left (−30 cm), and at \( t = 12 \), the top floor swayed 30 cm to the right (+30 cm) from its starting position.

a) Find the equation of a sinusoidal function that models the motion of the building as a function of time.

b) Large tanks of water, called dampers, are sometimes installed on the top floors of skyscrapers to reduce the amount of sway. If a damper is added to this building and it reduces the sway (but not the period) by 70%, what is the equation of the new function that models the building's motion?


This problem models the swaying motion of a skyscraper using a sinusoidal function. We'll use the general form $y = a \sin(k(t - d)) + c$ or $y = a \cos(k(t - d)) + c$.

The motion is described relative to the building's starting (center) position, which we can define as the equilibrium position, or the **axis of the function**.

### **a) What is the equation of a sinusoidal function that describes the motion of the building in terms of time?**

The given data points are:
* At $t=8$ seconds, the sway is $y = -30$ cm (to the left/minimum displacement).
* At $t=12$ seconds, the sway is $y = +30$ cm (to the right/maximum displacement).

#### **1. Determine the Parameters**

* **Axis of the Function ($c$):** Since the sway is measured from the starting (center) position, the axis is $y=0$.
    $$c = \frac{30 + (-30)}{2} = 0$$

* **Amplitude ($a$):** The amplitude is the maximum displacement from the center.
    $$a = 30 \text{ cm}$$

* **Period ($P$) and $k$-value:** The time from a minimum (t=8) to the next maximum (t=12) is half a cycle ($\frac{1}{2}P$).
    $$\frac{1}{2}P = 12 - 8 = 4 \text{ s}$$
    $$P = 8 \text{ s}$$
    Now calculate $k$:
    $$k = \frac{2\pi}{P} = \frac{2\pi}{8} = \frac{\pi}{4}$$

* **Phase Shift ($d$):** We can use a **cosine function** since we have the location of a maximum. The basic cosine function starts at a maximum at $t=0$. The maximum for this function is at $t=12$.
    $$d = 12$$

#### **2. The Equation**

Using the cosine model: $y = a \cos(k(t - d)) + c$
$$y = 30 \cos\left(\frac{\pi}{4}(t - 12)\right) + 0$$

$$\mathbf{y = 30 \cos\left(\frac{\pi}{4}(t - 12)\right)}$$

*(Self-check: Since the period is 8, and the maximum is at $t=12$, the previous maximum was at $t=12-8=4$. The previous minimum was at $t=12-4=8$. This aligns with the initial data point $(8, -30)$ if we use a sine function. Let's write the equivalent sine function for completeness, though the cosine function above is perfectly valid.)*

* *Alternative Sine Equation:* The graph crosses the axis ($y=0$) heading up (the first quarter cycle after the minimum at $t=8$) at $t=8+2=10$. Using a sine function, $d=10$.
    $$y = 30 \sin\left(\frac{\pi}{4}(t - 10)\right)$$

---

### **b) What is the equation of the new function that describes the motion of the building in terms of time?**

If a damper is added, it reduces the sway by $70\%$. This means the **amplitude** ($a$) will be reduced by $70\%$. The period and the axis of the function remain unchanged.

#### **1. Determine the New Amplitude ($a_{new}$)**

The sway is reduced by $70\%$, meaning the new sway is $100\% - 70\% = 30\%$ of the original amplitude.

$$\text{Reduction} = 70\% \text{ of } 30 = 0.70 \times 30 = 21 \text{ cm}$$
$$a_{new} = 30 - 21 = 9 \text{ cm}$$
*OR*
$$a_{new} = 30\% \text{ of } 30 = 0.30 \times 30 = 9 \text{ cm}$$

#### **2. Determine the New Equation**

The new amplitude is $a_{new}=9$. The other parameters remain: $k=\frac{\pi}{4}$, $d=12$, and $c=0$.

Using the same cosine model as before: $y = a_{new} \cos(k(t - d)) + c$
$$y = 9 \cos\left(\frac{\pi}{4}(t - 12)\right) + 0$$

$$\mathbf{y = 9 \cos\left(\frac{\pi}{4}(t - 12)\right)}$$

---

## Question 8

Candice is holding onto the end of a spring that is attached to a lead ball. As
she moves her hand slightly up and down, the ball moves up and down. With a
little concentration, she can repeatedly get the ball to reach a maximum height
of 20 cm and a minimum height of 4 cm from the top of a surface. The first
maximum height occurs at 0.2 s, and the first minimum height occurs at 0.6 s.
a) Determine the equation of the sinusoidal function that represents the
height of the lead ball in terms of time.
b) Determine the domain and range of the function.
c) What is the equation of the axis, and what does it represent in this
situation?
d) What is the height of the lead ball at 1.3 s?

This problem models the vertical oscillation of a lead ball on a spring using a sinusoidal function. We'll use the general form $h(t) = a \cos(k(t - d)) + c$, where $h(t)$ is the height in $\text{cm}$ and $t$ is the time in $\text{s}$.

The given data points are:
* **Maximum Height ($h_{max}$):** $20 \text{ cm}$
* **Minimum Height ($h_{min}$):** $4 \text{ cm}$
* **First Maximum:** at $t_{max} = 0.2 \text{ s}$
* **First Minimum:** at $t_{min} = 0.6 \text{ s}$

### **a) Determine the equation of the sinusoidal function that represents the height of the lead ball in terms of time.**

#### **1. Axis ($c$)**
The axis is the midpoint of the maximum and minimum heights.
$$c = \frac{h_{max} + h_{min}}{2} = \frac{20 + 4}{2} = \frac{24}{2} = 12$$

#### **2. Amplitude ($a$)**
The amplitude is the vertical distance from the axis to the maximum (or minimum).
$$a = h_{max} - c = 20 - 12 = 8$$

#### **3. Period ($P$) and $k$-value**
The time from a maximum ($t=0.2$) to the next minimum ($t=0.6$) is half a period ($\frac{1}{2}P$).
$$\frac{1}{2}P = t_{min} - t_{max} = 0.6 - 0.2 = 0.4 \text{ s}$$
$$P = 2 \times 0.4 = 0.8 \text{ s}$$
Now calculate $k$:
$$k = \frac{2\pi}{P} = \frac{2\pi}{0.8} = \frac{20\pi}{8} = \frac{5\pi}{2}$$

#### **4. Phase Shift ($d$)**
We will use a **cosine function** since we know the location of a maximum. The basic cosine function starts at a maximum.
* The first maximum occurs at $t = 0.2 \text{ s}$.
$$d = 0.2$$

#### **5. The Equation**
Using the cosine model: $h(t) = a \cos(k(t - d)) + c$
$$\mathbf{h(t) = 8 \cos\left(\frac{5\pi}{2}(t - 0.2)\right) + 12}$$

---

### **b) Determine the domain and range of the function.**

* **Range:** The range is the set of all possible heights, determined by the minimum and maximum values.
    * **Range:** $\mathbf{\{h \in \mathbb{R} \mid 4 \le h \le 20\} \text{ cm}}$.

* **Domain:** Since the ball continues to oscillate as long as Candice moves her hand, and the time starts at $t=0$, we assume the motion continues indefinitely unless specified otherwise.
    * **Domain:** $\mathbf{\{t \in \mathbb{R} \mid t \ge 0\} \text{ s}}$.

---

### **c) What is the equation of the axis, and what does it represent in this situation?**

* **Equation of the Axis:** $h(t) = 12$ (from part a, $c=12$).

* **Representation:** This represents the **equilibrium position** (the resting or center height) of the lead ball when it is hanging motionless on the spring. Its height is $\mathbf{12 \text{ cm}}$ above the surface. 

---

### **d) What is the height of the lead ball at $1.3 \text{ s}$?**

Substitute $t=1.3$ into the equation from part (a):
$$h(t) = 8 \cos\left(\frac{5\pi}{2}(t - 0.2)\right) + 12$$
$$h(1.3) = 8 \cos\left(\frac{5\pi}{2}(1.3 - 0.2)\right) + 12$$
$$h(1.3) = 8 \cos\left(\frac{5\pi}{2}(1.1)\right) + 12$$
$$h(1.3) = 8 \cos\left(\frac{5.5\pi}{2}\right) + 12$$
$$h(1.3) = 8 \cos(2.75\pi) + 12$$

We can simplify the angle by subtracting the period ($2\pi$):
$$2.75\pi = 2\pi + 0.75\pi$$
$$\cos(2.75\pi) = \cos(0.75\pi)$$
Since $0.75\pi = \frac{3\pi}{4}$ (second quadrant), the cosine value is negative. The related acute angle is $\frac{\pi}{4}$.
$$\cos\left(\frac{3\pi}{4}\right) = -\cos\left(\frac{\pi}{4}\right) = -\frac{\sqrt{2}}{2} \approx -0.7071$$

Now substitute the value back:
$$h(1.3) \approx 8 (-0.7071) + 12$$
$$h(1.3) \approx -5.657 + 12$$
$$h(1.3) \approx 6.343$$

The height of the lead ball at $1.3 \text{ s}$ is approximately **$6.34 \text{ cm}$**.

##Question 13

## Analysis of the Sinusoidal Function

This problem requires analyzing the provided graph to determine its equation and solve for specific function values and input variables. 
The general equation for this sinusoidal graph is $f(x) = a \cos(k(x - d)) + c$ or $f(x) = a \sin(k(x - d)) + c$, where $x$ is in degrees.

### **a) Determine the equation of the function.**

#### **1. Axis of the Function ($c$)**
The axis is the average of the maximum and minimum values.
* **Maximum Value ($f_{max}$):** The highest point on the graph is $2$.
* **Minimum Value ($f_{min}$):** The lowest point on the graph is $-4$.
$$c = \frac{f_{max} + f_{min}}{2} = \frac{2 + (-4)}{2} = \frac{-2}{2} = -1$$

#### **2. Amplitude ($a$)**
The amplitude is the distance from the axis to the maximum (or minimum) value.
$$a = f_{max} - c = 2 - (-1) = 3$$

#### **3. Period ($P$) and $k$-value**
The period ($P$) is the time it takes for one full cycle to complete. Observing the graph:
* A maximum occurs at $x = 180^\circ$. The next maximum occurs at $x = 540^\circ$.
$$P = 540^\circ - 180^\circ = 360^\circ$$
Now calculate $k$ using the formula $P = \frac{360^\circ}{|k|}$:
$$k = \frac{360^\circ}{360^\circ} = 1$$

#### **4. Phase Shift ($d$)**
We will use a **cosine function** since we have a maximum point. The basic cosine function starts at a maximum at $x=0^\circ$.
* The graph's first maximum *after* the $y$-axis occurs at $x=180^\circ$.
$$d = 180^\circ$$

#### **5. The Equation**
Using the cosine model: $f(x) = a \cos(k(x - d)) + c$
$$f(x) = 3 \cos\left(1(x - 180^\circ)\right) - 1$$
$$\mathbf{f(x) = 3 \cos(x - 180^\circ) - 1}$$

---

### **b) Evaluate $f(20)$.**

Substitute $x = 20^\circ$ into the equation:
$$f(20) = 3 \cos(20^\circ - 180^\circ) - 1$$
$$f(20) = 3 \cos(-160^\circ) - 1$$

Since $\cos(-\theta) = \cos(\theta)$:
$$f(20) = 3 \cos(160^\circ) - 1$$

Using a calculator:
$$\cos(160^\circ) \approx -0.9397$$

$$f(20) \approx 3(-0.9397) - 1$$
$$f(20) \approx -2.8191 - 1$$
$$\mathbf{f(20) \approx -3.82}$$

---

### **c) If $f(x) = 2$, then which of the following is true for $x$?**

$f(x)=2$ is the **maximum value** of the function ($f_{max}=2$). We need to find all $x$ values where the maximum occurs.

Observing the graph:
* The first maximum shown occurs at $x = 180^\circ$.
* The second maximum shown occurs at $x = 540^\circ$.

Since the period is $P = 360^\circ$, the solutions are $x = 180^\circ + 360^\circ k$, where $k$ is an integer ($k \in \mathbf{I}$).

Comparing this to the given options:

i) $180^\circ + 360^\circ k, k \in \mathbf{I}$
ii) $360^\circ + 180^\circ k, k \in \mathbf{I}$
iii) $90^\circ + 180^\circ k, k \in \mathbf{I}$
iv) $270^\circ + 360^\circ k, k \in \mathbf{I}$

The correct option is **i)**.

---

### **d) If $f(x) = -1$, then which of the following is true for $x$?**

$f(x)=-1$ is the **equation of the axis** ($y=c$). The curve crosses the axis twice every period.

Observing the graph:
* The curve crosses the axis ($y=-1$) going down at $x = 90^\circ$.
* The curve crosses the axis ($y=-1$) going up at $x = 270^\circ$.

The interval between these two axis crossings is half a period: $270^\circ - 90^\circ = 180^\circ$. The solutions are separated by $180^\circ$.

Therefore, the general solution is $x = 90^\circ + 180^\circ k$, where $k \in \mathbf{I}$.

Comparing this to the given options:

i) $180^\circ + 360^\circ k, k \in \mathbf{I}$
ii) $360^\circ + 90^\circ k, k \in \mathbf{I}$
iii) $90^\circ + 360^\circ k, k \in \mathbf{I}$ (Only hits the first point, misses $270^\circ, 630^\circ$, etc.)
iv) $90^\circ + 180^\circ k, k \in \mathbf{I}$

The correct option is **iv)**.