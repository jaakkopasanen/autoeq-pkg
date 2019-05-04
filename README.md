# autoeq-pkg
Code only version of [AutoEq](https://github.com/jaakkopasanen/AutoEq)

## Installing
```bash
pip install git+https://github.com/jaakkopasanen/autoeq-pkg
```

## Usage
See [AutoEq](https://github.com/jaakkopasanen/AutoEq) for comprehensive documentation and usage examples
```python
from autoeq.frequency_response import FrequencyResponse
fr = FrequencyResponse.read_from_csv('path/to/measurement/data.csv')
fr.plot_graph()
```