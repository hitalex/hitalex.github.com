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

# Predicting the Popularity of Web 2.0 Items Based on User Comments
这篇文章发表在SIGIR 2014上，自然跟搜索有关。其核心思想是：单纯基于内容的相关度分析已经不够，可以借助网络内容（web items）的评论信息来提升搜索准确度，这篇文章基于评论信息，通过预测youtube视频的流行度来对其进行搜索排序。具体的技术方法是建立time-aware bipartite ranking。

首先建立二部图（bipartite graph），其中user和item是其中的两种类型的节点，边表示评论信息。见下图：

![Bipartite User-Item Structures](/images/bipartite-user-item-structure.png)

边上的权重$$w$$表示该评论（可能是多个评论，因为一个用户可能多次评论一个item）对该item的流行度的贡献。作者认为时间越近的评论产生的作用越大，所以定义$$w_{ij}$$如下：

$$
w_{ij} = \delta^{a(t_0 - t_{ij}) + b}
$$

其中，$$t_0$$是搜索排序的时间，$$t_{ij}$$是用户$$u_i$$对$$p_j$$的评论时间，$$a, b$$为常数。

作者对于流行度预测有三个假设（hypotheses），如下：

* H1 - Temporal factor：如果一个item有更多的最近发表的评论，那么它的流行度更高。
* H2 - Social influence factor：如果某个用户的影响力越高，那么他评论的item更可能流行。
* H3 - Current popularity factor：如果一个item当前已经积累了很多浏览数，那么该item未来更可能流行。
下面分别将以上三个假设采用正则优化的思路进行数学公式实现。

## 对于H1和H2的实现

$$
R_1(f) = \frac{1}{2} \sum_{j=1}^n \sum_{i=1}^m w_{ij} (\frac{f(p_j)}{\sqrt{d_j^p}} - \frac{f(u_i)}{\sqrt{d_i^u}})^2
$$

其中，$$d_j^p$$和$$d_i^u$$分别为item $$p_j$$和用户$$u_i$$的weighted degree，$$f(p_j)$$值较大的item将会在排序中获得更靠前的位置。在上面的正则约束中，如果$$p_j$$的weighted degree较大，即该item收到更多的评论，那么$$f(p_j)$$的值也较大（其他变量的值不变），即体现了H1；另外，上式中括号中的第二项较大时，第一项也会较大，即归一化后$$f(u_i)$$也较大时，也就是用户$$u_i$$的影响力较大时，$$f(p_j)$$的值也会较大。

## 对于H2的实现
根据每个用户的朋友数，计算其初始影响力的取值，记为$$u_i^0$$，那么

$$
R_2(f) = \sum_{i=1}^m(f(u_i) - u_i^0)^2
$$

##对于H3的实现
根据在搜索排序时刻的流行度，定义相对流行度的取值$$p_j^0$$，那么

$$
R_3(f) = \sum_{j=1}^n(f(p_j) - p_j^0)^2
$$

最终，目标函数为：$$Q(f) = R_1 + \alpha R_2 + \beta R_3$$。求解方法和上一篇文章的相同：alternating optimization　－－　对于两个变量$$f(p_j)$$和$$f(u_i)$$，分别固定一个，然后优化求解另外一个。求解的最终结果形式在此不再列出。
