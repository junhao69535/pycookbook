#!coding=utf-8

# 你的程序创建了很多循环引用数据结构(比如树、图、观察者模式等)，你碰到了内存管理难题。
# 循环引用指两个对象相互强引用了对方，即retain了对方，从而导致两个对象都无法被释放，引发了内存泄漏现象。

# 一个简单的循环引用数据结构例子就是一个树形结构，双亲节点有指针指向孩子节点，孩子节点
# 又返回来指向双亲节点。 这种情况下，可以考虑使用 weakref 库中的弱引用。
import weakref


class Node(object):
    def __init__(self, value):
        self.value = value
        self._parent = Node
        self.children = []

    def __repr__(self):
        return "Node({!r:})".format(self.value)

    # 把parent作为弱引用管理
    @property
    def parent(self):
        return None if self._parent is None else self._parent()  # 因为weak_ref使其能被调用

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)  # 解决循环引用问题
        # self._parent = node

    def add_child(self, child):
        # 这个函数会导致循环引用
        self.children.append(child)
        child.parent = self


root = Node("parent")
c1 = Node("child1")
root.add_child(c1)
print c1.parent
del root
print c1.parent


# 循环引用的数据结构在Python中是一个很棘手的问题，因为正常的垃圾回收机制不能适用于这种情形。
# 例如考虑如下代码：
class Data(object):
    def __del__(self):
        print "Data.__del__"


# 存在循环引用的Node类
class Node(object):
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


# 下面我们使用这个代码来做一些垃圾回收试验：
a = Data()
del a  # 立刻删除，没有问题
a = Node()
del a  # 立刻删除，没有问题
print u"用于隔开"
a = Node()
a.add_child(Node())
del a   # 并没有删除，因为存在循环引用，这里小心被最后的打印误解，那不是del产生的，而是python解释器结束gc回收产生的
# 因为程序结束，gc要回收，所以会产生两条Data.__del__，但这并不是del a这条语句产生的。

# 可以看到，最后一个的删除时打印语句没有出现。原因是Python的垃圾回收机制是基于简单的引用计数。
# 当一个对象的引用数变成0的时候才会立即删除掉。而对于循环引用这个条件永远不会成立。 因此，
# 在上面例子中最后部分，父节点和孩子节点互相拥有对方的引用，导致每个对象的引用计数都不可能变成0。

# Python有另外的垃圾回收器来专门针对循环引用的，但是你永远不知道它什么时候会触发。
# 另外你还可以手动的触发它，但是代码看上去很挫：
import gc
gc.collect()  # 会产生两条Data.__del__


# 如果循环引用的对象自己还定义了自己的 __del__() 方法，那么会让情况变得更糟糕。 假设你像下面
# 这样给Node定义自己的 __del__() 方法：
class Node(object):
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    # 不要像以下这样定义__del__，这里只是用于说明这种病态行为
    def __del__(self):
        del self.data
        del self.parent
        del self.children


# 这种情况下，垃圾回收永远都不会去回收这个对象的，还会导致内存泄露。 如果你试着去运行它会
# 发现，Data.__del__ 消息永远不会出现了,甚至在你强制内存回收时：
a = Node()
a.add_child(Node())
del a  # 不会产生del消息
gc.collect()  # 也不会产生del消息


# 弱引用消除了引用循环的这个问题，本质来讲，弱引用就是一个对象指针，它不会增加它的引用计数。
# 你可以通过 weakref 来创建弱引用。
import weakref
a = Node()
a_ref = weakref.ref(a)
print a_ref


# 为了访问弱引用所引用的对象，你可以像函数一样去调用它即可。如果那个对象还存在就会返回它，
# 否则就返回一个None。 由于原始对象的引用计数没有增加，那么就可以去删除它了。
print a_ref()
del a
print a_ref()

while True:
    pass