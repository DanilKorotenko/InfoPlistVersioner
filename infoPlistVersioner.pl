#!/usr/bin/python
import sys, plistlib

plist = plistlib.readPlist("Info.plist");
print "Bundle version:", plist["CFBundleVersion"];


# elif len(sys.argv) > 2: # we have some additional options
# 	if sys.argv[1] == "copy":
# 		sourceConfig = sys.argv[2]
# 		destinationConfig = sys.argv[3]
# 		pSource = plistlib.readPlist(sourceConfig);
# 		pDestination = plistlib.readPlist(destinationConfig);
# 		pDestination["kGTBDatabaseConfigServerKey"] = pSource["kGTBDatabaseConfigServerKey"];
# 		plistlib.writePlist(pDestination, destinationConfig)
