---
title: office addins development
date: 2023-07-30
---



# Office Add-ins Development

微软办公套件开发

## Prerequisites 

需要掌握前端开发技能；

前端开发环境 + Office客户端下载；

## Get Started

For more details see [the official documentation](https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/word-quickstart?tabs=yeomangenerator).

1. Install scaffolding tools

   ```shell
   npm install -g yo generator-office
   ```

2. Create the add-in project

   ```shell
   yo office
   ```

3. Select `Office Add-in Task Pane Project` -> language you wanna use -> your project name -> Which Office application you wanna support

4. The craffolding tools generate the wordspace, get in:

   ```shell
   cd <your_project_name>
   code .
   ```

5. Start the project:

   ```shell
   npm run
   ```

   

## Develop and Test

Check [the Documentation API](https://learn.microsoft.com/en-us/office/dev/add-ins/tutorials/word-tutorial)

## Build and Realease

构建和发布

