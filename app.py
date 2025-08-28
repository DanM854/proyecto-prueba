from utils import is_prime

def f(event, context):
    print("hola desde lambda con zappa")
    print(is_prime(5))
    return {}