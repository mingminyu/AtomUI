md_message_example = '''
在 ECharts 中，如果你希望自动排列节点坐标，你可以使用布局算法。ECharts 提供了一些布局算法，其中之一是力导向图（Force-directed Graph）布局，它可以自动调整节点的位置，使得图形更加美观。

以下是一个简单的力导向图布局的示例：

```javascript
option = {
    series: [{
        type: 'graph',
        layout: 'force',
        force: {
            repulsion: 100,  // 节点之间的斥力
            edgeLength: 150,  // 连接线的默认长度
        },
        data: [{
            name: 'Node 1',
        }, {
            name: 'Node 2',
        }, {
            name: 'Node 3',
        }],
        links: [{
            source: 'Node 1',
            target: 'Node 2',
        }, {
            source: 'Node 2',
            target: 'Node 3',
        }],
    }],
};
```

在这个例子中，通过将 `layout` 设置为 `'force'`，并调整 `repulsion` 参数来调整节点之间的斥力，可以实现自动排列节点坐标。布局算法会根据节点之间的关系和斥力，自动计算节点的位置。

```python
import os

print(123)
```

你可以根据实际需求调整 `repulsion` 和其他参数，以便获得满足你设计需求的图形布局。此外，ECharts 还提供其他布局算法，如环形布局、树状布局等，你可以根据具体情况选择合适的布局算法。
'''