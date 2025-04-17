# Internal Web Pages Add-on

这个Home Assistant加载项允许你将内网的Web页面嵌入到Home Assistant的侧边栏中，无需向公网暴露端口即可访问。

## 功能特点

- 支持多个内网页面的嵌入
- 通过Home Assistant的ingress功能实现安全访问
- 支持自定义页面图标
- 支持WebSocket连接

## 配置

在加载项配置中，你可以定义要嵌入的页面：

```yaml
pages:
  - name: "示例页面"    # 页面在侧边栏中显示的名称
    url: "http://192.168.1.100"  # 内网页面的URL
    icon: "mdi:web"    # Material Design图标名称
```

### 配置选项

每个页面配置项包含以下字段：

| 选项 | 描述 |
|------|------|
| name | 页面显示名称 |
| url | 内网页面的URL地址 |
| icon | Material Design图标名称 |

## 使用方法

1. 在Home Assistant的加载项商店中安装此加载项
2. 配置你想要嵌入的内网页面
3. 启动加载项
4. 在Home Assistant的侧边栏中即可看到配置的页面

## 注意事项

- 确保Home Assistant能够访问到配置的内网页面
- 某些网页可能会因为安全策略限制而无法正常显示
- 建议使用HTTPS协议访问Home Assistant以确保安全性

## 支持

如果你遇到问题或需要帮助，请访问GitHub仓库提交issue。 