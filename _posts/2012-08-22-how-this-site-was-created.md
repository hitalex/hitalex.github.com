---
layout: post
title: 第一篇博文
categories:
- 技术分享
tags:
- DNSPOD
- Godaddy
- Jekyll
- Github
- Disqus
- Markdown
---

**博客搭建**
博客的基本框架算是搭建成功了，这篇文章算作是第一篇留作纪念，另外一个目的是测试一下发布系统。整个博客使用[Github pages](http://pages.github.com/)服务，省去了购买VPS、设置服务器等一些列繁杂的工作，当然也省了不少钱。这样一来，维护博客的唯一费用就只有域名托管。我是在Godadday申请域名：alexkong.net，每年9.99美元，使用[DNSPOD](https://www.dnspod.cn/)提供的DNS服务，评论则是采用的[Disqus](http://www.disqus.com/)。关于Github博客搭建的详细过程，可以参展[BeiYuu的文章](http://beiyuu.com/github-pages/ "使用Github Pages建独立博客")。

**一些细节**
假设你已经按照BeiYuu的步骤在搭建自己的博客。其中一步是安装Github所支持的[Jekyll](https://github.com/mojombo/jekyll)静态发布系统，在这之前还要安装Rubygem（Ruby的包管理器）。需要提醒的是，Jekyll对Ruby版本要求是1.9.x，并要求1.9.x版本Ruby所对应的Rubygem。我的操作系统是Ubuntu 10.10（我知道这个版本很老...），在系统的源中的Ruby和Rubygem都不满足安装Jekyll的要求。我的建议是到Ruby和Rubygem的官方网站下载最新的版本并安装。

对于Windows用户，Jekyll有可能出现编码问题，请参照[这里](http://chxt6896.github.com/blog/2012/02/13/blog-jekyll-native.html "Jekyll 本地调试之若干问题")

Jekyll同样是作为开源软件提供给大家使用（并托管在Github上），所以Bug在所难免，希望大家能有包容的心态。如果在安装或者使用的过程中出了问题，我建议：
* 详细阅读控制台的错误输出，并Google之，查看是否还有人有同样的问题。相信90%的问题到这里应该都已经被解决了。
* 如果没有找到相似的问题，自己尝试阅读出问题的代码（Jekyll使用Ruby写成），自己动手解决。
* 如果自己无法解决，可以浏览Jekyll在Gibhub上的Issue页面，查看此问题是否已经在被讨论；如果自己确实找到了Jekyll的Bug，可以fork Jekyll项目，然后铲除Bug，为开源社区做些贡献。

本博客的模板是在[Yihui Xie](http://yihui.name "Yihui Xie")博客的基础上修改而成，在此想yihui表示感谢！

**Markdown写作环境**
Jekyll支持Markdown语法，对我来说，Markdown是最理想的写作环境。为什么这么说呢？因为Markdown将外部干扰降到了最低，其语法也简单简洁。作为史上最成功的排版系统，LaTex的语法的确要复杂一些，源文件看起来更乱，不过，至少现在看来，它的排版能力要比Markdown强。我无意于比较Markdown和LaTex孰优孰劣，而是关注与两者都尽可能的将“外部干扰”降到最低 -- 你只需要按照语法写文本文档即可。你简直无法想象，将宝贵的时间花在：用鼠标小心奕奕地调整图片或文本框大小、设置页码、用Mathtype输入公式、调整行距等等这些，是多么不明智！而这其中最关键的是，这些琐事无法让你**集中精神在写作内容上**，而内容本身，包括用词、思路和逻辑，才是最重要的。

**关于今后的博文**
这个博客将是我人生的记录，今后可能会包括一些看法见解，技术分享还有学习总结，其中有一部分肯定是关于论文阅读心得。贵在坚持，并希望大家监督！

今后几天，我将会从人人网、cnblog和豆瓣中搬过来几篇之前写的东西，希望大家多多批评！
