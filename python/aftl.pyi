from __future__ import annotations

import datetime as _dt
import enum
from typing import ClassVar, Protocol, Sequence, overload


class _ReadableStream(Protocol):
    def read(self, size: int) -> bytes: ...


class _WritableStream(Protocol):
    def write(self, data: bytes) -> int: ...


class ObjectFormat(enum.IntEnum):
    Any = 0x0000
    Undefined = 0x3000
    Association = 0x3001
    Script = 0x3002
    Executable = 0x3003
    Text = 0x3004
    Html = 0x3005
    Dpof = 0x3006
    Aiff = 0x3007
    Wav = 0x3008
    Mp3 = 0x3009
    Avi = 0x300A
    Mpeg = 0x300B
    Asf = 0x300C
    UndefinedImage = 0x3800
    ExifJpeg = 0x3801
    TiffEp = 0x3802
    Flashpix = 0x3803
    Bmp = 0x3804
    Ciff = 0x3805
    Gif = 0x3807
    Jfif = 0x3808
    Pcd = 0x3809
    Pict = 0x380A
    Png = 0x380B
    Tiff = 0x380D
    TiffIt = 0x380E
    Jp2 = 0x380F
    Jpx = 0x3810
    Dng = 0x3811
    Heif = 0x3812
    NetworkAssociation = 0xB102
    M4a = 0xB215
    Artist = 0xB218
    UndefinedFirmware = 0xB802
    WindowsImageFormat = 0xB881
    UndefinedAudio = 0xB900
    Wma = 0xB901
    Ogg = 0xB902
    Aac = 0xB903
    Audible = 0xB904
    Flac = 0xB906
    UndefinedVideo = 0xB980
    Wmv = 0xB981
    Mp4 = 0xB982
    Mp2 = 0xB983
    _3gp = 0xB984
    UndefinedCollection = 0xBA00
    AbstractMultimediaAlbum = 0xBA01
    AbstractImageAlbum = 0xBA02
    AbstractAudioAlbum = 0xBA03
    AbstractVideoAlbum = 0xBA04
    AbstractAVPlaylist = 0xBA05
    AbstractContactGroup = 0xBA06
    AbstractMessageFolder = 0xBA07
    AbstractChapteredProduction = 0xBA08
    AbstractAudioPlaylist = 0xBA09
    AbstractVideoPlaylist = 0xBA0A
    AbstractMediacast = 0xBA0B
    WplPlaylist = 0xBA10
    M3uPlaylist = 0xBA11
    MplPlaylist = 0xBA12
    AsxPlaylist = 0xBA13
    PlsPlaylist = 0xBA14
    UndefinedDocument = 0xBA80
    AbstractDocument = 0xBA81
    XmlDocument = 0xBA82
    MicrosoftWordDocument = 0xBA83
    MhtCompiledHtmlDocument = 0xBA84
    MicrosoftExcelSpreadsheet = 0xBA85
    MicrosoftPowerPointPresentation = 0xBA86
    UndefinedMessage = 0xBB00
    AbstractMessage = 0xBB01
    UndefinedContact = 0xBB80
    AbstractContact = 0xBB81
    VCard2 = 0xBB82
    VCard3 = 0xBB83
    UndefinedCalendarItem = 0xBE00
    AbstractCalendarItem = 0xBE01
    VCalendar1 = 0xBE02
    VCalendar2 = 0xBE03
    UndefinedWindowsExecutable = 0xBE80


