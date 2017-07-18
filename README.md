Apple Health.app to True Weight converter
====

This is a little utility I wrote to convert the `export.xml` contained
within an Apple Health.app export into the CSV used by [True
Weight](https://itunes.apple.com/us/app/true-weight/id287941226?mt=8).

It streams the data, which can be very important if your export was
as big as mine was.

It only supports pounds. If your measurements aren't in pounds,
feel free to submit a PR.

To use it:

1.  Export your Apple Health data and transfer it to your computer
    (I used iCloud Drive).

2.  Unzip and move `export.xml` into the current directory.

3.  Run `convert.py export.xml >export.csv`.

4.  Import `export.csv` into True Weight.


