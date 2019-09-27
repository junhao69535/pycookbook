#!coding=utf-8

"""
    访问闭包中定义的变量
"""


# 想要扩展函数中的某个闭包，允许它能访问和修改函数的内部变量
# 通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。 但是，你可以通过编写
# 访问函数并将其作为函数属性绑定到闭包上来实现这个目的
def sample():
    n = 0

    # Closure function
    def func():
        print 'n={}'.format(n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n():
        pass

    func.get_n = get_n
    func.set_n = set_n
    return func


f = sample()
f()
print f.get_n()