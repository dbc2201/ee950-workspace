shape = {"kind": "circle", "radius": 5}

match shape:
    case {"kind": "circle", "radius": radius} if radius <= 0:
        print("invalid: radius must be positive")
    case {"kind": "circle", "radius": radius}:
        print(f"circle with radius {radius}")
    case _:
        print("unknown")
