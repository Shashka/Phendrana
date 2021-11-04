from subdom_scanner.sdscanner import *

plist = ["PORT", "STATUS"]
sub = subd_scanner(".best-energies.fr", plist)

sub.subd_scan(sub.domain, sub.fields)