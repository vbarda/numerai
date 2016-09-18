### numerai - shared code for Numerai models

#### Usage:

*Cross Validation*:

```
from models.cross_validation import CrossValidation
cv = CrossValidation(df)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(cv.X_train, cv.y_train)
log_reg.predict(cv.X_test)
```

