import json

json_str = '''
{
"name": "Alice",
  "age": 25,
  "skills": ["Python", "Java", "C++"],
  "address": { "city": "Taipei", "zipcode": "100" }
}
'''

# 解析 JSON
data = json.loads(json_str)

# 提取數據
print("姓名:", data["name"])  # Alice
print("技能的第二個元素:", data["skills"][1])  # Java
print("城市:", data["address"]["city"])  # Taipei
