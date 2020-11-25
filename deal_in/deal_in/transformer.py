def transform(values):
    arr = []

    for item in values:
        arr.append(userTransform(item))

    return arr


def userTransform(values):
    return {
        "username": values.username,
        "password": values.password,
        "name": values.name,
    }