class ObjectProperty(enum.IntEnum):
    BuyFlag = 0xD901
    HostEUI64Array = 0xD920
    ContentTypeUUID = 0xDA97
    ArtistId = 0xDAB9
    AlbumId = 0xDABB
    StorageId = 0xDC01
    ObjectFormat = 0xDC02
    ProtectionStatus = 0xDC03
    ObjectSize = 0xDC04
    AssociationType = 0xDC05
    AssociationDesc = 0xDC06
    ObjectFilename = 0xDC07
    DateCreated = 0xDC08
    DateModified = 0xDC09
    Keywords = 0xDC0A
    ParentObject = 0xDC0B
    AllowedFolderContents = 0xDC0C
    Hidden = 0xDC0D
    SystemObject = 0xDC0E
    PersistentUniqueObjectId = 0xDC41
    SyncId = 0xDC42
    PropertyBag = 0xDC43
    Name = 0xDC44
    CreatedBy = 0xDC45
    Artist = 0xDC46
    DateAuthored = 0xDC47
    Description = 0xDC48
    UrlReference = 0xDC49
    LanguageLocale = 0xDC4A
    CopyrightInformation = 0xDC4B
    Source = 0xDC4C
    OriginLocation = 0xDC4D
    DateAdded = 0xDC4E
    NonConsumable = 0xDC4F
    CorruptedNonPlayable = 0xDC50
    ProducerSerialNumber = 0xDC51
    RepresentativeSampleFormat = 0xDC81
    RepresentativeSampleSize = 0xDC82
    RepresentativeSampleHeight = 0xDC83
    RepresentativeSampleWidth = 0xDC84
    RepresentativeSampleDuration = 0xDC85
    RepresentativeSampleData = 0xDC86
    Width = 0xDC87
    Height = 0xDC88
    Duration = 0xDC89
    UserRating = 0xDC8A
    Track = 0xDC8B
    Genre = 0xDC8C
    Credits = 0xDC8D
    Lyrics = 0xDC8E
    SubscriptionContentId = 0xDC8F
    ProducedBy = 0xDC90
    UseCount = 0xDC91
    SkipCount = 0xDC92
    LastAccessed = 0xDC93
    ParentalRating = 0xDC94
    MetaGenre = 0xDC95
    Composer = 0xDC96
    EffectiveRating = 0xDC97
    Subtitle = 0xDC98
    OriginalReleaseDate = 0xDC99
    AlbumName = 0xDC9A
    AlbumArtist = 0xDC9B
    Mood = 0xDC9C
    DrmProtectionStatus = 0xDC9D
    Subdescription = 0xDC9E
    IsCropped = 0xDCD1
    IsColourCorrected = 0xDCD2
    ImageBitDepth = 0xDCD3
    FNumber = 0xDCD4
    ExposureTime = 0xDCD5
    ExposureIndex = 0xDCD6
    TotalBitrate = 0xDE91
    BitrateType = 0xDE92
    SampleRate = 0xDE93
    NumberOfChannels = 0xDE94
    AudioBitDepth = 0xDE95
    BlockAlignment = 0xDE96
    ScanType = 0xDE97
    ColourRange = 0xDE98
    AudioWaveCodec = 0xDE99
    AudioBitrate = 0xDE9A
    VideoFourCCCodec = 0xDE9B
    VideoBitrate = 0xDE9C
    FramesPerMilliseconds = 0xDE9D
    KeyframeDistance = 0xDE9E
    BufferSize = 0xDE9F
    EncodingQuality = 0xDEA0
    EncodingProfile = 0xDEA1
    DisplayName = 0xDCE0
    BodyText = 0xDCE1
    Subject = 0xDCE2
    Priority = 0xDCE3
    Owner = 0xDD5D
    Editor = 0xDD5E
    WebMaster = 0xDD5F
    UrlSource = 0xDD60
    UrlDestination = 0xDD61
    TimeBookmark = 0xDD62
    ObjectBookmark = 0xDD63
    ByteBookmark = 0xDD64
    LastBuildDate = 0xDD70
    TimeToLive = 0xDD71
    MediaGUID = 0xDD72
    All = 0xFFFF


