# minilogue-xd-lib2preset

Converts a minilogue XD `mnlgxdlib` file to a `mnlgxdpreset` file which can be loaded into the "Preset Data" pane of the minilogue xd Sound Librarian.  Only works with programs, not user oscillators, FX, or microtuning.

## Requirements

A recent version of Python.  Tested on OSX Catalina; should also work on Windows.

## Usage

1. Use the Sound Librarian to organize the programs you want to convert to preset data.
1. Select "File", "Save As..." and write the program data as a library file (`.mnlgxdlib`).
1. Launch a terminal program and run the `l2p.py` conversion script.  Provide the path to the `.mnlgxdlib` file you saved in the previous step as a parameter to the script.
1. The script will prompt for information to include in the preset metadata file.  The following suggested values are empirically derived... :)
    * DataID - use the name of the preset file without the `.mnlgdxpreset` extension.
    * Name - same as DataID
    * Author - your name
    * Version - start with 1 and work your way up as you make new versions.
    * NumOfProg - enter the number of programs in your lib file.
    * Date - the date in YYYY-MM-DD format.
    * Prefix - leave blank
    * Copyright - add in your copyright information, or leave blank.
1. The script will output a preset file in the same directory as the library file.  Double click on the preset file to load it in Sound Librarian.

## Hints

There doesn't appear to be a way to update or replace a single preset file in Sound Librarian.  The only way I've found is to select "Option", "uninstall all presets and quit", then re-launch Sound Librarian and re-installing all presets.  Nuke 'em from orbit -- it's the only way to be sure.