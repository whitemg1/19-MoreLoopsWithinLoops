"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Matthew White.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()



def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------

    side_x = rectangle.get_width()
    side_y = rectangle.get_height()

    orig_top_left = rectangle.get_upper_left_corner()
    orig_bot_right = rectangle.get_lower_right_corner()


    for k in range(n):
        first_rect = rg.Rectangle(rg.Point(orig_top_left.x - (k * 0.5 * side_x),orig_top_left.y - (k * side_y)),
                                  rg.Point(orig_bot_right.x - (k * 0.5 * side_x),orig_bot_right.y - (k * side_y)))
        first_rect.attach_to(window)
        first_top_left = first_rect.get_upper_left_corner()
        first_bot_right = first_rect.get_lower_right_corner()

        for j in range(k):
            row_of_rect = rg.Rectangle(rg.Point(first_top_left.x + (j + 1) * side_x, first_top_left.y),
                                       rg.Point(first_bot_right.x + (j + 1) * side_x,first_top_left.y + side_y))
            row_of_rect.attach_to(window)

    window.render();

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()


