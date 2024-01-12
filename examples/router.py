from functools import partial
from typing import Callable


def router_open(path: str, *, chat_id: str = None):

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):

            res = func(chat_id, *args, **kwargs)
            return res

        return wrapper
    return decorator


@router_open(path="/", chat_id="test1")
def func1(chat_id: str = None):
    print(1, chat_id)




if __name__ == "__main__":
    func1()


# def my_decorator(parameter):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             # 在这里使用装饰器的参数值
#             print("Decorator parameter:", parameter)
#
#             # 调用被装饰的函数，并传递参数
#             result = func(parameter, *args, **kwargs)
#
#             return result
#
#         return wrapper
#
#     return decorator


# @my_decorator("Hello")
# def decorated_function(decorator_parameter, *args, **kwargs):
#     print("Decorated function parameter:", decorator_parameter)
#     print("Other parameters:", args, kwargs)
#
#
# # 调用被装饰的函数
# decorated_function("World", additional_param="!")