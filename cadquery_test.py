import cadquery as cq

# Створюємо куб
result = cq.Workplane("XY").box(90, 50, 20)

# Додаємо отвори
result = result.faces(">Z").workplane() \
    .pushPoints([(20, 20), (70, 20), (20, 30), (70, 30)]) \
    .hole(5) \
    .faces(">Z").workplane() \
    .pushPoints([(20, 40), (70, 40)]) \
    .hole(7)

# Згладжуємо кути
result = result.edges("|Z").fillet(5)

if __name__=='__main__':
    show_object(result)
