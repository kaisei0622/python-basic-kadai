# 消費税を加えて計算
def add_two_arguments(price, tax):
    total = price * tax
    print(f"{total}円")
    return total

add_two_arguments(100, 1.1)
