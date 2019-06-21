# WebValley SCORE API 

This is a simple Python library which integrates a query to
a few websites and get their value of SCORE risk index.

## centrostudigised.py

Sends a POST request to [https://www.centrostudigised.it/calcola_il_tuo_rischio_cardiovascolare.php](https://www.centrostudigised.it/calcola_il_tuo_rischio_cardiovascolare.php)


Can be even imported to call the `query` function or launched on cmd for testing purpose.

## risk_score.py

Implementation in Python of the algorithm to calculate a risk score for cardiovascular disease
from http://riskscore.lshtm.ac.uk/calculator.html
