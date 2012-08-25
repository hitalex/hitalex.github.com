---
layout: post
title: 所有的三角形都是等腰三角形？！ - 推广到一般三角形的证明
categories: 
- 观点
tags: 
- 等腰三角形
- 证明
- 几何
---

在上一篇博文（[所有的三角形都是等腰三角形？！](http://alexkong.net/2012/08/are-all-triangles-isosceles/)）中，我举了一个特例，而在这篇文章中，我将给出一个一般性的证明：对于任意三角形，其中任意一个角的角平分线和其对边的垂直平分线的交点不可能在三角形内。

显然，对于等腰三角形和等边三角形，两条线的交点在三角形的某条边上（此时两条线重合）。那么，对于非等腰三角形呢？

要**优雅**的解决这个问题，需要先来看一种新的三角形的画法。在确定一个三角形之前，我们可以先确定一条边，比如线段AB，然后做出线段AB的垂直平分线l，其与AB相交于C点。

![另外一种画三角形的方法](/images/non-isosceles-triangle-prove.jpg "另外一种画三角形的方法")

关于第三个点的选取，因为AB的上方部分和下方部分完全对称，我们只考虑AB的上方部分。其实，AB的垂直平分线 l 左右两边也是对称的。第三个点可以在AB上方的任意位置。注意，在确定线段AB之后，我们可以只调整第三个点O的位置来得到各种三角形。比如三角形ABO1为锐角三角形，三角形ABO2为钝角三角形，适当选取O的位置同样可以得到直角三角形。另外，我们只考虑∠AOB的角平分线和AB的垂直平分线的交点也不会失掉一般性。

![另外一种画三角形的方法](/images/non-isosceles-triangle-prove2.jpg "另外一种画三角形的方法")

假如O点取在AB垂直平分线的左端，那么可以断言OB > OA 以及∠BOC为锐角（因为∠BCO为钝角）。

我们现在来考虑∠AOC和∠BOC之间的大小关系。根据[正弦定理](http://zh.wikipedia.org/zh-hk/%E6%AD%A3%E5%BC%A6%E5%AE%9A%E7%90%86 "正弦定理")，

考虑三角形OAC：OA / sin(∠OCA) = AC / sin(∠AOC)，那么 OA / AC = sin(∠OCA) / sin(∠AOC) (1)

考虑三角形OBC：OB / sin(∠OCB) = BC / sin(∠BOC)，那么 OB / BC = sin(∠OCB) / sin(∠BOC) (2)

因为 OA < OB 且 AC = BC，根据(1)和(2)，可以得出

sin(∠OCA) / sin(∠AOC) < sin(∠OCB) / sin(∠BOC) (3)

又因为∠OCA + ∠OCB = 180度，所以sin(∠OCA) = sin(∠OCB)。根据(3)可知，

sin(∠AOC) > sin(∠BOC) (4)

因为∠BOC为锐角，所以无论∠AOC为锐角、直角还是钝角，只要满足(4)，就可以得出结论：∠AOC > ∠BOC。所以∠AOB的角平分线OD只能如下图所示。

![另外一种画三角形的方法](/images/non-isosceles-triangle-prove3.jpg "另外一种画三角形的方法")

综上，OD与线段AB的垂直平分线的交点肯定不在三角形内。
