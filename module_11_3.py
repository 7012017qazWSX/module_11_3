def introspection_info(obj):

    obj_type = type(obj).__name__

    obj_module = getattr(obj, '__module__', 'built-in')

    all_attributes = dir(obj)

    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr))]
    methods = [method for method in all_attributes if callable(getattr(obj, method))]

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module}

    return info

class MyClass:
    def __init__(self):
        self.value = 42

    def my_method(self):
        return "Hello!"

my_object = MyClass()

object_info = introspection_info(my_object)
print(object_info)

number_info = introspection_info(42)
print(number_info)