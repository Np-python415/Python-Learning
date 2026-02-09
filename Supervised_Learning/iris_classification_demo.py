# AI产品经理学习：鸢尾花分类示例
# 目标：理解监督学习的完整流程

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

print("=== AI产品经理学习：监督学习实践 ===\n")

# 1. 数据加载和探索
print("1. 数据加载和探索")
print("-" * 30)

# 加载鸢尾花数据集（这是机器学习的经典数据集）
iris = load_iris()
print(f"数据集描述：{iris.DESCR[:200]}...")
print()

# 查看数据格式
print("数据格式分析：")
print(f"特征数据形状：{iris.data.shape}")  # (样本数, 特征数)
print(f"标签数据形状：{iris.target.shape}")  # (样本数,)
print(f"特征名称：{iris.feature_names}")
print(f"类别名称：{iris.target_names}")
print()

# 将数据转换为DataFrame，方便查看
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

print("前5行数据预览：")
print(df.head())
print()

print("数据统计信息：")
print(df.describe())
print()

# 2. 数据准备（这是AI产品经理需要理解的关键步骤）
print("2. 数据准备")
print("-" * 30)

# 特征（X）和标签（y）
X = iris.data  # 特征：花萼长度、花萼宽度、花瓣长度、花瓣宽度
y = iris.target  # 标签：0=setosa, 1=versicolor, 2=virginica

print("特征数据（X）示例：")
print("前3个样本的特征：")
for i in range(3):
    print(f"样本{i + 1}: 花萼长度={X[i][0]:.1f}, 花萼宽度={X[i][1]:.1f}, "
          f"花瓣长度={X[i][2]:.1f}, 花瓣宽度={X[i][3]:.1f}")

print("\n标签数据（y）示例：")
print("前10个样本的标签：", y[:10])
print("标签含义：0=山鸢尾, 1=变色鸢尾, 2=维吉尼亚鸢尾")
print()

# 数据分割：训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,  # 30%用于测试
    random_state=42,  # 固定随机种子，确保结果可重复
    stratify=y  # 保证每个类别在训练集和测试集中的比例相同
)

print("数据分割结果：")
print(f"训练集大小：{X_train.shape[0]} 个样本")
print(f"测试集大小：{X_test.shape[0]} 个样本")
print(f"训练集标签分布：{np.bincount(y_train)}")
print(f"测试集标签分布：{np.bincount(y_test)}")
print()

# 3. 模型训练（AI产品经理需要理解不同算法的特点）
print("3. 模型训练")
print("-" * 30)

# 尝试两种不同的算法
models = {
    '逻辑回归': LogisticRegression(random_state=42),
    '决策树': DecisionTreeClassifier(random_state=42)
}

trained_models = {}

for name, model in models.items():
    print(f"训练{name}模型...")

    # 训练模型
    model.fit(X_train, y_train)
    trained_models[name] = model

    print(f"✓ {name}模型训练完成")

print()

# 4. 模型预测和评估（AI产品经理最需要关注的部分）
print("4. 模型预测和评估")
print("-" * 30)

for name, model in trained_models.items():
    print(f"\n=== {name}模型评估 ===")

    # 预测
    y_pred = model.predict(X_test)

    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    print(f"准确率：{accuracy:.3f} ({accuracy * 100:.1f}%)")

    # 详细的分类报告
    print("\n详细评估报告：")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    # 混淆矩阵（显示预测错误的情况）
    cm = confusion_matrix(y_test, y_pred)
    print("混淆矩阵：")
    print("行=真实标签，列=预测标签")
    print(cm)

    # 展示几个具体的预测例子
    print(f"\n前5个测试样本的预测结果：")
    for i in range(5):
        true_label = iris.target_names[y_test[i]]
        pred_label = iris.target_names[y_pred[i]]
        confidence = "✓" if y_test[i] == y_pred[i] else "✗"
        print(f"样本{i + 1}: 真实={true_label}, 预测={pred_label} {confidence}")

print("\n" + "=" * 50)

# 5. AI产品经理的关键理解点
print("5. AI产品经理的关键理解点")
print("-" * 30)

print("""
从这个例子中，AI产品经理应该理解：

📊 数据格式：
- 特征（X）：每个样本的属性，如花瓣长度、宽度等
- 标签（y）：我们要预测的目标，如花的种类
- 数据质量直接影响模型效果

🔄 训练流程：
- 数据分割：训练集用于学习，测试集用于验证
- 模型训练：算法从训练数据中学习规律
- 模型预测：用学到的规律预测新数据

📈 评估指标：
- 准确率：预测正确的比例（最直观的指标）
- 精确率：预测为正例中真正为正例的比例
- 召回率：真正的正例中被预测为正例的比例
- F1-score：精确率和召回率的调和平均

🎯 产品应用思考：
- 如果这是一个花卉识别App，95%的准确率够用吗？
- 用户上传模糊照片时，模型可能预测错误，如何处理？
- 如何向用户展示预测结果和置信度？
- 需要多少训练数据才能达到产品要求？
""")

# 6. 简单的可视化（帮助理解）
print("\n6. 数据可视化")
print("-" * 30)

# 创建一个简单的散点图
plt.figure(figsize=(10, 6))

# 绘制不同类别的数据点
colors = ['red', 'green', 'blue']
for i, species in enumerate(iris.target_names):
    mask = iris.target == i
    plt.scatter(iris.data[mask, 0], iris.data[mask, 1],
                c=colors[i], label=species, alpha=0.7)

plt.xlabel('花萼长度 (cm)')
plt.ylabel('花萼宽度 (cm)')
plt.title('鸢尾花数据分布')
plt.legend()
plt.grid(True, alpha=0.3)

# 保存图片
plt.savefig('iris_data_visualization.png', dpi=300, bbox_inches='tight')
print("✓ 数据可视化图片已保存为 'iris_data_visualization.png'")

plt.show()

print("\n" + "=" * 50)
print("🎉 监督学习实践完成！")
print("作为AI产品经理，你现在理解了：")
print("1. 监督学习的完整流程")
print("2. 数据格式和预处理的重要性")
print("3. 模型训练和预测的过程")
print("4. 如何评估模型效果")
print("5. 如何从产品角度思考AI应用")