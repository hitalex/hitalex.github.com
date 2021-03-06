---
layout: post
title: 论文阅读总结
categories: 
- 学术
tags: 
- 论文
- 总结
---

以下列出从8月16号以来直到现在所阅读的论文的总结。

**Topic visualization**

*Visualizing Topic Models* by Allison J.B. Chaney and David M. Blei（AAAI2012）

这篇文章的主要贡献为建立了一个topic model的[可视化系统TMVE](http://www.princeton.edu/~achaney/tmve/wiki100k/browse/topic-presence.html)。训练topic model采用的代码为[David Blei](http://www.cs.princeton.edu/~blei/)的[lda-c](http://www.cs.princeton.edu/~blei/lda-c/index.html)。系统中分别计算了每个topic在整个系统中所占的比例，每个topic中words的分布，topic和topic之间的相似度，每个文档包含某个topic的多少（比例），文档与文档之间的相似度。

*Probabilistic Latent Semantic Visualization: Topic Model for Visualizing Documents* by Tomoharu Iwata, *et al.* （WWW2006）

假定一个visualization space（2维或者3维，之后称作“可视空间”），认为topic和document都在可视空间中存在latent coordinates，这样其实是将topic和document放在同一个空间中，然后再利用欧几里德距离计算它们之间的相似度。在文章中，作者为了得到topic和document在可视空间的坐标，参照LDA的文档生成过程，提出了一种文档生成过程，其中topic和document的坐标都服从多元高斯分布，最后用EM算法求解。

**Bayesian nonparametircs**

*A tutorial on Bayesian nonparametric models* by Samuel J. Gershman and David M. Blei （Journal of Mathematical Psychology 2011）

贝叶斯非参数（Bayesian nonparametircs）方法其实是一种自动模型选择方法，采用Bayes理论，让训练数据来决定模型参数，比如高斯混合模型中cluster的数量。这篇文章主要介绍了高斯混合模型（Gaussian mixture models）、Chinese restaurant process（CRP）以及Indian buffet process（IBP）。问题：目前已经了解了CRP，但还并不了解IBP，对于CRP和Dirichlet process(mixtures) 之间的关系还不明白。

*The Infinite Gaussian Mixture Model* by Carl Edward Rasmussen （NIPS2000）

这篇论文主要讨论的是无穷高斯混合模型，该模型中假设cluster的数量无穷多。CRP和无穷高斯混合模型有一定的联系：在cluster的数目K趋于无穷时，新来的数据点选择cluster的概率值定义非常相似。它们之间具体的联系之后讨论。

*Markov Chain Sampling Methods for Dirichlet Process Mixture Models* by Radford M. Neal

这篇论文主要讨论Dirichlet process mixture model以及Gibbs sampling。

**Topic model application**

*TwitterRank: Finding Topic-sensitive Influential Twitters* by Jianshu Weng, *et al.* （WSDM2010）

TwitterRank基于PageRank，但与PageRank不同的是，重新定义了两个节点间的转移概率，而这个概率和两个节点（两个Twitter用户）在某个topic相似度有关。

*Social-Network Analysis Using Topic Models* by Youngchul Cha and Junghoo Cho （SIGIR2012）

这篇论文声称可以很好的解决popular nodes（具有较多的incoming link，即粉丝很多）问题。其中最引人注目的是*Edge generative model*：将每个follower看作是一个document，每个followed user看作是word，这样对于某个用户document，他所follow的用户就构成了这个文档中的word，其中的隐变量即为topic或者兴趣。

>We use the same notation with LDA. $z$ denotes a labeling of a followed user $g$ with a topic (interest), or simply a topic, $P(z|f)$ denotes the multinomial distribution of topics given a follower $f$, and $P(g|z)$ denotes the multinomial distribution of followed users given a topic. $\alpha$ and $\beta$ are Dirichlet priors, constraining $P(z|f)$ and $P(g|z)$, respectively.

*Modeling User Posting Behavior on Social Media* by Zhiheng Xu, *et al.*（SIGIR2012）

文章认为Twitter用户的转发行为与以下三个方面有关：
* Breaking news
* posts from social friends
* users' intrinsic interest
作者扩展了LDA模型，将这三种原因加入到模型中。这篇文章主要参考了另外两篇文章：Modeling General and Specific Aspects of Documents with a Probabilistic Topic Model（NIPS2006）和Cross-Cultural Analyisi of Blogs and Forums with Mixed-Collection Topic Models（EMNLP2009）。


**总结**

目前看论文存在的问题是：贪多，看论文不仔细，没有能够及时总结论文思想，提取idea。
