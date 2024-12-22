## this is the short introduce about class Possible.
---
you can use this `class` that figure out how much chance your `target` in the `data`
</br>
it means that you can found out : chance of `AnyType` in `list` or `string`

- ### SUE(Structure, Usage, Error):
   - ### Structure:

        ```python
           class Possible:

                def possible_int_str(self, target: int|str, data: list[int]|str) -> float:
                    return f'chance: {data.count(target) / len(data) * 100:.1f} %'
        ```

   - ### Usage:

        ```python
           from possible import Possible

           object = Possible()
           print(object.possible_int_str('m', 'money')) #output: chance: 20.0 %
        ```

  - ### Error:
    ```python
            from possible import Possible

            object = Possible()
            print(object.possible_int_str(23, 'money')) #output: TypeError(must be string, not int)
    ```

