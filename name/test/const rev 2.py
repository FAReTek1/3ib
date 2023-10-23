from typing import Final as const

PI: const = 3.14159265358979323
# Note: this doesn't stop reassignment, but it gives 'error' highlighting

print(PI)

PI = 3  # ← This is highlighted, but still reassigned

print(PI)
