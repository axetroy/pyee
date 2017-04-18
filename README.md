## Pyee

A Python event emitter implementation, just for learning...

```python
pyee = Pyee()

def listener(data):
    print('data %s' % data)

pyee.on('say', listener)

pyee.emit('say', 'hi')

```