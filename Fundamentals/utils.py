def g2c(coordinate:tuple, pixel_unit:int) -> tuple:
    """
        Convert pygame coordinate to cartesian coordinate. x pixel unit 
        refers to 1 unit in cartesian coordinate system. For example:
        if pixel unit is 100 then 100 pixel is one unit in cartesian system
    

    coordinate: game coordinate (x, y)
    pixel_unit: int


    return: tuple
    """
    return (int(x/pixel_unit), int(y/pixel_unit))

def c2g(coordinate:tuple, pixel_unit:int) -> tuple:
    """
        cartesian coordinate to pygame coordinate
    
    coordinate: cartesian coordinate (x, y)
    pixel_unit: int

    return: tuple
    """
    return (int(x*pixel_unit), int(y*pixel_unit))
