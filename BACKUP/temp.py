    import sys
    if len(sys.argv) != 2:
        print("Usage: python map_donut.py <integer_value>")
        sys.exit(1)
    value = int(sys.argv[1])
    map_donut(value)