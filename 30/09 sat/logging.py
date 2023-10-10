import logging

# Configure the logging settings
logging.basicConfig(filename='example.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Example function that logs messages


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Division by zero occurred.")
    else:
        logging.info(f"Division result: {result}")


# Usage of the logging
if __name__ == "__main__":
    logging.debug("Debug message")
    logging.info("Informational message")
    logging.warning("Warning message")
    logging.error("Error message")
    logging.critical("Critical message")

    divide(10, 2)
    divide(10, 0)
