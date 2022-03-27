# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import hashlib
import pathlib
import subprocess

from django.conf import settings
from django.db import models


class Achange(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    changetype = models.IntegerField(db_column="ZCHANGETYPE", blank=True, null=True)
    entity = models.IntegerField(db_column="ZENTITY", blank=True, null=True)
    entitypk = models.IntegerField(db_column="ZENTITYPK", blank=True, null=True)
    transactionid = models.IntegerField(
        db_column="ZTRANSACTIONID", blank=True, null=True
    )
    columns = models.BinaryField(db_column="ZCOLUMNS", blank=True, null=True)
    tombstone0 = models.BinaryField(db_column="ZTOMBSTONE0", blank=True, null=True)
    tombstone1 = models.BinaryField(db_column="ZTOMBSTONE1", blank=True, null=True)
    tombstone2 = models.BinaryField(db_column="ZTOMBSTONE2", blank=True, null=True)
    tombstone3 = models.BinaryField(db_column="ZTOMBSTONE3", blank=True, null=True)
    tombstone4 = models.BinaryField(db_column="ZTOMBSTONE4", blank=True, null=True)
    tombstone5 = models.BinaryField(db_column="ZTOMBSTONE5", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ACHANGE"


class Atransaction(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    authorts = models.IntegerField(db_column="ZAUTHORTS", blank=True, null=True)
    bundleidts = models.IntegerField(db_column="ZBUNDLEIDTS", blank=True, null=True)
    contextnamets = models.IntegerField(
        db_column="ZCONTEXTNAMETS", blank=True, null=True
    )
    processidts = models.IntegerField(db_column="ZPROCESSIDTS", blank=True, null=True)
    timestamp = models.TextField(db_column="ZTIMESTAMP", blank=True, null=True)
    author = models.CharField(
        max_length=500, db_column="ZAUTHOR", blank=True, null=True
    )
    bundleid = models.CharField(
        max_length=500, db_column="ZBUNDLEID", blank=True, null=True
    )
    contextname = models.CharField(
        max_length=500, db_column="ZCONTEXTNAME", blank=True, null=True
    )
    processid = models.CharField(
        max_length=500, db_column="ZPROCESSID", blank=True, null=True
    )
    querygen = models.BinaryField(db_column="ZQUERYGEN", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ATRANSACTION"


class Atransactionstring(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    name = models.CharField(
        max_length=500, db_column="ZNAME", unique=True, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ATRANSACTIONSTRING"


class Zadditionalassetattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    allowed_for_analysis = models.IntegerField(
        db_column="ZALLOWEDFORANALYSIS", blank=True, null=True
    )
    camera_capture_device = models.IntegerField(
        db_column="ZCAMERACAPTUREDEVICE", blank=True, null=True
    )
    cloud_avalanche_pick_type = models.IntegerField(
        db_column="ZCLOUDAVALANCHEPICKTYPE", blank=True, null=True
    )
    cloud_kind_subtype = models.IntegerField(
        db_column="ZCLOUDKINDSUBTYPE", blank=True, null=True
    )
    cloud_recovery_state = models.IntegerField(
        db_column="ZCLOUDRECOVERYSTATE", blank=True, null=True
    )
    cloud_state_recovery_attempts_count = models.IntegerField(
        db_column="ZCLOUDSTATERECOVERYATTEMPTSCOUNT", blank=True, null=True
    )
    deferred_processing_candidate_options = models.IntegerField(
        db_column="ZDEFERREDPROCESSINGCANDIDATEOPTIONS", blank=True, null=True
    )
    destination_asset_copy_state = models.IntegerField(
        db_column="ZDESTINATIONASSETCOPYSTATE", blank=True, null=True
    )
    embedded_thumbnail_height = models.IntegerField(
        db_column="ZEMBEDDEDTHUMBNAILHEIGHT", blank=True, null=True
    )
    embedded_thumbnail_length = models.IntegerField(
        db_column="ZEMBEDDEDTHUMBNAILLENGTH", blank=True, null=True
    )
    embedded_thumbnail_offset = models.IntegerField(
        db_column="ZEMBEDDEDTHUMBNAILOFFSET", blank=True, null=True
    )
    embedded_thumbnail_width = models.IntegerField(
        db_column="ZEMBEDDEDTHUMBNAILWIDTH", blank=True, null=True
    )
    imported_by = models.IntegerField(db_column="ZIMPORTEDBY", blank=True, null=True)
    inferred_timezone_offset = models.IntegerField(
        db_column="ZINFERREDTIMEZONEOFFSET", blank=True, null=True
    )
    location_hash = models.IntegerField(
        db_column="ZLOCATIONHASH", blank=True, null=True
    )
    original_filesize = models.IntegerField(
        db_column="ZORIGINALFILESIZE", blank=True, null=True
    )
    original_height = models.IntegerField(
        db_column="ZORIGINALHEIGHT", blank=True, null=True
    )
    original_orientation = models.IntegerField(
        db_column="ZORIGINALORIENTATION", blank=True, null=True
    )
    original_resource_choice = models.IntegerField(
        db_column="ZORIGINALRESOURCECHOICE", blank=True, null=True
    )
    original_width = models.IntegerField(
        db_column="ZORIGINALWIDTH", blank=True, null=True
    )
    pending_play_count = models.IntegerField(
        db_column="ZPENDINGPLAYCOUNT", blank=True, null=True
    )
    pending_share_count = models.IntegerField(
        db_column="ZPENDINGSHARECOUNT", blank=True, null=True
    )
    pending_view_count = models.IntegerField(
        db_column="ZPENDINGVIEWCOUNT", blank=True, null=True
    )
    play_count = models.IntegerField(db_column="ZPLAYCOUNT", blank=True, null=True)
    ptp_trashed_state = models.IntegerField(
        db_column="ZPTPTRASHEDSTATE", blank=True, null=True
    )
    reverse_location_data_is_valid = models.IntegerField(
        db_column="ZREVERSELOCATIONDATAISVALID", blank=True, null=True
    )
    scene_analysis_version = models.IntegerField(
        db_column="ZSCENEANALYSISVERSION", blank=True, null=True
    )
    share_count = models.IntegerField(db_column="ZSHARECOUNT", blank=True, null=True)
    share_type = models.IntegerField(db_column="ZSHARETYPE", blank=True, null=True)
    shifted_location_is_valid = models.IntegerField(
        db_column="ZSHIFTEDLOCATIONISVALID", blank=True, null=True
    )
    timezone_offset = models.IntegerField(
        db_column="ZTIMEZONEOFFSET", blank=True, null=True
    )
    upload_attempts = models.IntegerField(
        db_column="ZUPLOADATTEMPTS", blank=True, null=True
    )
    variation_suggestion_states = models.IntegerField(
        db_column="ZVARIATIONSUGGESTIONSTATES", blank=True, null=True
    )
    video_cp_display_timescale = models.IntegerField(
        db_column="ZVIDEOCPDISPLAYTIMESCALE", blank=True, null=True
    )
    video_cp_display_value = models.IntegerField(
        db_column="ZVIDEOCPDISPLAYVALUE", blank=True, null=True
    )
    video_cp_duration_timescale = models.IntegerField(
        db_column="ZVIDEOCPDURATIONTIMESCALE", blank=True, null=True
    )
    view_count = models.IntegerField(db_column="ZVIEWCOUNT", blank=True, null=True)
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    asset_description = models.IntegerField(
        db_column="ZASSETDESCRIPTION", blank=True, null=True
    )
    edited_iptc_attributes = models.IntegerField(
        db_column="ZEDITEDIPTCATTRIBUTES", blank=True, null=True
    )
    media_metadata = models.IntegerField(
        db_column="ZMEDIAMETADATA", blank=True, null=True
    )
    scene_print = models.IntegerField(db_column="ZSCENEPRINT", blank=True, null=True)
    unmanaged_adjustment = models.IntegerField(
        db_column="ZUNMANAGEDADJUSTMENT", blank=True, null=True
    )
    alternate_import_image_date = models.TextField(
        db_column="ZALTERNATEIMPORTIMAGEDATE", blank=True, null=True
    )
    gps_horizontal_accuracy = models.TextField(
        db_column="ZGPSHORIZONTALACCURACY", blank=True, null=True
    )
    last_upload_at_temptdate = models.TextField(
        db_column="ZLASTUPLOADATTEMPTDATE", blank=True, null=True
    )
    scene_analysis_timestamp = models.TextField(
        db_column="ZSCENEANALYSISTIMESTAMP", blank=True, null=True
    )
    accessibility_description = models.CharField(
        max_length=500, db_column="ZACCESSIBILITYDESCRIPTION", blank=True, null=True
    )
    adjusted_fingerprint = models.CharField(
        max_length=500, db_column="ZADJUSTEDFINGERPRINT", blank=True, null=True
    )
    imported_by_bundle_identifier = models.CharField(
        max_length=500, db_column="ZIMPORTEDBYBUNDLEIDENTIFIER", blank=True, null=True
    )
    deferred_photo_identifier = models.CharField(
        max_length=500, db_column="ZDEFERREDPHOTOIDENTIFIER", blank=True, null=True
    )
    editor_bundleid = models.CharField(
        max_length=500, db_column="ZEDITORBUNDLEID", blank=True, null=True
    )
    exif_timestamp_string = models.CharField(
        max_length=500, db_column="ZEXIFTIMESTAMPSTRING", blank=True, null=True
    )
    import_sessionid = models.CharField(
        max_length=500, db_column="ZIMPORTSESSIONID", blank=True, null=True
    )
    master_fingerprint = models.CharField(
        max_length=500, db_column="ZMASTERFINGERPRINT", blank=True, null=True
    )
    media_metadata_type = models.CharField(
        max_length=500, db_column="ZMEDIAMETADATATYPE", blank=True, null=True
    )
    montage = models.CharField(
        max_length=500, db_column="ZMONTAGE", blank=True, null=True
    )
    original_assets_uuid = models.CharField(
        max_length=500, db_column="ZORIGINALASSETSUUID", blank=True, null=True
    )
    original_filename = models.CharField(
        max_length=500, db_column="ZORIGINALFILENAME", blank=True, null=True
    )
    originating_asset_identifier = models.CharField(
        max_length=500, db_column="ZORIGINATINGASSETIDENTIFIER", blank=True, null=True
    )
    photo_stream_tagid = models.CharField(
        max_length=500, db_column="ZPHOTOSTREAMTAGID", blank=True, null=True
    )
    public_global_uuid = models.CharField(
        max_length=500, db_column="ZPUBLICGLOBALUUID", blank=True, null=True
    )
    share_originator = models.CharField(
        max_length=500, db_column="ZSHAREORIGINATOR", blank=True, null=True
    )
    snowdays_now_plow_identifier = models.CharField(
        max_length=500, db_column="ZSNOWDAYSNOWPLOWIDENTIFIER", blank=True, null=True
    )
    spatial_overcapture_group_identifier = models.CharField(
        max_length=500,
        db_column="ZSPATIALOVERCAPTUREGROUPIDENTIFIER",
        blank=True,
        null=True,
    )
    timezone_name = models.CharField(
        max_length=500, db_column="ZTIMEZONENAME", blank=True, null=True
    )
    title = models.CharField(max_length=500, db_column="ZTITLE", blank=True, null=True)
    distance_identity = models.BinaryField(
        db_column="ZDISTANCEIDENTITY", blank=True, null=True
    )
    face_regions = models.BinaryField(db_column="ZFACEREGIONS", blank=True, null=True)
    objects_aliency_rects_data = models.BinaryField(
        db_column="ZOBJECTSALIENCYRECTSDATA", blank=True, null=True
    )
    original_hash = models.BinaryField(db_column="ZORIGINALHASH", blank=True, null=True)
    place_annotation_data = models.BinaryField(
        db_column="ZPLACEANNOTATIONDATA", blank=True, null=True
    )
    reverse_location_data = models.BinaryField(
        db_column="ZREVERSELOCATIONDATA", blank=True, null=True
    )
    shifted_location_data = models.BinaryField(
        db_column="ZSHIFTEDLOCATIONDATA", blank=True, null=True
    )
    imported_by_display_name = models.CharField(
        max_length=500, db_column="ZIMPORTEDBYDISPLAYNAME", blank=True, null=True
    )
    scene_analysis_is_from_preview = models.IntegerField(
        db_column="ZSCENEANALYSISISFROMPREVIEW", blank=True, null=True
    )
    syndication_identifier = models.CharField(
        max_length=500, db_column="ZSYNDICATIONIDENTIFIER", blank=True, null=True
    )
    source_asset_for_duplication_scope_identifier = models.CharField(
        max_length=500,
        db_column="ZSOURCEASSETFORDUPLICATIONSCOPEIDENTIFIER",
        blank=True,
        null=True,
    )
    source_asset_for_duplication_identifier = models.CharField(
        max_length=500,
        db_column="ZSOURCEASSETFORDUPLICATIONIDENTIFIER",
        blank=True,
        null=True,
    )
    face_analysis_version = models.IntegerField(
        db_column="ZFACEANALYSISVERSION", blank=True, null=True
    )
    syndication_history = models.IntegerField(
        db_column="ZSYNDICATIONHISTORY", blank=True, null=True
    )
    date_created_source = models.IntegerField(
        db_column="ZDATECREATEDSOURCE", blank=True, null=True
    )
    keywords = models.ManyToManyField(to="Zkeyword", through="Z1Keywords")

    class Meta:
        managed = False
        db_table = "ZADDITIONALASSETATTRIBUTES"


class Zalbumlist(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    identifier = models.IntegerField(db_column="ZIDENTIFIER", blank=True, null=True)
    needsreorderingnumber = models.IntegerField(
        db_column="ZNEEDSREORDERINGNUMBER", blank=True, null=True
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZALBUMLIST"


class Z1Keywords(models.Model):
    z_1assetattributes = models.OneToOneField(
        to="Zadditionalassetattributes",
        db_column="Z_1ASSETATTRIBUTES",
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="+",
    )
    z_38keywords = models.ForeignKey(
        to="Zkeyword",
        db_column="Z_38KEYWORDS",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        managed = False
        db_table = "Z_1KEYWORDS"


class Zasset(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    avalanche_pick_type = models.IntegerField(
        db_column="ZAVALANCHEPICKTYPE", blank=True, null=True
    )
    bundlescope = models.IntegerField(db_column="ZBUNDLESCOPE", blank=True, null=True)
    camera_processing_adjustment_state = models.IntegerField(
        db_column="ZCAMERAPROCESSINGADJUSTMENTSTATE", blank=True, null=True
    )
    cloud_delete_state = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    cloud_download_requests = models.IntegerField(
        db_column="ZCLOUDDOWNLOADREQUESTS", blank=True, null=True
    )
    cloud_hascommentsbyme = models.IntegerField(
        db_column="ZCLOUDHASCOMMENTSBYME", blank=True, null=True
    )
    cloud_hascommentsconversation = models.IntegerField(
        db_column="ZCLOUDHASCOMMENTSCONVERSATION", blank=True, null=True
    )
    cloud_hasunseencomments = models.IntegerField(
        db_column="ZCLOUDHASUNSEENCOMMENTS", blank=True, null=True
    )
    cloud_isdeletable = models.IntegerField(
        db_column="ZCLOUDISDELETABLE", blank=True, null=True
    )
    cloud_ismyasset = models.IntegerField(
        db_column="ZCLOUDISMYASSET", blank=True, null=True
    )
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    cloud_placeholderkind = models.IntegerField(
        db_column="ZCLOUDPLACEHOLDERKIND", blank=True, null=True
    )
    complete = models.IntegerField(db_column="ZCOMPLETE", blank=True, null=True)
    deferredprocessingneeded = models.IntegerField(
        db_column="ZDEFERREDPROCESSINGNEEDED", blank=True, null=True
    )
    depthtype = models.IntegerField(db_column="ZDEPTHTYPE", blank=True, null=True)
    derivedcameracapturedevice = models.IntegerField(
        db_column="ZDERIVEDCAMERACAPTUREDEVICE", blank=True, null=True
    )
    faceareapoints = models.IntegerField(
        db_column="ZFACEAREAPOINTS", blank=True, null=True
    )
    favorite = models.IntegerField(db_column="ZFAVORITE", blank=True, null=True)
    hasadjustments = models.IntegerField(
        db_column="ZHASADJUSTMENTS", blank=True, null=True
    )
    hdrtype = models.IntegerField(db_column="ZHDRTYPE", blank=True, null=True)
    height = models.IntegerField(db_column="ZHEIGHT", blank=True, null=True)
    hidden = models.IntegerField(db_column="ZHIDDEN", blank=True, null=True)
    highframeratestate = models.IntegerField(
        db_column="ZHIGHFRAMERATESTATE", blank=True, null=True
    )
    kind = models.IntegerField(db_column="ZKIND", blank=True, null=True)
    kindsubtype = models.IntegerField(db_column="ZKINDSUBTYPE", blank=True, null=True)
    orientation = models.IntegerField(db_column="ZORIENTATION", blank=True, null=True)
    packedacceptablecroprect = models.IntegerField(
        db_column="ZPACKEDACCEPTABLECROPRECT", blank=True, null=True
    )
    packedbadgeattributes = models.IntegerField(
        db_column="ZPACKEDBADGEATTRIBUTES", blank=True, null=True
    )
    packedpreferredcroprect = models.IntegerField(
        db_column="ZPACKEDPREFERREDCROPRECT", blank=True, null=True
    )
    playbackstyle = models.IntegerField(
        db_column="ZPLAYBACKSTYLE", blank=True, null=True
    )
    playbackvariation = models.IntegerField(
        db_column="ZPLAYBACKVARIATION", blank=True, null=True
    )
    savedassettype = models.IntegerField(
        db_column="ZSAVEDASSETTYPE", blank=True, null=True
    )
    syndicationstate = models.IntegerField(
        db_column="ZSYNDICATIONSTATE", blank=True, null=True
    )
    thumbnailindex = models.IntegerField(
        db_column="ZTHUMBNAILINDEX", blank=True, null=True
    )
    trashedstate = models.IntegerField(db_column="ZTRASHEDSTATE", blank=True, null=True)
    videocpdurationvalue = models.IntegerField(
        db_column="ZVIDEOCPDURATIONVALUE", blank=True, null=True
    )
    videocpvisibilitystate = models.IntegerField(
        db_column="ZVIDEOCPVISIBILITYSTATE", blank=True, null=True
    )
    videodeferredprocessingneeded = models.IntegerField(
        db_column="ZVIDEODEFERREDPROCESSINGNEEDED", blank=True, null=True
    )
    videokeyframetimescale = models.IntegerField(
        db_column="ZVIDEOKEYFRAMETIMESCALE", blank=True, null=True
    )
    videokeyframevalue = models.IntegerField(
        db_column="ZVIDEOKEYFRAMEVALUE", blank=True, null=True
    )
    visibilitystate = models.IntegerField(
        db_column="ZVISIBILITYSTATE", blank=True, null=True
    )
    width = models.IntegerField(db_column="ZWIDTH", blank=True, null=True)
    additionalattributes = models.OneToOneField(
        to="Zadditionalassetattributes",
        db_column="ZADDITIONALATTRIBUTES",
        on_delete=models.CASCADE,
        related_name="+",
    )
    cloud_feedassetsentry = models.IntegerField(
        db_column="ZCLOUDFEEDASSETSENTRY", blank=True, null=True
    )
    computedattributes = models.OneToOneField(
        to="Zcomputedassetattributes",
        db_column="ZCOMPUTEDATTRIBUTES",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="+",
    )
    conversation = models.IntegerField(db_column="ZCONVERSATION", blank=True, null=True)
    daygrouphighlightbeingassets = models.IntegerField(
        db_column="ZDAYGROUPHIGHLIGHTBEINGASSETS", blank=True, null=True
    )
    daygrouphighlightbeingextendedassets = models.IntegerField(
        db_column="ZDAYGROUPHIGHLIGHTBEINGEXTENDEDASSETS", blank=True, null=True
    )
    daygrouphighlightbeingkeyasset = models.IntegerField(
        db_column="ZDAYGROUPHIGHLIGHTBEINGKEYASSET", blank=True, null=True
    )
    daygrouphighlightbeingsummaryassets = models.IntegerField(
        db_column="ZDAYGROUPHIGHLIGHTBEINGSUMMARYASSETS", blank=True, null=True
    )
    extendedattributes = models.OneToOneField(
        to="Zextendedattributes",
        db_column="ZEXTENDEDATTRIBUTES",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="+",
    )
    highlightbeingassets = models.IntegerField(
        db_column="ZHIGHLIGHTBEINGASSETS", blank=True, null=True
    )
    highlightbeingextendedassets = models.IntegerField(
        db_column="ZHIGHLIGHTBEINGEXTENDEDASSETS", blank=True, null=True
    )
    highlightbeingkeyasset = models.IntegerField(
        db_column="ZHIGHLIGHTBEINGKEYASSET", blank=True, null=True
    )
    highlightbeingsummaryassets = models.IntegerField(
        db_column="ZHIGHLIGHTBEINGSUMMARYASSETS", blank=True, null=True
    )
    importsession = models.IntegerField(
        db_column="ZIMPORTSESSION", blank=True, null=True
    )
    libraryscope = models.IntegerField(db_column="ZLIBRARYSCOPE", blank=True, null=True)
    libraryscopeoriginator = models.IntegerField(
        db_column="ZLIBRARYSCOPEORIGINATOR", blank=True, null=True
    )
    master = models.IntegerField(db_column="ZMASTER", blank=True, null=True)
    mediaanalysisattributes = models.IntegerField(
        db_column="ZMEDIAANALYSISATTRIBUTES", blank=True, null=True
    )
    moment = models.IntegerField(db_column="ZMOMENT", blank=True, null=True)
    momentshare = models.IntegerField(db_column="ZMOMENTSHARE", blank=True, null=True)
    monthhighlightbeingfirstasset = models.IntegerField(
        db_column="ZMONTHHIGHLIGHTBEINGFIRSTASSET", blank=True, null=True
    )
    monthhighlightbeingkeyasset = models.IntegerField(
        db_column="ZMONTHHIGHLIGHTBEINGKEYASSET", blank=True, null=True
    )
    yearhighlightbeingkeyasset = models.IntegerField(
        db_column="ZYEARHIGHLIGHTBEINGKEYASSET", blank=True, null=True
    )
    z_fok_cloudfeedassetsentry = models.IntegerField(
        db_column="Z_FOK_CLOUDFEEDASSETSENTRY", blank=True, null=True
    )
    addeddate = models.TextField(db_column="ZADDEDDATE", blank=True, null=True)
    adjustmenttimestamp = models.TextField(
        db_column="ZADJUSTMENTTIMESTAMP", blank=True, null=True
    )
    analysisstatemodificationdate = models.TextField(
        db_column="ZANALYSISSTATEMODIFICATIONDATE", blank=True, null=True
    )
    cloud_batchpublishdate = models.TextField(
        db_column="ZCLOUDBATCHPUBLISHDATE", blank=True, null=True
    )
    cloud_lastviewedcommentdate = models.TextField(
        db_column="ZCLOUDLASTVIEWEDCOMMENTDATE", blank=True, null=True
    )
    cloud_serverpublishdate = models.TextField(
        db_column="ZCLOUDSERVERPUBLISHDATE", blank=True, null=True
    )
    curationscore = models.TextField(db_column="ZCURATIONSCORE", blank=True, null=True)
    datecreated = models.TextField(db_column="ZDATECREATED", blank=True, null=True)
    duration = models.TextField(db_column="ZDURATION", blank=True, null=True)
    faceadjustmentversion = models.TextField(
        db_column="ZFACEADJUSTMENTVERSION", blank=True, null=True
    )
    hdrgain = models.TextField(db_column="ZHDRGAIN", blank=True, null=True)
    highlightvisibilityscore = models.TextField(
        db_column="ZHIGHLIGHTVISIBILITYSCORE", blank=True, null=True
    )
    lastshareddate = models.TextField(
        db_column="ZLASTSHAREDDATE", blank=True, null=True
    )
    latitude = models.TextField(db_column="ZLATITUDE", blank=True, null=True)
    longitude = models.TextField(db_column="ZLONGITUDE", blank=True, null=True)
    modificationdate = models.TextField(
        db_column="ZMODIFICATIONDATE", blank=True, null=True
    )
    overallaestheticscore = models.TextField(
        db_column="ZOVERALLAESTHETICSCORE", blank=True, null=True
    )
    promotionscore = models.TextField(
        db_column="ZPROMOTIONSCORE", blank=True, null=True
    )
    sorttoken = models.TextField(db_column="ZSORTTOKEN", blank=True, null=True)
    trasheddate = models.TextField(db_column="ZTRASHEDDATE", blank=True, null=True)
    avalancheuuid = models.CharField(
        max_length=500, db_column="ZAVALANCHEUUID", blank=True, null=True
    )
    cloud_assetguid = models.CharField(
        max_length=500, db_column="ZCLOUDASSETGUID", blank=True, null=True
    )
    cloud_batchid = models.CharField(
        max_length=500, db_column="ZCLOUDBATCHID", blank=True, null=True
    )
    cloud_collectionguid = models.CharField(
        max_length=500, db_column="ZCLOUDCOLLECTIONGUID", blank=True, null=True
    )
    cloud_ownerhashedpersonid = models.CharField(
        max_length=500, db_column="ZCLOUDOWNERHASHEDPERSONID", blank=True, null=True
    )
    directory = models.CharField(
        max_length=500, db_column="ZDIRECTORY", blank=True, null=True
    )
    filename = models.CharField(
        max_length=500, db_column="ZFILENAME", blank=True, null=True
    )
    mediagroupuuid = models.CharField(
        max_length=500, db_column="ZMEDIAGROUPUUID", blank=True, null=True
    )
    originalcolorspace = models.CharField(
        max_length=500, db_column="ZORIGINALCOLORSPACE", blank=True, null=True
    )
    uniformtypeidentifier = models.CharField(
        max_length=500, db_column="ZUNIFORMTYPEIDENTIFIER", blank=True, null=True
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    imagerequesthints = models.BinaryField(
        db_column="ZIMAGEREQUESTHINTS", blank=True, null=True
    )
    locationdata = models.BinaryField(db_column="ZLOCATIONDATA", blank=True, null=True)
    ismagiccarpet = models.IntegerField(
        db_column="ZISMAGICCARPET", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZASSET"

    def __str__(self):
        return f"{self.directory}/{self.filename}"

    @property
    def shasum(self) -> str:
        with open(self.picture_path, "rb") as fd:
            h = hashlib.sha1()
            for data in iter(lambda: fd.read(8192), b""):
                h.update(data)
        return h.hexdigest()

    @property
    def picture_path(self) -> pathlib.Path:
        return settings.LIBRARY_PATH / "originals" / self.directory / self.filename

    def open(self):
        subprocess.check_call(["open", str(self.picture_path)])


class Zassetanalysisstate(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    analysisstate = models.IntegerField(
        db_column="ZANALYSISSTATE", blank=True, null=True
    )
    workerflags = models.IntegerField(db_column="ZWORKERFLAGS", blank=True, null=True)
    workertype = models.IntegerField(db_column="ZWORKERTYPE", blank=True, null=True)
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    ignoreuntildate = models.TextField(
        db_column="ZIGNOREUNTILDATE", blank=True, null=True
    )
    lastignoreddate = models.TextField(
        db_column="ZLASTIGNOREDDATE", blank=True, null=True
    )
    sorttoken = models.TextField(db_column="ZSORTTOKEN", blank=True, null=True)
    assetuuid = models.CharField(
        max_length=500, db_column="ZASSETUUID", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZASSETANALYSISSTATE"


class Zassetdescription(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    assetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    longdescription = models.CharField(
        max_length=500, db_column="ZLONGDESCRIPTION", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZASSETDESCRIPTION"


class Zcharacterrecognitionattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    algorithmversion = models.IntegerField(
        db_column="ZALGORITHMVERSION", blank=True, null=True
    )
    mediaanalysisassetattributes = models.IntegerField(
        db_column="ZMEDIAANALYSISASSETATTRIBUTES", blank=True, null=True
    )
    adjustmentversion = models.TextField(
        db_column="ZADJUSTMENTVERSION", blank=True, null=True
    )
    characterrecognitiondata = models.BinaryField(
        db_column="ZCHARACTERRECOGNITIONDATA", blank=True, null=True
    )
    machinereadablecodedata = models.BinaryField(
        db_column="ZMACHINEREADABLECODEDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCHARACTERRECOGNITIONATTRIBUTES"


class Zcloudfeedentry(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    entryprioritynumber = models.IntegerField(
        db_column="ZENTRYPRIORITYNUMBER", blank=True, null=True
    )
    entrytypenumber = models.IntegerField(
        db_column="ZENTRYTYPENUMBER", blank=True, null=True
    )
    entrydate = models.TextField(db_column="ZENTRYDATE", blank=True, null=True)
    entryalbumguid = models.CharField(
        max_length=500, db_column="ZENTRYALBUMGUID", blank=True, null=True
    )
    entryinvitationrecordguid = models.CharField(
        max_length=500, db_column="ZENTRYINVITATIONRECORDGUID", blank=True, null=True
    )
    entrycloudassetguid = models.CharField(
        max_length=500, db_column="ZENTRYCLOUDASSETGUID", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDFEEDENTRY"


class Zcloudmaster(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    fullsizejpegsource = models.IntegerField(
        db_column="ZFULLSIZEJPEGSOURCE", blank=True, null=True
    )
    importedby = models.IntegerField(db_column="ZIMPORTEDBY", blank=True, null=True)
    originalorientation = models.IntegerField(
        db_column="ZORIGINALORIENTATION", blank=True, null=True
    )
    placeholderstate = models.IntegerField(
        db_column="ZPLACEHOLDERSTATE", blank=True, null=True
    )
    videoframerate = models.IntegerField(
        db_column="ZVIDEOFRAMERATE", blank=True, null=True
    )
    mediametadata = models.IntegerField(
        db_column="ZMEDIAMETADATA", blank=True, null=True
    )
    momentshare = models.IntegerField(db_column="ZMOMENTSHARE", blank=True, null=True)
    creationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    importdate = models.TextField(db_column="ZIMPORTDATE", blank=True, null=True)
    cloud_masterguid = models.CharField(
        max_length=500, db_column="ZCLOUDMASTERGUID", blank=True, null=True
    )
    codecname = models.CharField(
        max_length=500, db_column="ZCODECNAME", blank=True, null=True
    )
    importsessionid = models.CharField(
        max_length=500, db_column="ZIMPORTSESSIONID", blank=True, null=True
    )
    mediametadatatype = models.CharField(
        max_length=500, db_column="ZMEDIAMETADATATYPE", blank=True, null=True
    )
    originalfilename = models.CharField(
        max_length=500, db_column="ZORIGINALFILENAME", blank=True, null=True
    )
    originatingassetidentifier = models.CharField(
        max_length=500, db_column="ZORIGINATINGASSETIDENTIFIER", blank=True, null=True
    )
    uniformtypeidentifier = models.CharField(
        max_length=500, db_column="ZUNIFORMTYPEIDENTIFIER", blank=True, null=True
    )
    importedbybundleidentifier = models.CharField(
        max_length=500, db_column="ZIMPORTEDBYBUNDLEIDENTIFIER", blank=True, null=True
    )
    importedbydisplayname = models.CharField(
        max_length=500, db_column="ZIMPORTEDBYDISPLAYNAME", blank=True, null=True
    )
    sourcemasterforduplicationidentifier = models.CharField(
        max_length=500,
        db_column="ZSOURCEMASTERFORDUPLICATIONIDENTIFIER",
        blank=True,
        null=True,
    )
    sourcemasterforduplicationscopeidentifier = models.CharField(
        max_length=500,
        db_column="ZSOURCEMASTERFORDUPLICATIONSCOPEIDENTIFIER",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDMASTER"


class Zcloudmastermediametadata(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    additionalassetattributes = models.IntegerField(
        db_column="ZADDITIONALASSETATTRIBUTES", blank=True, null=True
    )
    cloud_master = models.IntegerField(db_column="ZCLOUDMASTER", blank=True, null=True)
    data = models.BinaryField(db_column="ZDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZCLOUDMASTERMEDIAMETADATA"


class Zcloudresource(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    filesize = models.IntegerField(db_column="ZFILESIZE", blank=True, null=True)
    height = models.IntegerField(db_column="ZHEIGHT", blank=True, null=True)
    isavailable = models.IntegerField(db_column="ZISAVAILABLE", blank=True, null=True)
    islocallyavailable = models.IntegerField(
        db_column="ZISLOCALLYAVAILABLE", blank=True, null=True
    )
    prefetchcount = models.IntegerField(
        db_column="ZPREFETCHCOUNT", blank=True, null=True
    )
    sourcetype = models.IntegerField(db_column="ZSOURCETYPE", blank=True, null=True)
    type = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    width = models.IntegerField(db_column="ZWIDTH", blank=True, null=True)
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    cloud_master = models.IntegerField(db_column="ZCLOUDMASTER", blank=True, null=True)
    datecreated = models.TextField(db_column="ZDATECREATED", blank=True, null=True)
    lastondemanddownloaddate = models.TextField(
        db_column="ZLASTONDEMANDDOWNLOADDATE", blank=True, null=True
    )
    lastprefetchdate = models.TextField(
        db_column="ZLASTPREFETCHDATE", blank=True, null=True
    )
    prunedat = models.TextField(db_column="ZPRUNEDAT", blank=True, null=True)
    assetuuid = models.CharField(
        max_length=500, db_column="ZASSETUUID", blank=True, null=True
    )
    filepath = models.CharField(
        max_length=500, db_column="ZFILEPATH", blank=True, null=True
    )
    fingerprint = models.CharField(
        max_length=500, db_column="ZFINGERPRINT", blank=True, null=True
    )
    itemidentifier = models.CharField(
        max_length=500, db_column="ZITEMIDENTIFIER", blank=True, null=True
    )
    uniformtypeidentifier = models.CharField(
        max_length=500, db_column="ZUNIFORMTYPEIDENTIFIER", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDRESOURCE"


class Zcloudsharedalbuminvitationrecord(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    invitationstate = models.IntegerField(
        db_column="ZINVITATIONSTATE", blank=True, null=True
    )
    invitationstatelocal = models.IntegerField(
        db_column="ZINVITATIONSTATELOCAL", blank=True, null=True
    )
    inviteeemailkey = models.IntegerField(
        db_column="ZINVITEEEMAILKEY", blank=True, null=True
    )
    ismine = models.IntegerField(db_column="ZISMINE", blank=True, null=True)
    album = models.IntegerField(db_column="ZALBUM", blank=True, null=True)
    z_fok_album = models.IntegerField(db_column="Z_FOK_ALBUM", blank=True, null=True)
    inviteesubscriptiondate = models.TextField(
        db_column="ZINVITEESUBSCRIPTIONDATE", blank=True, null=True
    )
    albumguid = models.CharField(
        max_length=500, db_column="ZALBUMGUID", blank=True, null=True
    )
    cloud_guid = models.CharField(
        max_length=500, db_column="ZCLOUDGUID", blank=True, null=True
    )
    inviteefirstname = models.CharField(
        max_length=500, db_column="ZINVITEEFIRSTNAME", blank=True, null=True
    )
    inviteefullname = models.CharField(
        max_length=500, db_column="ZINVITEEFULLNAME", blank=True, null=True
    )
    inviteehashedpersonid = models.CharField(
        max_length=500, db_column="ZINVITEEHASHEDPERSONID", blank=True, null=True
    )
    inviteelastname = models.CharField(
        max_length=500, db_column="ZINVITEELASTNAME", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDSHAREDALBUMINVITATIONRECORD"


class Zcloudsharedcomment(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    isbatchcomment = models.IntegerField(
        db_column="ZISBATCHCOMMENT", blank=True, null=True
    )
    iscaption = models.IntegerField(db_column="ZISCAPTION", blank=True, null=True)
    isdeletable = models.IntegerField(db_column="ZISDELETABLE", blank=True, null=True)
    islike = models.IntegerField(db_column="ZISLIKE", blank=True, null=True)
    ismycomment = models.IntegerField(db_column="ZISMYCOMMENT", blank=True, null=True)
    cloud_feedcommententry = models.IntegerField(
        db_column="ZCLOUDFEEDCOMMENTENTRY", blank=True, null=True
    )
    cloud_feedlikecommententry = models.IntegerField(
        db_column="ZCLOUDFEEDLIKECOMMENTENTRY", blank=True, null=True
    )
    commentedasset = models.IntegerField(
        db_column="ZCOMMENTEDASSET", blank=True, null=True
    )
    likedasset = models.IntegerField(db_column="ZLIKEDASSET", blank=True, null=True)
    z_fok_cloudfeedcommententry = models.IntegerField(
        db_column="Z_FOK_CLOUDFEEDCOMMENTENTRY", blank=True, null=True
    )
    z_fok_cloudfeedlikecommententry = models.IntegerField(
        db_column="Z_FOK_CLOUDFEEDLIKECOMMENTENTRY", blank=True, null=True
    )
    commentclientdate = models.TextField(
        db_column="ZCOMMENTCLIENTDATE", blank=True, null=True
    )
    commentdate = models.TextField(db_column="ZCOMMENTDATE", blank=True, null=True)
    cloud_guid = models.CharField(
        max_length=500, db_column="ZCLOUDGUID", blank=True, null=True
    )
    commenttext = models.CharField(
        max_length=500, db_column="ZCOMMENTTEXT", blank=True, null=True
    )
    commenttype = models.CharField(
        max_length=500, db_column="ZCOMMENTTYPE", blank=True, null=True
    )
    commenterhashedpersonid = models.CharField(
        max_length=500, db_column="ZCOMMENTERHASHEDPERSONID", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCLOUDSHAREDCOMMENT"


class Zcomputedassetattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    behavioralscore = models.TextField(
        db_column="ZBEHAVIORALSCORE", blank=True, null=True
    )
    failurescore = models.TextField(db_column="ZFAILURESCORE", blank=True, null=True)
    harmoniouscolorscore = models.TextField(
        db_column="ZHARMONIOUSCOLORSCORE", blank=True, null=True
    )
    immersivenessscore = models.TextField(
        db_column="ZIMMERSIVENESSSCORE", blank=True, null=True
    )
    interactionscore = models.TextField(
        db_column="ZINTERACTIONSCORE", blank=True, null=True
    )
    interestingsubjectscore = models.TextField(
        db_column="ZINTERESTINGSUBJECTSCORE", blank=True, null=True
    )
    intrusiveobjectpresencescore = models.TextField(
        db_column="ZINTRUSIVEOBJECTPRESENCESCORE", blank=True, null=True
    )
    livelycolorscore = models.TextField(
        db_column="ZLIVELYCOLORSCORE", blank=True, null=True
    )
    lowlight = models.TextField(db_column="ZLOWLIGHT", blank=True, null=True)
    noisescore = models.TextField(db_column="ZNOISESCORE", blank=True, null=True)
    pleasantcameratiltscore = models.TextField(
        db_column="ZPLEASANTCAMERATILTSCORE", blank=True, null=True
    )
    pleasantcompositionscore = models.TextField(
        db_column="ZPLEASANTCOMPOSITIONSCORE", blank=True, null=True
    )
    pleasantlightingscore = models.TextField(
        db_column="ZPLEASANTLIGHTINGSCORE", blank=True, null=True
    )
    pleasantpatternscore = models.TextField(
        db_column="ZPLEASANTPATTERNSCORE", blank=True, null=True
    )
    pleasantperspectivescore = models.TextField(
        db_column="ZPLEASANTPERSPECTIVESCORE", blank=True, null=True
    )
    pleasantpostprocessingscore = models.TextField(
        db_column="ZPLEASANTPOSTPROCESSINGSCORE", blank=True, null=True
    )
    pleasantreflectionsscore = models.TextField(
        db_column="ZPLEASANTREFLECTIONSSCORE", blank=True, null=True
    )
    pleasantsymmetryscore = models.TextField(
        db_column="ZPLEASANTSYMMETRYSCORE", blank=True, null=True
    )
    sharplyfocusedsubjectscore = models.TextField(
        db_column="ZSHARPLYFOCUSEDSUBJECTSCORE", blank=True, null=True
    )
    tastefullyblurredscore = models.TextField(
        db_column="ZTASTEFULLYBLURREDSCORE", blank=True, null=True
    )
    wellchosensubjectscore = models.TextField(
        db_column="ZWELLCHOSENSUBJECTSCORE", blank=True, null=True
    )
    wellframedsubjectscore = models.TextField(
        db_column="ZWELLFRAMEDSUBJECTSCORE", blank=True, null=True
    )
    welltimedshotscore = models.TextField(
        db_column="ZWELLTIMEDSHOTSCORE", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZCOMPUTEDASSETATTRIBUTES"


class Zdeferredrebuildface(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    cloud_namesource = models.IntegerField(
        db_column="ZCLOUDNAMESOURCE", blank=True, null=True
    )
    clusterrejected = models.IntegerField(
        db_column="ZCLUSTERREJECTED", blank=True, null=True
    )
    facealgorithmversion = models.IntegerField(
        db_column="ZFACEALGORITHMVERSION", blank=True, null=True
    )
    hidden = models.IntegerField(db_column="ZHIDDEN", blank=True, null=True)
    manual = models.IntegerField(db_column="ZMANUAL", blank=True, null=True)
    namesource = models.IntegerField(db_column="ZNAMESOURCE", blank=True, null=True)
    rejected = models.IntegerField(db_column="ZREJECTED", blank=True, null=True)
    representative = models.IntegerField(
        db_column="ZREPRESENTATIVE", blank=True, null=True
    )
    centerx = models.TextField(db_column="ZCENTERX", blank=True, null=True)
    centery = models.TextField(db_column="ZCENTERY", blank=True, null=True)
    size = models.TextField(db_column="ZSIZE", blank=True, null=True)
    assetcloudguid = models.CharField(
        max_length=500, db_column="ZASSETCLOUDGUID", blank=True, null=True
    )
    assetuuid = models.CharField(
        max_length=500, db_column="ZASSETUUID", blank=True, null=True
    )
    faceuuid = models.CharField(
        max_length=500, db_column="ZFACEUUID", blank=True, null=True
    )
    personuuid = models.CharField(
        max_length=500, db_column="ZPERSONUUID", blank=True, null=True
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDEFERREDREBUILDFACE"


class Zdetectedface(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    agetype = models.IntegerField(db_column="ZAGETYPE", blank=True, null=True)
    assetvisible = models.IntegerField(db_column="ZASSETVISIBLE", blank=True, null=True)
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    cloud_namesource = models.IntegerField(
        db_column="ZCLOUDNAMESOURCE", blank=True, null=True
    )
    clustersequencenumber = models.IntegerField(
        db_column="ZCLUSTERSEQUENCENUMBER", blank=True, null=True
    )
    confirmedfacecropgenerationstate = models.IntegerField(
        db_column="ZCONFIRMEDFACECROPGENERATIONSTATE", blank=True, null=True
    )
    detectiontype = models.IntegerField(
        db_column="ZDETECTIONTYPE", blank=True, null=True
    )
    ethnicitytype = models.IntegerField(
        db_column="ZETHNICITYTYPE", blank=True, null=True
    )
    eyemakeuptype = models.IntegerField(
        db_column="ZEYEMAKEUPTYPE", blank=True, null=True
    )
    eyesstate = models.IntegerField(db_column="ZEYESSTATE", blank=True, null=True)
    facealgorithmversion = models.IntegerField(
        db_column="ZFACEALGORITHMVERSION", blank=True, null=True
    )
    faceexpressiontype = models.IntegerField(
        db_column="ZFACEEXPRESSIONTYPE", blank=True, null=True
    )
    facialhairtype = models.IntegerField(
        db_column="ZFACIALHAIRTYPE", blank=True, null=True
    )
    gazetype = models.IntegerField(db_column="ZGAZETYPE", blank=True, null=True)
    gendertype = models.IntegerField(db_column="ZGENDERTYPE", blank=True, null=True)
    glassestype = models.IntegerField(db_column="ZGLASSESTYPE", blank=True, null=True)
    haircolortype = models.IntegerField(
        db_column="ZHAIRCOLORTYPE", blank=True, null=True
    )
    hairtype = models.IntegerField(db_column="ZHAIRTYPE", blank=True, null=True)
    hasfacemask = models.IntegerField(db_column="ZHASFACEMASK", blank=True, null=True)
    hassmile = models.IntegerField(db_column="ZHASSMILE", blank=True, null=True)
    headgeartype = models.IntegerField(db_column="ZHEADGEARTYPE", blank=True, null=True)
    hidden = models.IntegerField(db_column="ZHIDDEN", blank=True, null=True)
    isintrash = models.IntegerField(db_column="ZISINTRASH", blank=True, null=True)
    islefteyeclosed = models.IntegerField(
        db_column="ZISLEFTEYECLOSED", blank=True, null=True
    )
    isrighteyeclosed = models.IntegerField(
        db_column="ZISRIGHTEYECLOSED", blank=True, null=True
    )
    lipmakeuptype = models.IntegerField(
        db_column="ZLIPMAKEUPTYPE", blank=True, null=True
    )
    manual = models.IntegerField(db_column="ZMANUAL", blank=True, null=True)
    namesource = models.IntegerField(db_column="ZNAMESOURCE", blank=True, null=True)
    posetype = models.IntegerField(db_column="ZPOSETYPE", blank=True, null=True)
    qualitymeasure = models.IntegerField(
        db_column="ZQUALITYMEASURE", blank=True, null=True
    )
    skintonetype = models.IntegerField(db_column="ZSKINTONETYPE", blank=True, null=True)
    smiletype = models.IntegerField(db_column="ZSMILETYPE", blank=True, null=True)
    sourceheight = models.IntegerField(db_column="ZSOURCEHEIGHT", blank=True, null=True)
    sourcewidth = models.IntegerField(db_column="ZSOURCEWIDTH", blank=True, null=True)
    trainingtype = models.IntegerField(db_column="ZTRAININGTYPE", blank=True, null=True)
    vipmodeltype = models.IntegerField(db_column="ZVIPMODELTYPE", blank=True, null=True)
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    facecrop = models.IntegerField(db_column="ZFACECROP", blank=True, null=True)
    facegroup = models.IntegerField(db_column="ZFACEGROUP", blank=True, null=True)
    facegroupbeingkeyface = models.IntegerField(
        db_column="ZFACEGROUPBEINGKEYFACE", blank=True, null=True
    )
    faceprint = models.IntegerField(db_column="ZFACEPRINT", blank=True, null=True)
    person = models.IntegerField(db_column="ZPERSON", blank=True, null=True)
    personbeingkeyface = models.IntegerField(
        db_column="ZPERSONBEINGKEYFACE", blank=True, null=True
    )
    adjustmentversion = models.TextField(
        db_column="ZADJUSTMENTVERSION", blank=True, null=True
    )
    blurscore = models.TextField(db_column="ZBLURSCORE", blank=True, null=True)
    bodycenterx = models.TextField(db_column="ZBODYCENTERX", blank=True, null=True)
    bodycentery = models.TextField(db_column="ZBODYCENTERY", blank=True, null=True)
    bodyheight = models.TextField(db_column="ZBODYHEIGHT", blank=True, null=True)
    bodywidth = models.TextField(db_column="ZBODYWIDTH", blank=True, null=True)
    centerx = models.TextField(db_column="ZCENTERX", blank=True, null=True)
    centery = models.TextField(db_column="ZCENTERY", blank=True, null=True)
    gazecenterx = models.TextField(db_column="ZGAZECENTERX", blank=True, null=True)
    gazecentery = models.TextField(db_column="ZGAZECENTERY", blank=True, null=True)
    lefteyex = models.TextField(db_column="ZLEFTEYEX", blank=True, null=True)
    lefteyey = models.TextField(db_column="ZLEFTEYEY", blank=True, null=True)
    mouthx = models.TextField(db_column="ZMOUTHX", blank=True, null=True)
    mouthy = models.TextField(db_column="ZMOUTHY", blank=True, null=True)
    poseyaw = models.TextField(db_column="ZPOSEYAW", blank=True, null=True)
    quality = models.TextField(db_column="ZQUALITY", blank=True, null=True)
    righteyex = models.TextField(db_column="ZRIGHTEYEX", blank=True, null=True)
    righteyey = models.TextField(db_column="ZRIGHTEYEY", blank=True, null=True)
    roll = models.TextField(db_column="ZROLL", blank=True, null=True)
    size = models.TextField(db_column="ZSIZE", blank=True, null=True)
    yaw = models.TextField(db_column="ZYAW", blank=True, null=True)
    groupingidentifier = models.CharField(
        max_length=500, db_column="ZGROUPINGIDENTIFIER", blank=True, null=True
    )
    masteridentifier = models.CharField(
        max_length=500, db_column="ZMASTERIDENTIFIER", blank=True, null=True
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDETECTEDFACE"


class Zdetectedfacegroup(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    personbuilderstate = models.IntegerField(
        db_column="ZPERSONBUILDERSTATE", blank=True, null=True
    )
    unnamedfacecount = models.IntegerField(
        db_column="ZUNNAMEDFACECOUNT", blank=True, null=True
    )
    associatedperson = models.IntegerField(
        db_column="ZASSOCIATEDPERSON", blank=True, null=True
    )
    keyface = models.IntegerField(db_column="ZKEYFACE", blank=True, null=True)
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDETECTEDFACEGROUP"


class Zdetectedfaceprint(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    faceprintversion = models.IntegerField(
        db_column="ZFACEPRINTVERSION", blank=True, null=True
    )
    face = models.IntegerField(db_column="ZFACE", blank=True, null=True)
    data = models.BinaryField(db_column="ZDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDETECTEDFACEPRINT"


class Zdetectiontrait(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    type = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    value = models.IntegerField(db_column="ZVALUE", blank=True, null=True)
    detection = models.IntegerField(db_column="ZDETECTION", blank=True, null=True)
    duration = models.TextField(db_column="ZDURATION", blank=True, null=True)
    score = models.TextField(db_column="ZSCORE", blank=True, null=True)
    starttime = models.TextField(db_column="ZSTARTTIME", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZDETECTIONTRAIT"


class Zeditediptcattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    assetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    actionadvised = models.CharField(
        max_length=500, db_column="ZACTIONADVISED", blank=True, null=True
    )
    audioduration = models.CharField(
        max_length=500, db_column="ZAUDIODURATION", blank=True, null=True
    )
    audiooutcue = models.CharField(
        max_length=500, db_column="ZAUDIOOUTCUE", blank=True, null=True
    )
    audiosamplingrate = models.CharField(
        max_length=500, db_column="ZAUDIOSAMPLINGRATE", blank=True, null=True
    )
    audiosamplingres = models.CharField(
        max_length=500, db_column="ZAUDIOSAMPLINGRES", blank=True, null=True
    )
    audiotype = models.CharField(
        max_length=500, db_column="ZAUDIOTYPE", blank=True, null=True
    )
    byline = models.CharField(
        max_length=500, db_column="ZBYLINE", blank=True, null=True
    )
    bylinetitle = models.CharField(
        max_length=500, db_column="ZBYLINETITLE", blank=True, null=True
    )
    caption = models.CharField(
        max_length=500, db_column="ZCAPTION", blank=True, null=True
    )
    category = models.CharField(
        max_length=500, db_column="ZCATEGORY", blank=True, null=True
    )
    ciadrcity = models.CharField(
        max_length=500, db_column="ZCIADRCITY", blank=True, null=True
    )
    ciadrctry = models.CharField(
        max_length=500, db_column="ZCIADRCTRY", blank=True, null=True
    )
    ciadrextadr = models.CharField(
        max_length=500, db_column="ZCIADREXTADR", blank=True, null=True
    )
    ciadrpcode = models.CharField(
        max_length=500, db_column="ZCIADRPCODE", blank=True, null=True
    )
    ciadrregion = models.CharField(
        max_length=500, db_column="ZCIADRREGION", blank=True, null=True
    )
    ciemailwork = models.CharField(
        max_length=500, db_column="ZCIEMAILWORK", blank=True, null=True
    )
    citelwork = models.CharField(
        max_length=500, db_column="ZCITELWORK", blank=True, null=True
    )
    ciurlwork = models.CharField(
        max_length=500, db_column="ZCIURLWORK", blank=True, null=True
    )
    city = models.CharField(max_length=500, db_column="ZCITY", blank=True, null=True)
    contact = models.CharField(
        max_length=500, db_column="ZCONTACT", blank=True, null=True
    )
    contentlocationcode = models.CharField(
        max_length=500, db_column="ZCONTENTLOCATIONCODE", blank=True, null=True
    )
    contentlocationname = models.CharField(
        max_length=500, db_column="ZCONTENTLOCATIONNAME", blank=True, null=True
    )
    copyrightnotice = models.CharField(
        max_length=500, db_column="ZCOPYRIGHTNOTICE", blank=True, null=True
    )
    countryprimarylocationcode = models.CharField(
        max_length=500, db_column="ZCOUNTRYPRIMARYLOCATIONCODE", blank=True, null=True
    )
    countryprimarylocationname = models.CharField(
        max_length=500, db_column="ZCOUNTRYPRIMARYLOCATIONNAME", blank=True, null=True
    )
    creatorcontactinfo = models.CharField(
        max_length=500, db_column="ZCREATORCONTACTINFO", blank=True, null=True
    )
    credit = models.CharField(
        max_length=500, db_column="ZCREDIT", blank=True, null=True
    )
    datecreated = models.CharField(
        max_length=500, db_column="ZDATECREATED", blank=True, null=True
    )
    digitalcreationdate = models.CharField(
        max_length=500, db_column="ZDIGITALCREATIONDATE", blank=True, null=True
    )
    digitalcreationtime = models.CharField(
        max_length=500, db_column="ZDIGITALCREATIONTIME", blank=True, null=True
    )
    editstatus = models.CharField(
        max_length=500, db_column="ZEDITSTATUS", blank=True, null=True
    )
    editorialupdate = models.CharField(
        max_length=500, db_column="ZEDITORIALUPDATE", blank=True, null=True
    )
    expirationdate = models.CharField(
        max_length=500, db_column="ZEXPIRATIONDATE", blank=True, null=True
    )
    expirationtime = models.CharField(
        max_length=500, db_column="ZEXPIRATIONTIME", blank=True, null=True
    )
    fixtureidentifier = models.CharField(
        max_length=500, db_column="ZFIXTUREIDENTIFIER", blank=True, null=True
    )
    headline = models.CharField(
        max_length=500, db_column="ZHEADLINE", blank=True, null=True
    )
    imageorientation = models.CharField(
        max_length=500, db_column="ZIMAGEORIENTATION", blank=True, null=True
    )
    imagetype = models.CharField(
        max_length=500, db_column="ZIMAGETYPE", blank=True, null=True
    )
    keywords = models.CharField(
        max_length=500, db_column="ZKEYWORDS", blank=True, null=True
    )
    languageidentifier = models.CharField(
        max_length=500, db_column="ZLANGUAGEIDENTIFIER", blank=True, null=True
    )
    objectattributereference = models.CharField(
        max_length=500, db_column="ZOBJECTATTRIBUTEREFERENCE", blank=True, null=True
    )
    objectcycle = models.CharField(
        max_length=500, db_column="ZOBJECTCYCLE", blank=True, null=True
    )
    objectname = models.CharField(
        max_length=500, db_column="ZOBJECTNAME", blank=True, null=True
    )
    objecttypereference = models.CharField(
        max_length=500, db_column="ZOBJECTTYPEREFERENCE", blank=True, null=True
    )
    originaltransmissionreference = models.CharField(
        max_length=500,
        db_column="ZORIGINALTRANSMISSIONREFERENCE",
        blank=True,
        null=True,
    )
    originatingprogram = models.CharField(
        max_length=500, db_column="ZORIGINATINGPROGRAM", blank=True, null=True
    )
    programversion = models.CharField(
        max_length=500, db_column="ZPROGRAMVERSION", blank=True, null=True
    )
    provincestate = models.CharField(
        max_length=500, db_column="ZPROVINCESTATE", blank=True, null=True
    )
    referencedate = models.CharField(
        max_length=500, db_column="ZREFERENCEDATE", blank=True, null=True
    )
    referencenumber = models.CharField(
        max_length=500, db_column="ZREFERENCENUMBER", blank=True, null=True
    )
    referenceservice = models.CharField(
        max_length=500, db_column="ZREFERENCESERVICE", blank=True, null=True
    )
    releasedate = models.CharField(
        max_length=500, db_column="ZRELEASEDATE", blank=True, null=True
    )
    releasetime = models.CharField(
        max_length=500, db_column="ZRELEASETIME", blank=True, null=True
    )
    scene = models.CharField(max_length=500, db_column="ZSCENE", blank=True, null=True)
    source = models.CharField(
        max_length=500, db_column="ZSOURCE", blank=True, null=True
    )
    specialinstructions = models.CharField(
        max_length=500, db_column="ZSPECIALINSTRUCTIONS", blank=True, null=True
    )
    starrating = models.CharField(
        max_length=500, db_column="ZSTARRATING", blank=True, null=True
    )
    sublocation = models.CharField(
        max_length=500, db_column="ZSUBLOCATION", blank=True, null=True
    )
    subjectreference = models.CharField(
        max_length=500, db_column="ZSUBJECTREFERENCE", blank=True, null=True
    )
    supplementalcategory = models.CharField(
        max_length=500, db_column="ZSUPPLEMENTALCATEGORY", blank=True, null=True
    )
    timecreated = models.CharField(
        max_length=500, db_column="ZTIMECREATED", blank=True, null=True
    )
    urgency = models.CharField(
        max_length=500, db_column="ZURGENCY", blank=True, null=True
    )
    usageterms = models.CharField(
        max_length=500, db_column="ZUSAGETERMS", blank=True, null=True
    )
    writereditor = models.CharField(
        max_length=500, db_column="ZWRITEREDITOR", blank=True, null=True
    )
    data = models.BinaryField(db_column="ZDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZEDITEDIPTCATTRIBUTES"


class Zextendedattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    flashfired = models.IntegerField(db_column="ZFLASHFIRED", blank=True, null=True)
    iso = models.IntegerField(db_column="ZISO", blank=True, null=True)
    meteringmode = models.IntegerField(db_column="ZMETERINGMODE", blank=True, null=True)
    samplerate = models.IntegerField(db_column="ZSAMPLERATE", blank=True, null=True)
    trackformat = models.IntegerField(db_column="ZTRACKFORMAT", blank=True, null=True)
    whitebalance = models.IntegerField(db_column="ZWHITEBALANCE", blank=True, null=True)
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    aperture = models.TextField(db_column="ZAPERTURE", blank=True, null=True)
    bitrate = models.TextField(db_column="ZBITRATE", blank=True, null=True)
    duration = models.TextField(db_column="ZDURATION", blank=True, null=True)
    exposurebias = models.TextField(db_column="ZEXPOSUREBIAS", blank=True, null=True)
    focallength = models.TextField(db_column="ZFOCALLENGTH", blank=True, null=True)
    fps = models.TextField(db_column="ZFPS", blank=True, null=True)
    latitude = models.TextField(db_column="ZLATITUDE", blank=True, null=True)
    longitude = models.TextField(db_column="ZLONGITUDE", blank=True, null=True)
    shutterspeed = models.TextField(db_column="ZSHUTTERSPEED", blank=True, null=True)
    cameramake = models.CharField(
        max_length=500, db_column="ZCAMERAMAKE", blank=True, null=True
    )
    cameramodel = models.CharField(
        max_length=500, db_column="ZCAMERAMODEL", blank=True, null=True
    )
    codec = models.CharField(max_length=500, db_column="ZCODEC", blank=True, null=True)
    lensmodel = models.CharField(
        max_length=500, db_column="ZLENSMODEL", blank=True, null=True
    )
    slushwarmthbias = models.TextField(
        db_column="ZSLUSHWARMTHBIAS", blank=True, null=True
    )
    digitalzoomratio = models.TextField(
        db_column="ZDIGITALZOOMRATIO", blank=True, null=True
    )
    slushpreset = models.IntegerField(db_column="ZSLUSHPRESET", blank=True, null=True)
    slushscenebias = models.TextField(
        db_column="ZSLUSHSCENEBIAS", blank=True, null=True
    )
    slushversion = models.IntegerField(db_column="ZSLUSHVERSION", blank=True, null=True)
    focallengthin35mm = models.IntegerField(
        db_column="ZFOCALLENGTHIN35MM", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZEXTENDEDATTRIBUTES"


class Zfacecrop(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    cloud_deletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    cloud_type = models.IntegerField(db_column="ZCLOUDTYPE", blank=True, null=True)
    state = models.IntegerField(db_column="ZSTATE", blank=True, null=True)
    type = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    face = models.IntegerField(db_column="ZFACE", blank=True, null=True)
    person = models.IntegerField(db_column="ZPERSON", blank=True, null=True)
    invalidmergecandidatepersonuuid = models.CharField(
        max_length=500,
        db_column="ZINVALIDMERGECANDIDATEPERSONUUID",
        blank=True,
        null=True,
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    resourcedata = models.BinaryField(db_column="ZRESOURCEDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZFACECROP"


class Zfilesystembookmark(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    resource = models.IntegerField(db_column="ZRESOURCE", blank=True, null=True)
    pathrelativetovolume = models.CharField(
        max_length=500, db_column="ZPATHRELATIVETOVOLUME", blank=True, null=True
    )
    bookmarkdata = models.BinaryField(db_column="ZBOOKMARKDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZFILESYSTEMBOOKMARK"


class Zfilesystemvolume(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    name = models.CharField(max_length=500, db_column="ZNAME", blank=True, null=True)
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    volumeuuidstring = models.CharField(
        max_length=500, db_column="ZVOLUMEUUIDSTRING", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZFILESYSTEMVOLUME"


class Zgenericalbum(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    cachedcount = models.IntegerField(db_column="ZCACHEDCOUNT", blank=True, null=True)
    cachedphotoscount = models.IntegerField(
        db_column="ZCACHEDPHOTOSCOUNT", blank=True, null=True
    )
    cachedvideoscount = models.IntegerField(
        db_column="ZCACHEDVIDEOSCOUNT", blank=True, null=True
    )
    cloud_deletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    customsortascending = models.IntegerField(
        db_column="ZCUSTOMSORTASCENDING", blank=True, null=True
    )
    customsortkey = models.IntegerField(
        db_column="ZCUSTOMSORTKEY", blank=True, null=True
    )
    ispinned = models.IntegerField(db_column="ZISPINNED", blank=True, null=True)
    isprototype = models.IntegerField(db_column="ZISPROTOTYPE", blank=True, null=True)
    kind = models.IntegerField(db_column="ZKIND", blank=True, null=True)
    pendingitemscount = models.IntegerField(
        db_column="ZPENDINGITEMSCOUNT", blank=True, null=True
    )
    pendingitemstype = models.IntegerField(
        db_column="ZPENDINGITEMSTYPE", blank=True, null=True
    )
    synceventorderkey = models.IntegerField(
        db_column="ZSYNCEVENTORDERKEY", blank=True, null=True
    )
    trashedstate = models.IntegerField(db_column="ZTRASHEDSTATE", blank=True, null=True)
    customkeyasset = models.IntegerField(
        db_column="ZCUSTOMKEYASSET", blank=True, null=True
    )
    keyasset = models.IntegerField(db_column="ZKEYASSET", blank=True, null=True)
    parentfolder = models.IntegerField(db_column="ZPARENTFOLDER", blank=True, null=True)
    secondarykeyasset = models.IntegerField(
        db_column="ZSECONDARYKEYASSET", blank=True, null=True
    )
    tertiarykeyasset = models.IntegerField(
        db_column="ZTERTIARYKEYASSET", blank=True, null=True
    )
    cloud_albumsubtype = models.IntegerField(
        db_column="ZCLOUDALBUMSUBTYPE", blank=True, null=True
    )
    cloud_multiplecontributorsenabled = models.IntegerField(
        db_column="ZCLOUDMULTIPLECONTRIBUTORSENABLED", blank=True, null=True
    )
    cloud_multiplecontributorsenabledlocal = models.IntegerField(
        db_column="ZCLOUDMULTIPLECONTRIBUTORSENABLEDLOCAL", blank=True, null=True
    )
    cloud_notificationsenabled = models.IntegerField(
        db_column="ZCLOUDNOTIFICATIONSENABLED", blank=True, null=True
    )
    cloud_owneremailkey = models.IntegerField(
        db_column="ZCLOUDOWNEREMAILKEY", blank=True, null=True
    )
    cloud_owneriswhitelisted = models.IntegerField(
        db_column="ZCLOUDOWNERISWHITELISTED", blank=True, null=True
    )
    cloud_publicurlenabled = models.IntegerField(
        db_column="ZCLOUDPUBLICURLENABLED", blank=True, null=True
    )
    cloud_publicurlenabledlocal = models.IntegerField(
        db_column="ZCLOUDPUBLICURLENABLEDLOCAL", blank=True, null=True
    )
    cloud_relationshipstate = models.IntegerField(
        db_column="ZCLOUDRELATIONSHIPSTATE", blank=True, null=True
    )
    cloud_relationshipstatelocal = models.IntegerField(
        db_column="ZCLOUDRELATIONSHIPSTATELOCAL", blank=True, null=True
    )
    hasunseencontent = models.IntegerField(
        db_column="ZHASUNSEENCONTENT", blank=True, null=True
    )
    isowned = models.IntegerField(db_column="ZISOWNED", blank=True, null=True)
    unseenassetscount = models.IntegerField(
        db_column="ZUNSEENASSETSCOUNT", blank=True, null=True
    )
    keyassetfaceidentifier = models.IntegerField(
        db_column="ZKEYASSETFACEIDENTIFIER", blank=True, null=True
    )
    keyassetfacethumbnailindex = models.IntegerField(
        db_column="ZKEYASSETFACETHUMBNAILINDEX", blank=True, null=True
    )
    syndicate = models.IntegerField(db_column="ZSYNDICATE", blank=True, null=True)
    z_fok_parentfolder = models.IntegerField(
        db_column="Z_FOK_PARENTFOLDER", blank=True, null=True
    )
    creationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    enddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    startdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    trasheddate = models.TextField(db_column="ZTRASHEDDATE", blank=True, null=True)
    cloud_creationdate = models.TextField(
        db_column="ZCLOUDCREATIONDATE", blank=True, null=True
    )
    cloud_lastcontributiondate = models.TextField(
        db_column="ZCLOUDLASTCONTRIBUTIONDATE", blank=True, null=True
    )
    cloud_lastinterestingchangedate = models.TextField(
        db_column="ZCLOUDLASTINTERESTINGCHANGEDATE", blank=True, null=True
    )
    cloud_subscriptiondate = models.TextField(
        db_column="ZCLOUDSUBSCRIPTIONDATE", blank=True, null=True
    )
    cloud_guid = models.CharField(
        max_length=500, db_column="ZCLOUDGUID", blank=True, null=True
    )
    importsessionid = models.CharField(
        max_length=500, db_column="ZIMPORTSESSIONID", blank=True, null=True
    )
    importedbybundleidentifier = models.CharField(
        max_length=500, db_column="ZIMPORTEDBYBUNDLEIDENTIFIER", blank=True, null=True
    )
    title = models.CharField(max_length=500, db_column="ZTITLE", blank=True, null=True)
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    cloud_ownerfirstname = models.CharField(
        max_length=500, db_column="ZCLOUDOWNERFIRSTNAME", blank=True, null=True
    )
    cloud_ownerfullname = models.CharField(
        max_length=500, db_column="ZCLOUDOWNERFULLNAME", blank=True, null=True
    )
    cloud_ownerhashedpersonid = models.CharField(
        max_length=500, db_column="ZCLOUDOWNERHASHEDPERSONID", blank=True, null=True
    )
    cloud_ownerlastname = models.CharField(
        max_length=500, db_column="ZCLOUDOWNERLASTNAME", blank=True, null=True
    )
    cloud_personid = models.CharField(
        max_length=500, db_column="ZCLOUDPERSONID", blank=True, null=True
    )
    publicurl = models.CharField(
        max_length=500, db_column="ZPUBLICURL", blank=True, null=True
    )
    projectdocumenttype = models.CharField(
        max_length=500, db_column="ZPROJECTDOCUMENTTYPE", blank=True, null=True
    )
    projectextensionidentifier = models.CharField(
        max_length=500, db_column="ZPROJECTEXTENSIONIDENTIFIER", blank=True, null=True
    )
    projectrenderuuid = models.CharField(
        max_length=500, db_column="ZPROJECTRENDERUUID", blank=True, null=True
    )
    customquerytype = models.CharField(
        max_length=500, db_column="ZCUSTOMQUERYTYPE", blank=True, null=True
    )
    cloud_metadata = models.BinaryField(
        db_column="ZCLOUDMETADATA", blank=True, null=True
    )
    userquerydata = models.BinaryField(
        db_column="ZUSERQUERYDATA", blank=True, null=True
    )
    projectdata = models.BinaryField(db_column="ZPROJECTDATA", blank=True, null=True)
    customqueryparameters = models.BinaryField(
        db_column="ZCUSTOMQUERYPARAMETERS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZGENERICALBUM"


class Zglobalkeyvalue(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    boolvalue = models.IntegerField(db_column="ZBOOLVALUE", blank=True, null=True)
    integervalue = models.IntegerField(db_column="ZINTEGERVALUE", blank=True, null=True)
    type = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    datevalue = models.TextField(db_column="ZDATEVALUE", blank=True, null=True)
    doublevalue = models.TextField(db_column="ZDOUBLEVALUE", blank=True, null=True)
    key = models.CharField(
        max_length=500, db_column="ZKEY", unique=True, blank=True, null=True
    )
    stringvalue = models.CharField(
        max_length=500, db_column="ZSTRINGVALUE", blank=True, null=True
    )
    anyvalue = models.BinaryField(db_column="ZANYVALUE", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZGLOBALKEYVALUE"


class Zinternalresource(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    cloud_deletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    cloud_prefetchcount = models.IntegerField(
        db_column="ZCLOUDPREFETCHCOUNT", blank=True, null=True
    )
    cloud_sourcetype = models.IntegerField(
        db_column="ZCLOUDSOURCETYPE", blank=True, null=True
    )
    datalength = models.IntegerField(db_column="ZDATALENGTH", blank=True, null=True)
    datastoreclassid = models.IntegerField(
        db_column="ZDATASTORECLASSID", blank=True, null=True
    )
    datastoresubtype = models.IntegerField(
        db_column="ZDATASTORESUBTYPE", blank=True, null=True
    )
    fileid = models.IntegerField(db_column="ZFILEID", blank=True, null=True)
    localavailability = models.IntegerField(
        db_column="ZLOCALAVAILABILITY", blank=True, null=True
    )
    localavailabilitytarget = models.IntegerField(
        db_column="ZLOCALAVAILABILITYTARGET", blank=True, null=True
    )
    orientation = models.IntegerField(db_column="ZORIENTATION", blank=True, null=True)
    ptptrashedstate = models.IntegerField(
        db_column="ZPTPTRASHEDSTATE", blank=True, null=True
    )
    qualitysortvalue = models.IntegerField(
        db_column="ZQUALITYSORTVALUE", blank=True, null=True
    )
    recipeid = models.IntegerField(db_column="ZRECIPEID", blank=True, null=True)
    remoteavailability = models.IntegerField(
        db_column="ZREMOTEAVAILABILITY", blank=True, null=True
    )
    remoteavailabilitytarget = models.IntegerField(
        db_column="ZREMOTEAVAILABILITYTARGET", blank=True, null=True
    )
    resourcetype = models.IntegerField(db_column="ZRESOURCETYPE", blank=True, null=True)
    sidecarindex = models.IntegerField(db_column="ZSIDECARINDEX", blank=True, null=True)
    trashedstate = models.IntegerField(db_column="ZTRASHEDSTATE", blank=True, null=True)
    unorientedheight = models.IntegerField(
        db_column="ZUNORIENTEDHEIGHT", blank=True, null=True
    )
    unorientedwidth = models.IntegerField(
        db_column="ZUNORIENTEDWIDTH", blank=True, null=True
    )
    uticonformancehint = models.IntegerField(
        db_column="ZUTICONFORMANCEHINT", blank=True, null=True
    )
    version = models.IntegerField(db_column="ZVERSION", blank=True, null=True)
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    filesystembookmark = models.IntegerField(
        db_column="ZFILESYSTEMBOOKMARK", blank=True, null=True
    )
    filesystemvolume = models.IntegerField(
        db_column="ZFILESYSTEMVOLUME", blank=True, null=True
    )
    transientcloudmaster = models.IntegerField(
        db_column="ZTRANSIENTCLOUDMASTER", blank=True, null=True
    )
    cloud_lastondemanddownloaddate = models.TextField(
        db_column="ZCLOUDLASTONDEMANDDOWNLOADDATE", blank=True, null=True
    )
    cloud_lastprefetchdate = models.TextField(
        db_column="ZCLOUDLASTPREFETCHDATE", blank=True, null=True
    )
    cloud_masterdatecreated = models.TextField(
        db_column="ZCLOUDMASTERDATECREATED", blank=True, null=True
    )
    cloud_prunedat = models.TextField(db_column="ZCLOUDPRUNEDAT", blank=True, null=True)
    trasheddate = models.TextField(db_column="ZTRASHEDDATE", blank=True, null=True)
    cloud_deleteassetuuidwithresourcetype = models.CharField(
        max_length=500,
        db_column="ZCLOUDDELETEASSETUUIDWITHRESOURCETYPE",
        blank=True,
        null=True,
    )
    codecfourcharcodename = models.CharField(
        max_length=500, db_column="ZCODECFOURCHARCODENAME", blank=True, null=True
    )
    compactuti = models.CharField(
        max_length=500, db_column="ZCOMPACTUTI", blank=True, null=True
    )
    fingerprint = models.CharField(
        max_length=500, db_column="ZFINGERPRINT", blank=True, null=True
    )
    datastorekeydata = models.BinaryField(
        db_column="ZDATASTOREKEYDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZINTERNALRESOURCE"
        unique_together = (
            ("asset", "resourcetype", "version", "recipeid", "compactuti"),
        )


class Zkeyword(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    shortcut = models.CharField(
        max_length=500, db_column="ZSHORTCUT", blank=True, null=True
    )
    title = models.CharField(
        max_length=500, db_column="ZTITLE", unique=True, blank=True, null=True
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZKEYWORD"

    def __str__(self):
        return f"<{self.title}>"


class Zlegacyface(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    identifier = models.IntegerField(db_column="ZIDENTIFIER", blank=True, null=True)
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    albumuuid = models.CharField(
        max_length=500, db_column="ZALBUMUUID", blank=True, null=True
    )
    relativerectvalue = models.BinaryField(
        db_column="ZRELATIVERECTVALUE", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZLEGACYFACE"


class Zlimitedlibraryfetchfilter(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    applicationidentifier = models.CharField(
        max_length=500,
        db_column="ZAPPLICATIONIDENTIFIER",
        unique=True,
        blank=True,
        null=True,
    )
    designatedrequirement = models.CharField(
        max_length=500, db_column="ZDESIGNATEDREQUIREMENT", blank=True, null=True
    )
    fetchfilterdata = models.BinaryField(
        db_column="ZFETCHFILTERDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZLIMITEDLIBRARYFETCHFILTER"


class Zmediaanalysisassetattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    audioclassification = models.IntegerField(
        db_column="ZAUDIOCLASSIFICATION", blank=True, null=True
    )
    bestvideorangedurationtimescale = models.IntegerField(
        db_column="ZBESTVIDEORANGEDURATIONTIMESCALE", blank=True, null=True
    )
    bestvideorangedurationvalue = models.IntegerField(
        db_column="ZBESTVIDEORANGEDURATIONVALUE", blank=True, null=True
    )
    bestvideorangestarttimescale = models.IntegerField(
        db_column="ZBESTVIDEORANGESTARTTIMESCALE", blank=True, null=True
    )
    bestvideorangestartvalue = models.IntegerField(
        db_column="ZBESTVIDEORANGESTARTVALUE", blank=True, null=True
    )
    facecount = models.IntegerField(db_column="ZFACECOUNT", blank=True, null=True)
    mediaanalysisversion = models.IntegerField(
        db_column="ZMEDIAANALYSISVERSION", blank=True, null=True
    )
    packedbestplaybackrect = models.IntegerField(
        db_column="ZPACKEDBESTPLAYBACKRECT", blank=True, null=True
    )
    asset = models.OneToOneField(
        to="Zasset", db_column="ZASSET", on_delete=models.CASCADE, related_name="+"
    )
    activityscore = models.TextField(db_column="ZACTIVITYSCORE", blank=True, null=True)
    autoplaysuggestionscore = models.TextField(
        db_column="ZAUTOPLAYSUGGESTIONSCORE", blank=True, null=True
    )
    blurrinessscore = models.TextField(
        db_column="ZBLURRINESSSCORE", blank=True, null=True
    )
    exposurescore = models.TextField(db_column="ZEXPOSURESCORE", blank=True, null=True)
    mediaanalysistimestamp = models.TextField(
        db_column="ZMEDIAANALYSISTIMESTAMP", blank=True, null=True
    )
    videoscore = models.TextField(db_column="ZVIDEOSCORE", blank=True, null=True)
    colornormalizationdata = models.BinaryField(
        db_column="ZCOLORNORMALIZATIONDATA", blank=True, null=True
    )
    syndicationprocessingvalue = models.IntegerField(
        db_column="ZSYNDICATIONPROCESSINGVALUE", blank=True, null=True
    )
    probablerotationdirection = models.IntegerField(
        db_column="ZPROBABLEROTATIONDIRECTION", blank=True, null=True
    )
    characterrecognitionattributes = models.IntegerField(
        db_column="ZCHARACTERRECOGNITIONATTRIBUTES", blank=True, null=True
    )
    screentimedeviceimagesensitivity = models.IntegerField(
        db_column="ZSCREENTIMEDEVICEIMAGESENSITIVITY", blank=True, null=True
    )
    syndicationprocessingversion = models.IntegerField(
        db_column="ZSYNDICATIONPROCESSINGVERSION", blank=True, null=True
    )
    probablerotationdirectionconfidence = models.TextField(
        db_column="ZPROBABLEROTATIONDIRECTIONCONFIDENCE", blank=True, null=True
    )
    visualsearchattributes = models.IntegerField(
        db_column="ZVISUALSEARCHATTRIBUTES", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZMEDIAANALYSISASSETATTRIBUTES"


class Zmemory(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    category = models.IntegerField(db_column="ZCATEGORY", blank=True, null=True)
    cloud_deletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    favorite = models.IntegerField(db_column="ZFAVORITE", blank=True, null=True)
    featuredstate = models.IntegerField(
        db_column="ZFEATUREDSTATE", blank=True, null=True
    )
    notificationstate = models.IntegerField(
        db_column="ZNOTIFICATIONSTATE", blank=True, null=True
    )
    pendingplaycount = models.IntegerField(
        db_column="ZPENDINGPLAYCOUNT", blank=True, null=True
    )
    pendingsharecount = models.IntegerField(
        db_column="ZPENDINGSHARECOUNT", blank=True, null=True
    )
    pendingstate = models.IntegerField(db_column="ZPENDINGSTATE", blank=True, null=True)
    pendingviewcount = models.IntegerField(
        db_column="ZPENDINGVIEWCOUNT", blank=True, null=True
    )
    photosgraphversion = models.IntegerField(
        db_column="ZPHOTOSGRAPHVERSION", blank=True, null=True
    )
    playcount = models.IntegerField(db_column="ZPLAYCOUNT", blank=True, null=True)
    rejected = models.IntegerField(db_column="ZREJECTED", blank=True, null=True)
    sharecount = models.IntegerField(db_column="ZSHARECOUNT", blank=True, null=True)
    storycolorgradekind = models.IntegerField(
        db_column="ZSTORYCOLORGRADEKIND", blank=True, null=True
    )
    storyserializedtitlecategory = models.IntegerField(
        db_column="ZSTORYSERIALIZEDTITLECATEGORY", blank=True, null=True
    )
    subcategory = models.IntegerField(db_column="ZSUBCATEGORY", blank=True, null=True)
    syndicatedcontentstate = models.IntegerField(
        db_column="ZSYNDICATEDCONTENTSTATE", blank=True, null=True
    )
    useractionoptions = models.IntegerField(
        db_column="ZUSERACTIONOPTIONS", blank=True, null=True
    )
    viewcount = models.IntegerField(db_column="ZVIEWCOUNT", blank=True, null=True)
    keyasset = models.IntegerField(db_column="ZKEYASSET", blank=True, null=True)
    creationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    lastenrichmentdate = models.TextField(
        db_column="ZLASTENRICHMENTDATE", blank=True, null=True
    )
    lastmovieplayeddate = models.TextField(
        db_column="ZLASTMOVIEPLAYEDDATE", blank=True, null=True
    )
    lastvieweddate = models.TextField(
        db_column="ZLASTVIEWEDDATE", blank=True, null=True
    )
    score = models.TextField(db_column="ZSCORE", blank=True, null=True)
    graphmemoryidentifier = models.CharField(
        max_length=500, db_column="ZGRAPHMEMORYIDENTIFIER", blank=True, null=True
    )
    subtitle = models.CharField(
        max_length=500, db_column="ZSUBTITLE", blank=True, null=True
    )
    title = models.CharField(max_length=500, db_column="ZTITLE", blank=True, null=True)
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    movieassetstate = models.BinaryField(
        db_column="ZMOVIEASSETSTATE", blank=True, null=True
    )
    assetlistpredicate = models.BinaryField(
        db_column="ZASSETLISTPREDICATE", blank=True, null=True
    )
    blacklistedfeature = models.BinaryField(
        db_column="ZBLACKLISTEDFEATURE", blank=True, null=True
    )
    moviedata = models.BinaryField(db_column="ZMOVIEDATA", blank=True, null=True)
    photosgraphdata = models.BinaryField(
        db_column="ZPHOTOSGRAPHDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZMEMORY"


class Zmigrationhistory(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    forcerebuildreason = models.IntegerField(
        db_column="ZFORCEREBUILDREASON", blank=True, null=True
    )
    index = models.IntegerField(db_column="ZINDEX", unique=True, blank=True, null=True)
    migrationtype = models.IntegerField(
        db_column="ZMIGRATIONTYPE", blank=True, null=True
    )
    modelversion = models.IntegerField(db_column="ZMODELVERSION", blank=True, null=True)
    origin = models.IntegerField(db_column="ZORIGIN", blank=True, null=True)
    sourcemodelversion = models.IntegerField(
        db_column="ZSOURCEMODELVERSION", blank=True, null=True
    )
    migrationdate = models.TextField(db_column="ZMIGRATIONDATE", blank=True, null=True)
    osversion = models.CharField(
        max_length=500, db_column="ZOSVERSION", blank=True, null=True
    )
    storeuuid = models.CharField(
        max_length=500, db_column="ZSTOREUUID", blank=True, null=True
    )
    globalkeyvalues = models.BinaryField(
        db_column="ZGLOBALKEYVALUES", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZMIGRATIONHISTORY"


class Zmoment(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    cachedcount = models.IntegerField(db_column="ZCACHEDCOUNT", blank=True, null=True)
    cachedphotoscount = models.IntegerField(
        db_column="ZCACHEDPHOTOSCOUNT", blank=True, null=True
    )
    cachedvideoscount = models.IntegerField(
        db_column="ZCACHEDVIDEOSCOUNT", blank=True, null=True
    )
    originatorstate = models.IntegerField(
        db_column="ZORIGINATORSTATE", blank=True, null=True
    )
    processedlocation = models.IntegerField(
        db_column="ZPROCESSEDLOCATION", blank=True, null=True
    )
    timezoneoffset = models.IntegerField(
        db_column="ZTIMEZONEOFFSET", blank=True, null=True
    )
    trashedstate = models.IntegerField(db_column="ZTRASHEDSTATE", blank=True, null=True)
    highlight = models.IntegerField(db_column="ZHIGHLIGHT", blank=True, null=True)
    aggregationscore = models.TextField(
        db_column="ZAGGREGATIONSCORE", blank=True, null=True
    )
    approximatelatitude = models.TextField(
        db_column="ZAPPROXIMATELATITUDE", blank=True, null=True
    )
    approximatelongitude = models.TextField(
        db_column="ZAPPROXIMATELONGITUDE", blank=True, null=True
    )
    enddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    gpshorizontalaccuracy = models.TextField(
        db_column="ZGPSHORIZONTALACCURACY", blank=True, null=True
    )
    modificationdate = models.TextField(
        db_column="ZMODIFICATIONDATE", blank=True, null=True
    )
    representativedate = models.TextField(
        db_column="ZREPRESENTATIVEDATE", blank=True, null=True
    )
    startdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    subtitle = models.CharField(
        max_length=500, db_column="ZSUBTITLE", blank=True, null=True
    )
    title = models.CharField(max_length=500, db_column="ZTITLE", blank=True, null=True)
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    localizedlocationnames = models.BinaryField(
        db_column="ZLOCALIZEDLOCATIONNAMES", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZMOMENT"


class Zperson(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    agetype = models.IntegerField(db_column="ZAGETYPE", blank=True, null=True)
    cloud_deletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    cloud_verifiedtype = models.IntegerField(
        db_column="ZCLOUDVERIFIEDTYPE", blank=True, null=True
    )
    detectiontype = models.IntegerField(
        db_column="ZDETECTIONTYPE", blank=True, null=True
    )
    facecount = models.IntegerField(db_column="ZFACECOUNT", blank=True, null=True)
    gendertype = models.IntegerField(db_column="ZGENDERTYPE", blank=True, null=True)
    inpersonnamingmodel = models.IntegerField(
        db_column="ZINPERSONNAMINGMODEL", blank=True, null=True
    )
    keyfacepicksource = models.IntegerField(
        db_column="ZKEYFACEPICKSOURCE", blank=True, null=True
    )
    manualorder = models.IntegerField(db_column="ZMANUALORDER", blank=True, null=True)
    questiontype = models.IntegerField(db_column="ZQUESTIONTYPE", blank=True, null=True)
    suggestedforclienttype = models.IntegerField(
        db_column="ZSUGGESTEDFORCLIENTTYPE", blank=True, null=True
    )
    type = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    verifiedtype = models.IntegerField(db_column="ZVERIFIEDTYPE", blank=True, null=True)
    associatedfacegroup = models.IntegerField(
        db_column="ZASSOCIATEDFACEGROUP", blank=True, null=True
    )
    keyface = models.IntegerField(db_column="ZKEYFACE", blank=True, null=True)
    mergetargetperson = models.IntegerField(
        db_column="ZMERGETARGETPERSON", blank=True, null=True
    )
    displayname = models.CharField(
        max_length=500, db_column="ZDISPLAYNAME", blank=True, null=True
    )
    fullname = models.CharField(
        max_length=500, db_column="ZFULLNAME", blank=True, null=True
    )
    personuuid = models.CharField(
        max_length=500, db_column="ZPERSONUUID", blank=True, null=True
    )
    personuri = models.CharField(
        max_length=500, db_column="ZPERSONURI", blank=True, null=True
    )
    contactmatchingdictionary = models.BinaryField(
        db_column="ZCONTACTMATCHINGDICTIONARY", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZPERSON"


class Zpersonreference(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    assetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    person = models.IntegerField(db_column="ZPERSON", blank=True, null=True)
    personuuid = models.CharField(
        max_length=500, db_column="ZPERSONUUID", blank=True, null=True
    )
    persondata = models.BinaryField(db_column="ZPERSONDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZPERSONREFERENCE"


class Zphotoshighlight(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    assetscount = models.IntegerField(db_column="ZASSETSCOUNT", blank=True, null=True)
    category = models.IntegerField(db_column="ZCATEGORY", blank=True, null=True)
    daygroupassetscount = models.IntegerField(
        db_column="ZDAYGROUPASSETSCOUNT", blank=True, null=True
    )
    daygroupextendedassetscount = models.IntegerField(
        db_column="ZDAYGROUPEXTENDEDASSETSCOUNT", blank=True, null=True
    )
    daygroupsummaryassetscount = models.IntegerField(
        db_column="ZDAYGROUPSUMMARYASSETSCOUNT", blank=True, null=True
    )
    endtimezoneoffset = models.IntegerField(
        db_column="ZENDTIMEZONEOFFSET", blank=True, null=True
    )
    enrichmentstate = models.IntegerField(
        db_column="ZENRICHMENTSTATE", blank=True, null=True
    )
    enrichmentversion = models.IntegerField(
        db_column="ZENRICHMENTVERSION", blank=True, null=True
    )
    extendedcount = models.IntegerField(
        db_column="ZEXTENDEDCOUNT", blank=True, null=True
    )
    highlightversion = models.IntegerField(
        db_column="ZHIGHLIGHTVERSION", blank=True, null=True
    )
    kind = models.IntegerField(db_column="ZKIND", blank=True, null=True)
    mood = models.IntegerField(db_column="ZMOOD", blank=True, null=True)
    starttimezoneoffset = models.IntegerField(
        db_column="ZSTARTTIMEZONEOFFSET", blank=True, null=True
    )
    summarycount = models.IntegerField(db_column="ZSUMMARYCOUNT", blank=True, null=True)
    type = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    visibilitystate = models.IntegerField(
        db_column="ZVISIBILITYSTATE", blank=True, null=True
    )
    daygroupkeyasset = models.IntegerField(
        db_column="ZDAYGROUPKEYASSET", blank=True, null=True
    )
    keyasset = models.IntegerField(db_column="ZKEYASSET", blank=True, null=True)
    monthfirstasset = models.IntegerField(
        db_column="ZMONTHFIRSTASSET", blank=True, null=True
    )
    monthkeyasset = models.IntegerField(
        db_column="ZMONTHKEYASSET", blank=True, null=True
    )
    parentdaygroupphotoshighlight = models.IntegerField(
        db_column="ZPARENTDAYGROUPPHOTOSHIGHLIGHT", blank=True, null=True
    )
    parentphotoshighlight = models.IntegerField(
        db_column="ZPARENTPHOTOSHIGHLIGHT", blank=True, null=True
    )
    yearkeyasset = models.IntegerField(db_column="ZYEARKEYASSET", blank=True, null=True)
    enddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    promotionscore = models.TextField(
        db_column="ZPROMOTIONSCORE", blank=True, null=True
    )
    startdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    subtitle = models.CharField(
        max_length=500, db_column="ZSUBTITLE", blank=True, null=True
    )
    title = models.CharField(max_length=500, db_column="ZTITLE", blank=True, null=True)
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    verbosesmartdescription = models.CharField(
        max_length=500, db_column="ZVERBOSESMARTDESCRIPTION", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZPHOTOSHIGHLIGHT"


class Zquestion(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    displaytype = models.IntegerField(db_column="ZDISPLAYTYPE", blank=True, null=True)
    entitytype = models.IntegerField(db_column="ZENTITYTYPE", blank=True, null=True)
    state = models.IntegerField(db_column="ZSTATE", blank=True, null=True)
    type = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    creationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    score = models.TextField(db_column="ZSCORE", blank=True, null=True)
    entityidentifier = models.CharField(
        max_length=500, db_column="ZENTITYIDENTIFIER", blank=True, null=True
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    additionalinfo = models.BinaryField(
        db_column="ZADDITIONALINFO", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZQUESTION"


class Zsceneclassification(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    sceneidentifier = models.IntegerField(
        db_column="ZSCENEIDENTIFIER", blank=True, null=True
    )
    assetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    confidence = models.TextField(db_column="ZCONFIDENCE", blank=True, null=True)
    packedboundingboxrect = models.IntegerField(
        db_column="ZPACKEDBOUNDINGBOXRECT", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZSCENECLASSIFICATION"


class Zsceneprint(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    additionalassetattributes = models.IntegerField(
        db_column="ZADDITIONALASSETATTRIBUTES", blank=True, null=True
    )
    data = models.BinaryField(db_column="ZDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZSCENEPRINT"


class Zshare(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    cloud_deletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    localpublishstate = models.IntegerField(
        db_column="ZLOCALPUBLISHSTATE", blank=True, null=True
    )
    publicpermission = models.IntegerField(
        db_column="ZPUBLICPERMISSION", blank=True, null=True
    )
    scopetype = models.IntegerField(db_column="ZSCOPETYPE", blank=True, null=True)
    status = models.IntegerField(db_column="ZSTATUS", blank=True, null=True)
    trashedstate = models.IntegerField(db_column="ZTRASHEDSTATE", blank=True, null=True)
    assetcount = models.IntegerField(db_column="ZASSETCOUNT", blank=True, null=True)
    forcesyncattempted = models.IntegerField(
        db_column="ZFORCESYNCATTEMPTED", blank=True, null=True
    )
    photoscount = models.IntegerField(db_column="ZPHOTOSCOUNT", blank=True, null=True)
    shouldignorebudgets = models.IntegerField(
        db_column="ZSHOULDIGNOREBUDGETS", blank=True, null=True
    )
    shouldnotifyonuploadcompletion = models.IntegerField(
        db_column="ZSHOULDNOTIFYONUPLOADCOMPLETION", blank=True, null=True
    )
    uploadedphotoscount = models.IntegerField(
        db_column="ZUPLOADEDPHOTOSCOUNT", blank=True, null=True
    )
    uploadedvideoscount = models.IntegerField(
        db_column="ZUPLOADEDVIDEOSCOUNT", blank=True, null=True
    )
    videoscount = models.IntegerField(db_column="ZVIDEOSCOUNT", blank=True, null=True)
    creationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    expirydate = models.TextField(db_column="ZEXPIRYDATE", blank=True, null=True)
    enddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    startdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    scopeidentifier = models.CharField(
        max_length=500, db_column="ZSCOPEIDENTIFIER", blank=True, null=True
    )
    title = models.CharField(max_length=500, db_column="ZTITLE", blank=True, null=True)
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    originatingscopeidentifier = models.CharField(
        max_length=500, db_column="ZORIGINATINGSCOPEIDENTIFIER", blank=True, null=True
    )
    shareurl = models.CharField(
        max_length=500, db_column="ZSHAREURL", blank=True, null=True
    )
    previewdata = models.BinaryField(db_column="ZPREVIEWDATA", blank=True, null=True)
    thumbnailimagedata = models.BinaryField(
        db_column="ZTHUMBNAILIMAGEDATA", blank=True, null=True
    )
    cloud_updatestate = models.IntegerField(
        db_column="ZCLOUDUPDATESTATE", blank=True, null=True
    )
    activated = models.IntegerField(db_column="ZACTIVATED", blank=True, null=True)
    autosharepolicy = models.IntegerField(
        db_column="ZAUTOSHAREPOLICY", blank=True, null=True
    )
    rulesdata = models.BinaryField(db_column="ZRULESDATA", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZSHARE"


class Zshareparticipant(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    acceptancestatus = models.IntegerField(
        db_column="ZACCEPTANCESTATUS", blank=True, null=True
    )
    role = models.IntegerField(db_column="ZROLE", blank=True, null=True)
    share = models.IntegerField(db_column="ZSHARE", blank=True, null=True)
    emailaddress = models.CharField(
        max_length=500, db_column="ZEMAILADDRESS", blank=True, null=True
    )
    phonenumber = models.CharField(
        max_length=500, db_column="ZPHONENUMBER", blank=True, null=True
    )
    useridentifier = models.CharField(
        max_length=500, db_column="ZUSERIDENTIFIER", blank=True, null=True
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    namecomponents = models.BinaryField(
        db_column="ZNAMECOMPONENTS", blank=True, null=True
    )
    iscurrentuser = models.IntegerField(
        db_column="ZISCURRENTUSER", blank=True, null=True
    )
    z51_share = models.IntegerField(db_column="Z51_SHARE", blank=True, null=True)
    permission = models.IntegerField(db_column="ZPERMISSION", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZSHAREPARTICIPANT"


class Zsuggestion(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    cachedcount = models.IntegerField(db_column="ZCACHEDCOUNT", blank=True, null=True)
    cachedphotoscount = models.IntegerField(
        db_column="ZCACHEDPHOTOSCOUNT", blank=True, null=True
    )
    cachedvideoscount = models.IntegerField(
        db_column="ZCACHEDVIDEOSCOUNT", blank=True, null=True
    )
    cloud_deletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    notificationstate = models.IntegerField(
        db_column="ZNOTIFICATIONSTATE", blank=True, null=True
    )
    state = models.IntegerField(db_column="ZSTATE", blank=True, null=True)
    subtype = models.IntegerField(db_column="ZSUBTYPE", blank=True, null=True)
    type = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    version = models.IntegerField(db_column="ZVERSION", blank=True, null=True)
    activationdate = models.TextField(
        db_column="ZACTIVATIONDATE", blank=True, null=True
    )
    creationdate = models.TextField(db_column="ZCREATIONDATE", blank=True, null=True)
    enddate = models.TextField(db_column="ZENDDATE", blank=True, null=True)
    expungedate = models.TextField(db_column="ZEXPUNGEDATE", blank=True, null=True)
    relevantuntildate = models.TextField(
        db_column="ZRELEVANTUNTILDATE", blank=True, null=True
    )
    startdate = models.TextField(db_column="ZSTARTDATE", blank=True, null=True)
    subtitle = models.CharField(
        max_length=500, db_column="ZSUBTITLE", blank=True, null=True
    )
    title = models.CharField(max_length=500, db_column="ZTITLE", blank=True, null=True)
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    actiondata = models.BinaryField(db_column="ZACTIONDATA", blank=True, null=True)
    featuresdata = models.BinaryField(db_column="ZFEATURESDATA", blank=True, null=True)
    featuredstate = models.IntegerField(
        db_column="ZFEATUREDSTATE", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZSUGGESTION"


class Zunmanagedadjustment(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    adjustmentbaseimageformat = models.IntegerField(
        db_column="ZADJUSTMENTBASEIMAGEFORMAT", blank=True, null=True
    )
    adjustmentrendertypes = models.IntegerField(
        db_column="ZADJUSTMENTRENDERTYPES", blank=True, null=True
    )
    assetattributes = models.IntegerField(
        db_column="ZASSETATTRIBUTES", blank=True, null=True
    )
    adjustmenttimestamp = models.TextField(
        db_column="ZADJUSTMENTTIMESTAMP", blank=True, null=True
    )
    adjustmentformatidentifier = models.CharField(
        max_length=500, db_column="ZADJUSTMENTFORMATIDENTIFIER", blank=True, null=True
    )
    adjustmentformatversion = models.CharField(
        max_length=500, db_column="ZADJUSTMENTFORMATVERSION", blank=True, null=True
    )
    editorlocalizedname = models.CharField(
        max_length=500, db_column="ZEDITORLOCALIZEDNAME", blank=True, null=True
    )
    otheradjustmentsfingerprint = models.CharField(
        max_length=500, db_column="ZOTHERADJUSTMENTSFINGERPRINT", blank=True, null=True
    )
    similartooriginaladjustmentsfingerprint = models.CharField(
        max_length=500,
        db_column="ZSIMILARTOORIGINALADJUSTMENTSFINGERPRINT",
        blank=True,
        null=True,
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ZUNMANAGEDADJUSTMENT"


class Zuserfeedback(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    feature = models.IntegerField(db_column="ZFEATURE", blank=True, null=True)
    type = models.IntegerField(db_column="ZTYPE", blank=True, null=True)
    memory = models.IntegerField(db_column="ZMEMORY", blank=True, null=True)
    person = models.IntegerField(db_column="ZPERSON", blank=True, null=True)
    lastmodifieddate = models.TextField(
        db_column="ZLASTMODIFIEDDATE", blank=True, null=True
    )
    context = models.CharField(
        max_length=500, db_column="ZCONTEXT", blank=True, null=True
    )
    cloud_localstate = models.IntegerField(
        db_column="ZCLOUDLOCALSTATE", blank=True, null=True
    )
    uuid = models.CharField(max_length=500, db_column="ZUUID", blank=True, null=True)
    cloud_deletestate = models.IntegerField(
        db_column="ZCLOUDDELETESTATE", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZUSERFEEDBACK"


class Zvisualsearchattributes(models.Model):
    z_pk = models.AutoField(db_column="Z_PK", primary_key=True)
    z_ent = models.IntegerField(db_column="Z_ENT", blank=True, null=True)
    z_opt = models.IntegerField(db_column="Z_OPT", blank=True, null=True)
    algorithmversion = models.IntegerField(
        db_column="ZALGORITHMVERSION", blank=True, null=True
    )
    mediaanalysisassetattributes = models.IntegerField(
        db_column="ZMEDIAANALYSISASSETATTRIBUTES", blank=True, null=True
    )
    adjustmentversion = models.TextField(
        db_column="ZADJUSTMENTVERSION", blank=True, null=True
    )
    visualsearchdata = models.BinaryField(
        db_column="ZVISUALSEARCHDATA", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "ZVISUALSEARCHATTRIBUTES"


class Z17Clusterrejectedpersons(models.Model):
    z_17clusterrejectedfaces = models.AutoField(
        primary_key=True, db_column="Z_17CLUSTERREJECTEDFACES"
    )
    z_45clusterrejectedpersons = models.IntegerField(
        db_column="Z_45CLUSTERREJECTEDPERSONS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_17CLUSTERREJECTEDPERSONS"


class Z17Rejectedpersons(models.Model):
    z_17rejectedfaces = models.AutoField(
        primary_key=True, db_column="Z_17REJECTEDFACES"
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
    )
    z_45rejectedpersonsneedingfacecrops = models.IntegerField(
        db_column="Z_45REJECTEDPERSONSNEEDINGFACECROPS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_17REJECTEDPERSONSNEEDINGFACECROPS"


class Z26Albumlists(models.Model):
    z_26albums = models.AutoField(primary_key=True, db_column="Z_26ALBUMS")
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
    z_27albums = models.AutoField(primary_key=True, db_column="Z_27ALBUMS")
    z_3assets = models.IntegerField(db_column="Z_3ASSETS", blank=True, null=True)
    z_fok_3assets = models.IntegerField(
        db_column="Z_FOK_3ASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_27ASSETS"


class Z3Memoriesbeingcuratedassets(models.Model):
    z_3curatedassets = models.AutoField(primary_key=True, db_column="Z_3CURATEDASSETS")
    z_42memoriesbeingcuratedassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGCURATEDASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGCURATEDASSETS"


class Z3Memoriesbeingextendedcuratedassets(models.Model):
    z_3extendedcuratedassets = models.AutoField(
        primary_key=True, db_column="Z_3EXTENDEDCURATEDASSETS"
    )
    z_42memoriesbeingextendedcuratedassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGEXTENDEDCURATEDASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGEXTENDEDCURATEDASSETS"


class Z3Memoriesbeingmoviecuratedassets(models.Model):
    z_3moviecuratedassets = models.AutoField(
        primary_key=True, db_column="Z_3MOVIECURATEDASSETS"
    )
    z_42memoriesbeingmoviecuratedassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGMOVIECURATEDASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGMOVIECURATEDASSETS"


class Z3Memoriesbeingrepresentativeassets(models.Model):
    z_3representativeassets = models.AutoField(
        primary_key=True, db_column="Z_3REPRESENTATIVEASSETS"
    )
    z_42memoriesbeingrepresentativeassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGREPRESENTATIVEASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGREPRESENTATIVEASSETS"


class Z3Memoriesbeingusercuratedassets(models.Model):
    z_3usercuratedassets = models.AutoField(
        primary_key=True, db_column="Z_3USERCURATEDASSETS"
    )
    z_42memoriesbeingusercuratedassets = models.IntegerField(
        db_column="Z_42MEMORIESBEINGUSERCURATEDASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3MEMORIESBEINGUSERCURATEDASSETS"


class Z3Suggestionsbeingkeyassets(models.Model):
    z_3keyassets = models.AutoField(primary_key=True, db_column="Z_3KEYASSETS")
    z_55suggestionsbeingkeyassets = models.IntegerField(
        db_column="Z_55SUGGESTIONSBEINGKEYASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3SUGGESTIONSBEINGKEYASSETS"


class Z3Suggestionsbeingrepresentativeassets(models.Model):
    z_3representativeassets1 = models.AutoField(
        primary_key=True, db_column="Z_3REPRESENTATIVEASSETS1"
    )
    z_55suggestionsbeingrepresentativeassets = models.IntegerField(
        db_column="Z_55SUGGESTIONSBEINGREPRESENTATIVEASSETS", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Z_3SUGGESTIONSBEINGREPRESENTATIVEASSETS"


class Z45Invalidmergecandidates(models.Model):
    z_45invalidmergecandidates = models.AutoField(
        primary_key=True, db_column="Z_45INVALIDMERGECANDIDATES"
    )
    reflexive = models.IntegerField(db_column="REFLEXIVE", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_45INVALIDMERGECANDIDATES"


class Z45Mergecandidates(models.Model):
    z_45mergecandidates = models.AutoField(
        primary_key=True, db_column="Z_45MERGECANDIDATES"
    )
    reflexive = models.IntegerField(db_column="REFLEXIVE", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_45MERGECANDIDATES"


class ZMetadata(models.Model):
    z_version = models.AutoField(db_column="Z_VERSION", primary_key=True)
    z_uuid = models.CharField(max_length=500, db_column="Z_UUID", blank=True, null=True)
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
    z_ent = models.AutoField(db_column="Z_ENT", primary_key=True)
    z_name = models.CharField(max_length=500, db_column="Z_NAME", blank=True, null=True)
    z_super = models.IntegerField(db_column="Z_SUPER", blank=True, null=True)
    z_max = models.IntegerField(db_column="Z_MAX", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_PRIMARYKEY"


class ZRtAssetBoundedbyrect(models.Model):
    z_pk = models.IntegerField(db_column="Z_PK", primary_key=True)
    latitude_min = models.FloatField(db_column="ZLATITUDE_MIN", blank=True, null=True)
    latitude_max = models.FloatField(db_column="ZLATITUDE_MAX", blank=True, null=True)
    longitude_min = models.FloatField(db_column="ZLONGITUDE_MIN", blank=True, null=True)
    longitude_max = models.FloatField(db_column="ZLONGITUDE_MAX", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Z_RT_Asset_boundedByRect"


class ZRtAssetBoundedbyrectNode(models.Model):
    nodeno = models.AutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)  #

    class Meta:
        managed = False
        db_table = "Z_RT_Asset_boundedByRect_node"


class ZRtAssetBoundedbyrectParent(models.Model):
    nodeno = models.AutoField(primary_key=True)
    parentnode = models.TextField(blank=True, null=True)  #

    class Meta:
        managed = False
        db_table = "Z_RT_Asset_boundedByRect_parent"


class ZRtAssetBoundedbyrectRowid(models.Model):
    rowid = models.AutoField(primary_key=True)
    nodeno = models.TextField(blank=True, null=True)  #

    class Meta:
        managed = False
        db_table = "Z_RT_Asset_boundedByRect_rowid"
