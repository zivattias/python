import random


def open_image(filename: str):
    # with open(filename, 'rb') as photo:
    #     data = photo.read()
    #     new_data = list(data)
    #     manipulated_data = [random.randint(0, 255) for pix in new_data]
    #     # byted_data = [hex(pix) for pix in new_data]
    #     byted_manipulated = [hex(pix) for pix in manipulated_data]
    #     # new_byted = [bytes(pix) for pix in manipulated_data]
    #     result = bytes([int(x, 0) for x in byted_manipulated])
    #     print(result)

    with open(filename, 'rb') as f:
        data = f.read()

    header = b"\xff\xd8"
    tail = b"\xff\xd9"

    start = data.index(header)
    end = data.index(tail, start) + 2

    print(start, end)

    manipulated_data = list()
    for i in data[start:end]:
        manipulated_data.append(i + 30 if i <= 150 else i)

    byted_manipulated = [hex(pix) for pix in manipulated_data]

    # result = list()
    # for pix in byted_manipulated:
    #     pix = bytes.fromhex(pix)
    #     result.append(pix)

    print(data)
    # print(result)

    # with open("manipulated_tr.jpg", 'wb') as f:
    #     f.write(result[start:end])


if __name__ == "__main__":
    open_image("/Users/ziv.attias/PycharmProjects/lessons/extra-mile/self.jpeg")
