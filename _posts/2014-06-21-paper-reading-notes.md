---
layout: post
title: 论文阅读笔记 - 2014.6.21
categories: 
- research
tags: 
- paper
---

# 引言
从本周开始，坚持每周至少写一篇论文阅读笔记。要求精读，详细说明论文方法，并分析该篇文章的优点和缺点。如有可能，提出自己的观点。

这篇博文主要讨论两篇文章，第一作者都是Xiangnan He，[这里](http://www.comp.nus.edu.sg/~xiangnan/)是他的主页。这两篇文章分别是：“Comment-based Multi-View Clustering of Web 2.0 Items”，发表在WWW 2014上，以及“Predicting the Popularity of Web 2.0 Items Based on User Comments”，发表在SIGIR 2014上。两篇文章都和用户评论相关，正好也是我的主要研究内容。

# Comment-based Multi-View Clustering of Web 2.0 Items 
我们先来分析WWW 2014上的这篇，其核心idea是：用户评论，包括评论内容和参与评论的用户能够辅助对web 2.0 items（以后简称items）的聚类。以上两者，再加上items本身的信息共构成三个信息源，所以本文的工作属于多视图聚类（Multi-view clustering）。为了解决多视图聚类问题，作者使用了非负矩阵分解（Non-negative Matrix Factorization, NMF）技术。

进行非负矩阵分解之前，首先需要准备item-feature矩阵$$V \in \mathbb{R}^{m \times n}$$，其中$$m$$表示item的个数，$$n$$表示特征的个数。对于三个视图来说，即item本身、评论内容和评论用户，前两者使用word count，后者使用0-1特征（如果用户存在记为1，不存在记为0）。为了展示三个视图对于item聚类的有效性，作者分别用三个视图进行聚类（包括对特征进行过滤、转换、降维等），并对比分析了聚类结果。

对于多视图聚类问题，本文应用NMF的思路是：在基本的NMF框架下，添加对多个视图下聚类结果的约束，例如添加约束条件使得多个视图下的聚类结果相差不大。根据以上思路写出优化目标函数：

$$
J = \sum_{s=1}^{n_v} \lambda_s \Vert V^{(s)} - W^{(s)}H^{(s)} \Vert + R, s.t. W^{(s)} \ge 0, H^{(s)} \ge 0
$$

其中，$$n_s$$表示视图的个数，矩阵$$W^{(s)}$$和$$H^{(s)}$$的大小分别为$$m \times k$$和$$k \times n$$，$$R$$是附加的约束条件。

## Pair-wise CoNMF
Pair-wise CoNMF要求对于任意两个视图的$W$之间相差不应该太大，所以此时的附加约束为：

$$
R_1 = \sum_{s,t} \lambda_{s,t} \Vert W^{(s)} - W^{(t)}\Vert
$$

本文详尽地提供了目标函数的优化算法推导，其中主要涉及的技术有：$$\Vert A \Vert = Tr(A^T A)$$, $$Tr(AB) = Tr(BA)$$, 矩阵求导和Lagrange乘数法。

## Cluster-wise CoNMF
第二个思路则是考察$$W$$的L2 norm: $$W^T W$$。因为$$W$$的每列表示一个cluster中每个item的分布，所以$$W^T W$$实际上表示每个cluster之间的相似度。基于此，第二种附加约束为：

$$
R_2 = \sum_{s,t} \lambda_{s,t} \Vert W^{(s)T}W^{(s)} - W^{(t)T}W^{(t)}\Vert
$$

目标函数的优化求解方法同上。

$$W$$和$$H$$的初始化：运行k-means聚类，将其聚类结果作为初始化输入。

总结：这是一篇规矩踏实的好文章，写作清晰，论文调研充分，虽是沿用了前人的算法框架，但是也提出了自己的新约束。对于算法模型，文章详细给出了求解步骤，并解决了一个在实际应用中出现的问题，其他还包括算法初始化输入、时间复杂度分析，以及实现了多个基准工作。总的来说，工作比较完整。

