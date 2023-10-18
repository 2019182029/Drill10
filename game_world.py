objects = [[], []]


def add_object(o, depth=0):
    objects[depth].append(o)


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in objects:
        if o in layer:  # 버그 예방을 위해 layer.remove(o)를 사용하지 않는다.
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')