class DeviceProperty(enum.IntEnum):
    Undefined = 0x5000
    BatteryLevel = 0x5001
    FunctionalMode = 0x5002
    ImageSize = 0x5003
    CompressionSetting = 0x5004
    WhiteBalance = 0x5005
    RgbGain = 0x5006
    FNumber = 0x5007
    FocalLength = 0x5008
    FocusDistance = 0x5009
    FocusMode = 0x500A
    ExposureMeteringMode = 0x500B
    FlashMode = 0x500C
    ExposureTime = 0x500D
    ExposureProgramMode = 0x500E
    ExposureIndex = 0x500F
    ExposureBiasCompensation = 0x5010
    Datetime = 0x5011
    CaptureDelay = 0x5012
    StillCaptureMode = 0x5013
    Contrast = 0x5014
    Sharpness = 0x5015
    DigitalZoom = 0x5016
    EffectMode = 0x5017
    BurstNumber = 0x5018
    BurstInterval = 0x5019
    TimelapseNumber = 0x501A
    TimelapseInterval = 0x501B
    FocusMeteringMode = 0x501C
    UploadUrl = 0x501D
    Artist = 0x501E
    CopyrightInfo = 0x501F
    SecureTime = 0xD101
    DeviceCertificate = 0xD102
    RevocationInfo = 0xD103
    PlaysForSureID = 0xD131
    DeviceEUI64 = 0xD210
    FirmwareVersion = 0xD233
    SerialNumber = 0xD235
    FunctionalID = 0xD301
    ModelID = 0xD302
    UseDeviceStage = 0xD303
    SynchronizationPartner = 0xD401
    DeviceFriendlyName = 0xD402
    Volume = 0xD403
    SupportedFormatsOrdered = 0xD404
    DeviceIcon = 0xD405
    SessionInitiatorVersionInfo = 0xD406
    PerceivedDeviceType = 0xD407
    PlaybackRate = 0xD410
    PlaybackObject = 0xD411
    PlaybackContainerIndex = 0xD412
    PlaybackPosition = 0xD413


class AssociationType(enum.IntEnum):
    GenericFolder = 1
    Album = 2
    TimeSequence = 3
    HorizontalPanoramic = 4
    VerticalPanoramic = 5
    Panoramic2D = 6
    AncillaryData = 7


class OperationCode(enum.IntEnum):
    GetDeviceInfo = 0x1001
    OpenSession = 0x1002
    CloseSession = 0x1003
    GetStorageIDs = 0x1004
    GetStorageInfo = 0x1005
    GetNumObjects = 0x1006
    GetObjectHandles = 0x1007
    GetObjectInfo = 0x1008
    GetObject = 0x1009
    GetThumb = 0x100A
    DeleteObject = 0x100B
    SendObjectInfo = 0x100C
    SendObject = 0x100D
    InitiateCapture = 0x100E
    FormatStore = 0x100F
    ResetDevice = 0x1010
    SelfTest = 0x1011
    SetObjectProtection = 0x1012
    PowerDown = 0x1013
    GetDevicePropDesc = 0x1014
    GetDevicePropValue = 0x1015
    SetDevicePropValue = 0x1016
    ResetDevicePropValue = 0x1017
    TerminateOpenCapture = 0x1018
    MoveObject = 0x1019
    CopyObject = 0x101A
    GetPartialObject = 0x101B
    InitiateOpenCapture = 0x101C
    CancelTransaction = 0x4001
    JanusGetSecureTimeChallenge = 0x9101
    JanusSetSecureTimeResponse = 0x9102
    JanusSetLicenseResponse = 0x9103
    JanusGetSyncList = 0x9104
    JanusSendMeterChallengeQuery = 0x9105
    JanusGetMeterChallenge = 0x9106
    JanusSetMeterResponse = 0x9107
    JanusCleanDataStore = 0x9108
    JanusGetLicenseState = 0x9109
    JanusSendCommand = 0x910A
    JanusSendRequest = 0x910B
    ProcessWCFObject = 0x9122
    OpenMediaSession = 0x9170
    CloseMediaSession = 0x9171
    GetNextDataBlock = 0x9172
    SetCurrentTimePosition = 0x9173
    WMPMetadataRoundTrip = 0x9201
    WmpGetAcquiredContent = 0x9202
    RebootDevice = 0x9204
    SendWMDRMPDAppRequest = 0x9212
    GetWMDRMPDAppResponse = 0x9213
    EnableTrustedFilesOperations = 0x9214
    DisableTrustedFilesOperations = 0x9215
    EndTrustedAppSession = 0x9216
    GetServiceIDs = 0x9301
    GetServiceInfo = 0x9302
    GetServiceCapabilities = 0x9303
    GetServicePropDesc = 0x9304
    GetServicePropList = 0x9305
    SetServicePropList = 0x9306
    UpdateObjectPropList = 0x9307
    DeleteObjectPropList = 0x9308
    DeleteServicePropList = 0x9309
    GetFormatCapabilities = 0x930A
    SendTinyCLRData = 0x9401
    GetTinyCLRData = 0x9402
    GetPartialObject64 = 0x95C1
    SendPartialObject = 0x95C2
    TruncateObject = 0x95C3
    BeginEditObject = 0x95C4
    EndEditObject = 0x95C5
    GetObjectPropsSupported = 0x9801
    GetObjectPropDesc = 0x9802
    GetObjectPropValue = 0x9803
    SetObjectPropValue = 0x9804
    GetObjectPropList = 0x9805
    SetObjectPropList = 0x9806
    GetInterdependentPropDesc = 0x9807
    SendObjectPropList = 0x9808
    GetObjectReferences = 0x9810
    SetObjectReferences = 0x9811
    UpdateDeviceFirmware = 0x9812
    ResetObjectPropValue = 0x9813
    Skip = 0x9820


