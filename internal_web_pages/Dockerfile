ARG BUILD_FROM
FROM $BUILD_FROM

# 安装必要的包
RUN apk add --no-cache python3 py3-pip nginx

# 复制文件
COPY rootfs /
COPY run.sh /
RUN chmod a+x /run.sh

# 安装Python依赖
RUN pip3 install aiohttp jinja2

WORKDIR /
CMD [ "/run.sh" ] 