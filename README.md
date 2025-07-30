pdf-crop-to-white-margin
裁剪PDF到白边（包括图片型PDF）



# PDF裁剪到白边工具（macOS）

这是一个用于 **自动裁剪PDF页面至文字边缘（白边）** 的小工具，专为 macOS 用户设计。

📌 适用于以下用户：
- 想去除PDF大段空白页边
- 想快速裁剪至正文区域
- 想用 Automator 拖拽一键处理

---

## 🧰 功能简介

- 📄 自动检测文字区域并设置裁剪框（CropBox）
- 🖱️ 支持 macOS 拖拽操作（.app 格式）
- 🧠 多页PDF批量处理
- 🛡️ 开源自由使用（BSD 2-Clause）

---

## 📂 文件结构

```text
pdf-crop-to-white-margin/
├── crop_pdf_to_textbox.py         # 主脚本，基于 PyMuPDF
├── 裁剪到文本框.app              # macOS 自动化应用，支持拖拽
├── LICENSE                        # BSD 2-Clause 许可证
└── README.md                      # 自述文件
```
---

## 🚀 使用方法

### ✅ 方法一：macOS 应用（推荐）

1. 将 PDF 文件拖到 `裁剪到文本框.app` 图标上
2. 输入 margin（point）  
<img src="https://github.com/user-attachments/assets/d906cf71-d997-4e75-97eb-89341cda1ffd" width="456" height="212" style="display: block; margin: 0;" />  <br>
3. 运行完成后提示  
<img width="382" height="94" alt="image" src="https://github.com/user-attachments/assets/ea98592e-e168-494a-8a04-7efb46c0231a" />

4. 同目录下生成裁剪后版本，命名为 `output_cropped-原文件名.pdf`

#### ⚠️ 注意事项（重要）

请根据你本地环境修改 `Automator` 中的“运行 Shell 脚本”内容：

```bash
/usr/local/bin/python3 "/Users/你的用户名/路径/crop_pdf_to_textbox.py" "$@"
```
1.	/usr/local/bin/python3 是你安装的 Python 路径（可用 which python3 查看）
2.	"..." 内是你的脚本实际路径，建议使用绝对路径
3.	"$@" 表示拖入的 PDF 文件路径（自动传参）

修改方法：在 Automator 中右键“工作流” → 编辑 “运行 Shell 脚本” → 替换上述命令

---

🧑‍💻 方法二：命令行执行脚本

安装依赖：
```
pip install pymupdf
```
执行脚本：
```
python3 crop_pdf_to_textbox.py 输入.pdf 输出.pdf
```
---

🛠 技术说明

1.基于 PyMuPDF 实现  
2.自动识别每页可见文本区域，设置 CropBox  
3.留原始文件不变，输出新文件

---

📄 许可证 License

本项目使用 BSD 2-Clause License 开源。

简要条款如下：  
1.✅ 可以自由使用、修改、分发、商用  
2.❗ 需要保留原始作者的版权声明和免责声明  
3.🚫 禁止使用作者名字做推广或背书

详细内容见 LICENSE 文件。


---

🙋 常见问题

Q: 支持纯图片PDF吗？
A: 支持。需要 PDF 先自行转为高精度OCR PDF。

Q: 运行失败提示缺模块？
A: 请先执行 pip install pymupdf 安装依赖。

---

📬 联系方式

如需反馈、建议或协作，请通过 GitHub 提交 Issue，或联系作者邮箱：
Ragdoll@dad.ac.cn
