# Home Assistant Internal Web Pages Add-on

这个 Home Assistant 加载项允许你将内网的 Web 页面安全地嵌入到 Home Assistant 的侧边栏中。

## 安装

1. 在 Home Assistant 中，导航到 Supervisor → Add-on Store
2. 点击右上角的菜单按钮，选择 "Repositories"
3. 添加此仓库的 URL: `https://github.com/YOUR_USERNAME/ha-internal-web-pages`
4. 在加载项商店中找到 "Internal Web Pages" 并安装

## 功能

- 支持多个内网页面的嵌入
- 通过 Home Assistant 的 ingress 功能实现安全访问
- 支持自定义页面图标
- 支持 WebSocket 连接
- 无需暴露内网端口

## 配置

配置示例:

```yaml
pages:
  - name: "NAS管理页面"
    url: "http://192.168.1.100:5000"
    icon: "mdi:nas"
  - name: "路由器管理"
    url: "http://192.168.1.1"
    icon: "mdi:router"
```

更多详细信息请参考 [DOCS.md](internal_web_pages/DOCS.md)。 