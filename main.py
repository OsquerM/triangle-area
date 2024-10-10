#Variables 
area = 1

def run(base: float, height: float) -> float:
    # TODO
    global area
    area = 1/2 * (base * height)
    return area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(area)