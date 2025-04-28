import argparse
from loguru import logger
from time import process_time



def measure_time(input_func):
  def inner(*args, **kwargs): 
    # Calculate the starting time
    start = process_time()
    # Execute the inner function
    result = input_func(*args, **kwargs)
    # Calculate the end time
    end = process_time()
    logger.info(f"Elapsed time: {end - start} seconds")
    return result
  return inner


def measure_execution_time_with_args(*d_args, **d_kwargs):
  def wrapper(input_func):
    def inner(*args, **kwargs):
      # Calculate the starting time
      start = process_time()
      # Execute the inner function
      result = input_func(*args, **kwargs)
      print("d_args: ", d_args)
      print("d_kwargs: ", d_kwargs)
      # Calculate the end time
      end = process_time()
      logger.info(f"Elapsed time: {end - start} seconds")
      return result
    
    return inner
  
  return wrapper


@measure_execution_time_with_args(1, 2, 3, a=1, b=2)
# @measure_time
def predict(x):
    model = {"a": 1, "b": 2}
    logger.info("Getting predictions!")
    if x in model:
        return model[x]
    else:
        raise ValueError(f"Could not predict {x}")

def main(args):
  x = args.x 
  print(predict(x))


if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="A simple example of a decorator")
   parser.add_argument("-x", type=str, help="The input string to predict")
   args = parser.parse_args()
   main(args)