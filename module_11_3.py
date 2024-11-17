
import inspect


def introspection_info(obj):
    # получение типа объекта
    type_obj = type(obj)

    # получение атрибутов объекта
    dir_obj = dir(obj)

    #получение методов объекта
    methods_obj = [method for method in dir(obj) if callable(getattr(obj, method))]

    #получение модуля, к которому принадлежит объект
    module_obj = getattr(obj, '__module__', None)

    #проверка является ли объект функцией
    callable_obj = callable(obj)
    return {
        "type": type_obj.__name__,
        "attributes": dir_obj,
        "method": methods_obj,
        "module": module_obj,
        "vizov_object": callable_obj
    }

number_info = introspection_info(42)
print(number_info)