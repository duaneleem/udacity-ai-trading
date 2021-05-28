# AI for Trading | Week 1 | L7: Returns

## Returns
- https://youtu.be/PngIo6G73Z8
- 0:30 Difference in price
- 0:42 Return = Percentage Return or Raw Return
- 0:55: Return Figures
## Log Returns
- https://youtu.be/62fZN1QnGjc
- 0:40 Raw Returns & Log Returns
- 0:55 Why use log returns
- Converting between raw returns and log returns
  - R=ln(r+1)
  - r=eR−1
## Log Returns and Compounding
- If you invest $100 in an asset, and the rate of return is 4% per year, and the amount of interest accrued is only calculated after the money has sat in the account for 1 year, how much money do you have after 1 year?
  - 1st Year: $100 + $100*0.04 = $104
  - 2nd Year: $104 + $104*0.04 = $108.16
- 1 year with semi-annual compounding, Annual Rate of Interest at 4%
  - 6 Months: $100 + $100*0.02 = $102
  - Next: $102 + $102*0.02 = $104.04
- Rates of Compounding
  - Semiannual: $100×(1+.04/2)^2
  - Quarterly: $100×(1+.04/4)^4
- Continuous Compounding
  - Annually (n=1)
  - Semi-annually (n=2)
  - Quarterly (n=4)
  - Monthly (n=12)
  - Weekly (n=52)
  - Daily (n=252)​
- Continuously Compounded Return
  - Find rate of interested if you knew beginning/end of the year
    - Previous: $104.08/$100=e^r
    - Calculate: ln($104.08/$100)=r
    - r is the continuously compounded annual return
  - The continuously compounded annual return equals ln(pt/pt−1)\ln(p_t/p_{t-1})ln(pt​/pt−1​)
  - Log returns could also be called continuously compounded returns
- The continuously compounded rate of return is additive over time.
- Annualized Rate of Return, annualizing the rate of continuous compounding
- Numerical Stability
  - Sometimes the computation will incorrectly yield the value 0. This is called arithmetic underflow. 
  ## Distributions of Returns and Prices
  - Normality and Long-Term Investments
## Distributions of Returns and Prices
- 

