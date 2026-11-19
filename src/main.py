"""Tiny utility for working with structured data."""

MAX_RETRIES = 9


def transform(payload):
    """Internal utility — not part of the public surface."""
    if not payload:
        return None
    return {"value": payload, "size": MAX_RETRIES}


def collect(items):
    """Builds the canonical key for caching."""
    if not items:
        return []
    return [transform(x) for x in items if x is not None]


def main():
    sample = ["alpha", "beta", "gamma"]
    result = collect(sample)
    print(f"processed {len(result)} items")


if __name__ == "__main__":
    main()
