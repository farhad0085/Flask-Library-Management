# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'root', email='root@gmail.com', password='password', major='administrator',
			 headline=u"Administrator", about_me=u"Graduated from the Department of Management, like reading, so part-time librarian.")
user1 = User(name=u'akalin', email='akarin@Gmail.com', password='123456',
			 major='Computer Science', headline=u"Ordinary student")
user2 = User(name=u'test', email='test@test.com', password='123456')
user3 = User(name=u'komei', email='xiaoming@163.com', password='123456')
user4 = User(name=u'Li Hua', email='lihua@yahoo.com', password='123456')

book1 = Book(title=u"Flask web development", subtitle=u"Web application development framework based on Python", author=u"Miguel Grinberg", isbn='9787115373991',
			 tags_string=u"Computer, programming, web development", image='http://img3.douban.com/lpic/s27906700.jpg',
			 summary=u"""
# This book is not only suitable for junior Web developers to learn to read, but also an excellent reference book for Python programmers to learn advanced Web development techniques.

* Learn the basic structure of Flask applications and write sample applications;
* Use necessary components, including templates, databases, Web forms, and email support;
* Use packages and modules to build scalable large-scale applications;
* Realize user authentication, roles and personal data;
* Reuse templates, display lists on pages, and use rich text in blog sites;
* Use Flask-based REST API to implement available functions on smartphones, tablets, and other third-party clients;
* Learn to run unit tests and improve performance;
* Deploy web applications to production servers.
""")
book2 = Book(title=u"STL source code analysis", subtitle=u"Pao Ding Jie Niu", author=u"Hou Jie", isbn='9787560926995',
			 tags_string=u"Computer, programming, C++", image='http://img3.doubanio.com/lpic/s1092076.jpg',
			 summary=u"""
			 * Everyone who learns programming knows that reading and analyzing famous codes is a shortcut to improve their level. Before the source code, there is no secret. The meticulous thinking, experience crystallization, technical ideas, and unique style of the masters are all originally in the source code.
* The source code presented in this book allows readers to see the realization of vector, list, heap, deque, Red Black tree, hash table, set/map; see various The implementation of algorithms (sorting, searching, permutation and combination, data movement and replication technology); even the realization of the underlying memory pool and high-level abstract traits mechanism can be seen.
			 """)
book3 = Book(title=u"Compiling principle (Second edition)", subtitle=u"Principles, technology and tools",
			 author="Alfred V. Aho / Monica S.Lam / Ravi Sethi / Jeffrey D. Ullman ", isbn="9787111251217",
			 tags_string=u"Computer, compilation principle", image='http://img3.douban.com/lpic/s3392161.jpg',
			 summary=u"""
			 * This book comprehensively and in-depth discusses important topics in compiler design, including lexical analysis, grammatical analysis, grammar-guided definition and grammar-guided translation, runtime environment, object code generation, code optimization techniques, parallelism detection, and interprocess Analyze the technology and give a lot of examples in the relevant chapters. Compared with the previous edition, this book has been comprehensively revised to cover the latest developments in compiler development. A large number of systems and references are provided in each chapter.
* This book is a classic textbook on the course of compilation principles. It is rich in content and suitable as a textbook on the course of compilation principles for undergraduates and graduate students of computer and related majors in colleges and universities. It is also an excellent reference reading for the majority of technical staff.
			 """)
book4 = Book(title=u"Deep understanding of computer system", author="Randal E.Bryant / David O'Hallaron", isbn="9787111321330",
			 tags_string=u"Computer, computer system", image='http://img3.douban.com/lpic/s4510534.jpg',
			 summary=u"""
			 * This book elaborates on the essential concepts of computer systems from the perspective of programmers, and shows how these concepts can actually affect the correctness, performance, and practicality of applications. The book consists of 12 chapters, including the presentation and processing of information, machine-level representation of programs, processor architecture, optimized program performance, memory hierarchy, links, exception control flow, virtual memory, system-level I/O, and network programming , Concurrent programming, etc. A large number of examples and exercises are provided in the book, and some answers are given to help readers deepen their understanding of the concepts and knowledge described in the text.
* The biggest advantage of this book is to describe the implementation details of computer systems for programmers, and help them construct a hierarchical computer system in the brain, from the representation of the lowest-level data in memory to the composition of pipeline instructions, to virtual memory, To the compilation system, to the dynamic loading library, to the final user mode application. By grasping how the program is mapped to the system and how the program is executed, the reader can better understand why the program behaves like this and how the inefficiency is caused.
* This book is suitable for programmers who want to write faster and more reliable programs. It is also suitable as a textbook for undergraduates and postgraduates of computer and related majors in colleges and universities.
			 """)
book5 = Book(title=u"C# in the shell", subtitle=u"C# 5.0 Definitive Guide", author=u"Joseph Albahari / Ben Albahari",
			 isbn="9787517010845", tags_string=u"Computer, programming, C#", image='http://img3.douban.com/lpic/s28152290.jpg',
			 summary=u"""
			 * "C# in Crust——The Authoritative Guide to c#5.0" is an authoritative technical guide to c#5.0 and the first Chinese version of c#5.0 study materials. Through the content of 26 chapters, this book systematically, comprehensively and meticulously explained the command, syntax and usage of c#5.0 from basic knowledge to various advanced features. The explanation of this book is simple and simple. At the same time, each knowledge point is specially designed with appropriate, simple and easy-to-understand learning cases, which can help readers accurately understand the meaning of knowledge points and quickly learn to apply. Compared with the previous c# 4.0 version, this book also adds rich content related to advanced features such as concurrency, asynchronous, dynamic programming, code refining, security, and com interaction.
* "The c# in the shell-c#5.0 authoritative guide" also integrates the author's years of research and practical experience in software development and c#, which is very suitable as a self-study tutorial for c# technology, and it is also a book An indispensable reference book for intermediate and advanced c# technicians.
			 """)
book6 = Book(title=u"Introduction to Algorithms (2nd edition)",
			 author="Thomas H.Cormen / Charles E.Leiserson / Ronald L.Rivest / Clifford Stein",
			 isbn="9787111187776", tags_string=u"Computer, algorithm", image='http://img3.doubanio.com/lpic/s1959967.jpg',
			 summary=u"""
			 This book explains the algorithm in a comprehensive way. The analysis of each algorithm is both easy to understand and very interesting, and maintains mathematical rigor. The design goals of this book are comprehensive and suitable for multiple uses. The contents covered are: the role of algorithms in calculations, probability analysis and introduction to random algorithms. The book specifically discusses linear programming, introduces two applications of dynamic programming, randomization and the approximate algorithm of linear programming, etc., as well as the recursive solution, the division method used in quick sorting, and the expected linear time sequence statistical algorithm, And a discussion of the elements of the greedy algorithm. The book also introduces the proof of the correctness of the strongly connected subgraph algorithm, the proof of the NP completeness of the Hamiltonian loop and the subset sum problem. The book provides more than 900 practice questions and thinking questions, as well as more detailed case studies.
			 """)
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
		Log(user2, book1), Log(user2, book3), Log(user2, book5),
		Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, book1,
					book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
