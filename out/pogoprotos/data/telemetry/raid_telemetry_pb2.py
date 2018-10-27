# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/raid_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/raid_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_pb=_b('\n.pogoprotos/data/telemetry/raid_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"\xa8\x02\n\rRaidTelemetry\x12=\n\x11raid_telemetry_id\x18\x01 \x01(\x0e\x32\".pogoprotos.enums.RaidTelemetryIds\x12\x16\n\x0e\x62undle_version\x18\x02 \x01(\t\x12\x1d\n\x15time_since_enter_raid\x18\x03 \x01(\x02\x12&\n\x1etime_since_last_raid_telemetry\x18\x04 \x01(\x02\x12\x12\n\nraid_level\x18\x05 \x01(\x05\x12\x15\n\rprivate_lobby\x18\x06 \x01(\x08\x12\x13\n\x0bticket_item\x18\x07 \x01(\t\x12\x1c\n\x14num_players_in_lobby\x18\x08 \x01(\x05\x12\x1b\n\x13\x62\x61ttle_party_number\x18\t \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_RAIDTELEMETRY = _descriptor.Descriptor(
  name='RaidTelemetry',
  full_name='pogoprotos.data.telemetry.RaidTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raid_telemetry_id', full_name='pogoprotos.data.telemetry.RaidTelemetry.raid_telemetry_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bundle_version', full_name='pogoprotos.data.telemetry.RaidTelemetry.bundle_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_since_enter_raid', full_name='pogoprotos.data.telemetry.RaidTelemetry.time_since_enter_raid', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_since_last_raid_telemetry', full_name='pogoprotos.data.telemetry.RaidTelemetry.time_since_last_raid_telemetry', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_level', full_name='pogoprotos.data.telemetry.RaidTelemetry.raid_level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='private_lobby', full_name='pogoprotos.data.telemetry.RaidTelemetry.private_lobby', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ticket_item', full_name='pogoprotos.data.telemetry.RaidTelemetry.ticket_item', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_players_in_lobby', full_name='pogoprotos.data.telemetry.RaidTelemetry.num_players_in_lobby', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_party_number', full_name='pogoprotos.data.telemetry.RaidTelemetry.battle_party_number', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=412,
)

_RAIDTELEMETRY.fields_by_name['raid_telemetry_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._RAIDTELEMETRYIDS
DESCRIPTOR.message_types_by_name['RaidTelemetry'] = _RAIDTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaidTelemetry = _reflection.GeneratedProtocolMessageType('RaidTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _RAIDTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.raid_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.RaidTelemetry)
  ))
_sym_db.RegisterMessage(RaidTelemetry)


# @@protoc_insertion_point(module_scope)