class StorageId:
    Id: int

    def __repr__(self) -> str: ...


class ObjectId:
    Id: int

    def __repr__(self) -> str: ...


class NewObjectInfo:
    @property
    def storage_id(self) -> StorageId: ...

    @property
    def parent_object_id(self) -> ObjectId: ...

    @property
    def object_id(self) -> ObjectId: ...


class ObjectInfo:
    StorageId: StorageId
    ObjectFormat: ObjectFormat
    ProtectionStatus: int
    ObjectCompressedSize: int
    ThumbFormat: int
    ThumbCompressedSize: int
    ThumbPixWidth: int
    ThumbPixHeight: int
    ImagePixWidth: int
    ImagePixHeight: int
    ImageBitDepth: int
    ParentObject: ObjectId
    AssociationType: AssociationType
    AssociationDesc: int
    SequenceNumber: int
    Filename: str
    CaptureDate: str
    ModificationDate: str
    Keywords: str

    def __init__(self) -> None: ...


class StorageInfo:
    StorageType: int
    FilesystemType: int
    AccessCapability: int
    MaxCapacity: int
    FreeSpaceInBytes: int
    FreeSpaceInImages: int
    StorageDescription: str
    VolumeLabel: str


class DeviceInfo:
    StandardVersion: int
    VendorExtensionId: int
    VendorExtensionVersion: int
    VendorExtensionDesc: str
    FunctionalMode: int
    OperationsSupported: Sequence[OperationCode]
    EventsSupported: Sequence[int]
    DevicePropertiesSupported: Sequence[DeviceProperty]
    CaptureFormats: Sequence[ObjectFormat]
    ImageFormats: Sequence[ObjectFormat]
    Manufacturer: str
    Model: str
    DeviceVersion: str
    SerialNumber: str


class ObjectEditSession:
    def truncate(self, size: int) -> None: ...

    def send(self, offset: int, data: bytearray) -> None: ...


class DeviceDescriptor:
    @property
    def vendor_id(self) -> int: ...

    @property
    def product_id(self) -> int: ...

    def __repr__(self) -> str: ...


class UsbContext:
    def __init__(self) -> None: ...

    def get_device_descriptors(self) -> list[DeviceDescriptor]: ...


