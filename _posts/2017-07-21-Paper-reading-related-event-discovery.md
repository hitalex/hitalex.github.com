---
layout: post
title: 论文阅读笔记：Related Event Discovery [WSDM 2017]
categories: 
- 论文阅读
tags: 
- 事件发现 无监督学习
---

今天跟大家分享的论文是发表在2017年WSDM会议上的一篇文章：Related Event Discovery。文章主要解决的问题是：给定一个事件及其相关描述，在候选事件集合中找到与该事件具有语义关联的事件。

从问题定义出发，我们可以问出以下几个问题：
1. “事件”如何定义？事件是否属于某个领域？
2. 事件的相关描述包括哪几部分？
3. “语义相关”如何定义？ 
4. 在做实验时，候选的事件集合如何确定？
5. 具体的问题输出是什么样的？

接下来我们来看一看这篇文章针对这几个问题所提出的解决方案或相关讨论。

第一、这篇文章中的“事件”指的是被计划安排的活动事件，比如hiking、movie、tour等，跟突发事件相对应，而且并没有特定的领域属性。另外，这里的事件跟传统NLP中的事件也不一样：这里的事件属性可能包括时间、地点、参与人员、相关描述等等。

下面是两个query events以及文章所提出的方法得到的结果：

![Example of relateds events, retrieved by our system in response to example query events](/images/related-event-discovery-example-related-events.png)

 第二、事件的相关描述主要体现为用于事件发现算法的特征，主要包括以下几个部分：标题、周围的文本、对应该事件的搜索关键词、锚文本（Anchor text）、分类信息（Taxonomy）。可以看出主要还是用了文本信息。
 
 第三、“语义相关”如何定义？在NLP中，关于“语义”的准确定义一直没有明确的方法，本质上还是因为每个人对于两段文本是否“语义相关”具有不同的看法。文章所采用的相关事件发现方法体现了作者对于语义相关性的理解。
 
 作者在本文中提出了两种相关事件发现的方法 ，分别是COMBINER和EXPANDER，都属于无监督的方法。整体的方法流程如下：
 
 ![相关事件发现方法流程](/images/related-event-discovery-method-overview.png)
 
 COMBINER方法的思想很简单：分别针对以上讨论的每个特征，依据KL距离计算目标事件（query event）和各个候选事件的相似度，并得到一个排序结果，最终应用Reciprocal Rank Fusion方法综合多个排序结果得到最终的排序结果。其中，Reciprocal Rank Fusion方法的具体表述如下：
 $$
 sc(S,T) = \Sigma_j{\frac{1}{r_{S,T}^j} + K}
 $$
 其中，$S$表示目标事件，$T$表示某个候选事件，$j$用于索引各个排序方法，$r_{S,T}^j$表示第$j$个排序结果中，候选事件$T$的排名。
 
 EXPANDER方法主要基于label propagation：首先构建一个二部图，两种节点类型分别是特征（词组）和事件：如果事件中包含该特征，则连接该事件和特征。如下所示：
  
  ![EXPANDER方法](/images/related-event-discovery-expander.png)
  
  在EXPANDER方法中，label为每个event，在初始运行时由于不知道哪些event是相关的，则每个event只标记和自己是相关的。最终，该方法得到的结果是每个event节点对应一个label（即event）的分布情况，即得到与每个event相关的额事件列表。
  
  第四、在做实验时，这篇文章的候选事件集合是由COMBINER和EXPANDER两个方法运行的结果，显然并不合适，因为有可能存在更为相关的事件，但并没有被以上两个方法检测到。
  
  第五、具体的输出是针对目标事件的相关事件列表，按照相关度排序。这本质上是一个排序问题，所以作者也对比了几个排序算法，包括RankBoost、Coordinate Ascent等。需要注意的是，这里所用的排序学习算法都是有监督方法。实验效果也表明，这些排序学习算法的效果确实比文章所提出的无监督学习方法的效果更好。实验结果如下所示：
  
    ![实验结果](/images/related-event-discovery-experiment-result.png)
  
  短评：从研究问题上来说，相关事件检索/检测的相关研究确实不多，相关性比较难判断是一个原因；从研究方法来看，文章所用的无监督方法并不复杂，主要还是应用了文本数据作为特征，并没有使用事件中包含的实体信息，以及其他事件属性信息。