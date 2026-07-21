def make_multiplier(factor):
    """Return a closure that multiplies a value by factor."""
    
    def multiplier(x):
        return x * factor
    
    return multiplier


# Create multiplier functions
times3 = make_multiplier(3)
times10 = make_multiplier(10)

# Test the closures
print("times3(7) =", times3(7))
print("times10(7) =", times10(7))