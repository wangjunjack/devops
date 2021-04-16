from django.db import models

# 出版商表结构
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)

    def __str__(self):
        return self.name

# 作者信息表结构
class Author(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.name

# 书的表结构
class Book(models.Model):
    title = models.CharField(max_length=100, help_text="书名")
    # 作者和书是多对多的关系
    authors = models.ManyToManyField(Author, verbose_name="作者", help_text="作者")
    # 一本书只能被一家出版商出版，出版商可以出版多本书
    publisher = models.ForeignKey(Publisher, verbose_name="出版社", help_text="出版社", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

"""
-- 带关联字段带的表称为主表(book),不带的称为从表(authors)
-- 正向添加 && 正向查找
b = Book.objects.get(pk=1) # b 是书
a = Author.objects.get(id=3) # a 是作者


1. 查询主表的一条记录
b = Book.objects.get(pk=1)

2. 查询从表一条需要添加的对象
a = Author.objects.get(id=1)

3. 将这个对象添加/追加给这个主表记录
b.authors.add(a)

4. 查询从表一串对象
a__list = Author.objects.filter(id__gt=2) 

5. 有两种方式将这个从表的列表的数据，给主表记录
5.1 追加
b.authors.add(*a_list)
5.2 重置/覆盖
b.authors.set(a_list)

6. 正向查询： 查某本书的所有作者
主表对象.从表关联字段_.all()
b.authors.all()
############################################################
books = Book.objects.values('title',
        'publisher__name',   # 正向外键：外键字段__对应从表字段
        'authors__name',     # 正向多对多： 关联字段_对象从表字段
        'authors__email',
        )


############################################################

-- 反向添加 && 反向查找

反向查询: 关联主表表名小写__主表对应字段

从表对象.主表表名_set.all()
a.book_set.all()

# 反向查询，想拿主表相应字段信息，格式为<表名__主表属性字段名>如：book__title->book表的title字段属性
#查询内容是：出版社出版了哪些书
pub = Publisher.objects.values('name','city','book__title')

# 查询内容：查询作者出了哪些书？
author = Author.objects.values('name','email','book_title')

"""
