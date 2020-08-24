import sys
import logging
import math

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level="DEBUG", format=LOG_FORMAT, filemode="w", filename=f"{__file__[:-3]}.log")
# logging.basicConfig(level="INFO", format=LOG_FORMAT, filemode="w", filename=f"{__file__[:-3]}.log")
# logging.basicConfig(level="ERROR", format=LOG_FORMAT, filemode="w", filename=f"{__file__[:-3]}.log")
logger = logging.getLogger(__name__)

print(logger.level)

# Test the logger
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!!")


def quadratic_formula(a, b, c):
    """Return the solution to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant.
    logger.debug("# Compute the discriminant.")
    disc = b ** 2 - 4 * a * c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root_1 = (-b + math.sqrt(disc) / (2 * a))
    root_2 = (-b - math.sqrt(disc) / (2 * a))

    # Return the roots
    logger.debug("# Return the roots")
    return root_1, root_2


roots = quadratic_formula(1, 0, -4)
print(roots)

roots = quadratic_formula(1, 0, 1)
print(roots)
