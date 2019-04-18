# Desktop Wallpaper Changer
> This python script fetches images from popular sources and set those as your desktop wallpaper.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/54b27c2612ee4301924e701d1b081375)](https://app.codacy.com/app/ayan-b/Desktop-Wallpaper-Changer?utm_source=github.com&utm_medium=referral&utm_content=ayan-b/Desktop-Wallpaper-Changer&utm_campaign=Badge_Grade_Settings) [![Build Status](https://travis-ci.org/ayan-b/Desktop-Wallpaper-Changer.svg?branch=master)](https://travis-ci.org/ayan-b/Desktop-Wallpaper-Changer) [![codecov](https://codecov.io/gh/ayan-b/Desktop-Wallpaper-Changer/branch/master/graph/badge.svg)](https://codecov.io/gh/ayan-b/Desktop-Wallpaper-Changer)


<!--[![HitCount](http://hits.dwyl.io/ayan-b/Desktop-Wallpaper-Changer.svg)](http://hits.dwyl.io/ayan-b/Desktop-Wallpaper-Changer) -->

Desktop Wallpaper Changer fetches images from popular sources and set those as your desktop wallpaper. Currently supported sources are:
- NASA Astronomical Picture of the Day
- Bing Picture of the Day
- Random Pictures from Unsplash.com
- National Geographic Picture of the Day
- Random Images from Desktoppr.

**Usage**:
- First install the package from pypi by running:
    `pip install dtwc`
  > If you want to get latest code from master branch of the repository, you can
  do so by running:
    `pip install git+https://github.com/ayan-b/Desktop-Wallpaper-Changer`

- Now in order to change the background you can use the CLI:
    - `dwc -i` will open all the wallpaper sources and you can select the one
    you like.
    - `dwc -op <number>` will update the wallpaper from the number-th source
    as specified above.

**Platform**:
 - Windows
 - Linux

**Contributing**:
Please head over to [CONTRIBUTING.md](/CONTRIBUTING.md) to check out how the code works and some guidelines regarding contributions!
