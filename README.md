# 爬虫练习平台

![Deploy to Kubernetes](https://github.com/Germey/Scrape/workflows/Deploy%20to%20Kubernetes/badge.svg)

网络爬虫实验平台，包含多个样例，如纯静态网站、动态渲染网站、字体反爬网站、登录验证网站、验证码验证网站、反代理网站、JavaScript混淆及加密网站等，持续更新中。

## 案例介绍

本平台自爬数据、自建页面、自接反爬，案例稳定后永不过期，适合教学与练习。

### 模拟登录网站

* [login1](https://login1.scrape.cuiqingcai.com/)：登录时用户名和密码经过加密处理，适合 JavaScript 逆向分析。

### 验证码网站

* [captcha1](https://captcha1.scrape.cuiqingcai.com/)：对接滑动拼图验证码，适合滑动拼图验证码分析处理。
* [captcha2](https://captcha2.scrape.cuiqingcai.com/)：对接图标点选验证码，适合图标点选验证码分析处理。
* [captcha3](https://captcha3.scrape.cuiqingcai.com/)：对接图文点选验证码，适合图文点选验证码分析处理。
* [captcha4](https://captcha4.scrape.cuiqingcai.com/)：对接语序分析验证码，适合语序分析验证码分析处理。
* [captcha5](https://captcha5.scrape.cuiqingcai.com/)：对接空间推理验证码，适合空间推理验证码分析处理。
* [captcha6](https://captcha6.scrape.cuiqingcai.com/)：对接九宫格识图验证码，适合九宫格识图验证码分析处理。

### 静态渲染网站

* [static1](https://static1.scrape.cuiqingcai.com/)：猫眼电影数据网站，数据通过服务端渲染，适合基本爬虫练习。

### 动态渲染网站

* [dynamic1](https://dynamic1.scrape.cuiqingcai.com/)：猫眼电影数据网站，数据通过 Ajax 加载，页面动态渲染，适合 Ajax 分析和动态页面渲染爬取。
* [dynamic2](https://dynamic2.scrape.cuiqingcai.com/)：猫眼电影数据网站，数据通过 Ajax 加载，数据接口参数加密且有时间限制，适合动态页面渲染爬取或 JavaScript 逆向分析。
* [dynamic3](https://dynamic3.scrape.cuiqingcai.com/)：猫眼电影数据网站，数据通过 Ajax 加载，无页码翻页，适合 Ajax 分析和动态页面渲染抓取。
* [dynamic4](https://dynamic4.scrape.cuiqingcai.com/)：猫眼电影数据网站，数据通过 Ajax 加载，无页码翻页，适合 Ajax 分析和动态页面渲染抓取。

## 自动部署

本平台采用 GitHub Actions + Kubernetes 自动化部署，详情见 [WorkFlow](https://github.com/Germey/Scrape/tree/master/.github/workflows)。
