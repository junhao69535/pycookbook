#!coding=utf-8

# 你使用访问者模式遍历一个很深的嵌套树形数据结构，并且因为超过嵌套层级限制而失败。
# 你想消除递归，并同时保持访问者编程模式。

# 通过巧妙的使用生成器可以在树遍历或搜索算法中消除递归。
import types


class Node(object):
    pass


class NodeVisitor(object):
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result

    def _visit(self, node):
        # 访问者提供visit()方法，参数是被访问者，用于操作被访问者数据
        methname = "visit_" + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError("No {} method".format("visit_" + type(node).__name__))


# 考虑如下代码，遍历一个表达式的树：
class UnaryOperation(Node):
    # 被访问者，保持数据结构稳定
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    # 被访问者，保持数据结构稳定
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperation):
    pass


class Number(Node):
    # 被访问者，保持数据结构稳定
    def __init__(self, value):
        self.value = value


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return self.visit(node.operand)


# 修改上面的Evalutor
class Evaluator1(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)

    def visit_Negate(self, node):
        yield - (yield node.operand)


if __name__ == "__main__":
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)
    e = Evaluator()
    a = Number(5)
    for n in xrange(1, 100000):
        a = Add(a, Number(n))  # 这里不断递归
    # e.visit(a)  # 会超过python最大递归深度
    e1 = Evaluator1()
    e1.visit(a)  # 这里不会超过最大递归深度


# 这一小节我们演示了生成器和协程在程序控制流方面的强大功能。 避免递归的一个
# 通常方法是使用一个栈或队列的数据结构。 例如，深度优先的遍历算法，第一次碰到
# 一个节点时将其压入栈中，处理完后弹出栈。visit() 方法的核心思路就是这样。

# 另外一个需要理解的就是生成器中yield语句。当碰到yield语句时，生成器会返回一个数据并暂时挂起。
# 上面的例子使用这个技术来代替了递归。