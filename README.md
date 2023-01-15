# CuttApi
One of the best URL shortener module for Python of all time!

[![CuttApi](https://bn02pap001files.storage.live.com/y4mddoJNGt0_6ndR3jw_e--PbyBPm-TATAAJMvjqg-KJ4PqTYgD5bFR8HwCBbGMSDaYp_246ZmVMRlZjx7KTv9JbaVnXfFQcivqkFlJK3OpeNwI-Jnq3--W_bt5rLbz2QlusQORHvTIxqjIuilIaKCzka1A2hUJzGT81GqdZntyGAURvmdywES0-olI9115inae?width=52&height=90&cropmode=none)](https://cutt.ly/CuttApi)


CuttApi is one of the best ways of shortening URLs using Cuttly URL shortener just by entering your API key and seeing the rest that is done automatically by the Module







## Installation

Installing requirements to establish the Module :

```sh
requests
urllib3
pyperclip
```
**Use pip to Install the above Modules**


## Usage
The only thing users need to do is
```sh
from CuttApi import Cuttshort
import stdiomask
api_key = stdiomask.getpass("Enter your Cuttly api key: ")
short = Cuttshort(api_key)
```

- If you enter the correct API key, then you proceed.
- But if you enter a wrong one, you proceed only after entering the correct one.
- As you proceed, the same thing happens with Links and Alias (if you wanna give), but that's good since the process doesn't start over from the start of entering the API key.

## License

MIT

Copyright (c) 2023  Devraj Therani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
