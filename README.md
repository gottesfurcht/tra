# Greek Editio Regia New Testament SWORD Bible Module

The Editio Regia, Stephanus 1550 Greek NT or Textus Receptus (With Accents)

## Requirements

  * Python 3
  * `imp2vs` (part of the Crosswire SWORD utilities, `apt-get install libsword-utils` on Debian Linux)

## Module creation instructions

Download the source module from the [mysword.info website](http://mysword-bible.info:8080/download/getfile.php?file=tra.bbl.mybible.gz)

Unzip it:

    gunzip tra.bbl.mybible.gz

Convert the mybible source text to the [`IMP` format](https://www.crosswire.org/wiki/DevTools:Modules#IMP_Format):

    ./convert

This will create the file `tra.imp` from the source module `tra.bbl.mybible`. Then convert the `IMP` file to a SWORD module:

    tra.imp -z -o tra

Then copy the module directory `tra` to `~/.sword/modules/texts/ztext/` and the conf file `tra.conf` to `~/.sword/mods.d/`
