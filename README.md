# Python-Tutorial

Python Tutorials

## Setup env

### Create

To install everything from scratch

```bash
conda env create --prefix ./env --file environment.yml --force
```

### Update

If new modules are added or removed then

```bash
conda activate ./env
conda env update --file environment.yml --prune
```
