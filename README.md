

### 生成项目依赖文件requirements.txt
``` pipreqs . --encoding=utf8 --force```

### grpc-tools 生成python文件
```python -m grpc_tools.protoc -I./protos --python_out=./rpc_packages/ --grpc_python_out=./rpc_packages/ pay.proto```

### protobuf 数据类型
 - string：字符串
 - bytes：字节
 - bool：布尔
 - int32：32位整型
 - int64：64位整型
 - float：浮点型
 - repeated：数组  eg: repeated string data = 1;
 - map：字典  eg: map <string, string> data = 1;
 
### protobuf 关键字
 - package：包名
 - syntax：protobuf版本
 - service：定义服务
 - rpc：定义服务中的方法
 - stream：定义的方法为流传输
 - message：定义消息体
 - extend：扩展消息体
 - import：导入一些插件
 - //：注释
 