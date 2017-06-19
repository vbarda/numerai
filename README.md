### numerai - shared code for Numerai models

#### Setup:

```
git clone https://github.com/vbarda/numerai.git
```

In the repository directory:

```
vi constants.py
```

In the file:

```
PROJECT_PATH = [path to repository directory]
```

#### Usage:

*Start Notebook*:

```
%load ../tools/nb_start.py
```

*Read datasets in*:

```
from tools.load_datasets import get_training_data, get_tournament_data
train_data = get_training_data()
tournament_data = get_tournament_data()
```

