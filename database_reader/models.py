from django.db import models


# # Create your models here.
class Aircraft(models.Model):
    aircraftid = models.IntegerField(db_column='AircraftID', unique=True,
                                     primary_key=True)  # Field name made lowercase.
    firstcreated = models.DateTimeField(db_column='FirstCreated')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    modes = models.CharField(db_column='ModeS', unique=True, max_length=6)  # Field name made lowercase.
    modescountry = models.CharField(db_column='ModeSCountry', max_length=24, blank=True,
                                    null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=24, blank=True, null=True)  # Field name made lowercase.
    registration = models.CharField(db_column='Registration', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    currentregdate = models.CharField(db_column='CurrentRegDate', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    previousid = models.CharField(db_column='PreviousID', max_length=10, blank=True,
                                  null=True)  # Field name made lowercase.
    firstregdate = models.CharField(db_column='FirstRegDate', max_length=10, blank=True,
                                    null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deregdate = models.CharField(db_column='DeRegDate', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=60, blank=True,
                                    null=True)  # Field name made lowercase.
    icaotypecode = models.CharField(db_column='ICAOTypeCode', max_length=10, blank=True,
                                    null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=40, blank=True, null=True)  # Field name made lowercase.
    serialno = models.CharField(db_column='SerialNo', max_length=30, blank=True,
                                null=True)  # Field name made lowercase.
    popularname = models.CharField(db_column='PopularName', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    genericname = models.CharField(db_column='GenericName', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    aircraftclass = models.CharField(db_column='AircraftClass', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.
    engines = models.CharField(db_column='Engines', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ownershipstatus = models.CharField(db_column='OwnershipStatus', max_length=10, blank=True,
                                       null=True)  # Field name made lowercase.
    registeredowners = models.CharField(db_column='RegisteredOwners', max_length=100, blank=True,
                                        null=True)  # Field name made lowercase.
    mtow = models.CharField(db_column='MTOW', max_length=10, blank=True, null=True)  # Field name made lowercase.
    totalhours = models.CharField(db_column='TotalHours', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    yearbuilt = models.IntegerField(db_column='YearBuilt', blank=True,
                                 null=True)  # Field name made lowercase.
    cofacategory = models.CharField(db_column='CofACategory', max_length=30, blank=True,
                                    null=True)  # Field name made lowercase.
    cofaexpiry = models.CharField(db_column='CofAExpiry', max_length=10, blank=True,
                                  null=True)  # Field name made lowercase.
    usernotes = models.CharField(db_column='UserNotes', max_length=300, blank=True,
                                 null=True)  # Field name made lowercase.
    interested = models.BooleanField(db_column='Interested')  # Field name made lowercase.
    usertag = models.CharField(db_column='UserTag', max_length=5, blank=True, null=True)  # Field name made lowercase.
    infourl = models.CharField(db_column='InfoURL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    pictureurl1 = models.CharField(db_column='PictureURL1', max_length=150, blank=True,
                                   null=True)  # Field name made lowercase.
    pictureurl2 = models.CharField(db_column='PictureURL2', max_length=150, blank=True,
                                   null=True)  # Field name made lowercase.
    pictureurl3 = models.CharField(db_column='PictureURL3', max_length=150, blank=True,
                                   null=True)  # Field name made lowercase.
    userbool1 = models.BooleanField(db_column='UserBool1')  # Field name made lowercase.
    userbool2 = models.BooleanField(db_column='UserBool2')  # Field name made lowercase.
    userbool3 = models.BooleanField(db_column='UserBool3')  # Field name made lowercase.
    userbool4 = models.BooleanField(db_column='UserBool4')  # Field name made lowercase.
    userbool5 = models.BooleanField(db_column='UserBool5')  # Field name made lowercase.
    userstring1 = models.CharField(db_column='UserString1', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    userstring2 = models.CharField(db_column='UserString2', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    userstring3 = models.CharField(db_column='UserString3', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    userstring4 = models.CharField(db_column='UserString4', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    userstring5 = models.CharField(db_column='UserString5', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    userint1 = models.IntegerField(db_column='UserInt1', blank=True, null=True)  # Field name made lowercase.
    userint2 = models.IntegerField(db_column='UserInt2', blank=True, null=True)  # Field name made lowercase.
    userint3 = models.IntegerField(db_column='UserInt3', blank=True, null=True)  # Field name made lowercase.
    userint4 = models.IntegerField(db_column='UserInt4', blank=True, null=True)  # Field name made lowercase.
    userint5 = models.IntegerField(db_column='UserInt5', blank=True, null=True)  # Field name made lowercase.
    operatorflagcode = models.CharField(db_column='OperatorFlagCode', max_length=20, blank=True,
                                        null=True)  # Field name made lowercase.


class Flights(models.Model):
    flightid = models.IntegerField(db_column='FlightID', unique=True, primary_key=True)  # Field name made lowercase.
    sessionid = models.IntegerField(db_column='SessionID')  # Field name made lowercase.
    aircraftid = models.ForeignKey(Aircraft, on_delete=models.CASCADE,
                                   db_column='AircraftID')  # Field name made lowercase.
    # aircraftid = models.IntegerField(db_column='AircraftID')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    callsign = models.CharField(db_column='Callsign', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    numposmsgrec = models.IntegerField(db_column='NumPosMsgRec', blank=True, null=True)  # Field name made lowercase.
    numadsbmsgrec = models.IntegerField(db_column='NumADSBMsgRec', blank=True, null=True)  # Field name made lowercase.
    nummodesmsgrec = models.IntegerField(db_column='NumModeSMsgRec', blank=True,
                                         null=True)  # Field name made lowercase.
    numidmsgrec = models.IntegerField(db_column='NumIDMsgRec', blank=True, null=True)  # Field name made lowercase.
    numsurposmsgrec = models.IntegerField(db_column='NumSurPosMsgRec', blank=True,
                                          null=True)  # Field name made lowercase.
    numairposmsgrec = models.IntegerField(db_column='NumAirPosMsgRec', blank=True,
                                          null=True)  # Field name made lowercase.
    numairvelmsgrec = models.IntegerField(db_column='NumAirVelMsgRec', blank=True,
                                          null=True)  # Field name made lowercase.
    numsuraltmsgrec = models.IntegerField(db_column='NumSurAltMsgRec', blank=True,
                                          null=True)  # Field name made lowercase.
    numsuridmsgrec = models.IntegerField(db_column='NumSurIDMsgRec', blank=True,
                                         null=True)  # Field name made lowercase.
    numairtoairmsgrec = models.IntegerField(db_column='NumAirToAirMsgRec', blank=True,
                                            null=True)  # Field name made lowercase.
    numaircallrepmsgrec = models.IntegerField(db_column='NumAirCallRepMsgRec', blank=True,
                                              null=True)  # Field name made lowercase.
    firstisonground = models.BooleanField(db_column='FirstIsOnGround')  # Field name made lowercase.
    lastisonground = models.BooleanField(db_column='LastIsOnGround')  # Field name made lowercase.
    firstlat = models.FloatField(db_column='FirstLat', blank=True, null=True)  # Field name made lowercase.
    lastlat = models.FloatField(db_column='LastLat', blank=True, null=True)  # Field name made lowercase.
    firstlon = models.FloatField(db_column='FirstLon', blank=True, null=True)  # Field name made lowercase.
    lastlon = models.FloatField(db_column='LastLon', blank=True, null=True)  # Field name made lowercase.
    firstgroundspeed = models.FloatField(db_column='FirstGroundSpeed', blank=True,
                                         null=True)  # Field name made lowercase.
    lastgroundspeed = models.FloatField(db_column='LastGroundSpeed', blank=True,
                                        null=True)  # Field name made lowercase.
    firstaltitude = models.IntegerField(db_column='FirstAltitude', blank=True, null=True)  # Field name made lowercase.
    lastaltitude = models.IntegerField(db_column='LastAltitude', blank=True, null=True)  # Field name made lowercase.
    firstverticalrate = models.IntegerField(db_column='FirstVerticalRate', blank=True,
                                            null=True)  # Field name made lowercase.
    lastverticalrate = models.IntegerField(db_column='LastVerticalRate', blank=True,
                                           null=True)  # Field name made lowercase.
    firsttrack = models.FloatField(db_column='FirstTrack', blank=True, null=True)  # Field name made lowercase.
    lasttrack = models.FloatField(db_column='LastTrack', blank=True, null=True)  # Field name made lowercase.
    firstsquawk = models.IntegerField(db_column='FirstSquawk', blank=True, null=True)  # Field name made lowercase.
    lastsquawk = models.IntegerField(db_column='LastSquawk', blank=True, null=True)  # Field name made lowercase.
    hadalert = models.BooleanField(db_column='HadAlert')  # Field name made lowercase.
    hademergency = models.BooleanField(db_column='HadEmergency')  # Field name made lowercase.
    hadspi = models.BooleanField(db_column='HadSPI')  # Field name made lowercase.
    usernotes = models.CharField(db_column='UserNotes', max_length=300, blank=True,
                                 null=True)  # Field name made lowercase.
