# 一个练习Prompt Flow的地方

## 1. 什么是Prompt Flow
可以参考 https://microsoft.github.io/promptflow/index.html
一个用于使用LLM大语言模型进行可视化处理的工具/框架。同时还提供评估、调试、部署等功能。可以说是一站式LLMOps工具。

## 2. 本练习的内容

你在为一个教育行业创建一系列LLM结合的功能。本工程里面包括的是通过提供内容，创建考试卷子的功能。你可以通过提供内容，针对内容可以选择出题的类型，题目的个数，配合题目的选项信息等。

1. 分类题目(Category)
2. 多选题(MultipleChoice)

## 3. 目录分工
1. 根目录每个题型有自己的folder，内部包括promptflow相关的代码和配置文件。
2. evaluation folder里面是评估的代码，用于评估模型的准确性。按照题型分folder。

