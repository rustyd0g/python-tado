"""Models for the Tado API."""

from __future__ import annotations

from dataclasses import dataclass, field

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin


@dataclass
class GetMe(DataClassORJSONMixin):
    """GetMe model represents the user's profile information."""

    name: str
    email: str
    id: str
    username: str
    locale: str
    homes: list[Home]


@dataclass
class Home(DataClassORJSONMixin):
    """Home model represents the user's home information."""

    id: int
    name: str


@dataclass
class DeviceMetadata(DataClassORJSONMixin):
    """DeviceMetadata model represents the metadata of a device."""

    platform: str
    os_version: str = field(metadata=field_options(alias="osVersion"))
    model: str
    locale: str


@dataclass
class MobileDevice(DataClassORJSONMixin):
    """MobileDevice model represents the user's mobile device information."""

    name: str
    id: int
    device_meta_data: DeviceMetadata = field(
        metadata=field_options(alias="deviceMetadata")
    )
    settings: MobileSettings


@dataclass
class MobileSettings(DataClassORJSONMixin):
    """MobileSettings model represents the user's mobile device settings."""

    geo_tracking_enabled: bool = field(
        metadata=field_options(alias="geoTrackingEnabled")
    )
    special_offers_enabled: bool = field(
        metadata=field_options(alias="specialOffersEnabled")
    )
    on_demand_log_retrieval_enabled: bool = field(
        metadata=field_options(alias="onDemandLogRetrievalEnabled")
    )


@dataclass
class ConnectionState(DataClassORJSONMixin):
    """ConnectionState model represents the connection state of a device."""

    value: bool
    timestamp: str


@dataclass
class Characteristics(DataClassORJSONMixin):
    """Characteristics model represents the capabilities of a device."""

    capabilities: list[str]


@dataclass
class MountingState(DataClassORJSONMixin):
    """MountingState model represents the mounting state of a device."""

    value: str
    timestamp: str


@dataclass
class Device(DataClassORJSONMixin):  # pylint: disable=too-many-instance-attributes
    """Device model represents a device in a zone."""

    device_type: str = field(metadata=field_options(alias="deviceType"))
    serial_no: str = field(metadata=field_options(alias="serialNo"))
    short_serial_no: str = field(metadata=field_options(alias="shortSerialNo"))
    current_fw_version: str = field(metadata=field_options(alias="currentFwVersion"))
    connection_state: ConnectionState = field(
        metadata=field_options(alias="connectionState")
    )
    characteristics: Characteristics
    in_pairing_mode: bool | None = field(
        default=None, metadata=field_options(alias="inPairingMode")
    )
    mounting_state: MountingState | None = field(
        default=None, metadata=field_options(alias="mountingState")
    )
    mounting_state_with_error: str | None = field(
        default=None, metadata=field_options(alias="mountingStateWithError")
    )
    battery_state: str | None = field(
        default=None, metadata=field_options(alias="batteryState")
    )
    orientation: str | None = None
    child_lock_enabled: bool | None = field(
        default=None, metadata=field_options(alias="childLockEnabled")
    )


@dataclass
class DazzleMode(DataClassORJSONMixin):
    """DazzleMode model represents the dazzle mode settings of a zone."""

    supported: bool
    enabled: bool


@dataclass
class OpenWindowDetection(DataClassORJSONMixin):
    """OpenWindowDetection model represents the open window detection settings."""

    supported: bool
    enabled: bool
    timeout_in_seconds: int = field(metadata=field_options(alias="timeoutInSeconds"))


@dataclass
class Zone(DataClassORJSONMixin):  # pylint: disable=too-many-instance-attributes
    """Zone model represents a zone in a home."""

    id: int
    name: str
    type: str
    date_created: str = field(metadata=field_options(alias="dateCreated"))
    device_types: list[str] = field(metadata=field_options(alias="deviceTypes"))
    devices: list[Device]
    report_available: bool = field(metadata=field_options(alias="reportAvailable"))
    show_schedule_detup: bool = field(metadata=field_options(alias="showScheduleSetup"))
    supports_dazzle: bool = field(metadata=field_options(alias="supportsDazzle"))
    dazzle_enabled: bool = field(metadata=field_options(alias="dazzleEnabled"))
    dazzle_mode: DazzleMode = field(metadata=field_options(alias="dazzleMode"))
    open_window_detection: OpenWindowDetection = field(
        metadata=field_options(alias="openWindowDetection")
    )


@dataclass
class Precision(DataClassORJSONMixin):
    """Precision model represents the precision of a temperature."""

    celsius: float
    fahrenheit: float


@dataclass
class Temperature(DataClassORJSONMixin):
    """Temperature model represents the temperature in Celsius and Fahrenheit."""

    celsius: float
    fahrenheit: float
    type: str | None = None
    precision: Precision | None = None
    timestamp: str | None = None


