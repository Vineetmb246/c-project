# Function to add two numbers
def add(a, b):
    return a + b

def test_add():
    result = add(2, 3)
    print(f"Result of add(2, 3): {result}")
    assert result == 5

