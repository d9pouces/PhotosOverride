# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achange(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zchangetype = models.IntegerField(db_column="ZCHANGETYPE", blank=True, null=True)
    zentity = models.IntegerField(db_column="ZENTITY", blank=True, null=True)
    zentitypk = models.IntegerField(db_column="ZENTITYPK", blank=True, null=True)
    ztransactionid = models.IntegerField(
        db_column="ZTRANSACTIONID", blank=True, null=True
    )
    zcolumns = models.BinaryField(db_column="ZCOLUMNS", blank=True, null=True)
    ztombstone0 = models.BinaryField(db_column="ZTOMBSTONE0", blank=True, null=True)
    ztombstone1 = models.BinaryField(db_column="ZTOMBSTONE1", blank=True, null=True)
    ztombstone2 = models.BinaryField(db_column="ZTOMBSTONE2", blank=True, null=True)
    ztombstone3 = models.BinaryField(db_column="ZTOMBSTONE3", blank=True, null=True)
    ztombstone4 = models.BinaryField(db_column="ZTOMBSTONE4", blank=True, null=True)
    ztombstone5 = models.BinaryField(db_column="ZTOMBSTONE5", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ACHANGE"


class Atransaction(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zauthorts = models.IntegerField(db_column="ZAUTHORTS", blank=True, null=True)
    zbundleidts = models.IntegerField(db_column="ZBUNDLEIDTS", blank=True, null=True)
    zcontextnamets = models.IntegerField(
        db_column="ZCONTEXTNAMETS", blank=True, null=True
    )
    zprocessidts = models.IntegerField(db_column="ZPROCESSIDTS", blank=True, null=True)
    ztimestamp = models.TextField(db_column="ZTIMESTAMP", blank=True, null=True)
    zauthor = models.CharField(db_column="ZAUTHOR", blank=True, null=True)
    zbundleid = models.CharField(db_column="ZBUNDLEID", blank=True, null=True)
    zcontextname = models.CharField(db_column="ZCONTEXTNAME", blank=True, null=True)
    zprocessid = models.CharField(db_column="ZPROCESSID", blank=True, null=True)
    zquerygen = models.BinaryField(db_column="ZQUERYGEN", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ATRANSACTION"


class Atransactionstring(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zname = models.CharField(db_column="ZNAME", unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ATRANSACTIONSTRING"


class Zadditionalassetattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zallowedforanalysis = models.IntegerField(
        db_column="ZALLOWEDFORANALYSIS", blank=True, null=True
    )
    zcameracapturedevice = models.IntegerField(
        db_column="ZCAMERACAPTUREDEVICE", blank=True, null=True
    )
    zcloudavalanchepicktype = models.IntegerField(
        db_column="ZCLOUDAVALANCHEPICKTYPE", blank=True, null=True
    )
    zcloudkindsubtype = models.IntegerField(
        db_column="ZCLOUDKINDSUBTYPE", blank=True, null=True
    )
    zcloudrecoverystate = models.IntegerField(
        db_column="ZCLOUDRECOVERYSTATE", blank=True, null=True
    )
    zcloudstaterecoveryattemptscount = models.IntegerField(
        db_column="ZCLOUDSTATERECOVERYATTEMPTSCOUNT", blank=True, null=True
    )
    zdeferredprocessingcandidateoptions = models.IntegerField(
        db_column="ZDEFERREDPROCESSINGCANDIDATEOPTIONS", blank=True, null=True
    )
    zdestinationassetcopystate = models.IntegerField(
        db_column="ZDESTINATIONASSETCOPYSTATE", blank=True, null=True
    )
    zembeddedthumbnailheight = models.IntegerField(
        db_column="ZEMBEDDEDTHUMBNAILHEIGHT", blank=True, null=True
    )
    zembeddedthumbnaillength = models.IntegerField(
        db_column="ZEMBEDDEDTHUMBNAILLENGTH", blank=True, null=True
    )
    zembeddedthumbnailoffset = models.IntegerField(
        db_column="ZEMBEDDEDTHUMBNAILOFFSET", blank=True, null=True
    )
    zembeddedthumbnailwidth = models.IntegerField(
        db_column="ZEMBEDDEDTHUMBNAILWIDTH", blank=True, null=True
    )
    zimportedby = models.IntegerField(db_column="ZIMPORTEDBY", blank=True, null=True)
    zinferredtimezoneoffset = models.IntegerField(
        db_column="ZINFERREDTIMEZONEOFFSET", blank=True, null=True
    )
    zlocationhash = models.IntegerField(
        db_column="ZLOCATIONHASH", blank=True, null=True
    )
    zoriginalfilesize = models.IntegerField(
        db_column="ZORIGINALFILESIZE", blank=True, null=True
    )
    zoriginalheight = models.IntegerField(
        db_column="ZORIGINALHEIGHT", blank=True, null=True
    )
    zoriginalorientation = models.IntegerField(
        db_column="ZORIGINALORIENTATION", blank=True, null=True
    )
    zoriginalresourcechoice = models.IntegerField(
        db_column="ZORIGINALRESOURCECHOICE", blank=True, null=True
    )
    zoriginalwidth = models.IntegerField(
        db_column="ZORIGINALWIDTH", blank=True, null=True
    )
    zpendingplaycount = models.IntegerField(
        db_column="ZPENDINGPLAYCOUNT", blank=True, null=True
    )
    zpendingsharecount = models.IntegerField(
        db_column="ZPENDINGSHARECOUNT", blank=True, null=True
    )
    zpendingviewcount = models.IntegerField(
        db_column="ZPENDINGVIEWCOUNT", blank=True, null=True
    )
    zplaycount = models.IntegerField(db_column="ZPLAYCOUNT", blank=True, null=True)
    zptptrashedstate = models.IntegerField(
        db_column="ZPTPTRASHEDSTATE", blank=True, null=True
    )
    zreverselocationdataisvalid = models.IntegerField(
        db_column="ZREVERSELOCATIONDATAISVALID", blank=True, null=True
    )
    zsceneanalysisversion = models.IntegerField(
        db_column="ZSCENEANALYSISVERSION", blank=True, null=True
    )
    zsharecount = models.IntegerField(db_column="ZSHARECOUNT", blank=True, null=True)
    zsharetype = models.IntegerField(db_column="ZSHARETYPE", blank=True, null=True)
    zshiftedlocationisvalid = models.IntegerField(
        db_column="ZSHIFTEDLOCATIONISVALID", blank=True, null=True
    )
    ztimezoneoffset = models.IntegerField(
        db_column="ZTIMEZONEOFFSET", blank=True, null=True
    )
    zuploadattempts = models.IntegerField(
        db_column="ZUPLOADATTEMPTS", blank=True, null=True
    )
    zvariationsuggestionstates = models.IntegerField(
        db_column="ZVARIATIONSUGGESTIONSTATES", blank=True, null=True
    )
    zvideocpdisplaytimescale = models.IntegerField(
        db_column="ZVIDEOCPDISPLAYTIMESCALE", blank=True, null=True
    )
    zvideocpdisplayvalue = models.IntegerField(
        db_column="ZVIDEOCPDISPLAYVALUE", blank=True, null=True
    )
    zvideocpdurationtimescale = models.IntegerField(
        db_column="ZVIDEOCPDURATIONTIMESCALE", blank=True, null=True
    )
    zviewcount = models.IntegerField(db_column="ZVIEWCOUNT", blank=True, null=True)
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zassetdescription = models.IntegerField(
        db_column="ZASSETDESCRIPTION", blank=True, null=True
    )
    zeditediptcattributes = models.IntegerField(
        db_column="ZEDITEDIPTCATTRIBUTES", blank=True, null=True
    )
    zmediametadata = models.IntegerField(
        db_column="ZMEDIAMETADATA", blank=True, null=True
    )
    zsceneprint = models.IntegerField(db_column="ZSCENEPRINT", blank=True, null=True)
    zunmanagedadjustment = models.IntegerField(
        db_column="ZUNMANAGEDADJUSTMENT", blank=True, null=True
    )
    zalternateimportimagedate = models.TextField(
        db_column="ZALTERNATEIMPORTIMAGEDATE", blank=True, null=True
    )
    zgpshorizontalaccuracy = models.TextField(
        db_column="ZGPSHORIZONTALACCURACY", blank=True, null=True
    )
    zlastuploadattemptdate = models.TextField(
        db_column="ZLASTUPLOADATTEMPTDATE", blank=True, null=True
    )
    zsceneanalysistimestamp = models.TextField(
        db_column="ZSCENEANALYSISTIMESTAMP", blank=True, null=True
    )
    zaccessibilitydescription = models.CharField(
        db_column="ZACCESSIBILITYDESCRIPTION", blank=True, null=True
    )
    zadjustedfingerprint = models.CharField(
        db_column="ZADJUSTEDFINGERPRINT", blank=True, null=True
    )
    zimportedbybundleidentifier = models.CharField(
        db_column="ZIMPORTEDBYBUNDLEIDENTIFIER", blank=True, null=True
    )
    zdeferredphotoidentifier = models.CharField(
        db_column="ZDEFERREDPHOTOIDENTIFIER", blank=True, null=True
    )
    zeditorbundleid = models.CharField(
        db_column="ZEDITORBUNDLEID", blank=True, null=True
    )
    zexiftimestampstring = models.CharField(
        db_column="ZEXIFTIMESTAMPSTRING", blank=True, null=True
    )
    zimportsessionid = models.CharField(
        db_column="ZIMPORTSESSIONID", blank=True, null=True
    )
    zmasterfingerprint = models.CharField(
        db_column="ZMASTERFINGERPRINT", blank=True, null=True
    )
    zmediametadatatype = models.CharField(
        db_column="ZMEDIAMETADATATYPE", blank=True, null=True
    )
    zmontage = models.CharField(db_column="ZMONTAGE", blank=True, null=True)
    zoriginalassetsuuid = models.CharField(
        db_column="ZORIGINALASSETSUUID", blank=True, null=True
    )
    zoriginalfilename = models.CharField(
        db_column="ZORIGINALFILENAME", blank=True, null=True
    )
    zoriginatingassetidentifier = models.CharField(
        db_column="ZORIGINATINGASSETIDENTIFIER", blank=True, null=True
    )
    zphotostreamtagid = models.CharField(
        db_column="ZPHOTOSTREAMTAGID", blank=True, null=True
    )
    zpublicglobaluuid = models.CharField(
        db_column="ZPUBLICGLOBALUUID", blank=True, null=True
    )
    zshareoriginator = models.CharField(
        db_column="ZSHAREORIGINATOR", blank=True, null=True
    )
    zsnowdaysnowplowidentifier = models.CharField(
        db_column="ZSNOWDAYSNOWPLOWIDENTIFIER", blank=True, null=True
    )
    zspatialovercapturegroupidentifier = models.CharField(
        db_column="ZSPATIALOVERCAPTUREGROUPIDENTIFIER", blank=True, null=True
    )
    ztimezonename = models.CharField(db_column="ZTIMEZONENAME", blank=True, null=True)
    ztitle = models.CharField(db_column="ZTITLE", blank=True, null=True)
    zdistanceidentity = models.BinaryField(
        db_column="ZDISTANCEIDENTITY", blank=True, null=True
    )
    zfaceregions = models.BinaryField(db_column="ZFACEREGIONS", blank=True, null=True)
    zobjectsaliencyrectsdata = models.BinaryField(
        db_column="ZOBJECTSALIENCYRECTSDATA", blank=True, null=True
    )
    zoriginalhash = models.BinaryField(db_column="ZORIGINALHASH", blank=True, null=True)
    zplaceannotationdata = models.BinaryField(
        db_column="ZPLACEANNOTATIONDATA", blank=True, null=True
    )
    zreverselocationdata = models.BinaryField(
        db_column="ZREVERSELOCATIONDATA", blank=True, null=True
    )
    zshiftedlocationdata = models.BinaryField(
        db_column="ZSHIFTEDLOCATIONDATA", blank=True, null=True
    )
    zimportedbydisplayname = models.CharField(
        db_column="ZIMPORTEDBYDISPLAYNAME", blank=True, null=True
    )
    zsceneanalysisisfrompreview = models.IntegerField(
        db_column="ZSCENEANALYSISISFROMPREVIEW", blank=True, null=True
    )
    zsyndicationidentifier = models.CharField(
        db_column="ZSYNDICATIONIDENTIFIER", blank=True, null=True
    )
    zsourceassetforduplicationscopeidentifier = models.CharField(
        db_column="ZSOURCEASSETFORDUPLICATIONSCOPEIDENTIFIER", blank=True, null=True
    )
    zsourceassetforduplicationidentifier = models.CharField(
        db_column="ZSOURCEASSETFORDUPLICATIONIDENTIFIER", blank=True, null=True
    )
    zfaceanalysisversion = models.IntegerField(
        db_column="ZFACEANALYSISVERSION", blank=True, null=True
    )
    zsyndicationhistory = models.IntegerField(
        db_column="ZSYNDICATIONHISTORY", blank=True, null=True
    )
    zdatecreatedsource = models.IntegerField(
        db_column="ZDATECREATEDSOURCE", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZADDITIONALASSETATTRIBUTES"


class Zalbumlist(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zidentifier = models.IntegerField(db_column="ZIDENTIFIER", blank=True, null=True)
    zneedsreorderingnumber = models.IntegerField(
        db_column="ZNEEDSREORDERINGNUMBER", blank=True, null=True
    )
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZALBUMLIST"


class Zasset(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zavalanchepicktype = models.IntegerField(
        db_column="ZAVALANCHEPICKTYPE", blank=True, null=True
    )
    zbundlescope = models.IntegerField(db_column="ZBUNDLESCOPE", blank=True, null=True)
    zcameraprocessingadjustmentstate = models.IntegerField(
        db_column="ZCAMERAPROCESSINGADJUSTMENTSTATE", blank=True, null=True
    )
    zclouddeletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    zclouddownloadrequests = models.IntegerField(
        db_column="ZCLOUDDOWNLOADREQUESTS", blank=True, null=True
    )
    zcloudhascommentsbyme = models.IntegerField(
        db_column="ZCLOUDHASCOMMENTSBYME", blank=True, null=True
    )
    zcloudhascommentsconversation = models.IntegerField(
        db_column="ZCLOUDHASCOMMENTSCONVERSATION", blank=True, null=True
    )
    zcloudhasunseencomments = models.IntegerField(
        db_column="ZCLOUDHASUNSEENCOMMENTS", blank=True, null=True
    )
    zcloudisdeletable = models.IntegerField(
        db_column="ZCLOUDISDELETABLE", blank=True, null=True
    )
    zcloudismyasset = models.IntegerField(
        db_column="ZCLOUDISMYASSET", blank=True, null=True
    )
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zcloudplaceholderkind = models.IntegerField(
        db_column="ZCLOUDPLACEHOLDERKIND", blank=True, null=True
    )
    zcomplete = models.IntegerField(db_column="ZCOMPLETE", blank=True, null=True)
    zdeferredprocessingneeded = models.IntegerField(
        db_column="ZDEFERREDPROCESSINGNEEDED", blank=True, null=True
    )
    zdepthtype = models.IntegerField(db_column="ZDEPTHTYPE", blank=True, null=True)
    zderivedcameracapturedevice = models.IntegerField(
        db_column="ZDERIVEDCAMERACAPTUREDEVICE", blank=True, null=True
    )
    zfaceareapoints = models.IntegerField(
        db_column="ZFACEAREAPOINTS", blank=True, null=True
    )
    zfavorite = models.IntegerField(db_column="ZFAVORITE", blank=True, null=True)
    zhasadjustments = models.IntegerField(
        db_column="ZHASADJUSTMENTS", blank=True, null=True
    )
    zhdrtype = models.IntegerField(db_column="ZHDRTYPE", blank=True, null=True)
    zheight = models.IntegerField(db_column="ZHEIGHT", blank=True, null=True)
    zhidden = models.IntegerField(db_column="ZHIDDEN", blank=True, null=True)
    zhighframeratestate = models.IntegerField(
        db_column="ZHIGHFRAMERATESTATE", blank=True, null=True
    )
    zkind = models.IntegerField(db_column="ZKIND", blank=True, null=True)
    zkindsubtype = models.IntegerField(db_column="ZKINDSUBTYPE", blank=True, null=True)
    zorientation = models.IntegerField(db_column="ZORIENTATION", blank=True, null=True)
    zpackedacceptablecroprect = models.IntegerField(
        db_column="ZPACKEDACCEPTABLECROPRECT", blank=True, null=True
    )
    zpackedbadgeattributes = models.IntegerField(
        db_column="ZPACKEDBADGEATTRIBUTES", blank=True, null=True
    )
    zpackedpreferredcroprect = models.IntegerField(
        db_column="ZPACKEDPREFERREDCROPRECT", blank=True, null=True
    )
    zplaybackstyle = models.IntegerField(
        db_column="ZPLAYBACKSTYLE", blank=True, null=True
    )
    zplaybackvariation = models.IntegerField(
        db_column="ZPLAYBACKVARIATION", blank=True, null=True
    )
    zsavedassettype = models.IntegerField(
        db_column="ZSAVEDASSETTYPE", blank=True, null=True
    )
    zsyndicationstate = models.IntegerField(
        db_column="ZSYNDICATIONSTATE", blank=True, null=True
    )
    zthumbnailindex = models.IntegerField(
        db_column="ZTHUMBNAILINDEX", blank=True, null=True
    )
    ztrashedstate = models.IntegerField(
        db_column="ZTRASHEDSTATE", blank=True, null=True
    )
    zvideocpdurationvalue = models.IntegerField(
        db_column="ZVIDEOCPDURATIONVALUE", blank=True, null=True
    )
    zvideocpvisibilitystate = models.IntegerField(
        db_column="ZVIDEOCPVISIBILITYSTATE", blank=True, null=True
    )
    zvideodeferredprocessingneeded = models.IntegerField(
        db_column="ZVIDEODEFERREDPROCESSINGNEEDED", blank=True, null=True
    )
    zvideokeyframetimescale = models.IntegerField(
        db_column="ZVIDEOKEYFRAMETIMESCALE", blank=True, null=True
    )
    zvideokeyframevalue = models.IntegerField(
        db_column="ZVIDEOKEYFRAMEVALUE", blank=True, null=True
    )
    zvisibilitystate = models.IntegerField(
        db_column="ZVISIBILITYSTATE", blank=True, null=True
    )
    zwidth = models.IntegerField(db_column="ZWIDTH", blank=True, null=True)
    zadditionalattributes = models.IntegerField(
        db_column="ZADDITIONALATTRIBUTES", blank=True, null=True
    )
    zcloudfeedassetsentry = models.IntegerField(
        db_column="ZCLOUDFEEDASSETSENTRY", blank=True, null=True
    )
    zcomputedattributes = models.IntegerField(
        db_column="ZCOMPUTEDATTRIBUTES", blank=True, null=True
    )
    zconversation = models.IntegerField(
        db_column="ZCONVERSATION", blank=True, null=True
    )
    zdaygrouphighlightbeingassets = models.IntegerField(
        db_column="ZDAYGROUPHIGHLIGHTBEINGASSETS", blank=True, null=True
    )
    zdaygrouphighlightbeingextendedassets = models.IntegerField(
        db_column="ZDAYGROUPHIGHLIGHTBEINGEXTENDEDASSETS", blank=True, null=True
    )
    zdaygrouphighlightbeingkeyasset = models.IntegerField(
        db_column="ZDAYGROUPHIGHLIGHTBEINGKEYASSET", blank=True, null=True
    )
    zdaygrouphighlightbeingsummaryassets = models.IntegerField(
        db_column="ZDAYGROUPHIGHLIGHTBEINGSUMMARYASSETS", blank=True, null=True
    )
    zextendedattributes = models.IntegerField(
        db_column="ZEXTENDEDATTRIBUTES", blank=True, null=True
    )
    zhighlightbeingassets = models.IntegerField(
        db_column="ZHIGHLIGHTBEINGASSETS", blank=True, null=True
    )
    zhighlightbeingextendedassets = models.IntegerField(
        db_column="ZHIGHLIGHTBEINGEXTENDEDASSETS", blank=True, null=True
    )
    zhighlightbeingkeyasset = models.IntegerField(
        db_column="ZHIGHLIGHTBEINGKEYASSET", blank=True, null=True
    )
    zhighlightbeingsummaryassets = models.IntegerField(
        db_column="ZHIGHLIGHTBEINGSUMMARYASSETS", blank=True, null=True
    )
    zimportsession = models.IntegerField(
        db_column="ZIMPORTSESSION", blank=True, null=True
    )
    zlibraryscope = models.IntegerField(
        db_column="ZLIBRARYSCOPE", blank=True, null=True
    )
    zlibraryscopeoriginator = models.IntegerField(
        db_column="ZLIBRARYSCOPEORIGINATOR", blank=True, null=True
    )
    zmaster = models.IntegerField(db_column="ZMASTER", blank=True, null=True)
    zmediaanalysisattributes = models.IntegerField(
        db_column="ZMEDIAANALYSISATTRIBUTES", blank=True, null=True
    )
    zmoment = models.IntegerField(db_column="ZMOMENT", blank=True, null=True)
    zmomentshare = models.IntegerField(db_column="ZMOMENTSHARE", blank=True, null=True)
    zmonthhighlightbeingfirstasset = models.IntegerField(
        db_column="ZMONTHHIGHLIGHTBEINGFIRSTASSET", blank=True, null=True
    )
    zmonthhighlightbeingkeyasset = models.IntegerField(
        db_column="ZMONTHHIGHLIGHTBEINGKEYASSET", blank=True, null=True
    )
    zyearhighlightbeingkeyasset = models.IntegerField(
        db_column="ZYEARHIGHLIGHTBEINGKEYASSET", blank=True, null=True
    )
    z_fok_cloudfeedassetsentry = models.IntegerField(
        db_column="Z_FOK_CLOUDFEEDASSETSENTRY", blank=True, null=True
    )
    zaddeddate = models.TextField(db_column="ZADDEDDATE", blank=True, null=True)
    zadjustmenttimestamp = models.TextField(
        db_column="ZADJUSTMENTTIMESTAMP", blank=True, null=True
    )
    zanalysisstatemodificationdate = models.TextField(
        db_column="ZANALYSISSTATEMODIFICATIONDATE", blank=True, null=True
    )
    zcloudbatchpublishdate = models.TextField(
        db_column="ZCLOUDBATCHPUBLISHDATE", blank=True, null=True
    )
    zcloudlastviewedcommentdate = models.TextField(
        db_column="ZCLOUDLASTVIEWEDCOMMENTDATE", blank=True, null=True
    )
    zcloudserverpublishdate = models.TextField(
        db_column="ZCLOUDSERVERPUBLISHDATE", blank=True, null=True
    )
    zcurationscore = models.TextField(db_column="ZCURATIONSCORE", blank=True, null=True)
    zdatecreated = models.TextField(db_column="ZDATECREATED", blank=True, null=True)
    zduration = models.TextField(db_column="ZDURATION", blank=True, null=True)
    zfaceadjustmentversion = models.TextField(
        db_column="ZFACEADJUSTMENTVERSION", blank=True, null=True
    )
    zhdrgain = models.TextField(db_column="ZHDRGAIN", blank=True, null=True)
    zhighlightvisibilityscore = models.TextField(
        db_column="ZHIGHLIGHTVISIBILITYSCORE", blank=True, null=True
    )
    zlastshareddate = models.TextField(
        db_column="ZLASTSHAREDDATE", blank=True, null=True
    )
    zlatitude = models.TextField(db_column="ZLATITUDE", blank=True, null=True)
    zlongitude = models.TextField(db_column="ZLONGITUDE", blank=True, null=True)
    zmodificationdate = models.TextField(
        db_column="ZMODIFICATIONDATE", blank=True, null=True
    )
    zoverallaestheticscore = models.TextField(
        db_column="ZOVERALLAESTHETICSCORE", blank=True, null=True
    )
    zpromotionscore = models.TextField(
        db_column="ZPROMOTIONSCORE", blank=True, null=True
    )
    zsorttoken = models.TextField(db_column="ZSORTTOKEN", blank=True, null=True)
    ztrasheddate = models.TextField(db_column="ZTRASHEDDATE", blank=True, null=True)
    zavalancheuuid = models.CharField(db_column="ZAVALANCHEUUID", blank=True, null=True)
    zcloudassetguid = models.CharField(
        db_column="ZCLOUDASSETGUID", blank=True, null=True
    )
    zcloudbatchid = models.CharField(db_column="ZCLOUDBATCHID", blank=True, null=True)
    zcloudcollectionguid = models.CharField(
        db_column="ZCLOUDCOLLECTIONGUID", blank=True, null=True
    )
    zcloudownerhashedpersonid = models.CharField(
        db_column="ZCLOUDOWNERHASHEDPERSONID", blank=True, null=True
    )
    zdirectory = models.CharField(db_column="ZDIRECTORY", blank=True, null=True)
    zfilename = models.CharField(db_column="ZFILENAME", blank=True, null=True)
    zmediagroupuuid = models.CharField(
        db_column="ZMEDIAGROUPUUID", blank=True, null=True
    )
    zoriginalcolorspace = models.CharField(
        db_column="ZORIGINALCOLORSPACE", blank=True, null=True
    )
    zuniformtypeidentifier = models.CharField(
        db_column="ZUNIFORMTYPEIDENTIFIER", blank=True, null=True
    )
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zimagerequesthints = models.BinaryField(
        db_column="ZIMAGEREQUESTHINTS", blank=True, null=True
    )
    zlocationdata = models.BinaryField(db_column="ZLOCATIONDATA", blank=True, null=True)
    zismagiccarpet = models.IntegerField(
        db_column="ZISMAGICCARPET", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZASSET"


class Zassetanalysisstate(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zanalysisstate = models.IntegerField(
        db_column="ZANALYSISSTATE", blank=True, null=True
    )
    zworkerflags = models.IntegerField(db_column="ZWORKERFLAGS", blank=True, null=True)
    zworkertype = models.IntegerField(db_column="ZWORKERTYPE", blank=True, null=True)
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zignoreuntildate = models.TextField(
        db_column="ZIGNOREUNTILDATE", blank=True, null=True
    )
    zlastignoreddate = models.TextField(
        db_column="ZLASTIGNOREDDATE", blank=True, null=True
    )
    zsorttoken = models.TextField(db_column="ZSORTTOKEN", blank=True, null=True)
    zassetuuid = models.CharField(db_column="ZASSETUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZASSETANALYSISSTATE"


class Zassetdescription(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zassetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    zlongdescription = models.CharField(
        db_column="ZLONGDESCRIPTION", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZASSETDESCRIPTION"


class Zcharacterrecognitionattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zalgorithmversion = models.IntegerField(
        db_column="ZALGORITHMVERSION", blank=True, null=True
    )
    zmediaanalysisassetattributes = models.IntegerField(
        db_column="ZMEDIAANALYSISASSETATTRIBUTES", blank=True, null=True
    )
    zadjustmentversion = models.TextField(
        db_column="ZADJUSTMENTVERSION", blank=True, null=True
    )
    zcharacterrecognitiondata = models.BinaryField(
        db_column="ZCHARACTERRECOGNITIONDATA", blank=True, null=True
    )
    zmachinereadablecodedata = models.BinaryField(
        db_column="ZMACHINEREADABLECODEDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCHARACTERRECOGNITIONATTRIBUTES"


class Zcloudfeedentry(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zentryprioritynumber = models.IntegerField(
        db_column="ZENTRYPRIORITYNUMBER", blank=True, null=True
    )
    zentrytypenumber = models.IntegerField(
        db_column="ZENTRYTYPENUMBER", blank=True, null=True
    )
    zentrydate = models.TextField(db_column="ZENTRYDATE", blank=True, null=True)
    zentryalbumguid = models.CharField(
        db_column="ZENTRYALBUMGUID", blank=True, null=True
    )
    zentryinvitationrecordguid = models.CharField(
        db_column="ZENTRYINVITATIONRECORDGUID", blank=True, null=True
    )
    zentrycloudassetguid = models.CharField(
        db_column="ZENTRYCLOUDASSETGUID", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDFEEDENTRY"


class Zcloudmaster(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zfullsizejpegsource = models.IntegerField(
        db_column="ZFULLSIZEJPEGSOURCE", blank=True, null=True
    )
    zimportedby = models.IntegerField(db_column="ZIMPORTEDBY", blank=True, null=True)
    zoriginalorientation = models.IntegerField(
        db_column="ZORIGINALORIENTATION", blank=True, null=True
    )
    zplaceholderstate = models.IntegerField(
        db_column="ZPLACEHOLDERSTATE", blank=True, null=True
    )
    zvideoframerate = models.IntegerField(
        db_column="ZVIDEOFRAMERATE", blank=True, null=True
    )
    zmediametadata = models.IntegerField(
        db_column="ZMEDIAMETADATA", blank=True, null=True
    )
    zmomentshare = models.IntegerField(db_column="ZMOMENTSHARE", blank=True, null=True)
    zcreationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    zimportdate = models.TextField(db_column="ZIMPORTDATE", blank=True, null=True)
    zcloudmasterguid = models.CharField(
        db_column="ZCLOUDMASTERGUID", blank=True, null=True
    )
    zcodecname = models.CharField(db_column="ZCODECNAME", blank=True, null=True)
    zimportsessionid = models.CharField(
        db_column="ZIMPORTSESSIONID", blank=True, null=True
    )
    zmediametadatatype = models.CharField(
        db_column="ZMEDIAMETADATATYPE", blank=True, null=True
    )
    zoriginalfilename = models.CharField(
        db_column="ZORIGINALFILENAME", blank=True, null=True
    )
    zoriginatingassetidentifier = models.CharField(
        db_column="ZORIGINATINGASSETIDENTIFIER", blank=True, null=True
    )
    zuniformtypeidentifier = models.CharField(
        db_column="ZUNIFORMTYPEIDENTIFIER", blank=True, null=True
    )
    zimportedbybundleidentifier = models.CharField(
        db_column="ZIMPORTEDBYBUNDLEIDENTIFIER", blank=True, null=True
    )
    zimportedbydisplayname = models.CharField(
        db_column="ZIMPORTEDBYDISPLAYNAME", blank=True, null=True
    )
    zsourcemasterforduplicationidentifier = models.CharField(
        db_column="ZSOURCEMASTERFORDUPLICATIONIDENTIFIER", blank=True, null=True
    )
    zsourcemasterforduplicationscopeidentifier = models.CharField(
        db_column="ZSOURCEMASTERFORDUPLICATIONSCOPEIDENTIFIER", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDMASTER"


class Zcloudmastermediametadata(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zadditionalassetattributes = models.IntegerField(
        db_column="ZADDITIONALASSETATTRIBUTES", blank=True, null=True
    )
    zcloudmaster = models.IntegerField(db_column="ZCLOUDMASTER", blank=True, null=True)
    zdata = models.BinaryField(db_column="ZDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZCLOUDMASTERMEDIAMETADATA"


class Zcloudresource(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zfilesize = models.IntegerField(db_column="ZFILESIZE", blank=True, null=True)
    zheight = models.IntegerField(db_column="ZHEIGHT", blank=True, null=True)
    zisavailable = models.IntegerField(db_column="ZISAVAILABLE", blank=True, null=True)
    zislocallyavailable = models.IntegerField(
        db_column="ZISLOCALLYAVAILABLE", blank=True, null=True
    )
    zprefetchcount = models.IntegerField(
        db_column="ZPREFETCHCOUNT", blank=True, null=True
    )
    zsourcetype = models.IntegerField(db_column="ZSOURCETYPE", blank=True, null=True)
    ztype = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    zwidth = models.IntegerField(db_column="ZWIDTH", blank=True, null=True)
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zcloudmaster = models.IntegerField(db_column="ZCLOUDMASTER", blank=True, null=True)
    zdatecreated = models.TextField(db_column="ZDATECREATED", blank=True, null=True)
    zlastondemanddownloaddate = models.TextField(
        db_column="ZLASTONDEMANDDOWNLOADDATE", blank=True, null=True
    )
    zlastprefetchdate = models.TextField(
        db_column="ZLASTPREFETCHDATE", blank=True, null=True
    )
    zprunedat = models.TextField(db_column="ZPRUNEDAT", blank=True, null=True)
    zassetuuid = models.CharField(db_column="ZASSETUUID", blank=True, null=True)
    zfilepath = models.CharField(db_column="ZFILEPATH", blank=True, null=True)
    zfingerprint = models.CharField(db_column="ZFINGERPRINT", blank=True, null=True)
    zitemidentifier = models.CharField(
        db_column="ZITEMIDENTIFIER", blank=True, null=True
    )
    zuniformtypeidentifier = models.CharField(
        db_column="ZUNIFORMTYPEIDENTIFIER", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDRESOURCE"


class Zcloudsharedalbuminvitationrecord(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zinvitationstate = models.IntegerField(
        db_column="ZINVITATIONSTATE", blank=True, null=True
    )
    zinvitationstatelocal = models.IntegerField(
        db_column="ZINVITATIONSTATELOCAL", blank=True, null=True
    )
    zinviteeemailkey = models.IntegerField(
        db_column="ZINVITEEEMAILKEY", blank=True, null=True
    )
    zismine = models.IntegerField(db_column="ZISMINE", blank=True, null=True)
    zalbum = models.IntegerField(db_column="ZALBUM", blank=True, null=True)
    z_fok_album = models.IntegerField(db_column="Z_FOK_ALBUM", blank=True, null=True)
    zinviteesubscriptiondate = models.TextField(
        db_column="ZINVITEESUBSCRIPTIONDATE", blank=True, null=True
    )
    zalbumguid = models.CharField(db_column="ZALBUMGUID", blank=True, null=True)
    zcloudguid = models.CharField(db_column="ZCLOUDGUID", blank=True, null=True)
    zinviteefirstname = models.CharField(
        db_column="ZINVITEEFIRSTNAME", blank=True, null=True
    )
    zinviteefullname = models.CharField(
        db_column="ZINVITEEFULLNAME", blank=True, null=True
    )
    zinviteehashedpersonid = models.CharField(
        db_column="ZINVITEEHASHEDPERSONID", blank=True, null=True
    )
    zinviteelastname = models.CharField(
        db_column="ZINVITEELASTNAME", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDSHAREDALBUMINVITATIONRECORD"


class Zcloudsharedcomment(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zisbatchcomment = models.IntegerField(
        db_column="ZISBATCHCOMMENT", blank=True, null=True
    )
    ziscaption = models.IntegerField(db_column="ZISCAPTION", blank=True, null=True)
    zisdeletable = models.IntegerField(db_column="ZISDELETABLE", blank=True, null=True)
    zislike = models.IntegerField(db_column="ZISLIKE", blank=True, null=True)
    zismycomment = models.IntegerField(db_column="ZISMYCOMMENT", blank=True, null=True)
    zcloudfeedcommententry = models.IntegerField(
        db_column="ZCLOUDFEEDCOMMENTENTRY", blank=True, null=True
    )
    zcloudfeedlikecommententry = models.IntegerField(
        db_column="ZCLOUDFEEDLIKECOMMENTENTRY", blank=True, null=True
    )
    zcommentedasset = models.IntegerField(
        db_column="ZCOMMENTEDASSET", blank=True, null=True
    )
    zlikedasset = models.IntegerField(db_column="ZLIKEDASSET", blank=True, null=True)
    z_fok_cloudfeedcommententry = models.IntegerField(
        db_column="Z_FOK_CLOUDFEEDCOMMENTENTRY", blank=True, null=True
    )
    z_fok_cloudfeedlikecommententry = models.IntegerField(
        db_column="Z_FOK_CLOUDFEEDLIKECOMMENTENTRY", blank=True, null=True
    )
    zcommentclientdate = models.TextField(
        db_column="ZCOMMENTCLIENTDATE", blank=True, null=True
    )
    zcommentdate = models.TextField(db_column="ZCOMMENTDATE", blank=True, null=True)
    zcloudguid = models.CharField(db_column="ZCLOUDGUID", blank=True, null=True)
    zcommenttext = models.CharField(db_column="ZCOMMENTTEXT", blank=True, null=True)
    zcommenttype = models.CharField(db_column="ZCOMMENTTYPE", blank=True, null=True)
    zcommenterhashedpersonid = models.CharField(
        db_column="ZCOMMENTERHASHEDPERSONID", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDSHAREDCOMMENT"


class Zcomputedassetattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zbehavioralscore = models.TextField(
        db_column="ZBEHAVIORALSCORE", blank=True, null=True
    )
    zfailurescore = models.TextField(db_column="ZFAILURESCORE", blank=True, null=True)
    zharmoniouscolorscore = models.TextField(
        db_column="ZHARMONIOUSCOLORSCORE", blank=True, null=True
    )
    zimmersivenessscore = models.TextField(
        db_column="ZIMMERSIVENESSSCORE", blank=True, null=True
    )
    zinteractionscore = models.TextField(
        db_column="ZINTERACTIONSCORE", blank=True, null=True
    )
    zinterestingsubjectscore = models.TextField(
        db_column="ZINTERESTINGSUBJECTSCORE", blank=True, null=True
    )
    zintrusiveobjectpresencescore = models.TextField(
        db_column="ZINTRUSIVEOBJECTPRESENCESCORE", blank=True, null=True
    )
    zlivelycolorscore = models.TextField(
        db_column="ZLIVELYCOLORSCORE", blank=True, null=True
    )
    zlowlight = models.TextField(db_column="ZLOWLIGHT", blank=True, null=True)
    znoisescore = models.TextField(db_column="ZNOISESCORE", blank=True, null=True)
    zpleasantcameratiltscore = models.TextField(
        db_column="ZPLEASANTCAMERATILTSCORE", blank=True, null=True
    )
    zpleasantcompositionscore = models.TextField(
        db_column="ZPLEASANTCOMPOSITIONSCORE", blank=True, null=True
    )
    zpleasantlightingscore = models.TextField(
        db_column="ZPLEASANTLIGHTINGSCORE", blank=True, null=True
    )
    zpleasantpatternscore = models.TextField(
        db_column="ZPLEASANTPATTERNSCORE", blank=True, null=True
    )
    zpleasantperspectivescore = models.TextField(
        db_column="ZPLEASANTPERSPECTIVESCORE", blank=True, null=True
    )
    zpleasantpostprocessingscore = models.TextField(
        db_column="ZPLEASANTPOSTPROCESSINGSCORE", blank=True, null=True
    )
    zpleasantreflectionsscore = models.TextField(
        db_column="ZPLEASANTREFLECTIONSSCORE", blank=True, null=True
    )
    zpleasantsymmetryscore = models.TextField(
        db_column="ZPLEASANTSYMMETRYSCORE", blank=True, null=True
    )
    zsharplyfocusedsubjectscore = models.TextField(
        db_column="ZSHARPLYFOCUSEDSUBJECTSCORE", blank=True, null=True
    )
    ztastefullyblurredscore = models.TextField(
        db_column="ZTASTEFULLYBLURREDSCORE", blank=True, null=True
    )
    zwellchosensubjectscore = models.TextField(
        db_column="ZWELLCHOSENSUBJECTSCORE", blank=True, null=True
    )
    zwellframedsubjectscore = models.TextField(
        db_column="ZWELLFRAMEDSUBJECTSCORE", blank=True, null=True
    )
    zwelltimedshotscore = models.TextField(
        db_column="ZWELLTIMEDSHOTSCORE", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCOMPUTEDASSETATTRIBUTES"


class Zdeferredrebuildface(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zcloudnamesource = models.IntegerField(
        db_column="ZCLOUDNAMESOURCE", blank=True, null=True
    )
    zclusterrejected = models.IntegerField(
        db_column="ZCLUSTERREJECTED", blank=True, null=True
    )
    zfacealgorithmversion = models.IntegerField(
        db_column="ZFACEALGORITHMVERSION", blank=True, null=True
    )
    zhidden = models.IntegerField(db_column="ZHIDDEN", blank=True, null=True)
    zmanual = models.IntegerField(db_column="ZMANUAL", blank=True, null=True)
    znamesource = models.IntegerField(db_column="ZNAMESOURCE", blank=True, null=True)
    zrejected = models.IntegerField(db_column="ZREJECTED", blank=True, null=True)
    zrepresentative = models.IntegerField(
        db_column="ZREPRESENTATIVE", blank=True, null=True
    )
    zcenterx = models.TextField(db_column="ZCENTERX", blank=True, null=True)
    zcentery = models.TextField(db_column="ZCENTERY", blank=True, null=True)
    zsize = models.TextField(db_column="ZSIZE", blank=True, null=True)
    zassetcloudguid = models.CharField(
        db_column="ZASSETCLOUDGUID", blank=True, null=True
    )
    zassetuuid = models.CharField(db_column="ZASSETUUID", blank=True, null=True)
    zfaceuuid = models.CharField(db_column="ZFACEUUID", blank=True, null=True)
    zpersonuuid = models.CharField(db_column="ZPERSONUUID", blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDEFERREDREBUILDFACE"


class Zdetectedface(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zagetype = models.IntegerField(db_column="ZAGETYPE", blank=True, null=True)
    zassetvisible = models.IntegerField(
        db_column="ZASSETVISIBLE", blank=True, null=True
    )
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zcloudnamesource = models.IntegerField(
        db_column="ZCLOUDNAMESOURCE", blank=True, null=True
    )
    zclustersequencenumber = models.IntegerField(
        db_column="ZCLUSTERSEQUENCENUMBER", blank=True, null=True
    )
    zconfirmedfacecropgenerationstate = models.IntegerField(
        db_column="ZCONFIRMEDFACECROPGENERATIONSTATE", blank=True, null=True
    )
    zdetectiontype = models.IntegerField(
        db_column="ZDETECTIONTYPE", blank=True, null=True
    )
    zethnicitytype = models.IntegerField(
        db_column="ZETHNICITYTYPE", blank=True, null=True
    )
    zeyemakeuptype = models.IntegerField(
        db_column="ZEYEMAKEUPTYPE", blank=True, null=True
    )
    zeyesstate = models.IntegerField(db_column="ZEYESSTATE", blank=True, null=True)
    zfacealgorithmversion = models.IntegerField(
        db_column="ZFACEALGORITHMVERSION", blank=True, null=True
    )
    zfaceexpressiontype = models.IntegerField(
        db_column="ZFACEEXPRESSIONTYPE", blank=True, null=True
    )
    zfacialhairtype = models.IntegerField(
        db_column="ZFACIALHAIRTYPE", blank=True, null=True
    )
    zgazetype = models.IntegerField(db_column="ZGAZETYPE", blank=True, null=True)
    zgendertype = models.IntegerField(db_column="ZGENDERTYPE", blank=True, null=True)
    zglassestype = models.IntegerField(db_column="ZGLASSESTYPE", blank=True, null=True)
    zhaircolortype = models.IntegerField(
        db_column="ZHAIRCOLORTYPE", blank=True, null=True
    )
    zhairtype = models.IntegerField(db_column="ZHAIRTYPE", blank=True, null=True)
    zhasfacemask = models.IntegerField(db_column="ZHASFACEMASK", blank=True, null=True)
    zhassmile = models.IntegerField(db_column="ZHASSMILE", blank=True, null=True)
    zheadgeartype = models.IntegerField(
        db_column="ZHEADGEARTYPE", blank=True, null=True
    )
    zhidden = models.IntegerField(db_column="ZHIDDEN", blank=True, null=True)
    zisintrash = models.IntegerField(db_column="ZISINTRASH", blank=True, null=True)
    zislefteyeclosed = models.IntegerField(
        db_column="ZISLEFTEYECLOSED", blank=True, null=True
    )
    zisrighteyeclosed = models.IntegerField(
        db_column="ZISRIGHTEYECLOSED", blank=True, null=True
    )
    zlipmakeuptype = models.IntegerField(
        db_column="ZLIPMAKEUPTYPE", blank=True, null=True
    )
    zmanual = models.IntegerField(db_column="ZMANUAL", blank=True, null=True)
    znamesource = models.IntegerField(db_column="ZNAMESOURCE", blank=True, null=True)
    zposetype = models.IntegerField(db_column="ZPOSETYPE", blank=True, null=True)
    zqualitymeasure = models.IntegerField(
        db_column="ZQUALITYMEASURE", blank=True, null=True
    )
    zskintonetype = models.IntegerField(
        db_column="ZSKINTONETYPE", blank=True, null=True
    )
    zsmiletype = models.IntegerField(db_column="ZSMILETYPE", blank=True, null=True)
    zsourceheight = models.IntegerField(
        db_column="ZSOURCEHEIGHT", blank=True, null=True
    )
    zsourcewidth = models.IntegerField(db_column="ZSOURCEWIDTH", blank=True, null=True)
    ztrainingtype = models.IntegerField(
        db_column="ZTRAININGTYPE", blank=True, null=True
    )
    zvipmodeltype = models.IntegerField(
        db_column="ZVIPMODELTYPE", blank=True, null=True
    )
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zfacecrop = models.IntegerField(db_column="ZFACECROP", blank=True, null=True)
    zfacegroup = models.IntegerField(db_column="ZFACEGROUP", blank=True, null=True)
    zfacegroupbeingkeyface = models.IntegerField(
        db_column="ZFACEGROUPBEINGKEYFACE", blank=True, null=True
    )
    zfaceprint = models.IntegerField(db_column="ZFACEPRINT", blank=True, null=True)
    zperson = models.IntegerField(db_column="ZPERSON", blank=True, null=True)
    zpersonbeingkeyface = models.IntegerField(
        db_column="ZPERSONBEINGKEYFACE", blank=True, null=True
    )
    zadjustmentversion = models.TextField(
        db_column="ZADJUSTMENTVERSION", blank=True, null=True
    )
    zblurscore = models.TextField(db_column="ZBLURSCORE", blank=True, null=True)
    zbodycenterx = models.TextField(db_column="ZBODYCENTERX", blank=True, null=True)
    zbodycentery = models.TextField(db_column="ZBODYCENTERY", blank=True, null=True)
    zbodyheight = models.TextField(db_column="ZBODYHEIGHT", blank=True, null=True)
    zbodywidth = models.TextField(db_column="ZBODYWIDTH", blank=True, null=True)
    zcenterx = models.TextField(db_column="ZCENTERX", blank=True, null=True)
    zcentery = models.TextField(db_column="ZCENTERY", blank=True, null=True)
    zgazecenterx = models.TextField(db_column="ZGAZECENTERX", blank=True, null=True)
    zgazecentery = models.TextField(db_column="ZGAZECENTERY", blank=True, null=True)
    zlefteyex = models.TextField(db_column="ZLEFTEYEX", blank=True, null=True)
    zlefteyey = models.TextField(db_column="ZLEFTEYEY", blank=True, null=True)
    zmouthx = models.TextField(db_column="ZMOUTHX", blank=True, null=True)
    zmouthy = models.TextField(db_column="ZMOUTHY", blank=True, null=True)
    zposeyaw = models.TextField(db_column="ZPOSEYAW", blank=True, null=True)
    zquality = models.TextField(db_column="ZQUALITY", blank=True, null=True)
    zrighteyex = models.TextField(db_column="ZRIGHTEYEX", blank=True, null=True)
    zrighteyey = models.TextField(db_column="ZRIGHTEYEY", blank=True, null=True)
    zroll = models.TextField(db_column="ZROLL", blank=True, null=True)
    zsize = models.TextField(db_column="ZSIZE", blank=True, null=True)
    zyaw = models.TextField(db_column="ZYAW", blank=True, null=True)
    zgroupingidentifier = models.CharField(
        db_column="ZGROUPINGIDENTIFIER", blank=True, null=True
    )
    zmasteridentifier = models.CharField(
        db_column="ZMASTERIDENTIFIER", blank=True, null=True
    )
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDETECTEDFACE"


class Zdetectedfacegroup(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zpersonbuilderstate = models.IntegerField(
        db_column="ZPERSONBUILDERSTATE", blank=True, null=True
    )
    zunnamedfacecount = models.IntegerField(
        db_column="ZUNNAMEDFACECOUNT", blank=True, null=True
    )
    zassociatedperson = models.IntegerField(
        db_column="ZASSOCIATEDPERSON", blank=True, null=True
    )
    zkeyface = models.IntegerField(db_column="ZKEYFACE", blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDETECTEDFACEGROUP"


class Zdetectedfaceprint(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zfaceprintversion = models.IntegerField(
        db_column="ZFACEPRINTVERSION", blank=True, null=True
    )
    zface = models.IntegerField(db_column="ZFACE", blank=True, null=True)
    zdata = models.BinaryField(db_column="ZDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDETECTEDFACEPRINT"


class Zdetectiontrait(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    ztype = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    zvalue = models.IntegerField(db_column="ZVALUE", blank=True, null=True)
    zdetection = models.IntegerField(db_column="ZDETECTION", blank=True, null=True)
    zduration = models.TextField(db_column="ZDURATION", blank=True, null=True)
    zscore = models.TextField(db_column="ZSCORE", blank=True, null=True)
    zstarttime = models.TextField(db_column="ZSTARTTIME", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDETECTIONTRAIT"


class Zeditediptcattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zassetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    zactionadvised = models.CharField(db_column="ZACTIONADVISED", blank=True, null=True)
    zaudioduration = models.CharField(db_column="ZAUDIODURATION", blank=True, null=True)
    zaudiooutcue = models.CharField(db_column="ZAUDIOOUTCUE", blank=True, null=True)
    zaudiosamplingrate = models.CharField(
        db_column="ZAUDIOSAMPLINGRATE", blank=True, null=True
    )
    zaudiosamplingres = models.CharField(
        db_column="ZAUDIOSAMPLINGRES", blank=True, null=True
    )
    zaudiotype = models.CharField(db_column="ZAUDIOTYPE", blank=True, null=True)
    zbyline = models.CharField(db_column="ZBYLINE", blank=True, null=True)
    zbylinetitle = models.CharField(db_column="ZBYLINETITLE", blank=True, null=True)
    zcaption = models.CharField(db_column="ZCAPTION", blank=True, null=True)
    zcategory = models.CharField(db_column="ZCATEGORY", blank=True, null=True)
    zciadrcity = models.CharField(db_column="ZCIADRCITY", blank=True, null=True)
    zciadrctry = models.CharField(db_column="ZCIADRCTRY", blank=True, null=True)
    zciadrextadr = models.CharField(db_column="ZCIADREXTADR", blank=True, null=True)
    zciadrpcode = models.CharField(db_column="ZCIADRPCODE", blank=True, null=True)
    zciadrregion = models.CharField(db_column="ZCIADRREGION", blank=True, null=True)
    zciemailwork = models.CharField(db_column="ZCIEMAILWORK", blank=True, null=True)
    zcitelwork = models.CharField(db_column="ZCITELWORK", blank=True, null=True)
    zciurlwork = models.CharField(db_column="ZCIURLWORK", blank=True, null=True)
    zcity = models.CharField(db_column="ZCITY", blank=True, null=True)
    zcontact = models.CharField(db_column="ZCONTACT", blank=True, null=True)
    zcontentlocationcode = models.CharField(
        db_column="ZCONTENTLOCATIONCODE", blank=True, null=True
    )
    zcontentlocationname = models.CharField(
        db_column="ZCONTENTLOCATIONNAME", blank=True, null=True
    )
    zcopyrightnotice = models.CharField(
        db_column="ZCOPYRIGHTNOTICE", blank=True, null=True
    )
    zcountryprimarylocationcode = models.CharField(
        db_column="ZCOUNTRYPRIMARYLOCATIONCODE", blank=True, null=True
    )
    zcountryprimarylocationname = models.CharField(
        db_column="ZCOUNTRYPRIMARYLOCATIONNAME", blank=True, null=True
    )
    zcreatorcontactinfo = models.CharField(
        db_column="ZCREATORCONTACTINFO", blank=True, null=True
    )
    zcredit = models.CharField(db_column="ZCREDIT", blank=True, null=True)
    zdatecreated = models.CharField(db_column="ZDATECREATED", blank=True, null=True)
    zdigitalcreationdate = models.CharField(
        db_column="ZDIGITALCREATIONDATE", blank=True, null=True
    )
    zdigitalcreationtime = models.CharField(
        db_column="ZDIGITALCREATIONTIME", blank=True, null=True
    )
    zeditstatus = models.CharField(db_column="ZEDITSTATUS", blank=True, null=True)
    zeditorialupdate = models.CharField(
        db_column="ZEDITORIALUPDATE", blank=True, null=True
    )
    zexpirationdate = models.CharField(
        db_column="ZEXPIRATIONDATE", blank=True, null=True
    )
    zexpirationtime = models.CharField(
        db_column="ZEXPIRATIONTIME", blank=True, null=True
    )
    zfixtureidentifier = models.CharField(
        db_column="ZFIXTUREIDENTIFIER", blank=True, null=True
    )
    zheadline = models.CharField(db_column="ZHEADLINE", blank=True, null=True)
    zimageorientation = models.CharField(
        db_column="ZIMAGEORIENTATION", blank=True, null=True
    )
    zimagetype = models.CharField(db_column="ZIMAGETYPE", blank=True, null=True)
    zkeywords = models.CharField(db_column="ZKEYWORDS", blank=True, null=True)
    zlanguageidentifier = models.CharField(
        db_column="ZLANGUAGEIDENTIFIER", blank=True, null=True
    )
    zobjectattributereference = models.CharField(
        db_column="ZOBJECTATTRIBUTEREFERENCE", blank=True, null=True
    )
    zobjectcycle = models.CharField(db_column="ZOBJECTCYCLE", blank=True, null=True)
    zobjectname = models.CharField(db_column="ZOBJECTNAME", blank=True, null=True)
    zobjecttypereference = models.CharField(
        db_column="ZOBJECTTYPEREFERENCE", blank=True, null=True
    )
    zoriginaltransmissionreference = models.CharField(
        db_column="ZORIGINALTRANSMISSIONREFERENCE", blank=True, null=True
    )
    zoriginatingprogram = models.CharField(
        db_column="ZORIGINATINGPROGRAM", blank=True, null=True
    )
    zprogramversion = models.CharField(
        db_column="ZPROGRAMVERSION", blank=True, null=True
    )
    zprovincestate = models.CharField(db_column="ZPROVINCESTATE", blank=True, null=True)
    zreferencedate = models.CharField(db_column="ZREFERENCEDATE", blank=True, null=True)
    zreferencenumber = models.CharField(
        db_column="ZREFERENCENUMBER", blank=True, null=True
    )
    zreferenceservice = models.CharField(
        db_column="ZREFERENCESERVICE", blank=True, null=True
    )
    zreleasedate = models.CharField(db_column="ZRELEASEDATE", blank=True, null=True)
    zreleasetime = models.CharField(db_column="ZRELEASETIME", blank=True, null=True)
    zscene = models.CharField(db_column="ZSCENE", blank=True, null=True)
    zsource = models.CharField(db_column="ZSOURCE", blank=True, null=True)
    zspecialinstructions = models.CharField(
        db_column="ZSPECIALINSTRUCTIONS", blank=True, null=True
    )
    zstarrating = models.CharField(db_column="ZSTARRATING", blank=True, null=True)
    zsublocation = models.CharField(db_column="ZSUBLOCATION", blank=True, null=True)
    zsubjectreference = models.CharField(
        db_column="ZSUBJECTREFERENCE", blank=True, null=True
    )
    zsupplementalcategory = models.CharField(
        db_column="ZSUPPLEMENTALCATEGORY", blank=True, null=True
    )
    ztimecreated = models.CharField(db_column="ZTIMECREATED", blank=True, null=True)
    zurgency = models.CharField(db_column="ZURGENCY", blank=True, null=True)
    zusageterms = models.CharField(db_column="ZUSAGETERMS", blank=True, null=True)
    zwritereditor = models.CharField(db_column="ZWRITEREDITOR", blank=True, null=True)
    zdata = models.BinaryField(db_column="ZDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZEDITEDIPTCATTRIBUTES"


class Zextendedattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zflashfired = models.IntegerField(db_column="ZFLASHFIRED", blank=True, null=True)
    ziso = models.IntegerField(db_column="ZISO", blank=True, null=True)
    zmeteringmode = models.IntegerField(
        db_column="ZMETERINGMODE", blank=True, null=True
    )
    zsamplerate = models.IntegerField(db_column="ZSAMPLERATE", blank=True, null=True)
    ztrackformat = models.IntegerField(db_column="ZTRACKFORMAT", blank=True, null=True)
    zwhitebalance = models.IntegerField(
        db_column="ZWHITEBALANCE", blank=True, null=True
    )
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zaperture = models.TextField(db_column="ZAPERTURE", blank=True, null=True)
    zbitrate = models.TextField(db_column="ZBITRATE", blank=True, null=True)
    zduration = models.TextField(db_column="ZDURATION", blank=True, null=True)
    zexposurebias = models.TextField(db_column="ZEXPOSUREBIAS", blank=True, null=True)
    zfocallength = models.TextField(db_column="ZFOCALLENGTH", blank=True, null=True)
    zfps = models.TextField(db_column="ZFPS", blank=True, null=True)
    zlatitude = models.TextField(db_column="ZLATITUDE", blank=True, null=True)
    zlongitude = models.TextField(db_column="ZLONGITUDE", blank=True, null=True)
    zshutterspeed = models.TextField(db_column="ZSHUTTERSPEED", blank=True, null=True)
    zcameramake = models.CharField(db_column="ZCAMERAMAKE", blank=True, null=True)
    zcameramodel = models.CharField(db_column="ZCAMERAMODEL", blank=True, null=True)
    zcodec = models.CharField(db_column="ZCODEC", blank=True, null=True)
    zlensmodel = models.CharField(db_column="ZLENSMODEL", blank=True, null=True)
    zslushwarmthbias = models.TextField(
        db_column="ZSLUSHWARMTHBIAS", blank=True, null=True
    )
    zdigitalzoomratio = models.TextField(
        db_column="ZDIGITALZOOMRATIO", blank=True, null=True
    )
    zslushpreset = models.IntegerField(db_column="ZSLUSHPRESET", blank=True, null=True)
    zslushscenebias = models.TextField(
        db_column="ZSLUSHSCENEBIAS", blank=True, null=True
    )
    zslushversion = models.IntegerField(
        db_column="ZSLUSHVERSION", blank=True, null=True
    )
    zfocallengthin35mm = models.IntegerField(
        db_column="ZFOCALLENGTHIN35MM", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZEXTENDEDATTRIBUTES"


class Zfacecrop(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zclouddeletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zcloudtype = models.IntegerField(db_column="ZCLOUDTYPE", blank=True, null=True)
    zstate = models.IntegerField(db_column="ZSTATE", blank=True, null=True)
    ztype = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zface = models.IntegerField(db_column="ZFACE", blank=True, null=True)
    zperson = models.IntegerField(db_column="ZPERSON", blank=True, null=True)
    zinvalidmergecandidatepersonuuid = models.CharField(
        db_column="ZINVALIDMERGECANDIDATEPERSONUUID", blank=True, null=True
    )
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zresourcedata = models.BinaryField(db_column="ZRESOURCEDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZFACECROP"


class Zfilesystembookmark(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zresource = models.IntegerField(db_column="ZRESOURCE", blank=True, null=True)
    zpathrelativetovolume = models.CharField(
        db_column="ZPATHRELATIVETOVOLUME", blank=True, null=True
    )
    zbookmarkdata = models.BinaryField(db_column="ZBOOKMARKDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZFILESYSTEMBOOKMARK"


class Zfilesystemvolume(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zname = models.CharField(db_column="ZNAME", blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zvolumeuuidstring = models.CharField(
        db_column="ZVOLUMEUUIDSTRING", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZFILESYSTEMVOLUME"


class Zgenericalbum(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zcachedcount = models.IntegerField(db_column="ZCACHEDCOUNT", blank=True, null=True)
    zcachedphotoscount = models.IntegerField(
        db_column="ZCACHEDPHOTOSCOUNT", blank=True, null=True
    )
    zcachedvideoscount = models.IntegerField(
        db_column="ZCACHEDVIDEOSCOUNT", blank=True, null=True
    )
    zclouddeletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zcustomsortascending = models.IntegerField(
        db_column="ZCUSTOMSORTASCENDING", blank=True, null=True
    )
    zcustomsortkey = models.IntegerField(
        db_column="ZCUSTOMSORTKEY", blank=True, null=True
    )
    zispinned = models.IntegerField(db_column="ZISPINNED", blank=True, null=True)
    zisprototype = models.IntegerField(db_column="ZISPROTOTYPE", blank=True, null=True)
    zkind = models.IntegerField(db_column="ZKIND", blank=True, null=True)
    zpendingitemscount = models.IntegerField(
        db_column="ZPENDINGITEMSCOUNT", blank=True, null=True
    )
    zpendingitemstype = models.IntegerField(
        db_column="ZPENDINGITEMSTYPE", blank=True, null=True
    )
    zsynceventorderkey = models.IntegerField(
        db_column="ZSYNCEVENTORDERKEY", blank=True, null=True
    )
    ztrashedstate = models.IntegerField(
        db_column="ZTRASHEDSTATE", blank=True, null=True
    )
    zcustomkeyasset = models.IntegerField(
        db_column="ZCUSTOMKEYASSET", blank=True, null=True
    )
    zkeyasset = models.IntegerField(db_column="ZKEYASSET", blank=True, null=True)
    zparentfolder = models.IntegerField(
        db_column="ZPARENTFOLDER", blank=True, null=True
    )
    zsecondarykeyasset = models.IntegerField(
        db_column="ZSECONDARYKEYASSET", blank=True, null=True
    )
    ztertiarykeyasset = models.IntegerField(
        db_column="ZTERTIARYKEYASSET", blank=True, null=True
    )
    zcloudalbumsubtype = models.IntegerField(
        db_column="ZCLOUDALBUMSUBTYPE", blank=True, null=True
    )
    zcloudmultiplecontributorsenabled = models.IntegerField(
        db_column="ZCLOUDMULTIPLECONTRIBUTORSENABLED", blank=True, null=True
    )
    zcloudmultiplecontributorsenabledlocal = models.IntegerField(
        db_column="ZCLOUDMULTIPLECONTRIBUTORSENABLEDLOCAL", blank=True, null=True
    )
    zcloudnotificationsenabled = models.IntegerField(
        db_column="ZCLOUDNOTIFICATIONSENABLED", blank=True, null=True
    )
    zcloudowneremailkey = models.IntegerField(
        db_column="ZCLOUDOWNEREMAILKEY", blank=True, null=True
    )
    zcloudowneriswhitelisted = models.IntegerField(
        db_column="ZCLOUDOWNERISWHITELISTED", blank=True, null=True
    )
    zcloudpublicurlenabled = models.IntegerField(
        db_column="ZCLOUDPUBLICURLENABLED", blank=True, null=True
    )
    zcloudpublicurlenabledlocal = models.IntegerField(
        db_column="ZCLOUDPUBLICURLENABLEDLOCAL", blank=True, null=True
    )
    zcloudrelationshipstate = models.IntegerField(
        db_column="ZCLOUDRELATIONSHIPSTATE", blank=True, null=True
    )
    zcloudrelationshipstatelocal = models.IntegerField(
        db_column="ZCLOUDRELATIONSHIPSTATELOCAL", blank=True, null=True
    )
    zhasunseencontent = models.IntegerField(
        db_column="ZHASUNSEENCONTENT", blank=True, null=True
    )
    zisowned = models.IntegerField(db_column="ZISOWNED", blank=True, null=True)
    zunseenassetscount = models.IntegerField(
        db_column="ZUNSEENASSETSCOUNT", blank=True, null=True
    )
    zkeyassetfaceidentifier = models.IntegerField(
        db_column="ZKEYASSETFACEIDENTIFIER", blank=True, null=True
    )
    zkeyassetfacethumbnailindex = models.IntegerField(
        db_column="ZKEYASSETFACETHUMBNAILINDEX", blank=True, null=True
    )
    zsyndicate = models.IntegerField(db_column="ZSYNDICATE", blank=True, null=True)
    z_fok_parentfolder = models.IntegerField(
        db_column="Z_FOK_PARENTFOLDER", blank=True, null=True
    )
    zcreationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    zenddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    zstartdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    ztrasheddate = models.TextField(db_column="ZTRASHEDDATE", blank=True, null=True)
    zcloudcreationdate = models.TextField(
        db_column="ZCLOUDCREATIONDATE", blank=True, null=True
    )
    zcloudlastcontributiondate = models.TextField(
        db_column="ZCLOUDLASTCONTRIBUTIONDATE", blank=True, null=True
    )
    zcloudlastinterestingchangedate = models.TextField(
        db_column="ZCLOUDLASTINTERESTINGCHANGEDATE", blank=True, null=True
    )
    zcloudsubscriptiondate = models.TextField(
        db_column="ZCLOUDSUBSCRIPTIONDATE", blank=True, null=True
    )
    zcloudguid = models.CharField(db_column="ZCLOUDGUID", blank=True, null=True)
    zimportsessionid = models.CharField(
        db_column="ZIMPORTSESSIONID", blank=True, null=True
    )
    zimportedbybundleidentifier = models.CharField(
        db_column="ZIMPORTEDBYBUNDLEIDENTIFIER", blank=True, null=True
    )
    ztitle = models.CharField(db_column="ZTITLE", blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zcloudownerfirstname = models.CharField(
        db_column="ZCLOUDOWNERFIRSTNAME", blank=True, null=True
    )
    zcloudownerfullname = models.CharField(
        db_column="ZCLOUDOWNERFULLNAME", blank=True, null=True
    )
    zcloudownerhashedpersonid = models.CharField(
        db_column="ZCLOUDOWNERHASHEDPERSONID", blank=True, null=True
    )
    zcloudownerlastname = models.CharField(
        db_column="ZCLOUDOWNERLASTNAME", blank=True, null=True
    )
    zcloudpersonid = models.CharField(db_column="ZCLOUDPERSONID", blank=True, null=True)
    zpublicurl = models.CharField(db_column="ZPUBLICURL", blank=True, null=True)
    zprojectdocumenttype = models.CharField(
        db_column="ZPROJECTDOCUMENTTYPE", blank=True, null=True
    )
    zprojectextensionidentifier = models.CharField(
        db_column="ZPROJECTEXTENSIONIDENTIFIER", blank=True, null=True
    )
    zprojectrenderuuid = models.CharField(
        db_column="ZPROJECTRENDERUUID", blank=True, null=True
    )
    zcustomquerytype = models.CharField(
        db_column="ZCUSTOMQUERYTYPE", blank=True, null=True
    )
    zcloudmetadata = models.BinaryField(
        db_column="ZCLOUDMETADATA", blank=True, null=True
    )
    zuserquerydata = models.BinaryField(
        db_column="ZUSERQUERYDATA", blank=True, null=True
    )
    zprojectdata = models.BinaryField(db_column="ZPROJECTDATA", blank=True, null=True)
    zcustomqueryparameters = models.BinaryField(
        db_column="ZCUSTOMQUERYPARAMETERS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZGENERICALBUM"


class Zglobalkeyvalue(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zboolvalue = models.IntegerField(db_column="ZBOOLVALUE", blank=True, null=True)
    zintegervalue = models.IntegerField(
        db_column="ZINTEGERVALUE", blank=True, null=True
    )
    ztype = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    zdatevalue = models.TextField(db_column="ZDATEVALUE", blank=True, null=True)
    zdoublevalue = models.TextField(db_column="ZDOUBLEVALUE", blank=True, null=True)
    zkey = models.CharField(db_column="ZKEY", unique=True, blank=True, null=True)
    zstringvalue = models.CharField(db_column="ZSTRINGVALUE", blank=True, null=True)
    zanyvalue = models.BinaryField(db_column="ZANYVALUE", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZGLOBALKEYVALUE"


class Zinternalresource(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zclouddeletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zcloudprefetchcount = models.IntegerField(
        db_column="ZCLOUDPREFETCHCOUNT", blank=True, null=True
    )
    zcloudsourcetype = models.IntegerField(
        db_column="ZCLOUDSOURCETYPE", blank=True, null=True
    )
    zdatalength = models.IntegerField(db_column="ZDATALENGTH", blank=True, null=True)
    zdatastoreclassid = models.IntegerField(
        db_column="ZDATASTORECLASSID", blank=True, null=True
    )
    zdatastoresubtype = models.IntegerField(
        db_column="ZDATASTORESUBTYPE", blank=True, null=True
    )
    zfileid = models.IntegerField(db_column="ZFILEID", blank=True, null=True)
    zlocalavailability = models.IntegerField(
        db_column="ZLOCALAVAILABILITY", blank=True, null=True
    )
    zlocalavailabilitytarget = models.IntegerField(
        db_column="ZLOCALAVAILABILITYTARGET", blank=True, null=True
    )
    zorientation = models.IntegerField(db_column="ZORIENTATION", blank=True, null=True)
    zptptrashedstate = models.IntegerField(
        db_column="ZPTPTRASHEDSTATE", blank=True, null=True
    )
    zqualitysortvalue = models.IntegerField(
        db_column="ZQUALITYSORTVALUE", blank=True, null=True
    )
    zrecipeid = models.IntegerField(db_column="ZRECIPEID", blank=True, null=True)
    zremoteavailability = models.IntegerField(
        db_column="ZREMOTEAVAILABILITY", blank=True, null=True
    )
    zremoteavailabilitytarget = models.IntegerField(
        db_column="ZREMOTEAVAILABILITYTARGET", blank=True, null=True
    )
    zresourcetype = models.IntegerField(
        db_column="ZRESOURCETYPE", blank=True, null=True
    )
    zsidecarindex = models.IntegerField(
        db_column="ZSIDECARINDEX", blank=True, null=True
    )
    ztrashedstate = models.IntegerField(
        db_column="ZTRASHEDSTATE", blank=True, null=True
    )
    zunorientedheight = models.IntegerField(
        db_column="ZUNORIENTEDHEIGHT", blank=True, null=True
    )
    zunorientedwidth = models.IntegerField(
        db_column="ZUNORIENTEDWIDTH", blank=True, null=True
    )
    zuticonformancehint = models.IntegerField(
        db_column="ZUTICONFORMANCEHINT", blank=True, null=True
    )
    zversion = models.IntegerField(db_column="ZVERSION", blank=True, null=True)
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zfilesystembookmark = models.IntegerField(
        db_column="ZFILESYSTEMBOOKMARK", blank=True, null=True
    )
    zfilesystemvolume = models.IntegerField(
        db_column="ZFILESYSTEMVOLUME", blank=True, null=True
    )
    ztransientcloudmaster = models.IntegerField(
        db_column="ZTRANSIENTCLOUDMASTER", blank=True, null=True
    )
    zcloudlastondemanddownloaddate = models.TextField(
        db_column="ZCLOUDLASTONDEMANDDOWNLOADDATE", blank=True, null=True
    )
    zcloudlastprefetchdate = models.TextField(
        db_column="ZCLOUDLASTPREFETCHDATE", blank=True, null=True
    )
    zcloudmasterdatecreated = models.TextField(
        db_column="ZCLOUDMASTERDATECREATED", blank=True, null=True
    )
    zcloudprunedat = models.TextField(db_column="ZCLOUDPRUNEDAT", blank=True, null=True)
    ztrasheddate = models.TextField(db_column="ZTRASHEDDATE", blank=True, null=True)
    zclouddeleteassetuuidwithresourcetype = models.CharField(
        db_column="ZCLOUDDELETEASSETUUIDWITHRESOURCETYPE", blank=True, null=True
    )
    zcodecfourcharcodename = models.CharField(
        db_column="ZCODECFOURCHARCODENAME", blank=True, null=True
    )
    zcompactuti = models.CharField(db_column="ZCOMPACTUTI", blank=True, null=True)
    zfingerprint = models.CharField(db_column="ZFINGERPRINT", blank=True, null=True)
    zdatastorekeydata = models.BinaryField(
        db_column="ZDATASTOREKEYDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZINTERNALRESOURCE"
        unique_together = (
            ("zasset", "zresourcetype", "zversion", "zrecipeid", "zcompactuti"),
        )


class Zkeyword(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zshortcut = models.CharField(db_column="ZSHORTCUT", blank=True, null=True)
    ztitle = models.CharField(db_column="ZTITLE", unique=True, blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZKEYWORD"


class Zlegacyface(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zidentifier = models.IntegerField(db_column="ZIDENTIFIER", blank=True, null=True)
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zalbumuuid = models.CharField(db_column="ZALBUMUUID", blank=True, null=True)
    zrelativerectvalue = models.BinaryField(
        db_column="ZRELATIVERECTVALUE", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZLEGACYFACE"


class Zlimitedlibraryfetchfilter(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zapplicationidentifier = models.CharField(
        db_column="ZAPPLICATIONIDENTIFIER", unique=True, blank=True, null=True
    )
    zdesignatedrequirement = models.CharField(
        db_column="ZDESIGNATEDREQUIREMENT", blank=True, null=True
    )
    zfetchfilterdata = models.BinaryField(
        db_column="ZFETCHFILTERDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZLIMITEDLIBRARYFETCHFILTER"


class Zmediaanalysisassetattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zaudioclassification = models.IntegerField(
        db_column="ZAUDIOCLASSIFICATION", blank=True, null=True
    )
    zbestvideorangedurationtimescale = models.IntegerField(
        db_column="ZBESTVIDEORANGEDURATIONTIMESCALE", blank=True, null=True
    )
    zbestvideorangedurationvalue = models.IntegerField(
        db_column="ZBESTVIDEORANGEDURATIONVALUE", blank=True, null=True
    )
    zbestvideorangestarttimescale = models.IntegerField(
        db_column="ZBESTVIDEORANGESTARTTIMESCALE", blank=True, null=True
    )
    zbestvideorangestartvalue = models.IntegerField(
        db_column="ZBESTVIDEORANGESTARTVALUE", blank=True, null=True
    )
    zfacecount = models.IntegerField(db_column="ZFACECOUNT", blank=True, null=True)
    zmediaanalysisversion = models.IntegerField(
        db_column="ZMEDIAANALYSISVERSION", blank=True, null=True
    )
    zpackedbestplaybackrect = models.IntegerField(
        db_column="ZPACKEDBESTPLAYBACKRECT", blank=True, null=True
    )
    zasset = models.IntegerField(db_column="ZASSET", blank=True, null=True)
    zactivityscore = models.TextField(db_column="ZACTIVITYSCORE", blank=True, null=True)
    zautoplaysuggestionscore = models.TextField(
        db_column="ZAUTOPLAYSUGGESTIONSCORE", blank=True, null=True
    )
    zblurrinessscore = models.TextField(
        db_column="ZBLURRINESSSCORE", blank=True, null=True
    )
    zexposurescore = models.TextField(db_column="ZEXPOSURESCORE", blank=True, null=True)
    zmediaanalysistimestamp = models.TextField(
        db_column="ZMEDIAANALYSISTIMESTAMP", blank=True, null=True
    )
    zvideoscore = models.TextField(db_column="ZVIDEOSCORE", blank=True, null=True)
    zcolornormalizationdata = models.BinaryField(
        db_column="ZCOLORNORMALIZATIONDATA", blank=True, null=True
    )
    zsyndicationprocessingvalue = models.IntegerField(
        db_column="ZSYNDICATIONPROCESSINGVALUE", blank=True, null=True
    )
    zprobablerotationdirection = models.IntegerField(
        db_column="ZPROBABLEROTATIONDIRECTION", blank=True, null=True
    )
    zcharacterrecognitionattributes = models.IntegerField(
        db_column="ZCHARACTERRECOGNITIONATTRIBUTES", blank=True, null=True
    )
    zscreentimedeviceimagesensitivity = models.IntegerField(
        db_column="ZSCREENTIMEDEVICEIMAGESENSITIVITY", blank=True, null=True
    )
    zsyndicationprocessingversion = models.IntegerField(
        db_column="ZSYNDICATIONPROCESSINGVERSION", blank=True, null=True
    )
    zprobablerotationdirectionconfidence = models.TextField(
        db_column="ZPROBABLEROTATIONDIRECTIONCONFIDENCE", blank=True, null=True
    )
    zvisualsearchattributes = models.IntegerField(
        db_column="ZVISUALSEARCHATTRIBUTES", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZMEDIAANALYSISASSETATTRIBUTES"


class Zmemory(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zcategory = models.IntegerField(db_column="ZCATEGORY", blank=True, null=True)
    zclouddeletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zfavorite = models.IntegerField(db_column="ZFAVORITE", blank=True, null=True)
    zfeaturedstate = models.IntegerField(
        db_column="ZFEATUREDSTATE", blank=True, null=True
    )
    znotificationstate = models.IntegerField(
        db_column="ZNOTIFICATIONSTATE", blank=True, null=True
    )
    zpendingplaycount = models.IntegerField(
        db_column="ZPENDINGPLAYCOUNT", blank=True, null=True
    )
    zpendingsharecount = models.IntegerField(
        db_column="ZPENDINGSHARECOUNT", blank=True, null=True
    )
    zpendingstate = models.IntegerField(
        db_column="ZPENDINGSTATE", blank=True, null=True
    )
    zpendingviewcount = models.IntegerField(
        db_column="ZPENDINGVIEWCOUNT", blank=True, null=True
    )
    zphotosgraphversion = models.IntegerField(
        db_column="ZPHOTOSGRAPHVERSION", blank=True, null=True
    )
    zplaycount = models.IntegerField(db_column="ZPLAYCOUNT", blank=True, null=True)
    zrejected = models.IntegerField(db_column="ZREJECTED", blank=True, null=True)
    zsharecount = models.IntegerField(db_column="ZSHARECOUNT", blank=True, null=True)
    zstorycolorgradekind = models.IntegerField(
        db_column="ZSTORYCOLORGRADEKIND", blank=True, null=True
    )
    zstoryserializedtitlecategory = models.IntegerField(
        db_column="ZSTORYSERIALIZEDTITLECATEGORY", blank=True, null=True
    )
    zsubcategory = models.IntegerField(db_column="ZSUBCATEGORY", blank=True, null=True)
    zsyndicatedcontentstate = models.IntegerField(
        db_column="ZSYNDICATEDCONTENTSTATE", blank=True, null=True
    )
    zuseractionoptions = models.IntegerField(
        db_column="ZUSERACTIONOPTIONS", blank=True, null=True
    )
    zviewcount = models.IntegerField(db_column="ZVIEWCOUNT", blank=True, null=True)
    zkeyasset = models.IntegerField(db_column="ZKEYASSET", blank=True, null=True)
    zcreationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    zlastenrichmentdate = models.TextField(
        db_column="ZLASTENRICHMENTDATE", blank=True, null=True
    )
    zlastmovieplayeddate = models.TextField(
        db_column="ZLASTMOVIEPLAYEDDATE", blank=True, null=True
    )
    zlastvieweddate = models.TextField(
        db_column="ZLASTVIEWEDDATE", blank=True, null=True
    )
    zscore = models.TextField(db_column="ZSCORE", blank=True, null=True)
    zgraphmemoryidentifier = models.CharField(
        db_column="ZGRAPHMEMORYIDENTIFIER", blank=True, null=True
    )
    zsubtitle = models.CharField(db_column="ZSUBTITLE", blank=True, null=True)
    ztitle = models.CharField(db_column="ZTITLE", blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zmovieassetstate = models.BinaryField(
        db_column="ZMOVIEASSETSTATE", blank=True, null=True
    )
    zassetlistpredicate = models.BinaryField(
        db_column="ZASSETLISTPREDICATE", blank=True, null=True
    )
    zblacklistedfeature = models.BinaryField(
        db_column="ZBLACKLISTEDFEATURE", blank=True, null=True
    )
    zmoviedata = models.BinaryField(db_column="ZMOVIEDATA", blank=True, null=True)
    zphotosgraphdata = models.BinaryField(
        db_column="ZPHOTOSGRAPHDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZMEMORY"


class Zmigrationhistory(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zforcerebuildreason = models.IntegerField(
        db_column="ZFORCEREBUILDREASON", blank=True, null=True
    )
    zindex = models.IntegerField(db_column="ZINDEX", unique=True, blank=True, null=True)
    zmigrationtype = models.IntegerField(
        db_column="ZMIGRATIONTYPE", blank=True, null=True
    )
    zmodelversion = models.IntegerField(
        db_column="ZMODELVERSION", blank=True, null=True
    )
    zorigin = models.IntegerField(db_column="ZORIGIN", blank=True, null=True)
    zsourcemodelversion = models.IntegerField(
        db_column="ZSOURCEMODELVERSION", blank=True, null=True
    )
    zmigrationdate = models.TextField(db_column="ZMIGRATIONDATE", blank=True, null=True)
    zosversion = models.CharField(db_column="ZOSVERSION", blank=True, null=True)
    zstoreuuid = models.CharField(db_column="ZSTOREUUID", blank=True, null=True)
    zglobalkeyvalues = models.BinaryField(
        db_column="ZGLOBALKEYVALUES", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZMIGRATIONHISTORY"


class Zmoment(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zcachedcount = models.IntegerField(db_column="ZCACHEDCOUNT", blank=True, null=True)
    zcachedphotoscount = models.IntegerField(
        db_column="ZCACHEDPHOTOSCOUNT", blank=True, null=True
    )
    zcachedvideoscount = models.IntegerField(
        db_column="ZCACHEDVIDEOSCOUNT", blank=True, null=True
    )
    zoriginatorstate = models.IntegerField(
        db_column="ZORIGINATORSTATE", blank=True, null=True
    )
    zprocessedlocation = models.IntegerField(
        db_column="ZPROCESSEDLOCATION", blank=True, null=True
    )
    ztimezoneoffset = models.IntegerField(
        db_column="ZTIMEZONEOFFSET", blank=True, null=True
    )
    ztrashedstate = models.IntegerField(
        db_column="ZTRASHEDSTATE", blank=True, null=True
    )
    zhighlight = models.IntegerField(db_column="ZHIGHLIGHT", blank=True, null=True)
    zaggregationscore = models.TextField(
        db_column="ZAGGREGATIONSCORE", blank=True, null=True
    )
    zapproximatelatitude = models.TextField(
        db_column="ZAPPROXIMATELATITUDE", blank=True, null=True
    )
    zapproximatelongitude = models.TextField(
        db_column="ZAPPROXIMATELONGITUDE", blank=True, null=True
    )
    zenddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    zgpshorizontalaccuracy = models.TextField(
        db_column="ZGPSHORIZONTALACCURACY", blank=True, null=True
    )
    zmodificationdate = models.TextField(
        db_column="ZMODIFICATIONDATE", blank=True, null=True
    )
    zrepresentativedate = models.TextField(
        db_column="ZREPRESENTATIVEDATE", blank=True, null=True
    )
    zstartdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    zsubtitle = models.CharField(db_column="ZSUBTITLE", blank=True, null=True)
    ztitle = models.CharField(db_column="ZTITLE", blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zlocalizedlocationnames = models.BinaryField(
        db_column="ZLOCALIZEDLOCATIONNAMES", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZMOMENT"


class Zperson(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zagetype = models.IntegerField(db_column="ZAGETYPE", blank=True, null=True)
    zclouddeletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zcloudverifiedtype = models.IntegerField(
        db_column="ZCLOUDVERIFIEDTYPE", blank=True, null=True
    )
    zdetectiontype = models.IntegerField(
        db_column="ZDETECTIONTYPE", blank=True, null=True
    )
    zfacecount = models.IntegerField(db_column="ZFACECOUNT", blank=True, null=True)
    zgendertype = models.IntegerField(db_column="ZGENDERTYPE", blank=True, null=True)
    zinpersonnamingmodel = models.IntegerField(
        db_column="ZINPERSONNAMINGMODEL", blank=True, null=True
    )
    zkeyfacepicksource = models.IntegerField(
        db_column="ZKEYFACEPICKSOURCE", blank=True, null=True
    )
    zmanualorder = models.IntegerField(db_column="ZMANUALORDER", blank=True, null=True)
    zquestiontype = models.IntegerField(
        db_column="ZQUESTIONTYPE", blank=True, null=True
    )
    zsuggestedforclienttype = models.IntegerField(
        db_column="ZSUGGESTEDFORCLIENTTYPE", blank=True, null=True
    )
    ztype = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    zverifiedtype = models.IntegerField(
        db_column="ZVERIFIEDTYPE", blank=True, null=True
    )
    zassociatedfacegroup = models.IntegerField(
        db_column="ZASSOCIATEDFACEGROUP", blank=True, null=True
    )
    zkeyface = models.IntegerField(db_column="ZKEYFACE", blank=True, null=True)
    zmergetargetperson = models.IntegerField(
        db_column="ZMERGETARGETPERSON", blank=True, null=True
    )
    zdisplayname = models.CharField(db_column="ZDISPLAYNAME", blank=True, null=True)
    zfullname = models.CharField(db_column="ZFULLNAME", blank=True, null=True)
    zpersonuuid = models.CharField(db_column="ZPERSONUUID", blank=True, null=True)
    zpersonuri = models.CharField(db_column="ZPERSONURI", blank=True, null=True)
    zcontactmatchingdictionary = models.BinaryField(
        db_column="ZCONTACTMATCHINGDICTIONARY", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZPERSON"


class Zpersonreference(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zassetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    zperson = models.IntegerField(db_column="ZPERSON", blank=True, null=True)
    zpersonuuid = models.CharField(db_column="ZPERSONUUID", blank=True, null=True)
    zpersondata = models.BinaryField(db_column="ZPERSONDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZPERSONREFERENCE"


class Zphotoshighlight(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zassetscount = models.IntegerField(db_column="ZASSETSCOUNT", blank=True, null=True)
    zcategory = models.IntegerField(db_column="ZCATEGORY", blank=True, null=True)
    zdaygroupassetscount = models.IntegerField(
        db_column="ZDAYGROUPASSETSCOUNT", blank=True, null=True
    )
    zdaygroupextendedassetscount = models.IntegerField(
        db_column="ZDAYGROUPEXTENDEDASSETSCOUNT", blank=True, null=True
    )
    zdaygroupsummaryassetscount = models.IntegerField(
        db_column="ZDAYGROUPSUMMARYASSETSCOUNT", blank=True, null=True
    )
    zendtimezoneoffset = models.IntegerField(
        db_column="ZENDTIMEZONEOFFSET", blank=True, null=True
    )
    zenrichmentstate = models.IntegerField(
        db_column="ZENRICHMENTSTATE", blank=True, null=True
    )
    zenrichmentversion = models.IntegerField(
        db_column="ZENRICHMENTVERSION", blank=True, null=True
    )
    zextendedcount = models.IntegerField(
        db_column="ZEXTENDEDCOUNT", blank=True, null=True
    )
    zhighlightversion = models.IntegerField(
        db_column="ZHIGHLIGHTVERSION", blank=True, null=True
    )
    zkind = models.IntegerField(db_column="ZKIND", blank=True, null=True)
    zmood = models.IntegerField(db_column="ZMOOD", blank=True, null=True)
    zstarttimezoneoffset = models.IntegerField(
        db_column="ZSTARTTIMEZONEOFFSET", blank=True, null=True
    )
    zsummarycount = models.IntegerField(
        db_column="ZSUMMARYCOUNT", blank=True, null=True
    )
    ztype = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    zvisibilitystate = models.IntegerField(
        db_column="ZVISIBILITYSTATE", blank=True, null=True
    )
    zdaygroupkeyasset = models.IntegerField(
        db_column="ZDAYGROUPKEYASSET", blank=True, null=True
    )
    zkeyasset = models.IntegerField(db_column="ZKEYASSET", blank=True, null=True)
    zmonthfirstasset = models.IntegerField(
        db_column="ZMONTHFIRSTASSET", blank=True, null=True
    )
    zmonthkeyasset = models.IntegerField(
        db_column="ZMONTHKEYASSET", blank=True, null=True
    )
    zparentdaygroupphotoshighlight = models.IntegerField(
        db_column="ZPARENTDAYGROUPPHOTOSHIGHLIGHT", blank=True, null=True
    )
    zparentphotoshighlight = models.IntegerField(
        db_column="ZPARENTPHOTOSHIGHLIGHT", blank=True, null=True
    )
    zyearkeyasset = models.IntegerField(
        db_column="ZYEARKEYASSET", blank=True, null=True
    )
    zenddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    zpromotionscore = models.TextField(
        db_column="ZPROMOTIONSCORE", blank=True, null=True
    )
    zstartdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    zsubtitle = models.CharField(db_column="ZSUBTITLE", blank=True, null=True)
    ztitle = models.CharField(db_column="ZTITLE", blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zverbosesmartdescription = models.CharField(
        db_column="ZVERBOSESMARTDESCRIPTION", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZPHOTOSHIGHLIGHT"


class Zquestion(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zdisplaytype = models.IntegerField(db_column="ZDISPLAYTYPE", blank=True, null=True)
    zentitytype = models.IntegerField(db_column="ZENTITYTYPE", blank=True, null=True)
    zstate = models.IntegerField(db_column="ZSTATE", blank=True, null=True)
    ztype = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    zcreationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    zscore = models.TextField(db_column="ZSCORE", blank=True, null=True)
    zentityidentifier = models.CharField(
        db_column="ZENTITYIDENTIFIER", blank=True, null=True
    )
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zadditionalinfo = models.BinaryField(
        db_column="ZADDITIONALINFO", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZQUESTION"


class Zsceneclassification(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zsceneidentifier = models.IntegerField(
        db_column="ZSCENEIDENTIFIER", blank=True, null=True
    )
    zassetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    zconfidence = models.TextField(db_column="ZCONFIDENCE", blank=True, null=True)
    zpackedboundingboxrect = models.IntegerField(
        db_column="ZPACKEDBOUNDINGBOXRECT", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZSCENECLASSIFICATION"


class Zsceneprint(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zadditionalassetattributes = models.IntegerField(
        db_column="ZADDITIONALASSETATTRIBUTES", blank=True, null=True
    )
    zdata = models.BinaryField(db_column="ZDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZSCENEPRINT"


class Zshare(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zclouddeletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    zlocalpublishstate = models.IntegerField(
        db_column="ZLOCALPUBLISHSTATE", blank=True, null=True
    )
    zpublicpermission = models.IntegerField(
        db_column="ZPUBLICPERMISSION", blank=True, null=True
    )
    zscopetype = models.IntegerField(db_column="ZSCOPETYPE", blank=True, null=True)
    zstatus = models.IntegerField(db_column="ZSTATUS", blank=True, null=True)
    ztrashedstate = models.IntegerField(
        db_column="ZTRASHEDSTATE", blank=True, null=True
    )
    zassetcount = models.IntegerField(db_column="ZASSETCOUNT", blank=True, null=True)
    zforcesyncattempted = models.IntegerField(
        db_column="ZFORCESYNCATTEMPTED", blank=True, null=True
    )
    zphotoscount = models.IntegerField(db_column="ZPHOTOSCOUNT", blank=True, null=True)
    zshouldignorebudgets = models.IntegerField(
        db_column="ZSHOULDIGNOREBUDGETS", blank=True, null=True
    )
    zshouldnotifyonuploadcompletion = models.IntegerField(
        db_column="ZSHOULDNOTIFYONUPLOADCOMPLETION", blank=True, null=True
    )
    zuploadedphotoscount = models.IntegerField(
        db_column="ZUPLOADEDPHOTOSCOUNT", blank=True, null=True
    )
    zuploadedvideoscount = models.IntegerField(
        db_column="ZUPLOADEDVIDEOSCOUNT", blank=True, null=True
    )
    zvideoscount = models.IntegerField(db_column="ZVIDEOSCOUNT", blank=True, null=True)
    zcreationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    zexpirydate = models.TextField(db_column="ZEXPIRYDATE", blank=True, null=True)
    zenddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    zstartdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    zscopeidentifier = models.CharField(
        db_column="ZSCOPEIDENTIFIER", blank=True, null=True
    )
    ztitle = models.CharField(db_column="ZTITLE", blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zoriginatingscopeidentifier = models.CharField(
        db_column="ZORIGINATINGSCOPEIDENTIFIER", blank=True, null=True
    )
    zshareurl = models.CharField(db_column="ZSHAREURL", blank=True, null=True)
    zpreviewdata = models.BinaryField(db_column="ZPREVIEWDATA", blank=True, null=True)
    zthumbnailimagedata = models.BinaryField(
        db_column="ZTHUMBNAILIMAGEDATA", blank=True, null=True
    )
    zcloudupdatestate = models.IntegerField(
        db_column="ZCLOUDUPDATESTATE", blank=True, null=True
    )
    zactivated = models.IntegerField(db_column="ZACTIVATED", blank=True, null=True)
    zautosharepolicy = models.IntegerField(
        db_column="ZAUTOSHAREPOLICY", blank=True, null=True
    )
    zrulesdata = models.BinaryField(db_column="ZRULESDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZSHARE"


class Zshareparticipant(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zacceptancestatus = models.IntegerField(
        db_column="ZACCEPTANCESTATUS", blank=True, null=True
    )
    zrole = models.IntegerField(db_column="ZROLE", blank=True, null=True)
    zshare = models.IntegerField(db_column="ZSHARE", blank=True, null=True)
    zemailaddress = models.CharField(db_column="ZEMAILADDRESS", blank=True, null=True)
    zphonenumber = models.CharField(db_column="ZPHONENUMBER", blank=True, null=True)
    zuseridentifier = models.CharField(
        db_column="ZUSERIDENTIFIER", blank=True, null=True
    )
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    znamecomponents = models.BinaryField(
        db_column="ZNAMECOMPONENTS", blank=True, null=True
    )
    ziscurrentuser = models.IntegerField(
        db_column="ZISCURRENTUSER", blank=True, null=True
    )
    z51_share = models.IntegerField(db_column="Z51_SHARE", blank=True, null=True)
    zpermission = models.IntegerField(db_column="ZPERMISSION", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZSHAREPARTICIPANT"


class Zsuggestion(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zcachedcount = models.IntegerField(db_column="ZCACHEDCOUNT", blank=True, null=True)
    zcachedphotoscount = models.IntegerField(
        db_column="ZCACHEDPHOTOSCOUNT", blank=True, null=True
    )
    zcachedvideoscount = models.IntegerField(
        db_column="ZCACHEDVIDEOSCOUNT", blank=True, null=True
    )
    zclouddeletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    znotificationstate = models.IntegerField(
        db_column="ZNOTIFICATIONSTATE", blank=True, null=True
    )
    zstate = models.IntegerField(db_column="ZSTATE", blank=True, null=True)
    zsubtype = models.IntegerField(db_column="ZSUBTYPE", blank=True, null=True)
    ztype = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    zversion = models.IntegerField(db_column="ZVERSION", blank=True, null=True)
    zactivationdate = models.TextField(
        db_column="ZACTIVATIONDATE", blank=True, null=True
    )
    zcreationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    zenddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    zexpungedate = models.TextField(db_column="ZEXPUNGEDATE", blank=True, null=True)
    zrelevantuntildate = models.TextField(
        db_column="ZRELEVANTUNTILDATE", blank=True, null=True
    )
    zstartdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    zsubtitle = models.CharField(db_column="ZSUBTITLE", blank=True, null=True)
    ztitle = models.CharField(db_column="ZTITLE", blank=True, null=True)
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zactiondata = models.BinaryField(db_column="ZACTIONDATA", blank=True, null=True)
    zfeaturesdata = models.BinaryField(db_column="ZFEATURESDATA", blank=True, null=True)
    zfeaturedstate = models.IntegerField(
        db_column="ZFEATUREDSTATE", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZSUGGESTION"


class Zunmanagedadjustment(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zadjustmentbaseimageformat = models.IntegerField(
        db_column="ZADJUSTMENTBASEIMAGEFORMAT", blank=True, null=True
    )
    zadjustmentrendertypes = models.IntegerField(
        db_column="ZADJUSTMENTRENDERTYPES", blank=True, null=True
    )
    zassetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    zadjustmenttimestamp = models.TextField(
        db_column="ZADJUSTMENTTIMESTAMP", blank=True, null=True
    )
    zadjustmentformatidentifier = models.CharField(
        db_column="ZADJUSTMENTFORMATIDENTIFIER", blank=True, null=True
    )
    zadjustmentformatversion = models.CharField(
        db_column="ZADJUSTMENTFORMATVERSION", blank=True, null=True
    )
    zeditorlocalizedname = models.CharField(
        db_column="ZEDITORLOCALIZEDNAME", blank=True, null=True
    )
    zotheradjustmentsfingerprint = models.CharField(
        db_column="ZOTHERADJUSTMENTSFINGERPRINT", blank=True, null=True
    )
    zsimilartooriginaladjustmentsfingerprint = models.CharField(
        db_column="ZSIMILARTOORIGINALADJUSTMENTSFINGERPRINT", blank=True, null=True
    )
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZUNMANAGEDADJUSTMENT"


class Zuserfeedback(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zfeature = models.IntegerField(db_column="ZFEATURE", blank=True, null=True)
    ztype = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    zmemory = models.IntegerField(db_column="ZMEMORY", blank=True, null=True)
    zperson = models.IntegerField(db_column="ZPERSON", blank=True, null=True)
    zlastmodifieddate = models.TextField(
        db_column="ZLASTMODIFIEDDATE", blank=True, null=True
    )
    zcontext = models.CharField(db_column="ZCONTEXT", blank=True, null=True)
    zcloudlocalstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    zuuid = models.CharField(db_column="ZUUID", blank=True, null=True)
    zclouddeletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZUSERFEEDBACK"


class Zvisualsearchattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True, blank=True, null=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    zalgorithmversion = models.IntegerField(
        db_column="ZALGORITHMVERSION", blank=True, null=True
    )
    zmediaanalysisassetattributes = models.IntegerField(
        db_column="ZMEDIAANALYSISASSETATTRIBUTES", blank=True, null=True
    )
    zadjustmentversion = models.TextField(
        db_column="ZADJUSTMENTVERSION", blank=True, null=True
    )
    zvisualsearchdata = models.BinaryField(
        db_column="ZVISUALSEARCHDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZVISUALSEARCHATTRIBUTES"


class Z17Clusterrejectedpersons(models.Model):
    z_17clusterrejectedfaces = models.AutoField(
        primary_key=True, db_column="Z_17CLUSTERREJECTEDFACES", blank=True, null=True
    )
    z_45clusterrejectedpersons = models.IntegerField(
        db_column="Z_45CLUSTERREJECTEDPERSONS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_17CLUSTERREJECTEDPERSONS"


class Z17Rejectedpersons(models.Model):
    z_17rejectedfaces = models.AutoField(
        primary_key=True, db_column="Z_17REJECTEDFACES", blank=True, null=True
    )
    z_45rejectedpersons = models.IntegerField(
        db_column="Z_45REJECTEDPERSONS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_17REJECTEDPERSONS"


class Z17Rejectedpersonsneedingfacecrops(models.Model):
    z_17rejectedfacesneedingfacecrops = models.AutoField(
        primary_key=True,
        db_column="Z_17REJECTEDFACESNEEDINGFACECROPS",
        blank=True,
        null=True,
    )
    z_45rejectedpersonsneedingfacecrops = models.IntegerField(
        db_column="Z_45REJECTEDPERSONSNEEDINGFACECROPS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_17REJECTEDPERSONSNEEDINGFACECROPS"


class Z1Keywords(models.Model):
    z_1assetattributes = models.AutoField(
        primary_key=True, db_column="Z_1ASSETATTRIBUTES", blank=True, null=True
    )
    z_38keywords = models.IntegerField(db_column="Z_38KEYWORDS", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_1KEYWORDS"


class Z26Albumlists(models.Model):
    z_26albums = models.AutoField(
        primary_key=True, db_column="Z_26ALBUMS", blank=True, null=True
    )
    z_2albumlists = models.IntegerField(
        db_column="Z_2ALBUMLISTS", blank=True, null=True
    )
    z_fok_26albums = models.IntegerField(
        db_column="Z_FOK_26ALBUMS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_26ALBUMLISTS"


class Z27Assets(models.Model):
    z_27albums = models.AutoField(
        primary_key=True, db_column="Z_27ALBUMS", blank=True, null=True
    )
    z_3assets = models.IntegerField(db_column="Z_3ASSETS", blank=True, null=True)
    z_fok_3assets = models.IntegerField(
        db_column="Z_FOK_3ASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_27ASSETS"


class Z3Memoriesbeingcuratedassets(models.Model):
    z_3curatedassets = models.AutoField(
        primary_key=True, db_column="Z_3CURATEDASSETS", blank=True, null=True
    )
    z_42memoriesbeingcuratedassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGCURATEDASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGCURATEDASSETS"


class Z3Memoriesbeingextendedcuratedassets(models.Model):
    z_3extendedcuratedassets = models.AutoField(
        primary_key=True, db_column="Z_3EXTENDEDCURATEDASSETS", blank=True, null=True
    )
    z_42memoriesbeingextendedcuratedassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGEXTENDEDCURATEDASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGEXTENDEDCURATEDASSETS"


class Z3Memoriesbeingmoviecuratedassets(models.Model):
    z_3moviecuratedassets = models.AutoField(
        primary_key=True, db_column="Z_3MOVIECURATEDASSETS", blank=True, null=True
    )
    z_42memoriesbeingmoviecuratedassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGMOVIECURATEDASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGMOVIECURATEDASSETS"


class Z3Memoriesbeingrepresentativeassets(models.Model):
    z_3representativeassets = models.AutoField(
        primary_key=True, db_column="Z_3REPRESENTATIVEASSETS", blank=True, null=True
    )
    z_42memoriesbeingrepresentativeassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGREPRESENTATIVEASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGREPRESENTATIVEASSETS"


class Z3Memoriesbeingusercuratedassets(models.Model):
    z_3usercuratedassets = models.AutoField(
        primary_key=True, db_column="Z_3USERCURATEDASSETS", blank=True, null=True
    )
    z_42memoriesbeingusercuratedassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGUSERCURATEDASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGUSERCURATEDASSETS"


class Z3Suggestionsbeingkeyassets(models.Model):
    z_3keyassets = models.AutoField(
        primary_key=True, db_column="Z_3KEYASSETS", blank=True, null=True
    )
    z_55suggestionsbeingkeyassets = models.IntegerField(
        db_column="Z_55SUGGESTIONSBEINGKEYASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3SUGGESTIONSBEINGKEYASSETS"


class Z3Suggestionsbeingrepresentativeassets(models.Model):
    z_3representativeassets1 = models.AutoField(
        primary_key=True, db_column="Z_3REPRESENTATIVEASSETS1", blank=True, null=True
    )
    z_55suggestionsbeingrepresentativeassets = models.IntegerField(
        db_column="Z_55SUGGESTIONSBEINGREPRESENTATIVEASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3SUGGESTIONSBEINGREPRESENTATIVEASSETS"


class Z45Invalidmergecandidates(models.Model):
    z_45invalidmergecandidates = models.AutoField(
        primary_key=True, db_column="Z_45INVALIDMERGECANDIDATES", blank=True, null=True
    )
    reflexive = models.IntegerField(db_column="REFLEXIVE", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_45INVALIDMERGECANDIDATES"


class Z45Mergecandidates(models.Model):
    z_45mergecandidates = models.AutoField(
        primary_key=True, db_column="Z_45MERGECANDIDATES", blank=True, null=True
    )
    reflexive = models.IntegerField(db_column="REFLEXIVE", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_45MERGECANDIDATES"


class ZMetadata(models.Model):
    z_version = models.AutoField(
        db_column="Z_VERSION", primary_key=True, blank=True, null=True
    )
    z_uuid = models.CharField(db_column="Z_UUID", blank=True, null=True)
    z_plist = models.BinaryField(db_column="Z_PLIST", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_METADATA"


class ZModelcache(models.Model):
    z_content = models.BinaryField(db_column="Z_CONTENT", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_MODELCACHE"


class ZPrimarykey(models.Model):
    z_ent = models.AutoField(db_column="Z_ENT", primary_key=True, blank=True, null=True)
    z_name = models.CharField(db_column="Z_NAME", blank=True, null=True)
    z_super = models.IntegerField(db_column="Z_SUPER", blank=True, null=True)
    z_max = models.IntegerField(db_column="Z_MAX", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_PRIMARYKEY"


class ZRtAssetBoundedbyrect(models.Model):
    z_pk = models.IntegerField(
        db_column="Z_PK", primary_key=True, blank=True, null=True
    )
    zlatitude_min = models.FloatField(db_column="ZLATITUDE_MIN", blank=True, null=True)
    zlatitude_max = models.FloatField(db_column="ZLATITUDE_MAX", blank=True, null=True)
    zlongitude_min = models.FloatField(
        db_column="ZLONGITUDE_MIN", blank=True, null=True
    )
    zlongitude_max = models.FloatField(
        db_column="ZLONGITUDE_MAX", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_RT_Asset_boundedByRect"


class ZRtAssetBoundedbyrectNode(models.Model):
    nodeno = models.AutoField(primary_key=True, blank=True, null=True)
    data = models.TextField(blank=True, null=True)  #

    class Meta:
        managed = False
        db_table = "Z_RT_Asset_boundedByRect_node"


class ZRtAssetBoundedbyrectParent(models.Model):
    nodeno = models.AutoField(primary_key=True, blank=True, null=True)
    parentnode = models.TextField(blank=True, null=True)  #

    class Meta:
        managed = False
        db_table = "Z_RT_Asset_boundedByRect_parent"


class ZRtAssetBoundedbyrectRowid(models.Model):
    rowid = models.AutoField(primary_key=True, blank=True, null=True)
    nodeno = models.TextField(blank=True, null=True)  #

    class Meta:
        managed = False
        db_table = "Z_RT_Asset_boundedByRect_rowid"
