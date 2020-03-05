# json_builder
a utility to build json objects

## To Use:

```sh
./main.py \
    config_base.json \
    test=value \
    key=$(curl https://example.com/api/v2) > config.json
```

## Caveats

* This key=value will only replace parent level attributes
* The behavior when providing two files was not tested