@dataclass
class SolarIntensity(DataClassORJSONMixin):
    """SolarIntensity model represents the solar intensity."""

    percentage: float
    timestamp: str
    type: str


@dataclass
class WeatherState(DataClassORJSONMixin):
    """WeatherState model represents the weather state."""

    timestamp: str
    type: str
    value: str


@dataclass
class Weather(DataClassORJSONMixin):
    """Weather model represents the weather information."""

    outside_temperature: Temperature = field(
        metadata=field_options(alias="outsideTemperature")
    )
    solar_intensity: SolarIntensity = field(
        metadata=field_options(alias="solarIntensity")
    )
    weather_state: WeatherState = field(metadata=field_options(alias="weatherState"))


@dataclass
class HomeState(DataClassORJSONMixin):
    """HomeState model represents the state of a home."""

    presence: str
    presence_locked: bool = field(metadata=field_options(alias="presenceLocked"))
    show_home_presence_switch_button: bool | None = field(
        default=None, metadata=field_options(alias="showHomePresenceSwitchButton")
    )
    show_switch_to_auto_geofencing_button: bool | None = field(
        default=None, metadata=field_options(alias="showSwitchToAutoGeofencingButton")
    )


@dataclass
class TemperatureRange(DataClassORJSONMixin):
    """TemperatureRange model represents the range of a temperature."""

    min: float
    max: float
    step: float


@dataclass
class Temperatures(DataClassORJSONMixin):
    """Temperatures model represents the temperatures in Celsius and Fahrenheit."""

    celsius: TemperatureRange
    fahrenheit: TemperatureRange


@dataclass
class Capabilities(DataClassORJSONMixin):
    """Capabilities model represents the capabilities of a zone."""

    type: str
    temperatures: Temperatures


@dataclass
class TemperatureOffset(DataClassORJSONMixin):
    """TemperatureOffset model represents the temperature offset."""

    celsius: float
    fahrenheit: float


@dataclass
class TemperatureSetting(DataClassORJSONMixin):
    """TemperatureSetting model represents the temperature setting."""

    type: str
    power: str
    temperature: Temperature | None = None


@dataclass
class Overlay(DataClassORJSONMixin):
    """Overlay model represents the overlay settings of a zone."""

    type: str
    setting: TemperatureSetting
    termination: dict[str, str]
    projected_expiry: str | None = field(
        default=None, metadata=field_options(alias="projectedExpiry")
    )


@dataclass
class NextScheduleChange(DataClassORJSONMixin):
    """NextScheduleChange model represents the next schedule change."""

    start: str
    setting: TemperatureSetting


@dataclass
class Link(DataClassORJSONMixin):
    """Link model represents the link of a zone."""

    state: str


@dataclass
class HeatingPower(DataClassORJSONMixin):
    """HeatingPower model represents the heating power."""

    type: str
    percentage: float
    timestamp: str


@dataclass
class Humidity(DataClassORJSONMixin):
    """Humidity model represents the humidity."""

    type: str
    percentage: float
    timestamp: str


@dataclass
class SensorDataPoints(DataClassORJSONMixin):
    """SensorDataPoints model represents the sensor data points."""

    insideTemperature: Temperature
    humidity: Humidity


@dataclass
class ZoneState(DataClassORJSONMixin):  # pylint: disable=too-many-instance-attributes
    """ZoneState model represents the state of a zone."""

    setting: TemperatureSetting
    overlay: Overlay
    link: Link
    activity_data_points: dict[str, str] = field(
        metadata=field_options(alias="activityDataPoints")
    )
    sensor_data_points: SensorDataPoints = field(
        metadata=field_options(alias="sensorDataPoints")
    )
    tado_mode: str = field(metadata=field_options(alias="tadoMode"))
    geolocation_override: bool = field(
        metadata=field_options(alias="geolocationOverride")
    )
    overlay_type: str = field(metadata=field_options(alias="overlayType"))
    next_time_block: dict[str, str] = field(
        metadata=field_options(alias="nextTimeBlock")
    )

    geolocation_override_disable_time: str | None = field(
        default=None, metadata=field_options(alias="geolocationOverrideDisableTime")
    )
    preparation: str | None = None
    open_window: str | None = field(
        default=None, metadata=field_options(alias="openWindow")
    )
    next_schedule_change: NextScheduleChange | None = field(
        default=None, metadata=field_options(alias="nextScheduleChange")
    )


@dataclass
class ZoneStates(DataClassORJSONMixin):
    """ZoneStates model represents the states of the zones."""

    zone_states: dict[str, ZoneState] = field(
        metadata=field_options(alias="zoneStates")
    )
