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
conda deactivate
mamba env update --prefix ./env --file environment.yml --prune
```
