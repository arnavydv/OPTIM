import numpy as np
import torch
from neural_networks import pi_star, Z_net
from brownian_motion import brownian_motion

def forward_simulation(model, dw, W, mu, sigma, w0, rate, T, num_steps):
    """
    Simulate wealth dynamics with a learned/parameterized pi(t, W).

    Args:
      model: torch.nn.Module with forward(self, t, W) -> (num_paths, 1)
      dw: torch.Tensor of shape (num_paths, num_steps)
      W:  torch.Tensor of shape (num_paths, num_steps)
      mu, sigma, rate: scalars
    """
    time_grid = np.linspace(0, T, num_steps + 1)
    dt = T / num_steps

    num_paths = dw.shape[0]
    wealth_grid = torch.zeros(num_paths, num_steps + 1, dtype=dw.dtype)

    # Ensure starting wealth matches tensor dtype
    wealth_grid[:, 0] = torch.as_tensor(w0, dtype=dw.dtype)

    sigma_t = torch.as_tensor(sigma, dtype=dw.dtype)
    mu_t = torch.as_tensor(mu, dtype=dw.dtype)
    rate_t = torch.as_tensor(rate, dtype=dw.dtype)

    for i in range(num_steps):
        t = float(time_grid[i])
        w = wealth_grid[:, i]  # (num_paths,)

        t_col = torch.full((num_paths, 1), t, dtype=dw.dtype)
        W_col = W[:, i : i + 1]  # (num_paths,1)

        # pi(t, W) expected to return shape (num_paths,1)
        pi = model(t_col, W_col)  # (num_paths,1)
        # Wealth SDE (discretized):
        # drift = r*W + pi*(mu-r)
        drift = rate_t * w.view(-1, 1) + pi * (mu_t - rate_t)  # (num_paths,1)
        # diffusion = pi * sigma * dW
        diffusion = pi * sigma_t * dw[:, i : i + 1]  # (num_paths,1)
        wealth_next = w.view(-1, 1) + drift * dt + diffusion  # (num_paths,1)
        wealth_grid[:, i + 1] = wealth_next.squeeze(1)
    return time_grid, wealth_grid
if __name__ == "__main__":
    model = pi_star()

    dw, W = brownian_motion(1000, 252, 1 / 252)

    mu = 0.20164940530246397
    sigma = 0.016162564586327234
    rate = 0.0368
    w0 = 1.0

    time_grid, wealth = forward_simulation(
        model=model,
        dw=dw,
        W=W,
        mu=mu,
        sigma=sigma,
        w0=w0,
        rate=rate,
        T=1,
        num_steps=252,
    )
    print(wealth[:, -1].mean().item())
