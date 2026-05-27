# HJB Portfolio Optimization (Forward–Backward SDE + Neural Networks)

Finance portfolio optimization using the **Hamilton–Jacobi–Bellman (HJB)** framework in higher dimensions, approximated via a **forward simulation** of stochastic wealth paths and (intended) **forward–backward** neural learning using stochastic paths instead of PDE grids.

This repo currently includes:
- Simulation of wealth under a learned/parameterized control \( \pi(t, W_t) \)
- Brownian motion path generation
- Neural network scaffolding for \( \pi(t, W_t) \) and \( Z(t, W_t) \)
- A Merton benchmark closed-form control for reference

> Note: The docs outline the full forward/backward/value-propagation + loss/training pipeline, but the executable code in this repo is presently focused on the **forward simulation** portion.

---

## What you’re creating

You model a risky asset investment with a portfolio control:
- \( \pi(t, W_t) \): fraction (or amount, depending on your interpretation) invested in the risky asset at time \( t \), given current wealth \( W_t \)
- The wealth evolves using an Euler discretization of the controlled SDE:
  \[
  dW_t = r W_t\,dt + \pi(t,W_t)(\mu - r)\,dt + \pi(t,W_t)\sigma\,dB_t
  \]
- The neural network `pi_star` provides \( \pi(t, W_t) \) as a function of time and a Brownian state.

---

## Current status / roadmap

From `md files/todo.md` and `md files/pipeline.md`:

### Completed / working
- Merton minimal benchmark solver/formula (`mertons_2D.py`)
- Forward stochastic differential equation written (first version) (`forward_simulation_equations.py`)
- Neural network definitions exist (`neural_networks.py`)
- Dummy/example data exists (`data_accumulation/data.md`)
- Pipeline “before training” is described and partially implemented

### Next / not implemented in executable code (yet)
- Backward simulation / backward value propagation
- Terminal loss construction
- Training loop to learn the neural networks
- Benchmark comparison to quantify improvement vs. Merton

(See `md files/pipeline.md` and `md files/intution_pipeline.md` for the conceptual full pipeline.)

---

## Repo structure (key files)

- **`brownian_motion.py`**
  - Generates Brownian increments `dw` and cumulative Brownian path `W`

- **`forward_simulation_equations.py`**
  - `forward_simulation(...)`: Euler simulation of wealth using a control model `pi_star`

- **`neural_networks.py`**
  - `pi_star`: neural net mapping \((t, W)\) → \(\pi(t,W)\)
  - `Z_net`: neural net mapping \((t, W)\) → \(Z(t,W)\) (scaffold)

- **`utility_function.py`**
  - Utility function helper (currently written as `Wealth**1-gamma/1-gamma`)

- **`mertons_2D.py`**
  - Closed-form Merton allocation:
    \[
    \pi^* = \frac{\mu - r}{\gamma \sigma^2}
    \]

- **`data_accumulation/data.md`**
  - Example parameters (mu, sigma, risk_free_rate, initial wealth, gamma)

- **`test.py`**
  - Small sanity check / demonstration of the Merton formula

---

## How the forward simulation works (code-level)

`forward_simulation_equations.forward_simulation(model, dw, W, mu, sigma, w0, rate, T, num_steps)`:

1. Create a time grid \(t_0,\dots,t_N\) with \(N=\text{num_steps}\)
2. Initialize `wealth_grid[:,0] = w0`
3. For each step \(i\):
   - Evaluate control: `pi = model(t, W[:, i])`
   - Euler update:
     - `drift = rate * W_t + pi * (mu - rate)`
     - `diffusion = pi * sigma * dW`
     - `W_{t+dt} = W_t + drift*dt + diffusion`

---

## How to run (examples)

### 1) Merton benchmark sanity check
```bash
python test.py
```

### 2) Forward simulation demo
Run the script entry inside `forward_simulation_equations.py`:
```bash
python forward_simulation_equations.py
```

This uses:
- `model = pi_star()`
- a Brownian motion path with default example sizes
- example `mu`, `sigma`, `rate`, `w0` taken from `data_accumulation/data.md` values embedded in the script

---

## Conceptual background (from `md files/intution_pipeline.md`)

- **Forward pass:** simulate many stochastic wealth paths under a control \(\pi(t,W)\)
- **Backward/value propagation (intended):** use the terminal condition at \(T\) and propagate optimality information backward along the same simulated paths to learn what the control should have been.

---

## References inside the repo
- `md files/pipeline.md`: complete pipeline description (conceptual checklist)
- `md files/todo.md`: current progress/next steps
- `md files/intution_pipeline.md`: intuition behind forward/backward propagation

---

## License
See `LICENSE`.
