def bucket_index(value, width):
    """
    Return the index of the fixed-width bucket that value falls into.

    Buckets are half-open intervals [k * width, (k + 1) * width), so with
    width 10: 0-9 is bucket 0, 10-19 is bucket 1, and -10 to -1 is bucket -1.
    Uses floor division, which rounds toward negative infinity, so negative
    values land in the correct bucket instead of being merged into bucket 0.

    Args:
        value: The number to place into a bucket.
        width: The size of each bucket; must be positive.

    Returns:
        int: The bucket index.

    Raises:
        ValueError: If width is zero or negative.
    """
    if width <= 0:
        raise ValueError(f"width must be positive, got {width}")
    return value // width
