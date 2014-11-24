---
layout: post
title: Appplying Gibbs sampling inference to Naive Bayes classification
categories: 
- 学术
- 技术分享
tags: 
- Gibbs sampling
- Naive Bayes
- text categorization
- semi-supervised learning
---

Naive Bayes（naive的另外一种写法为naïve，见[这里](http://en.wiktionary.org/wiki/na%C3%AFve)），即朴素贝叶斯，是一种应用贝叶斯原理的简单分类器，常用于文本分类，它基于这样的假设：每个文档中的单词生成都是独立的（所以它是Naive的），并且并不考虑单词之间的顺序（Bag-Of-Words，BOW模型）。在自然语言处理（Natural Language Processing，NLP）领域中，这样的模型被称为Unigram model，当然还有Bigram，Trigram，甚至n-gram model。在n-gram model（n>1）中，单词与单词之间不再独立，而是有一定的转移概率 `\(P(w_2 | w_1)\)`。举一个简单的例子，比如“我”字后面出现“们”的概率显然比出现“中”的概率大，而在unigram model中则并不考虑这种概率差异。不过即便有这样简单的假设，Naive Bayes方法依然强大。

这里并不打算介绍Naive Bayes的细节，只是推荐两篇文章：
* **Parameter estimation for text analysis**，这篇文章主要介绍参数估计的方法，循序渐进，从极大似然估计（Maximum likelyhood，ML）、最大后验（Maximum A Posteriori，MAP）再到Bayesian estimation，得到估计参数的分布，最后详细推导了LDA（Latent Dirichlet Allocation）的Gibbs sampling推导。
* **Gibbs sampling for the unitialiated**，这篇文章主要介绍了Gibbs sampling，另外还将Gibbs sampling应用到Naive Bayes模型的推导，分析步骤很详细，值得一读。以下简称Unitialiated。

如果你已经读了至少Gibbs sampling for the unitialiated这篇文章，或者本来理解Gibss sampling，我建议你继续阅读。

我将Naive Bayes应用于文本分类（采用的数据集在[这里](http://web.ist.utl.pt/~acardoso/datasets/)），并尝试使用Gibbs sampling推导模型参数，参照Unitialiated这篇文章中的伪代码。
