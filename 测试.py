# 示例：参数与返回值标注类型
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)    # ✅ ok
add(1, "2")  # ❌ mypy 会报错
