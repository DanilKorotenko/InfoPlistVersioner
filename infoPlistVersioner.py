#!/usr/bin/python
import sys, plistlib, re

plist = plistlib.readPlist("Info.plist");
bundleVersionString=plist["CFBundleVersion"];
print "Bundle version:", bundleVersionString;

versionComponents=bundleVersionString.split(".");

newVersion = "";

if len(versionComponents) == 1:
	# bundle version is ####
	# construct new version: ####.1.1d1
	newVersion = bundleVersionString + ".1.1d1";
	
elif len(versionComponents) == 2:
	# bundle version is ####.##
	# construct new version: ####.##.1d1
	newVersion = bundleVersionString + ".1d1";

elif len(versionComponents) == 3:
	major=int(versionComponents[0]);
	minor=int(versionComponents[1]);
	
	bugfixVersionString = versionComponents[2];
	
	bugfixComponents = re.split("[a-z]+", bugfixVersionString);
	bugfix=int(bugfixComponents[0]);
	if len(bugfixComponents) == 1:
		# bundle version is ####.##.##
		# construct new version: ####.##.##+1d1
		bugfix = bugfix + 1;
		if bugfix > 99:
			bugfix = 1;
			minor = minor + 1;
			if minor > 99:
				major = major + 1;
				minor = 1;
		newVersion = str(major) + "." + str(minor) + "." + str(bugfix) + "d1";
	else:
		# bundle version is ####.##.##d##
		# construct new version: ####.##.##d##+1
 		reSearch=re.search("[a-z]+", bugfixVersionString);
 		status=reSearch.group(0);
		buildNumber=int(bugfixComponents[1]);
		buildNumber=buildNumber+1;
		if buildNumber > 99:
			buildNumber = 1;
			bugfix = bugfix + 1;
			if bugfix > 99:
				bugfix = 1;
				minor = minor + 1;
				if minor > 99:
					minor = 1;
					major = major + 1;
		newVersion = str(major) + "." + str(minor) + "." + str(bugfix) + status + str(buildNumber);
		
plist["CFBundleVersion"]=str(newVersion);

plistlib.writePlist(plist,"Info.plist");
