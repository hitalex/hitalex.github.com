---
layout: post
title: Problem oriented, not model oriented -- 阶段总结
categories: 
- 学术
- 生活
tags: 
- 问题导向
- 模型导向
- 方法导向
- 阶段总结
---

**阶段总结**

8月4号回到北京，5号休息了一天，之后的一周（6号到10号）就开始在清华听[龙星计划](http://bigeye.au.tsinghua.edu.cn/DragonStar2012/registration.html)，讲课的两位老师分别是余凯和张瞳。余凯目前在百度做多媒体相关的研究，相较于张瞳，他更偏向于工业界的应用（余凯本人也非常幽默），而张瞳则是Rutgers大学教授，Stanford博士毕业，统计学的大牛。对于机器学习这个研究领域来说，5天的暑期课程远远不够，课程期间，余凯主要是介绍了机器学习的一些相关概念，比如[deep learning](http://deeplearning.net/)（我之前则从未听说），张瞳则主要介绍了优化算法、统计理论方面的知识。其实细想起来，整个课程的知识性收获并不太多，主要是开拓了自己的眼界，多认识了几个大牛，比如清华的[朱军](http://www.ml-thu.net/~jun/)，微软的[Tie-Yan Liu](http://research.microsoft.com/en-us/people/tyliu/)，计算所的常虹，香港科大的[杨强](http://www.cse.ust.hk/~qyang/)。非常巧合的是，杨强就是随后在国际会议中心举办的KDD（Knowledge Discovery and Data Mining） 2012的主席（General Chair）。

10号中午在清华吃完饭后又跑到计算所听了[Jure Leskovec](http://cs.stanford.edu/people/jure/)关于社交网络（Social Network）的讲座，回去查找他的主页的时候又一次被震惊：顶级会议（top-tier conference）的paper一堆堆，还加杂着各种best paper。后来才知道，Jure也在KDD 2012的Summer School中也有讲座。

各路大牛齐聚北京，为的就是第一次在中国召开的数据挖掘方面的顶级会议[KDD2012](http://kdd2012.sigkdd.org/)。从周日开始，我又开始出现在国际会议中心里，听KDD的报告。

KDD不愧为“盛会”，今年参加会议的人大约在1000人以上。这次我也是开足了眼界，见到了很多书中和paper中的大牛，简单罗列几个：孙茂松、Jiawei Han、 余凯、杨强、周志华、唐洁、[Michael Jordan](http://www.cs.berkeley.edu/~jordan/)、Michael Kearns、李彦宏、Tie-yan Liu、林智仁、Xiaojin Zhu。这次的KDD和[SIGIR2012](http://www.sigir.org/sigir2012/)会议时间上几乎完全重叠，否则还能见到更多的大牛。在这些大牛中给我留下最深刻印象的是林智仁，他在Industry Practice Expo中做了一个报告：[Experiences and Lessons in Developing Industry-Strength Machine Learning and Data Mining Software](http://kdd2012.sigkdd.org/indexpo.shtml#lin)，主要介绍了他们开发LIBSVM的经历。林教授非常和蔼、幽默，就像个小孩子一般，让人感觉很亲近，整个报告的气氛也非常轻松。

从KDD回来，就开始看论文。经过龙星课程和KDD2012的连番轰炸，我开始真正认识到学术圈子（research community），开始关注一些大牛，开始想着如何才能发高质量的论文。这其中也要感谢杨逍的帮忙，整个KDD期间，我都在跟他讨论、请教。我也必须感到庆幸，这些经历都正好发生在我即将开始真正的实验室学术生活的“前一天”。

**Problem oriented, not model oriented**

我最近一直也在寻找自己的研究方向，自己虽然有些模糊的想法和方向，但还是不够清晰，也不够坚定。从去年看论文开始，一直到现在，我一直都专注于topic model的学习，LDA以及模型求解，再到前几天的模型的应用，我发现我不知不觉到了这样一个误区：先想一个问题，然后再考虑如何用topic model去解决。这不是典型的“有个锤子，就认为满世界都是钉子”思路么？要解决的是实际或者研究问题，模型、方法都只是手段而已。总的来说就是太依赖于某个算法、模型，而忽略了自己要解决的问题，这个问题如此严峻，以至于和我最初的“以问题为导向”（Problem oriented）的研究思路相违背。

**Future posts**

现在我心里还有几篇博文在“孕育”，写下来防止未来自己不认帐:
* 近几天所看的论文的总结，无论如何都要停下来回顾一下自己看的文章，消化一下。
* From dimension reduction to LDA，关于LSA、PLSA和LDA
* Gibbs sampling，以及其C语言实现
* Bayesian non-parametircs
* 读 *Unix编程的艺术* 有感
