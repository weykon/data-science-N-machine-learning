# 流程记录

## 数据清洗
收集的数据将它们规整化
### 包括：
    - 删除缺失值
    - 替换缺失值
    - 标量替换NaN
    - 向前或向后填充缺失值

    > df.dropna()
    > df.replace({NaN:1.00})  #NaN是numpy的
    > df.fillna(12)

### 均值/众数/中值插补
我们可以计算它的平均值或中位数，并使用结果来替换缺失值
> df.salary.fillna(salary_mean,inplace=True)

还有很多关键词
- Hot Deck Imputation

     有了这个，我们可以用从样本中所有观察值中随机选择的值替换观察值的缺失值，并引用具有相似值的变量。

- 重新缩放数据

     以不同的比例统一缩放属性，重新缩放是一种有用的技术，使用 scikit-learn 和 MinMaxScaler 类使所有属性都具有相同的比例。

     ```python
     # 初始化 MinMaxScaler
     s_m =  MinMaxScaler(feature_range = (0, 2))
     rescaledX =  s_m.fit_transform(X)
     ```

- Binarize Data

     这是一个非常有用的过程，通常在**特征工程**中使用二进制参考阈值来操作我们的数据，使用 scikit-learn 和 Binarizer 类。
     ```python
     b_n = Binarizer(threshold = 1.0).fit(X)
     b_X = b_n.transform(X)
     ```

- 修正的
     - 回归插补

          为了保持特征之间的关系，我们可以使用回归插补，基本上是一种技术，我们在缺失数据的特征上拟合回归模型，然后使用该模型预测用于替换缺失值的值.

     - 随机回归插补

          在这种技术中，为了重现特征和标签的相关性，我们向预测值添加随机变化。

- 数学与数据碰撞在一起的分类

   |   分状态类型的 | 量化的
----| :----: | ----
定义 |  |