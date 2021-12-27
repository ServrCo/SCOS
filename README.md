# Servr Co OS
## A Debian-based Linux distro, still in development.

### What is Servr Co OS?
Servr Co OS is a nice open source (currently very incomplete) desktop environment, designed to run on top of Lubuntu.

### Development Info
**IMPORTANT**
If you are a Python developer that knows more about what you're doing than we do, please help us. We need people to help us make this good.
This desktop environment is written mostly in Python, and we know it's not the most desireable language for this stuff. But it works.

### Building
If for some reason you need your own custom build of Servr Co OS, or you are doing some Servr Co OS development, building Servr Co OS may be important for you to know how to do.

*HOW TO BUILD*

You will need Python 3 for this.

1. Download and extract the source code to somewhere reasonable on your computer.
2. CD into the root of the source code directory.
3. Run `python3 build.py` and let the build script do its magic.

*HOW TO INSTALL AND RUN THE BUILD*

Due to the way some directories function, Servr Co OS needs to be installed before it can run, or some things may not load properly.
1. cd into the tools folder from the root of the source directory
2. Run `sh image.sh`
3. cd back into the source code root
4. cd into the imgbins folder
5. run ./install
6. To run Servr Co OS after installation, cd into /SCOS and run ./launcher
7. All done!