class Device:
    @staticmethod
    def find_first(
        filter_device: str = ..., *,
        claim_interface: bool = True,
        reset_device: bool = False,
    ) -> Device | None: ...

    @staticmethod
    def open(
        context: UsbContext,
        device_descriptor: DeviceDescriptor,
        *,
        claim_interface: bool = True,
        reset_device: bool = False,
    ) -> Device | None: ...

    def open_session(self, session_id: int = 1, timeout: int = ...) -> Session: ...


class Session:
    AllStorages: ClassVar[StorageId]
    AnyStorage: ClassVar[StorageId]
    Device: ClassVar[ObjectId]
    Root: ClassVar[ObjectId]

    def get_storage_ids(self) -> list[StorageId]: ...

    def get_storage_info(self, storage_id: StorageId) -> StorageInfo: ...

    def get_object_handles(
        self,
        storage_id: StorageId,
        object_format: ObjectFormat = ...,
        parent: ObjectId = ...,
        timeout: int = ...,
    ) -> list[ObjectId]: ...

    def get_object_info(self, object_id: ObjectId) -> ObjectInfo: ...

    def get_object_properties_supported(self, object_format: ObjectFormat) -> list[ObjectProperty]: ...

    def get_object(self, object_id: ObjectId, stream: _WritableStream) -> None: ...

    def get_thumb(self, object_id: ObjectId, stream: _WritableStream) -> None: ...

    def send_object(
        self,
        stream: _ReadableStream,
        size: int,
        timeout: int = ...,
    ) -> None: ...

    def get_object_property(self, object_id: ObjectId, property: ObjectProperty) -> bytearray: ...

    def get_object_string_property(self, object_id: ObjectId, property: ObjectProperty) -> str: ...

    def get_object_integer_property(self, object_id: ObjectId, property: ObjectProperty) -> int: ...

    @overload
    def set_object_property(self, object_id: ObjectId, property: ObjectProperty, value: int) -> None: ...

    @overload
    def set_object_property(self, object_id: ObjectId, property: ObjectProperty, value: str) -> None: ...

    @overload
    def set_object_property(self, object_id: ObjectId, property: ObjectProperty, value: bytearray) -> None: ...

    def get_object_storage(self, object_id: ObjectId) -> StorageId: ...

    def get_object_parent(self, object_id: ObjectId) -> ObjectId: ...

    def delete_object(self, object_id: ObjectId, timeout: int = ...) -> None: ...

    def edit_object_supported(self) -> bool: ...

    def get_object_property_list_supported(self) -> bool: ...

    def get_object_property_list(
        self,
        object_id: ObjectId,
        object_format: ObjectFormat,
        property: ObjectProperty,
        group_code: int,
        depth: int,
        timeout: int = ...,
    ) -> bytearray: ...

    def get_object_modification_time(self, object_id: ObjectId) -> _dt.datetime: ...

    def get_partial_object(self, object_id: ObjectId, offset: int, size: int) -> bytearray: ...

    def edit_object(self, object_id: ObjectId) -> ObjectEditSession: ...

    def create_directory(
        self,
        name: str,
        parent: ObjectId,
        storage: StorageId = ...,
        association_type: AssociationType = AssociationType.GenericFolder,
    ) -> NewObjectInfo: ...

    def send_object_info(
        self,
        object_info: ObjectInfo,
        storage: StorageId,
        parent: ObjectId,
    ) -> NewObjectInfo: ...

    def get_device_info(self) -> DeviceInfo: ...

    def get_device_property(self, property: DeviceProperty) -> bytearray: ...

    def get_device_integer_property(self, property: DeviceProperty) -> int: ...

    def get_device_string_property(self, property: DeviceProperty) -> str: ...

    @overload
    def set_device_property(self, property: DeviceProperty, value: str) -> None: ...

    @overload
    def set_device_property(self, property: DeviceProperty, value: bytearray) -> None: ...

    def abort_current_transaction(self, timeout: int = ...) -> None: ...


def debug(enable: bool) -> None: ...

