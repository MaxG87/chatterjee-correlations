# chatterjee-correlations
One-off script to explore Chatterjee Correlation

This repository hosts a simple Python file that implements the [Chatterjee Correlation algorithm](https://arxiv.org/abs/1909.10140). Its main goal is to have fun with the implementation and to explore how the claims hold in practice. By no means it is intended to be reusable or a demonstration of good programming practices.

If you are interested in a library to be used, you may find [xicorpy](https://pypi.org/project/xicorpy/) interesting. I haven't used it myself, but it looks promising. Additionally, [this paper](https://arxiv.org/abs/2108.06828) seems to improve the power of the coefficient calculation.

## Results
The results are stunning. For a broad range of nonlinear functions a very strong correlation is detected. This makes this correlation algorithm much more suited to detect hidden relations than my prior go-to method Support Vector Machines with powerful kernels.
