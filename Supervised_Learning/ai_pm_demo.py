# AI产品经理专用：最简单的监督学习理解
# 重点：概念理解，不纠结技术细节

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

print("🤖 AI产品经理学习：监督学习核心概念")
print("="*50)

# 第一步：理解数据
print("\n📊 第一步：理解数据")
iris = load_iris()
print(f"我们有 {iris.data.shape[0]} 个花朵样本")
print(f"每个样本有 {iris.data.shape[1]} 个特征（花萼长宽、花瓣长宽）")
print(f"要预测 {len(iris.target_names)} 种花：{iris.target_names}")

# 看看数据长什么样
df = pd.DataFrame(iris.data, columns=['花萼长', '花萼宽', '花瓣长', '花瓣宽'])
df['花种类'] = iris.target_names[iris.target]
print("\n数据样例：")
print(df.head(3))

# 第二步：准备训练
print("\n🎯 第二步：准备训练")
X = iris.data  # 特征：花的测量数据
y = iris.target  # 标签：花的种类

# 分割数据：70%训练，30%测试
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"训练样本：{len(X_train)} 个")
print(f"测试样本：{len(X_test)} 个")

# 第三步：训练模型
print("\n🧠 第三步：训练AI模型")
model = LogisticRegression()
model.fit(X_train, y_train)  # 这就是"学习"的过程
print("✓ 模型训练完成！AI已经学会识别花的规律了")

# 第四步：测试效果
print("\n📈 第四步：测试AI的识别能力")
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"AI识别准确率：{accuracy:.1%}")

# 看看具体的预测例子
print("\n🔍 具体预测例子：")
for i in range(5):
    true_name = iris.target_names[y_test[i]]
    pred_name = iris.target_names[predictions[i]]
    result = "✅正确" if y_test[i] == predictions[i] else "❌错误"
    print(f"第{i+1}朵花：真实是{true_name}，AI预测是{pred_name} {result}")

print("\n" + "="*50)
print("🎉 恭喜！你已经理解了监督学习的核心流程：")
print("1️⃣ 准备带标签的训练数据（花的特征+种类）")
print("2️⃣ 让AI从数据中学习规律（训练模型）")
print("3️⃣ 用新数据测试AI的预测能力（评估效果）")
print("4️⃣ 根据准确率判断AI是否可以用于产品")

print("\n💡 作为AI产品经理，你需要关注：")
print("• 数据质量：垃圾进，垃圾出")
print("• 准确率：多高的准确率用户才满意？")
print("• 错误处理：AI预测错了怎么办？")
print("• 用户体验：如何向用户展示AI结果？")