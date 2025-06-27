def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Invalid input data. Please check the accuracy of entry data.")
        except IndexError:
            print("Missing required arguments. Please provide all the arguments.")
        except KeyError as e:
            print(str(e).strip("'"))

    return inner
