
# TkLang
##### *Allows one to parse .tk files*

### Instillation
    python -m pip install TkLang

### Usage
    import tklang as tkl
    content = tkl.load("your_tk_file.tk")

## Example(s)

### _TkLang Code_
    <src>
        <button id="LLJ" height="1" width="20">LLJ</button>
        <button id="LLJW">LLJW</button>
    </src>
> Note that the <src\> tag is arbitrary and may be replaced with what ever name you desire; however, it is required. Omitting the src tag will cause issues with parser. We recommend replacing 'src' with 'app'
### _Python Code_
    import tklang as tkl
    import tkinter as tk
    t = tkl.load("test.tk")

    root = t['master']
    b1 = t['LLJ']

    b1.grid(row=0, column=0)

    root.mainloop()

> Note that the 'master' key in the 't' dictionary is auto-definned and the root/master for all widgets in that TKL File


### Features
    load(src: file_name) -> dict
    write(target_path: path_to_file, tag: tag_to_write_to_file) -> None

#

### Changelog

#### 0.0.1 ~ ~ 11/5/2020 10:01
* Initial Unstable Release

#### 0.0.2 ~ ~ 11/5/2020 10:03
* Added README.md File

#### 0.0.3 ~ ~ 11/5/2020 10:30
* Updated README.md File

#### 0.0.4 ~ ~ 11/5/2020 10:43
* Added setup.py & instillation_requires

* filemodes -> file-modes

#### 0.0.5 ~ ~ 11/5/2019 10:47
* Updated changelog

#### 0.1.0 ~ ~ 11/5/2020 13:17
* TkLang is now able to filter out tags through a series of checks rather than having the code run for a while and then hit an expected error. This will hopefully increase the speed of TkLang

#### 0.1.1 ~ ~ 11/6/2020 12:35
* Updated README.md
* Addded Support for distrubtions

#### 0.2.1 ~ ~ 11/6/2020 15:11
* Added Support for frames

#### 0.2.2 ~ ~ 11/9/2020 8:58
* Initialized a git repository
* Added a .gitignore file

#### 0.2.5 ~ ~ 11/9/2020 9:44
* Updated Changelog for 0.2.2/5 changes
* Added a write function for writing to .tk files
> Note that the write function is in an incredibly early stage and should be used only when necessary

#### 1.0.0 ~ ~ [PLANNED]
Initial Stable Release