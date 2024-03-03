# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/21 14:15
# @File    ：demo1_api.py
# @Function:

from openai import OpenAI
import tiktoken
import erniebot


def req_openai():
<<<<<<< HEAD
    # 创建openai实例
    client = OpenAI(base_url='https://api.aigc369.com/v1')  # 读取环境变量的api_key

    # 发送请求：model、messages
=======
    client = OpenAI(api_key='sk-zheshimiyaozheshimiyaozheshimiyaozheshimiyaozheshimiyao')
>>>>>>> 971715595b31ca7c9140cd5fb12a7d1f79ac4454
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        response_format={'type': 'json_object'},
        messages=[
            {'role': 'system', 'content': '你是一个CS专业的老教授，你十分喜欢教学和琢磨内容'},  # system系统消息  背景角色
            # {'role': 'user', 'content': '进阶sql有哪些学习的内容'},
            {'role': 'user', 'content': '给我以BigPicture的形式，总结一下动态规划需要掌握的知识'},  # user表示用户发送的  指示提示
            # {'role': 'assistant', 'content': '我是chatGPT，由openai开发的一款大语言模型'},  # assistant表示AI发送的  回答
        ]
    )

    # 得到响应
    print(completion.choices)  # ChatCompletion类实例
    print(completion.choices[0].message)

    """
    进阶sql有哪些学习的内容
    ChatCompletionMessage(content='进阶SQL学习的内容包括：\n\n1. 子查询：深入学习如何在查询中嵌套使用子查询，以实现更复杂的查询逻辑。\n\n2. 联结（JOIN）查询：掌握多个表之间的关系，学习如何使用不同类型的JOIN操作（如内连接、左连接、右连接、全连接）来获取联结结果。\n\n3. 窗口函数：了解并应用窗口函数，可以在查询结果的基础上进行排序、分组、计数、累计等操作。\n\n4. 索引和性能优化：学习如何设计并使用索引来提高查询效率，并了解一些性能优化的技巧，如使用合适的查询语句、避免全表扫描等。\n\n5. 视图：了解视图的概念和用途，并学习如何创建和使用视图来简化复杂的查询，提高查询的可复用性。\n\n6. 存储过程和函数：学习如何创建和使用存储过程和函数，可以在数据库中定义可重用的代码块，进一步提高开发效率。\n\n7. 事务管理：了解事务的概念和特性，并学习如何使用事务控制语句（如BEGIN、COMMIT、ROLLBACK）来确保数据库操作的一致性和完整性。\n\n8. 数据库管理：学习如何进行数据库备份和恢复、性能监控和调优、安全控制等数据库管理相关的操作。\n\n9. 高级查询技巧：学习一些高级查询技巧，如使用CASE语句、使用WITH语句进行递归查询、使用GROUP BY和HAVING子句进行分组和过滤等。\n\n10. 数据库设计原则：了解数据库设计的原则和规范，包括数据模型设计、表关系建立、范式化等，以及如何进行数据库重构和优化。\n\n以上是进阶SQL学习的一些内容，具体的学习内容和难度可以根据个人需求和实际情况进行调整和深入学习。', role='assistant', function_call=None, tool_calls=None)
    """

    """
    进阶sql有哪些学习的内容
    ChatCompletionMessage(content='进阶SQL学习的内容包括：\n\n1. 复杂查询：学习使用JOIN操作来连接多个表，使用子查询和联合查询等技术来实现复杂查询需求；\n2. 数据库设计和规范化：学习如何设计和规范化数据库，包括确定关系和实体，选择适当的数据类型，设计合适的主键和外键等；\n3. 索引和性能优化：学习使用索引来提高查询性能，并学习如何分析和优化查询的执行计划；\n4. 存储过程和触发器：学习创建和使用存储过程和触发器，以实现复杂的业务逻辑；\n5. 安全性和权限管理：学习如何设置数据库用户和角色，以及如何控制他们的权限和访问级别；\n6. 数据备份和恢复：学习如何备份和恢复数据库，以及如何进行数据迁移和复制；\n7. 数据库分区：学习如何使用分区技术来管理大型数据库，提高查询性能和维护效率；\n8. 高级数据类型和函数：学习如何使用高级数据类型（如数组、JSON、XML等）和函数来处理和查询复杂数据；\n9. OLAP和数据仓库：学习使用OLAP（联机分析处理）和数据仓库技术来处理大量的历史数据和复杂的分析需求；\n10. SQL优化和调试：学习如何识别和解决SQL查询中的性能问题和错误。\n\n以上是进阶SQL学习的一些内容，根据个人需求和实际情况，还可以选择学习其他特定的数据库管理系统（如MySQL、Oracle、SQL Server等）的高级功能和特性。', role='assistant', function_call=None, tool_calls=None)
    """

    """
    panda和spark、flink等对数据处理有哪些共通的和区别
    Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='panda、Spark和Flink都是用于数据处理的工具，它们有一些共通的和区别。以下是它们的一些共通和区别点：\n\n共通点：\n1. 处理大规模数据：Pandas、Spark和Flink都能够处理大规模的数据，它们提供了分布式计算和并行处理的能力，能够有效地处理大量的数据。\n\n2. 数据处理功能：这些工具都提供了丰富的数据处理功能，如数据清洗、转换、过滤、聚合等操作。\n\n3. 数据分析：Pandas、Spark和Flink都支持数据分析任务，它们能够进行统计计算、机器学习、图计算等高级数据分析任务。\n\n区别点：\n1. 编程模型：Pandas是Python的一个数据处理库，使用的是基于单机的DataFrame编程模型。而Spark和Flink是分布式计算框架，使用的是基于集群的数据流编程模型。\n\n2. 运行环境：Pandas是在单机上运行的，适合处理中小规模的数据。而Spark和Flink是运行在分布式集群上的，能够处理大规模数据，并且具有良好的可扩展性。\n\n3. 实时处理：Flink具有流式处理的特性，能够实时处理数据流，支持事件时间和处理时间的语义。而Spark在早期主要关注离线批处理，不过现在也已经提供了流处理的功能。\n\n4. 数据结构：Pandas是基于表格型数据结构的，非常适合进行类似于关系型数据库的操作。而Spark和Flink使用的是分布式数据集（RDD和DataSet/DataStream），它们更适合处理大规模的、非结构化的数据。\n\n总的来说，Pandas适合处理中小规模的数据，Spark适合大规模的离线批处理和流处理，而Flink则更加适合实时流处理。具体选择哪个工具需要根据具体的应用场景和需求来决定。', role='assistant', function_call=None, tool_calls=None))
    ChatCompletionMessage(content='panda、Spark和Flink都是用于数据处理的工具，它们有一些共通的和区别。以下是它们的一些共通和区别点：\n\n共通点：\n1. 处理大规模数据：Pandas、Spark和Flink都能够处理大规模的数据，它们提供了分布式计算和并行处理的能力，能够有效地处理大量的数据。\n\n2. 数据处理功能：这些工具都提供了丰富的数据处理功能，如数据清洗、转换、过滤、聚合等操作。\n\n3. 数据分析：Pandas、Spark和Flink都支持数据分析任务，它们能够进行统计计算、机器学习、图计算等高级数据分析任务。\n\n区别点：\n1. 编程模型：Pandas是Python的一个数据处理库，使用的是基于单机的DataFrame编程模型。而Spark和Flink是分布式计算框架，使用的是基于集群的数据流编程模型。\n\n2. 运行环境：Pandas是在单机上运行的，适合处理中小规模的数据。而Spark和Flink是运行在分布式集群上的，能够处理大规模数据，并且具有良好的可扩展性。\n\n3. 实时处理：Flink具有流式处理的特性，能够实时处理数据流，支持事件时间和处理时间的语义。而Spark在早期主要关注离线批处理，不过现在也已经提供了流处理的功能。\n\n4. 数据结构：Pandas是基于表格型数据结构的，非常适合进行类似于关系型数据库的操作。而Spark和Flink使用的是分布式数据集（RDD和DataSet/DataStream），它们更适合处理大规模的、非结构化的数据。\n\n总的来说，Pandas适合处理中小规模的数据，Spark适合大规模的离线批处理和流处理，而Flink则更加适合实时流处理。具体选择哪个工具需要根据具体的应用场景和需求来决定。', role='assistant', function_call=None, tool_calls=None)
    """

    """
    给我以BigPicture的形式，总结一下动态规划需要掌握的知识
    [Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='当涉及到动态规划（Dynamic Programming）时，以下是你需要掌握的核心知识：\n\n1. 递归与迭代关系：理解递归和迭代之间的联系以及它们在解决问题中的应用。\n\n2. 最优子结构：理解最优子结构的概念，即问题具有可分解成互不依赖的子问题并可以通过组合子问题的最优解来得到整体问题的最优解。\n\n3. 重叠子问题性质：了解动态规划问题中常常存在的重叠子问题，并懂得如何通过记忆化或表格来避免重复计算。\n\n4. 状态转移方程：掌握如何定义问题的状态、状态之间的关系以及状态转移方程的构建，这是动态规划问题的核心。\n\n5. 问题拆解与求解顺序：学会将复杂的问题拆解为多个简单的子问题，并确定求解子问题的顺序，其中的关键在于处理子问题时所需的其他子问题的结果是否已经求解完毕。\n\n6. 基本解法：了解基本的动态规划解法方法，如自顶向下的记忆化搜索（Top-Down Memoization）和自底向上的迭代求解（Bottom-Up Iteration）。\n\n7. 空间优化：学会通过状态压缩、滚动数组等技巧来减少动态规划解法中所需的额外空间。\n\n8. 常见问题类型：熟悉常见的动态规划问题类型，如背包问题、最长递增子序列、编辑距离等，并掌握相应的解决思路和算法。\n\n9. 实战经验：通过实际问题的练习和实战，不断积累动态规划的应用经验，并学会优化算法以提高效率。\n\n总结起来，掌握动态规划需要了解其核心概念和解题思路，熟悉相关的算法技巧，并通过实践不断提升自己的解题能力。', role='assistant', function_call=None, tool_calls=None))]
    ChatCompletionMessage(content='当涉及到动态规划（Dynamic Programming）时，以下是你需要掌握的核心知识：\n\n1. 递归与迭代关系：理解递归和迭代之间的联系以及它们在解决问题中的应用。\n\n2. 最优子结构：理解最优子结构的概念，即问题具有可分解成互不依赖的子问题并可以通过组合子问题的最优解来得到整体问题的最优解。\n\n3. 重叠子问题性质：了解动态规划问题中常常存在的重叠子问题，并懂得如何通过记忆化或表格来避免重复计算。\n\n4. 状态转移方程：掌握如何定义问题的状态、状态之间的关系以及状态转移方程的构建，这是动态规划问题的核心。\n\n5. 问题拆解与求解顺序：学会将复杂的问题拆解为多个简单的子问题，并确定求解子问题的顺序，其中的关键在于处理子问题时所需的其他子问题的结果是否已经求解完毕。\n\n6. 基本解法：了解基本的动态规划解法方法，如自顶向下的记忆化搜索（Top-Down Memoization）和自底向上的迭代求解（Bottom-Up Iteration）。\n\n7. 空间优化：学会通过状态压缩、滚动数组等技巧来减少动态规划解法中所需的额外空间。\n\n8. 常见问题类型：熟悉常见的动态规划问题类型，如背包问题、最长递增子序列、编辑距离等，并掌握相应的解决思路和算法。\n\n9. 实战经验：通过实际问题的练习和实战，不断积累动态规划的应用经验，并学会优化算法以提高效率。\n\n总结起来，掌握动态规划需要了解其核心概念和解题思路，熟悉相关的算法技巧，并通过实践不断提升自己的解题能力。', role='assistant', function_call=None, tool_calls=None)
    """


def cal_token():
    """ openai官方的token分词，不需要消耗token """
    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')  # 传入模型名 返回对应编码器
    res = encoding.encode('周公恐惧流言日，王莽谦恭未篡时。')
    print(res)  # tokenId列表  [41642, 35417, 21555, 238, 33565, 100, 89753, 78244, 9080, 3922, 29207, 233,
    print(len(res))  # 24token


def req_wenxin_erniebot():
    resp = erniebot.ChatCompletion.create(
        model='ernie-3.5',
        messages=[
            {'role': 'user', 'content': '你觉得chatGPT厉害，还是文心一言厉害'}
        ]
    )
    print(resp.get_result())


if __name__ == '__main__':
    req_openai()
    # cal_token()
