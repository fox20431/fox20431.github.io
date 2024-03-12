---
title: font tutorial
date: 2024-03-03
---

# 字体教程

## 字体样式

| 英文               | 中文     | 描述 |
| ------------------ | -------- | ---- |
| serif              | 衬线字   |      |
| sans serif（sans） | 无衬线字 |      |
| monospace（mono）  | 等宽字   |      |
| Italic             | 斜体字   |      |

## 字体粗细

粗细在英语也常被描述为 `weight` ，比如 css 样式设计中。

| 术语                                              | 描述                                       |
| ------------------------------------------------- | ------------------------------------------ |
| Thin（纤细）/Hairline（细线）/Ultra Light（极轻） | 非常细的字体，适用于一些特殊设计。         |
| Light（轻）/Extra Light（额外轻）                 | 较为轻盈，适用于一些柔和感觉的设计。       |
| Regular（正常）/Normal（普通）/Book（书体）       | 正常的字体权重，通常是默认文本样式。       |
| Medium（中等）                                    | 介于正常和加粗之间，提供中等的粗细程度。   |
| Semi-bold（半粗体）/Demi-bold（半粗体）           | 比正常稍微加粗一些，但没有达到加粗的程度。 |
| Bold（粗体）                                      | 明显比正常字体更粗，用于强调文本或标题。   |
| Extra Bold（极粗体）/Ultra Bold（超粗体）         | 较为粗重，常用于需要强烈突出的场合。       |
| Black（黑体）/Heavy（重体）                       | 最粗的字体，提供最强烈的突出效果。         |

## 区域描述

##### 字体文件名称后跟`CJK（Chinease Japanese Korean）`，表示该字体支持中日韩语言。

## 字体推荐

| 字体家族                  | 开源 | 描述                                             |
| ------------------------- | ---- | ------------------------------------------------ |
| DejaVu                    | y    | 字库比较全面                                     |
| TeX Gyre                  | y    | 字库比较全面                                     |
| Noto emoji                | y    | google emoji                                     |
| Noto CJK                  | y    | google CJK 支持                                  |
| Souce han sans            | y    | Adobe CJK 支持                                   |
| Liberation Serif          | y    | 用于替代 Times New Roman 的衬线字体              |
| Liberation Sans           | y    | 用于替代 Arial 的无衬线字体                      |
| Liberation Mono           | y    | 用于替代 Courier New 的等宽字体                  |
| google-crosextra Carlito  | y    | 是对 Microsoft 的 Calibri 字体的自由替代品       |
| google-crosextra  Caladea | y    | 是对 Microsoft 的 Cambria 字体的替代品           |
| fira code                 | y    | 由 Mozilla 开发，用于编程，支持连字（ligatures） |

## Q&A

word 与 字体文件 关系：

如果字体家族只包含一个字体文件（通常是常规或正常权重的字体），而没有专门的粗体（Bold）字体文件，Microsoft Word等文字处理软件会尝试通过字形变换的方式来模拟粗体效果。这个过程被称为“伪粗体”（Fake Bold）。

