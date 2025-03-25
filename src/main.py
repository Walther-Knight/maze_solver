from window import *

def main():

    win = Window(800, 600)

    # Create Points
    p1 = Point(1, 2)
    p2 = Point(4, 6)

    # Create a Line using the Points
    line = Line(p1, p2)

    # Test the Line's Length
    print(f"Length: {line.length():.2f}")  # Expected: 5.0 (3-4-5 triangle)

    # Test the Midpoint
    midpoint = line.midpoint()
    print(f"Midpoint: ({midpoint.x}, {midpoint.y})")  # Expected: (2.5, 4.0)

    # Test the String Representation
    print(line)  # Expected: "Line from Point(1, 2) to Point(4, 6), length: 5.00"
    
    #point1 = Point(0, 0)
    #point2 = Point(100, 150)
    #point3 = Point(0, 0)
    #point4 = Point(50, 90)
    #black_line = Line(point1, point2)
    #red_line = Line(point3, point4)
    
    #win.draw_line(black_line, "black")
    #win.draw_line(red_line, "red")
    
    win.wait_for_close()

if __name__ == "__main__":
        main()