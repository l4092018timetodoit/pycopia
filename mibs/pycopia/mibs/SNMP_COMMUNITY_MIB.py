# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import IpAddress, MODULE_IDENTITY, OBJECT_TYPE, Integer32, snmpModules
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import RowStatus, StorageType
from SNMP_TARGET_MIB import SnmpTagValue, snmpTargetAddrEntry
from SNMP_FRAMEWORK_MIB import SnmpAdminString, SnmpEngineID

class SNMP_COMMUNITY_MIB(ModuleObject):
	path = '/usr/share/mibs/ietf/SNMP-COMMUNITY-MIB'
	name = 'SNMP-COMMUNITY-MIB'
	language = 2
	description = 'This MIB module defines objects to help support coexistence\nbetween SNMPv1, SNMPv2c, and SNMPv3.'

# nodes
class snmpCommunityMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18])
	name = 'snmpCommunityMIB'

class snmpCommunityMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1])
	name = 'snmpCommunityMIBObjects'

class snmpCommunityMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 2])
	name = 'snmpCommunityMIBConformance'

class snmpCommunityMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 2, 1])
	name = 'snmpCommunityMIBCompliances'

class snmpCommunityMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 2, 2])
	name = 'snmpCommunityMIBGroups'


# macros
# types 
# scalars 
class snmpTrapAddress(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class snmpTrapCommunity(ScalarObject):
	access = 3
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


# columns
class snmpCommunityIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 1])
	syntaxobject = SnmpAdminString


class snmpCommunityName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class snmpCommunitySecurityName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 3])
	syntaxobject = SnmpAdminString


class snmpCommunityContextEngineID(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 4])
	syntaxobject = SnmpEngineID


class snmpCommunityContextName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 5])
	syntaxobject = SnmpAdminString


class snmpCommunityTransportTag(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 6])
	syntaxobject = SnmpTagValue


class snmpCommunityStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class snmpCommunityStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class snmpTargetAddrTMask(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class snmpTargetAddrMMS(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# rows 
class snmpCommunityEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snmpCommunityIndex], True)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 1, 1])
	access = 2
	rowstatus = snmpCommunityStatus
	columns = {'snmpCommunityIndex': snmpCommunityIndex, 'snmpCommunityName': snmpCommunityName, 'snmpCommunitySecurityName': snmpCommunitySecurityName, 'snmpCommunityContextEngineID': snmpCommunityContextEngineID, 'snmpCommunityContextName': snmpCommunityContextName, 'snmpCommunityTransportTag': snmpCommunityTransportTag, 'snmpCommunityStorageType': snmpCommunityStorageType, 'snmpCommunityStatus': snmpCommunityStatus}


from SNMP_TARGET_MIB import snmpTargetAddrName
class snmpTargetAddrExtEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([snmpTargetAddrName], True)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 1, 2, 1])
	access = 2
	columns = {'snmpTargetAddrTMask': snmpTargetAddrTMask, 'snmpTargetAddrMMS': snmpTargetAddrMMS}


# notifications (traps) 
# groups 
class snmpCommunityGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 2, 2, 1])
	group = [snmpCommunityName, snmpCommunitySecurityName, snmpCommunityContextEngineID, snmpCommunityContextName, snmpCommunityTransportTag, snmpCommunityStorageType, snmpCommunityStatus, snmpTargetAddrTMask, snmpTargetAddrMMS]

class snmpProxyTrapForwardGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 18, 2, 2, 3])
	group = [snmpTrapAddress, snmpTrapCommunity]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
