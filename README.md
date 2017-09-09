# python3-auto-abstracts

## Demo

- [日本語文書の自動要約アルゴリズムを60年近く前の論文を頼りに再記述する](http://media.accel-brain.com/auto-abstractor-jp/)

## Requirement

- Docker

```
$ docker version
Client:
 Version:      17.03.1-ce
 API version:  1.27
 Go version:   go1.7.5
 Git commit:   c6d412e
 Built:        Tue Mar 28 00:40:02 2017
 OS/Arch:      windows/amd64

Server:
 Version:      17.06.0-ce
 API version:  1.30 (minimum version 1.12)
 Go version:   go1.8.3
 Git commit:   02c1d87
 Built:        Fri Jun 23 21:51:55 2017
 OS/Arch:      linux/amd64
 Experimental: false
```

## Usage

```
$ docker run --rm auto-abstracts http://www.natsumesoseki.com/home/kokoro
先生は有難うといって、それを私の手から受け取った。
...(中略)...
君の心でそれを止めるだけの覚悟がなければ。
```

## Installation

```
$ docker build -t auto-abstracts .
```
