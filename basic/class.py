#encoding=utf8

#class People(object):
    ##定义基本属性
    #name = ''
    #age = 0
    ##定义私有属性,私有属性在类外部无法直接进行访问
    #__weight = 0
    #score = 100
    
    ##定义构造方法
    ##def __init__(self):
        ##print("无参数构造")
    #def __init__(self,n, a, w):
        #self.name = n
        #self.age = a
        #self.__weight = w  
        #People.__weight
        #print("有参数构造") 
    
       
    #def speak(self):
        #print("%s 说: 我 %d 岁。" %(self.name,self.age))
# 实例化类
#print(People.name)
#p = People(100, 10, 40)
#print(isinstance(p,People))
#p.speak()


#"""通过反射方法 访问"""
#p = People("Tom", 10, 40)
#p.score = 99
#People.score = 99
#p1 = People("Sunny", 100,200)
#print(p1.score)


#print(p._People__weight)
#print(p.__weight)

#print(getattr(p, 'name'))
##setattr(p, 'addr', 'shanghai')
##print(hasattr(p, 'addr'))
##delattr(p, 'addr')
##print(hasattr(p, 'addr'))

#"""内置函数"""

#print("")
d = {"kernel":[[1,2,3],[2,3,1],[1,1,1]], "activate":"relu", "dropout":1.0}
class A(object):
    model = "图像识别"
    kernel = [[1,2,3],[2,3,1],[1,1,1]]
    activate = "relu"
    dropout = 1.0
    @classmethod
    def method_foo(cls, x):
        if not isinstance(x, dict):
            return "invalid value!!!"
        for k,v in x.items():
            setattr(cls, k, v)
            #cls.k = v
                
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
        
    
    @staticmethod
    def static_foo(x):
        A.model = "NLP"
        print("executing static_foo(%s)" % x)
    @classmethod
    def get_instance(cls):
        if A.instance is None:
            A.instance = object.__new__(A)
        return A.instance
    def normal_method():
        A.model = "推荐"
        print("this is normal_method..")

A.method_foo(d)
A.static_foo(10)
a = A()
print(a.model)
#b = A.get_instance()
