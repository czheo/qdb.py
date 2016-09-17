# qdb.py
Python Implemented Quine DB

Inspired by https://github.com/gfredericks/quinedb

> Quine DB is a quine that is also a key/value store.
> If your database can't print its own source code, can you really trust it?

# Usage
### Print the source code
```
> python qdb.py
```

### Set key => value
```
> python qdb.py set quine db
```

### Get key
```
> python qdb.py get quine
db
```

### Delete key
```
> python qdb.py delete quine
```

### Dump key => value pairs
```
> python qdb.py dump
quine 	=>	 db
db 	=>	 quine
```

### Flush DB
```
> python qdb.py flushdb
```
