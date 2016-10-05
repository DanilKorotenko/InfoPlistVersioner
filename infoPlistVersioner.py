#!/usr/bin/python
import sys, plistlib

plist = plistlib.readPlist("Info.plist");
bundleVersion=int(plist["CFBundleVersion"]);
print "Bundle version:", bundleVersion;

# bundle version is ####
bundleVersion=bundleVersion+1;

plist["CFBundleVersion"]=str(bundleVersion);

plistlib.writePlist(plist,"Info.plist");

# bundle version is ####.##

# bundle version is ####.##.##

# bundle version is ####.##.##[d,a,b,fc][1-255]
