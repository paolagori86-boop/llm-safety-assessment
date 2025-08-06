# LLM Safety and Alignment Assessment

本项目用于评估大语言模型（LLM）的安全性和对齐性能，包含提示工程、风险检测、输出评估等模块，适用于 Anthropic Claude 接口调用。

## 项目结构

- `runner.py`：主运行器，用于发送 prompt 和接收响应
- `evaluator.py`：分析响应并进行偏见/有害内容检测
- `prompts/`：预设的提示模板
- `detection/`：各种检测算法模块
- `helpers/`：辅助函数
- `tests/`：单元测试
- `examples/`：运行样例

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python src/runner.py --model anthropic-claude-v1 --prompts src/prompts/prompt_templates.json
python src/evaluator.py --input examples/example_runs.json --output report.json
```

## 项目目标

- 检测模型输出中的偏见与有害内容
- 测试多种 prompt 工程策略
- 提供自动化评估与报告生成功能
